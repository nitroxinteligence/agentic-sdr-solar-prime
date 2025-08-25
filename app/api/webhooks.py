"""
Webhooks API - Recebe eventos externos (WhatsApp, Kommo)
Processa mensagens recebidas e eventos do CRM
"""

from datetime import datetime
from typing import Dict, Any, Optional, List
import asyncio
import re
import json
import traceback

from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from loguru import logger

from app.config import settings
from app.utils.logger import emoji_logger
from app.integrations.redis_client import redis_client
from app.integrations.evolution import evolution_client
from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.services.message_buffer import MessageBuffer, get_message_buffer
from app.services.message_splitter import MessageSplitter, get_message_splitter
from app.utils.agno_media_detection import AGNOMediaDetector
from app.exceptions import HandoffActiveException

router = APIRouter(prefix="/webhook", tags=["webhooks"])

agno_detector = AGNOMediaDetector()


def extract_message_content(message: Dict[str, Any]) -> Optional[str]:
    """Extrai o conteúdo de texto de vários tipos de mensagem."""
    # Primeiro, verificar se é uma mensagem do webhook padrão
    if "type" in message:
        return extract_webhook_message_content(message)
    
    # Caso contrário, usar a lógica original para Evolution API
    msg_content = message.get("message", {})
    if not msg_content:
        return None

    if "conversation" in msg_content:
        return msg_content["conversation"]
    if "extendedTextMessage" in msg_content:
        return msg_content["extendedTextMessage"].get("text")
    if "textMessage" in msg_content:
        return msg_content["textMessage"].get("text")
    
    for media_type in ["imageMessage", "videoMessage", "documentMessage"]:
        if media_type in msg_content:
            return msg_content[media_type].get("caption")
            
    return None


def extract_webhook_message_content(message: dict) -> str:
    """Extrai o conteúdo da mensagem baseado no tipo do webhook padrão"""
    message_type = message.get("type")
    emoji_logger.system_debug(f"Extraindo conteúdo de mensagem tipo: {message_type}")
    
    content = ""
    
    if message_type == "text":
        content = message.get("text", {}).get("body", "")
        emoji_logger.system_debug(f"Texto extraído: '{content}'")
    elif message_type == "image":
        caption = message.get("image", {}).get("caption", "")
        content = f"[Imagem enviada] {caption}".strip()
        emoji_logger.system_debug(f"Imagem com caption: '{caption}'")
    elif message_type == "document":
        caption = message.get("document", {}).get("caption", "")
        filename = message.get("document", {}).get("filename", "documento")
        content = f"[Documento: {filename}] {caption}".strip()
        emoji_logger.system_debug(f"Documento '{filename}' com caption: '{caption}'")
    elif message_type == "audio":
        content = "[Áudio enviado]"
        emoji_logger.system_debug("Áudio detectado")
    elif message_type == "video":
        caption = message.get("video", {}).get("caption", "")
        content = f"[Vídeo enviado] {caption}".strip()
        emoji_logger.system_debug(f"Vídeo com caption: '{caption}'")
    else:
        content = f"[Mensagem do tipo: {message_type}]"
        emoji_logger.system_warning(f"Tipo de mensagem não reconhecido: {message_type}")
        emoji_logger.system_debug(f"Estrutura da mensagem desconhecida: {json.dumps(message, indent=2)}")
    
    emoji_logger.system_debug(f"Conteúdo final extraído: '{content}'")
    return content


async def _handle_media_message(
        message: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """Lida com o processamento de mídia recebida via webhook base64."""
    import base64
    msg_content = message.get("message", {})
    media_type_map = {
        "imageMessage": "image",
        "videoMessage": "video",
        "audioMessage": "audio",
        "documentMessage": "document",
        "stickerMessage": "sticker",
    }

    for msg_type, media_type in media_type_map.items():
        if msg_type in msg_content:
            media_payload = msg_content[msg_type]
            try:
                base64_content = media_payload.get("media") or media_payload.get("body")

                if base64_content:
                    emoji_logger.system_debug(f"Mídia Base64 extraída diretamente do payload para {msg_type}")
                    return {
                        "type": media_type,
                        "content": base64_content,
                        "mimetype": media_payload.get("mimetype"),
                    }
                else:
                    emoji_logger.system_info(f"Payload para {msg_type} sem mídia. Usando endpoint getBase64FromMediaMessage.")
                    base64_from_api = await evolution_client.get_media_as_base64(message.get("key"))
                    if base64_from_api:
                        return {
                            "type": media_type,
                            "content": base64_from_api,
                            "mimetype": media_payload.get("mimetype"),
                        }
                    else:
                         emoji_logger.system_error(f"Falha no download de fallback para {msg_type}", "Não foi possível obter os bytes da mídia.")
                         return {"type": "error", "content": "Desculpe, não consegui obter a mídia que você enviou."}

            except Exception as e:
                emoji_logger.system_error(f"Falha ao processar mídia para {msg_type}", str(e))
                return {"type": "error", "content": "Desculpe, tive um problema ao processar a mídia que você enviou."}
    return None


async def process_connection_update(data: Dict[str, Any]):
    """Processa atualizações de status da conexão."""
    emoji_logger.system_info(f"Connection status update: {data}")
    if data:
        await redis_client.set("whatsapp:connection_status", data)
    else:
        emoji_logger.system_warning("Connection update received with empty data.")


async def process_qrcode_update(data: Dict[str, Any]):
    """Processa atualizações de QR code."""
    emoji_logger.system_info("QR code updated. Scan required.")


async def process_message_update(data: Dict[str, Any]):
    """Processa atualizações de status de mensagem (enviada, lida, etc.)."""
    update = data.get("update", {})
    status = update.get("status")
    msg_id = update.get("key", {}).get("id")
    if status and msg_id:
        emoji_logger.system_debug(
            f"Message {msg_id} status updated to {status}"
        )


async def process_presence_update(data: Dict[str, Any]):
    """Processa atualizações de presença (digitando, online, etc.)."""
    remote_jid = data.get("remoteJid")
    presence = data.get("presence")
    if remote_jid and presence:
        emoji_logger.system_debug(
            f"Presence update from {remote_jid}: {presence}"
        )


async def process_contacts_update(data: Dict[str, Any]):
    """Processa atualizações de contatos para extrair pushName e atualizar nomes no Supabase"""
    try:
        from app.integrations.supabase_client import supabase_client
        
        # Log detalhado do payload recebido para debugging
        emoji_logger.system_debug(f"CONTACTS_UPDATE payload completo: {data}")
        
        # Extrair informações do contato com múltiplos fallbacks
        contact_data = data.get('data', data)
        if isinstance(contact_data, list) and contact_data:
            contact_data = contact_data[0]
            emoji_logger.system_debug(f"Usando primeiro item da lista: {contact_data}")
        
        # Múltiplas tentativas de extração de pushName
        push_name = None
        phone_number = None
        
        # Tentativa 1: campos diretos
        for field in ['pushName', 'name', 'notify', 'displayName', 'verifiedName']:
            push_name = contact_data.get(field)
            if push_name:
                emoji_logger.system_debug(f"pushName encontrado em campo direto '{field}': '{push_name}'")
                break
        
        # Tentativa 2: estruturas aninhadas
        if not push_name:
            for key in ['contact', 'contactInfo', 'profile']:
                nested_data = contact_data.get(key, {})
                if isinstance(nested_data, dict):
                    for field in ['pushName', 'name', 'notify', 'displayName', 'verifiedName']:
                        nested_value = nested_data.get(field)
                        if nested_value:
                            push_name = nested_value
                            emoji_logger.system_debug(f"pushName encontrado em {key}.{field}: '{push_name}'")
                            break
                    if push_name:
                        break
        
        # Tentativa 3: estruturas ainda mais aninhadas (profile dentro de contactInfo, etc.)
        if not push_name:
            for key in ['contact', 'contactInfo']:
                nested_data = contact_data.get(key, {})
                if isinstance(nested_data, dict):
                    profile_data = nested_data.get('profile', {})
                    if isinstance(profile_data, dict):
                        for field in ['pushName', 'name', 'displayName']:
                            profile_value = profile_data.get(field)
                            if profile_value:
                                push_name = profile_value
                                emoji_logger.system_debug(f"pushName encontrado em {key}.profile.{field}: '{push_name}'")
                                break
                        if push_name:
                            break
        
        # Extração de telefone com múltiplos fallbacks e estruturas aninhadas
        phone_number = None
        
        # Tentativa 1: id direto
        phone_number = contact_data.get('id', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
        
        # Tentativa 2: phone/number direto
        if not phone_number:
            phone_number = contact_data.get('phone', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
        if not phone_number:
            phone_number = contact_data.get('number', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
        
        # Tentativa 3: estruturas aninhadas (contact, contactInfo, profile)
        if not phone_number:
            for key in ['contact', 'contactInfo', 'profile']:
                nested_data = contact_data.get(key, {})
                if isinstance(nested_data, dict):
                    nested_id = nested_data.get('id', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
                    if nested_id:
                        phone_number = nested_id
                        emoji_logger.system_debug(f"Telefone encontrado em {key}.id: '{phone_number}'")
                        break
                    nested_phone = nested_data.get('phone', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
                    if nested_phone:
                        phone_number = nested_phone
                        emoji_logger.system_debug(f"Telefone encontrado em {key}.phone: '{phone_number}'")
                        break
        
        # Tentativa 4: Buscar telefone em mensagens recentes se pushName estiver disponível
        if not phone_number and push_name:
            emoji_logger.system_debug(f"Tentando encontrar telefone para pushName '{push_name}' em mensagens recentes")
            try:
                from app.integrations.supabase_client import supabase_client
                # Buscar leads com nome similar
                recent_leads = await supabase_client.search_leads_by_name(push_name)
                if recent_leads:
                    # Usar o telefone do lead mais recente com nome similar
                    phone_number = recent_leads[0].get('phone_number', '')
                    emoji_logger.system_debug(f"Telefone encontrado via busca por nome: '{phone_number}'")
            except Exception as e:
                emoji_logger.system_debug(f"Erro ao buscar telefone por nome: {e}")
        
        emoji_logger.system_debug(f"Dados extraídos - Phone: '{phone_number}', PushName: '{push_name}'")
        
        # Validar se temos dados válidos (telefone não pode estar vazio)
        if push_name and phone_number and phone_number.strip():
            # Buscar lead existente por telefone
            existing_lead = await supabase_client.get_lead_by_phone(phone_number)
            
            if existing_lead:
                # Atualizar nome apenas se o lead não tiver nome ou tiver nome genérico
                current_name = existing_lead.get('name')
                is_generic_name = (
                    not current_name or 
                    current_name in ['Lead sem nome', 'Lead Sem Nome', None] or
                    'Lead sem nome' in current_name or
                    'Lead Sem Nome' in current_name
                )
                if is_generic_name:
                    await supabase_client.update_lead(
                        existing_lead['id'], 
                        {'name': push_name}
                    )
                    emoji_logger.system_success(
                        f"Nome do lead atualizado via CONTACTS_UPDATE: {phone_number} -> {push_name}"
                    )
                else:
                    emoji_logger.system_info(
                        f"Lead {phone_number} já possui nome '{current_name}', não sobrescrevendo com '{push_name}'"
                    )
            else:
                emoji_logger.system_info(
                    f"Lead não encontrado para telefone {phone_number}, pushName '{push_name}' não aplicado"
                )
        else:
            # Mensagem mais específica sobre o que está faltando
            missing_fields = []
            if not push_name:
                missing_fields.append("pushName")
            if not phone_number or not phone_number.strip():
                missing_fields.append("telefone válido")
            
            emoji_logger.system_warning(
                f"CONTACTS_UPDATE ignorado - faltando: {', '.join(missing_fields)}. "
                f"Phone: '{phone_number}', PushName: '{push_name}'"
            )
            emoji_logger.system_debug(f"Estrutura completa do contact_data: {contact_data}")
            
    except Exception as e:
        emoji_logger.system_error(f"Erro ao processar CONTACTS_UPDATE: {str(e)}")
        logger.exception("Detalhes do erro em process_contacts_update")

def extract_final_response(full_response: str) -> str:
    """
    Extrai e limpa o conteúdo dentro da tag <RESPOSTA_FINAL>, removendo
    outras tags de raciocínio e garantindo uma saída segura.
    """
    if not isinstance(full_response, str):
        return "Desculpe, ocorreu um erro inesperado."

    match = re.search(r'<RESPOSTA_FINAL>(.*?)</RESPOSTA_FINAL>', full_response, re.DOTALL | re.IGNORECASE)
    
    if match:
        final_response = match.group(1).strip()
    else:
        emoji_logger.system_warning(
            "Tag <RESPOSTA_FINAL> não encontrada na resposta do LLM.",
            raw_response=full_response[:500]
        )
        temp_response = re.sub(r'</?analise_interna>.*?</analise_interna>', '', full_response, flags=re.DOTALL | re.IGNORECASE)
        temp_response = re.sub(r'</?RESPOSTA_FINAL>', '', temp_response, flags=re.IGNORECASE)
        
        if '<' in temp_response and '>' in temp_response:
            emoji_logger.system_error("extract_final_response", "Nenhuma tag <RESPOSTA_FINAL> clara e ainda há outras tags. Usando fallback.")
            return "Estou finalizando sua solicitação. Um momento."
        final_response = temp_response.strip()

    if not final_response or final_response.lower() == "none":
        emoji_logger.system_warning("A resposta final do LLM estava vazia ou 'none'. Usando fallback de esclarecimento.")
        return "Pode repetir, por favor? Não entendi bem o que você quis dizer."

    return final_response


async def create_agent_with_context(
        phone: str,
        conversation_id: str = None,
        media_data: Optional[Dict[str, Any]] = None
) -> tuple:
    """
    Cria agente stateless com contexto completo, sincronizando com o CRM em tempo real.
    """
    from app.integrations.supabase_client import supabase_client
    from app.services.crm_service_100_real import CRMServiceReal

    emoji_logger.webhook_process("🏭 Criando agente stateless com contexto...")

    try:
        # Passo 1: Obter dados locais do Supabase
        lead_data = await supabase_client.get_lead_by_phone(phone)
        
        # Passo 2: Sincronização em Tempo Real com Kommo
        if lead_data and lead_data.get("kommo_lead_id"):
            crm_service = CRMServiceReal()
            await crm_service.initialize() # Garante que o serviço esteja inicializado
            kommo_lead = await crm_service.get_lead_by_id(str(lead_data["kommo_lead_id"]))

            if kommo_lead:
                current_status_id = kommo_lead.get('status_id')
                human_handoff_stage_id = settings.kommo_human_handoff_stage_id

                # Passo 3: Ativar/Desativar Pausa e lançar exceção
                if str(current_status_id) == str(human_handoff_stage_id):
                    await redis_client.set_human_handoff_pause(phone)
                    raise HandoffActiveException(f"Handoff ativo para {phone}")
                else:
                    await redis_client.clear_human_handoff_pause(phone)
                
                # Atualiza Supabase se necessário
                if lead_data.get('current_stage_id') != current_status_id:
                    await supabase_client.update_lead(lead_data['id'], {'current_stage_id': current_status_id})

        # Continua com a criação do contexto se o handoff não estiver ativo
        conversation_history = []
        if conversation_id:
            conversation_history = await supabase_client.get_conversation_messages(conversation_id, limit=500)

        execution_context = {
            "phone": phone,
            "lead_info": lead_data or {},
            "conversation_id": conversation_id,
            "conversation_history": conversation_history or [],
            "media": media_data,
            "timestamp": datetime.now().isoformat()
        }

        agent = AgenticSDRStateless()
        await agent.initialize()

        emoji_logger.system_ready(
            "✅ Agente stateless criado com contexto",
            history_count=len(conversation_history),
            lead_name=(lead_data.get('name') if lead_data else 'Não identificado')
        )

        return agent, execution_context

    except HandoffActiveException:
        raise
    except Exception as e:
        emoji_logger.system_error("Webhook", f"Erro ao criar agente com contexto: {e}")
        raise

def get_message_buffer_instance():
    """Obtém instância do Message Buffer"""
    buffer = get_message_buffer()
    if buffer is None:
        logger.warning("Message Buffer não foi inicializado no startup!")
        buffer = MessageBuffer(
            timeout=settings.message_buffer_timeout,
            max_size=10
        )
    return buffer

def get_message_splitter_instance():
    """Obtém instância do Message Splitter"""
    splitter = get_message_splitter()
    if splitter is None:
        logger.warning("Message Splitter não foi inicializado no startup!")
        splitter = MessageSplitter(
            max_length=settings.message_max_length,
            add_indicators=settings.message_add_indicators
        )
    return splitter


@router.post("/webhook")
async def webhook_handler(request: Request):
    """Manipula webhooks do WhatsApp"""
    try:
        body = await request.body()
        data = json.loads(body)
        
        # Log detalhado do webhook recebido
        emoji_logger.webhook_received(
            f"Webhook recebido - Tamanho: {len(body)} bytes, "
            f"Chaves principais: {list(data.keys())}"
        )
        emoji_logger.system_debug(f"Payload completo do webhook: {json.dumps(data, indent=2)}")
        
        # Processar diferentes tipos de webhook
        if "messages" in data:
            emoji_logger.webhook_info("Processando webhook de mensagem")
            await process_message_webhook(data)
        elif "contacts" in data:
            emoji_logger.webhook_info("Processando webhook de atualização de contatos")
            await process_contacts_update(data)
        else:
            emoji_logger.webhook_warning(
                f"Tipo de webhook não reconhecido. Chaves disponíveis: {list(data.keys())}"
            )
            emoji_logger.system_debug(f"Dados do webhook não reconhecido: {data}")
        
        emoji_logger.webhook_success("Webhook processado com sucesso")
        return {"status": "success"}
    
    except json.JSONDecodeError as e:
        emoji_logger.webhook_error(f"Erro ao decodificar JSON do webhook: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        emoji_logger.system_error(f"Erro crítico no webhook: {str(e)}")
        emoji_logger.system_debug(f"Traceback completo: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))


async def process_message_webhook(data: dict):
    """Processa webhooks de mensagens"""
    try:
        messages = data.get("messages", [])
        emoji_logger.webhook_info(f"Processando {len(messages)} mensagem(ns)")
        
        for i, message in enumerate(messages):
            emoji_logger.system_debug(f"Processando mensagem {i+1}/{len(messages)}")
            emoji_logger.system_debug(f"Dados da mensagem: {json.dumps(message, indent=2)}")
            
            phone_number = message.get("from")
            message_content = extract_message_content(message)
            message_type = message.get("type", "unknown")
            
            emoji_logger.system_debug(
                f"Mensagem extraída - Telefone: {phone_number}, "
                f"Tipo: {message_type}, Conteúdo: '{message_content[:100]}...'"
            )
            
            if phone_number and message_content:
                emoji_logger.webhook_success(
                    f"Enviando mensagem para processamento - {phone_number}: '{message_content[:50]}...'"
                )
                # Processar mensagem através do sistema principal
                await process_whatsapp_message(phone_number, message_content)
            else:
                emoji_logger.webhook_warning(
                    f"Mensagem ignorada - Telefone: {bool(phone_number)}, "
                    f"Conteúdo: {bool(message_content)}"
                )
    
    except Exception as e:
        emoji_logger.webhook_error(f"Erro ao processar webhook de mensagem: {str(e)}")
        emoji_logger.system_debug(f"Traceback: {traceback.format_exc()}")
        raise


@router.post("/evolution/{event_type}")
async def whatsapp_dynamic_webhook(
    event_type: str,
    request: Request,
    background_tasks: BackgroundTasks
):
    """Webhook dinâmico para eventos específicos do WhatsApp"""
    try:
        event = event_type.upper().replace("-", "_")
        data = await request.json()
        emoji_logger.webhook_receive(
            f"/whatsapp/{event_type}", "evolution-api", event=event
        )

        if event == "MESSAGES_UPSERT":
            actual_data = data.get("data", data)
            background_tasks.add_task(process_new_message, actual_data)
        elif event == "CONNECTION_UPDATE":
            await process_connection_update(data)
        elif event == "QRCODE_UPDATED":
            await process_qrcode_update(data)
        elif event == "MESSAGES_UPDATE":
            await process_message_update(data)
        elif event == "PRESENCE_UPDATE":
            await process_presence_update(data)
        elif event == "CHATS_UPDATE":
            logger.info(f"{event} update recebido: {data}")
        elif event == "CONTACTS_UPDATE":
            await process_contacts_update(data)
        else:
            logger.warning(f"Evento não reconhecido: {event}")

        return {"status": "ok", "event": event}

    except Exception as e:
        emoji_logger.system_error(f"Webhook WhatsApp {event_type}", str(e))
        return {"status": "error", "message": str(e)}


@router.post("/evolution")
async def evolution_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):
    """Webhook principal da Evolution API"""
    try:
        data = await request.json()
        event = data.get("event")
        instance = data.get("instance")

        emoji_logger.webhook_receive(
            "/evolution", "evolution-api", event=event, instance=instance
        )

        if event == "MESSAGES_UPSERT":
            actual_data = data.get("data", data)
            background_tasks.add_task(process_new_message, actual_data)
        elif event == "CONNECTION_UPDATE":
            await process_connection_update(data.get("data", {}))
        elif event == "QRCODE_UPDATED":
            await process_qrcode_update(data.get("data", {}))
        elif event == "MESSAGES_UPDATE":
            await process_message_update(data.get("data", {}))
        elif event == "PRESENCE_UPDATE":
            await process_presence_update(data.get("data", {}))

        return {"status": "ok", "event": event}

    except Exception as e:
        emoji_logger.system_error("Webhook Evolution", str(e))
        raise HTTPException(status_code=500, detail=str(e))


async def process_new_message(data: Any):
    """Processa cada nova mensagem recebida, normalizando o payload para sempre ser uma lista."""
    try:
        if isinstance(data, list):
            messages = data
        elif isinstance(data, dict):
            messages = [data]
        else:
            emoji_logger.system_warning(f"Payload de mensagens com formato inesperado: {type(data)}")
            return

        emoji_logger.webhook_process(f"Iniciando processamento de {len(messages)} nova(s) mensagem(ns)")

        if not messages:
            emoji_logger.system_warning("Payload de mensagens vazio")
            return

        for message in messages:
            if not isinstance(message, dict):
                logger.warning(f"Item ignorado no payload de mensagens pois não é um dicionário: {message}")
                continue

            key = message.get("key", {})
            remote_jid = key.get("remoteJid", "")
            from_me = key.get("fromMe", False)
            message_id = key.get("id", "")

            if from_me:
                emoji_logger.webhook_process("Mensagem própria ignorada")
                continue

            phone = remote_jid.split("@")[0] if "@" in remote_jid else remote_jid

            if "@g.us" in remote_jid:
                emoji_logger.webhook_process(f"Mensagem de grupo ignorada: {remote_jid}")
                continue

            emoji_logger.webhook_process(f"Processando mensagem de {phone}")
            
            message_content = extract_message_content(message)
            media_data = await _handle_media_message(message)

            if not message_content and not media_data:
                emoji_logger.system_warning(f"Mensagem sem conteúdo de texto ou mídia de {phone}")
                logger.debug(f"Payload completo: {message}")
                continue

            message_content = message_content or ""

            emoji_logger.evolution_receive(
                phone, 
                media_data["type"] if media_data else "text", 
                preview=message_content[:100]
            )

            if not await redis_client.check_rate_limit(
                f"message:{phone}", max_requests=10, window_seconds=60
            ):
                emoji_logger.system_warning(f"Rate limit excedido para {phone}")
                await evolution_client.send_text_message(
                    phone,
                    "⚠️ Você está enviando muitas mensagens. Por favor, aguarde um momento.",
                    delay=1
                )
                return

            if settings.enable_message_buffer:
                buffer = get_message_buffer_instance()
                await buffer.add_message(
                    phone=phone,
                    content=message_content,
                    message_data=message,
                    media_data=media_data
                )
            else:
                await process_message_with_agent(
                    phone=phone,
                    message_content=message_content,
                    original_message=message,
                    message_id=message_id,
                    media_data=media_data
                )

    except Exception as e:
        emoji_logger.system_error("Webhook Message Processing", str(e))
        logger.exception("Erro detalhado no processamento:")


async def process_message_with_agent(
    phone: str,
    message_content: str,
    original_message: Dict[str, Any],
    message_id: str,
    media_data: Optional[Dict[str, Any]] = None
):
    """Processa mensagem com o agente AGENTIC SDR"""
    from app.integrations.supabase_client import supabase_client

    # Log inicial do processamento
    emoji_logger.conversation_event(
        f"🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: {phone}, "
        f"Mensagem: '{message_content[:100]}...', ID: {message_id}"
    )
    
    if not original_message or not isinstance(original_message, dict):
        emoji_logger.system_error(
            "process_message_with_agent",
            f"Mensagem original inválida ou None recebida para o telefone {phone}. Abortando.",
            received_message=original_message
        )
        return
    
    if media_data and media_data.get("error"):
        emoji_logger.system_warning(f"Erro na mídia para {phone}: {media_data['error']}")
        await evolution_client.send_text_message(phone, media_data["error"])
        return

    # Log de busca de dados
    emoji_logger.system_debug("Buscando lead e conversa existentes...")
    lead_task = asyncio.create_task(supabase_client.get_lead_by_phone(phone))
    conversation_task = asyncio.create_task(
        supabase_client.get_conversation_by_phone(phone)
    )
    results = await asyncio.gather(
        lead_task, conversation_task, return_exceptions=True
    )
    lead_result, conv_result = results

    if isinstance(lead_result, Exception):
        emoji_logger.system_error("Lead Fetch", f"Erro ao buscar lead: {lead_result}")
        lead = None
    else:
        lead = lead_result
        if lead:
            emoji_logger.system_success(
                f"Lead encontrado - ID: {lead.get('id')}, Nome: '{lead.get('name', 'N/A')}'"
            )
        else:
            emoji_logger.system_info("Nenhum lead existente encontrado - será criado novo")

    message_data = {
        "content": message_content,
        "role": "user",
        "sender": "user",
        "media_data": {
            "message_id": message_id, "raw_data": original_message
        }
    }
    emoji_logger.system_debug(f"Dados da mensagem estruturados: {json.dumps(message_data, indent=2)[:200]}...")

    if isinstance(conv_result, Exception):
        emoji_logger.system_error("Conversation Fetch", f"Erro ao buscar conversa: {conv_result}")
        conversation = None
    else:
        conversation = conv_result
        if conversation:
            emoji_logger.system_success(
                f"Conversa encontrada - ID: {conversation.get('id')}"
            )
        else:
            emoji_logger.system_info("Nenhuma conversa existente - será criada nova")

    if not conversation:
        emoji_logger.system_debug("Criando nova conversa...")
        conversation = await supabase_client.create_conversation(
            phone, lead["id"] if lead else None
        )
        emoji_logger.system_success(f"Nova conversa criada - ID: {conversation.get('id')}")

    if not conversation or not isinstance(conversation, dict) or "id" not in conversation:
        emoji_logger.system_error("Conversation Validation", f"Conversa inválida criada/buscada: {conversation}")
        raise ValueError(f"Conversa inválida: {conversation}")

    emoji_logger.system_info(f"Conversa validada - ID: {conversation['id']}, Phone: {phone}")

    message_data["conversation_id"] = conversation["id"]
    emoji_logger.system_debug("Salvando mensagem e cache...")
    save_tasks = [
        supabase_client.save_message(message_data),
        redis_client.cache_conversation(
            phone,
            {
                "lead_id": lead["id"] if lead else None,
                "conversation_id": conversation["id"],
                "last_message": message_content,
                "timestamp": datetime.now().isoformat()
            }
        )
    ]
    await asyncio.gather(*save_tasks, return_exceptions=True)
    emoji_logger.system_success("Mensagem e cache salvos")

    emoji_logger.webhook_process("Criando AGENTIC SDR Stateless...")
    try:
        agentic, execution_context = await create_agent_with_context(
            phone=phone,
            conversation_id=conversation["id"],
            media_data=media_data
        )
        emoji_logger.webhook_process("AGENTIC SDR Stateless pronto para uso")
    except HandoffActiveException:
        emoji_logger.system_info(f"Processamento interrompido para {phone} devido a handoff ativo.")
        return
    except Exception as e:
        emoji_logger.system_error("Agent Creation", f"Erro ao criar agente: {e}")
        raise HTTPException(
            status_code=503, detail="Agente temporariamente indisponível"
        )

    emoji_logger.system_debug("Processando mensagem com agente...")
    response_text, updated_lead_info = await agentic.process_message(
        message=message_content,
        execution_context=execution_context
    )
    emoji_logger.system_success(
        f"Resposta gerada pelo agente: '{response_text[:100]}...'"
    )

    final_response = extract_final_response(response_text)
    emoji_logger.system_debug(f"Resposta final extraída: '{final_response[:100]}...'")

    if "<SILENCE>" in final_response or "<SILENCIO>" in final_response:
        emoji_logger.system_info(f"Protocolo de silêncio ativado para {phone}. Nenhuma mensagem será enviada.")
        return

    if final_response:
        emoji_logger.system_debug("Salvando resposta do assistente...")
        assistant_message_data = {
            "content": final_response,
            "role": "assistant",
            "sender": "agent",
            "conversation_id": conversation["id"],
            "media_data": {} 
        }
        await supabase_client.save_message(assistant_message_data)
        emoji_logger.system_success("Resposta do assistente salva")

    if updated_lead_info and updated_lead_info.get("id"):
        emoji_logger.system_debug("Atualizando informações do lead...")
        updated_lead_info.pop("processed_message_count", None)
        await supabase_client.update_lead(updated_lead_info["id"], updated_lead_info)
        emoji_logger.system_success("Lead atualizado")
    
    if final_response:
        emoji_logger.system_debug("Enviando resposta via WhatsApp...")
        splitter = get_message_splitter_instance()
        message_chunks = splitter.split_message(final_response)
        for i, chunk in enumerate(message_chunks):
            emoji_logger.system_debug(f"Enviando chunk {i+1}/{len(message_chunks)}: '{chunk[:50]}...'")
            await evolution_client.send_text_message(phone, chunk)
        emoji_logger.system_success("Resposta enviada via WhatsApp")
    else:
        emoji_logger.system_warning(
            "A resposta final estava vazia, não enviando mensagem."
        )
    
    emoji_logger.conversation_success(
        f"✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - {phone}: "
        f"'{message_content[:50]}...' -> '{final_response[:50]}...'"
    )