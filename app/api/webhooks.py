"""
Webhooks API - Recebe eventos externos (WhatsApp, Kommo)
Processa mensagens recebidas e eventos do CRM
"""

from datetime import datetime
from typing import Dict, Any, Optional, List
import asyncio
import re

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

router = APIRouter(prefix="/webhook", tags=["webhooks"])

agno_detector = AGNOMediaDetector()


def extract_message_content(message: Dict[str, Any]) -> Optional[str]:
    """Extrai o conteúdo de texto de vários tipos de mensagem."""
    msg_content = message.get("message", {})
    if not msg_content:
        return None

    if "conversation" in msg_content:
        return msg_content["conversation"]
    if "extendedTextMessage" in msg_content:
        return msg_content["extendedTextMessage"].get("text")
    if "textMessage" in msg_content:
        return msg_content["textMessage"].get("text")
    
    # Adiciona extração de legenda para mídias
    for media_type in ["imageMessage", "videoMessage", "documentMessage"]:
        if media_type in msg_content:
            return msg_content[media_type].get("caption")
            
    return None


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
                # A configuração do webhook (webhook_base64: True) deve enviar a mídia em base64.
                # A Evolution API normalmente usa a chave "media" para isso.
                base64_content = media_payload.get("media") or media_payload.get("body")

                if base64_content:
                    emoji_logger.system_debug(f"Mídia Base64 extraída diretamente do payload para {msg_type}")
                    return {
                        "type": media_type,
                        "content": base64_content,
                        "mimetype": media_payload.get("mimetype"),
                    }
                else:
                    # Fallback OTIMIZADO: Usa o endpoint específico para buscar a mídia em base64
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

def sanitize_final_response(text: str) -> str:
    """
    Sanitiza agressivamente o texto final para garantir conformidade total
    com as regras de formatação do WhatsApp.
    """
    if not isinstance(text, str):
        return ""

    emoji_pattern = re.compile(
        "["
        u"\U0001f600-\U0001f64f"
        u"\U0001f300-\U0001f5ff"
        u"\U0001f680-\U0001f6ff"
        u"\U0001f1e0-\U0001f1ff"
        u"\u2600-\u26ff"
        u"\u2700-\u27bf"
        u"\u2300-\u23ff"
        u"\ufe0f"
        u"\u200d"
        "]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub(r'', text)
    text = re.sub(r'\*{2,}', '', text)
    text = re.sub(r'[_~`]', '', text)

    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        cleaned_line = re.sub(
            r'^\s*\d+\.\s*|^\s*[-*]\s*', '', line.strip()
        )
        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    text = ' '.join(cleaned_lines)
    text = ' '.join(text.split())
    text = text.strip()

    if not text or text.lower() == "none":
        emoji_logger.system_error(
            "Sanitize",
            "⚠️ sanitize_final_response resultaria em vazio/None"
        )
        return "Oi! Como posso ajudar você hoje? 😊"

    return text


def extract_final_response(full_response: str) -> str:
    """
    Extrai e limpa o conteúdo dentro da tag <RESPOSTA_FINAL>, removendo
    outras tags de raciocínio e garantindo uma saída segura.
    """
    if not isinstance(full_response, str):
        return "Desculpe, ocorreu um erro inesperado."

    # Tenta extrair o conteúdo da tag principal
    match = re.search(r'<RESPOSTA_FINAL>(.*?)</RESPOSTA_FINAL>', full_response, re.DOTALL | re.IGNORECASE)
    
    if match:
        final_response = match.group(1).strip()
    else:
        # Fallback: se a tag não for encontrada, loga um aviso e limpa o texto de outras tags conhecidas
        emoji_logger.system_warning(
            "Tag <RESPOSTA_FINAL> não encontrada na resposta do LLM.",
            raw_response=full_response[:500]  # Loga os primeiros 500 caracteres da resposta bruta
        )
        temp_response = re.sub(r'</?analise_interna>.*?</analise_interna>', '', full_response, flags=re.DOTALL | re.IGNORECASE)
        temp_response = re.sub(r'</?RESPOSTA_FINAL>', '', temp_response, flags=re.IGNORECASE)
        
        # Se ainda houver tags, a resposta é muito incerta. Retorna um fallback seguro.
        if '<' in temp_response and '>' in temp_response:
            emoji_logger.system_error("extract_final_response", "Nenhuma tag <RESPOSTA_FINAL> clara e ainda há outras tags. Usando fallback.")
            return "Estou finalizando sua solicitação. Um momento."
        final_response = temp_response.strip()

    # Se a resposta final estiver vazia ou for "none", retorna um cumprimento padrão.
    if not final_response or final_response.lower() == "none":
        return "Oi! Como posso te ajudar com energia solar? ☀️"

    return final_response


def detect_media_format(media_data: Any) -> str:
    """Detecta o formato da mídia recebida"""
    if media_data is None:
        return 'unknown'

    if isinstance(media_data, str):
        if media_data.startswith("data:"):
            logger.info("Formato detectado: Data URL")
            return 'data_url'
        elif media_data.startswith(("http://", "https://")):
            logger.info("Formato detectado: URL para download")
            return 'url'
        elif len(media_data) > 50:
            try:
                import base64 as b64
                test_sample = media_data[:100]
                b64.b64decode(test_sample)
                logger.info("Formato detectado: Base64 válido")
                return 'base64'
            except Exception:
                logger.info("Formato detectado: String não-base64")
                return 'unknown'
        else:
            return 'unknown'
    elif isinstance(media_data, bytes):
        logger.info(f"Formato detectado: Bytes ({len(media_data)} bytes)")
        return 'bytes'
    else:
        logger.info(f"Formato desconhecido: {type(media_data)}")
        return 'unknown'


def extract_base64_from_data_url(data_url: str) -> str:
    """Extrai o base64 de uma data URL"""
    if ";base64," in data_url:
        return data_url.split(";base64,")[1]
    return data_url


async def create_agent_with_context(
        phone: str,
        conversation_id: str = None,
        media_data: Optional[Dict[str, Any]] = None
) -> tuple:
    """Cria agente stateless com contexto completo carregado"""
    from app.integrations.supabase_client import supabase_client
    emoji_logger.webhook_process("🏭 Criando agente stateless com contexto...")

    try:
        lead_data = await supabase_client.get_lead_by_phone(phone)
        conversation_history = []
        if conversation_id:
            conversation_history = (
                await supabase_client.get_conversation_messages(
                    conversation_id,
                    limit=500
                )
            )

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
            lead_name=(
                lead_data.get('name') if lead_data else 'Não identificado'
            )
        )

        return agent, execution_context

    except Exception as e:
        emoji_logger.system_error(
            "Webhook",
            f"Erro ao criar agente com contexto: {e}"
        )
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
        elif event in ["CHATS_UPDATE", "CONTACTS_UPDATE"]:
            logger.info(f"{event} update recebido: {data}")
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
            # Garante que 'message' seja um dicionário antes de prosseguir
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
                emoji_logger.webhook_process(
                    f"Mensagem de grupo ignorada: {remote_jid}"
                )
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
    
    if media_data and media_data.get("error"):
        await evolution_client.send_text_message(phone, media_data["error"])
        return

    lead_task = asyncio.create_task(supabase_client.get_lead_by_phone(phone))
    conversation_task = asyncio.create_task(
        supabase_client.get_conversation_by_phone(phone)
    )
    results = await asyncio.gather(
        lead_task, conversation_task, return_exceptions=True
    )
    lead_result, conv_result = results

    if isinstance(lead_result, Exception):
        emoji_logger.system_error(
            "Lead Fetch", f"Erro ao buscar lead: {lead_result}"
        )
        lead = None
    else:
        lead = lead_result

    message_data = {
        "content": message_content,
        "role": "user",
        "sender": "user",
        "media_data": {
            "message_id": message_id, "raw_data": original_message
        }
    }

    if isinstance(conv_result, Exception):
        emoji_logger.system_error(
            "Conversation Fetch", f"Erro ao buscar conversa: {conv_result}"
        )
        conversation = None
    else:
        conversation = conv_result

    if not conversation:
        conversation = await supabase_client.create_conversation(
            phone, lead["id"]
        )

    if not conversation or not isinstance(
            conversation,
            dict
    ) or "id" not in conversation:
        emoji_logger.system_error(
            "Conversation Validation",
            f"Conversa inválida criada/buscada: {conversation}"
        )
        raise ValueError(f"Conversa inválida: {conversation}")

    emoji_logger.system_info(
        f"Conversa validada - ID: {conversation['id']}, Phone: {phone}"
    )

    message_data["conversation_id"] = conversation["id"]
    save_tasks = [
        supabase_client.save_message(message_data),
        redis_client.cache_conversation(
            phone,
            {
                "lead_id": lead["id"],
                "conversation_id": conversation["id"],
                "last_message": message_content,
                "timestamp": datetime.now().isoformat()
            }
        )
    ]
    await asyncio.gather(*save_tasks, return_exceptions=True)

    emoji_logger.webhook_process("Criando AGENTIC SDR Stateless...")
    try:
        agentic, execution_context = await create_agent_with_context(
            phone=phone,
            conversation_id=conversation["id"],
            media_data=media_data
        )
        emoji_logger.webhook_process("AGENTIC SDR Stateless pronto para uso")
    except Exception as e:
        emoji_logger.system_error(
            "Agent Creation", f"Erro ao criar agente: {e}"
        )
        raise HTTPException(
            status_code=503, detail="Agente temporariamente indisponível"
        )

    if not conversation or not conversation.get("id"):
        emoji_logger.system_error(
            "WEBHOOK",
            f"❌ Conversation inválida! Lead: {lead}, Phone: {phone}"
        )
        try:
            conversation = await supabase_client.create_conversation(
                phone, lead["id"] if lead else None
            )
            emoji_logger.system_info(
                f"✅ Nova conversa criada: {conversation.get('id', 'N/A')}"
            )
        except Exception as conv_error:
            emoji_logger.system_error(
                "WEBHOOK", f"❌ Falha ao criar conversa: {conv_error}"
            )
            return

    response_text, updated_lead_info = await agentic.process_message(
        message=message_content,
        execution_context=execution_context
    )

    final_response = extract_final_response(response_text)

    # Salva a resposta do assistente no banco de dados
    if final_response:
        assistant_message_data = {
            "content": final_response,
            "role": "assistant",
            "sender": "agent",
            "conversation_id": conversation["id"],
            "media_data": {} 
        }
        await supabase_client.save_message(assistant_message_data)

    if updated_lead_info and updated_lead_info.get("id"):
        # Remove a chave transitória antes de salvar no banco
        updated_lead_info.pop("processed_message_count", None)
        await supabase_client.update_lead(updated_lead_info["id"], updated_lead_info)
    
    if final_response:
        splitter = get_message_splitter_instance()
        message_chunks = splitter.split_message(final_response)
        for chunk in message_chunks:
            await evolution_client.send_text_message(phone, chunk)
    else:
        emoji_logger.system_warning(
            "A resposta final estava vazia, não enviando mensagem."
        )
