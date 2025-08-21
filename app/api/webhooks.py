"""
Webhooks API - Recebe eventos externos (WhatsApp, Kommo)
Processa mensagens recebidas e eventos do CRM
"""

from datetime import datetime
from typing import Dict, Any, Optional
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
    return None


async def _handle_media_message(
        message: Dict[str, Any]
) -> Optional[Dict[str, Any]]:
    """Lida com o download e processamento de mídia."""
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
    Extrai apenas a resposta final das tags <RESPOSTA_FINAL>
    """
    emoji_logger.system_info(
        f"🔎 extract_final_response recebeu: "
        f"tipo={type(full_response)}, "
        f"tamanho={len(full_response) if full_response else 0}, "
        f"primeiros 200 chars: "
        f"{full_response[:200] if full_response else 'VAZIO'}"
    )

    try:
        patterns = [
            r'<RESPOSTA_FINAL>(.*?)</RESPOSTA_FINAL>',
            r'<RESPOSTAFINAL>(.*?)</RESPOSTAFINAL>',
            r'<RESPOSTA[_ ]FINAL[>:]'
        ]

        match = None
        for pattern in patterns:
            match = re.search(
                pattern, full_response, re.DOTALL | re.IGNORECASE
            )
            if match:
                break

        if match:
            final_response = match.group(1).strip()
            final_response = re.sub(r'<[^>]*>', '', final_response)
            final_response = re.sub(r'</?\w+[^>]*>', '', final_response)
            final_response = re.sub(r'^\s*[.,:;]*\s*', '', final_response)
            final_response = final_response.strip()

            emoji_logger.system_debug(
                f"✅ Resposta final extraída e limpa: {final_response[:50]}..."
            )

            forbidden_terms = [
                'cpf', 'c.p.f', 'cadastro de pessoa', 'documento',
                'rg', 'r.g', 'identidade', 'cnh', 'c.n.h',
                'carteira de motorista', 'carteira de identidade',
                'dados bancários', 'conta bancária', 'senha',
                'cartão de crédito', 'dados do cartão'
            ]

            response_lower = final_response.lower()
            contains_forbidden = False
            for term in forbidden_terms:
                pattern = r'\b' + re.escape(term) + r'\b'
                if re.search(pattern, response_lower):
                    contains_forbidden = True
                    break

            if contains_forbidden:
                emoji_logger.system_warning(
                    "🚨 ALERTA: Resposta contém solicitação de dados proibidos!"
                )
                emoji_logger.system_warning(
                    f"Resposta bloqueada: {final_response[:100]}..."
                )
                safe_response = (
                    "Ótimo! Para eu fazer uma proposta personalizada de "
                    "economia, preciso apenas saber o valor da sua conta de "
                    "luz. Quanto você está pagando em média?"
                )
                emoji_logger.system_debug(
                    "✅ Resposta substituída por versão segura"
                )
                return safe_response

            if (not final_response or final_response.strip() == "" or
                    final_response.strip().lower() == "none"):
                emoji_logger.system_error(
                    "Extract",
                    f"⚠️ extract_final_response retornaria vazio/None: "
                    f"'{final_response}'"
                )
                return "Oi! Como posso ajudar você com energia solar? ☀️"

            return final_response
        else:
            emoji_logger.system_error(
                "extract_final_response",
                "🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO"
            )
            emoji_logger.system_error(
                "extract_final_response",
                f"📝 Conteúdo original (primeiros 200 chars): "
                f"{full_response[:200]}..."
            )
            safe_fallback = "Oi! Me dê só um minutinho que já te respondo!"
            emoji_logger.system_warning(
                "🔒 Usando resposta segura para evitar vazamento de "
                "raciocínio interno"
            )
            return safe_fallback

    except Exception as e:
        emoji_logger.system_error(
            "extract_final_response",
            f"🚨 ERRO CRÍTICO ao extrair resposta: {e}"
        )
        emoji_logger.system_error(
            "extract_final_response",
            f"📝 Conteúdo que causou erro (primeiros 200 chars): "
            f"{full_response[:200] if full_response else 'None'}..."
        )
        emergency_fallback = "Oi! Me dê só um momento que já te retorno! 🔧"
        emoji_logger.system_warning(
            "🔒 Usando resposta de emergência para evitar vazamento em "
            "caso de erro"
        )
        return emergency_fallback


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
        conversation_id: str = None
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


@router.post("/whatsapp/{event_type}")
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


async def process_new_message(data: Dict[str, Any]):
    """Processa nova mensagem recebida"""
    try:
        emoji_logger.webhook_process("Iniciando processamento de nova mensagem")

        if not data:
            emoji_logger.system_warning("Payload vazio")
            return

        message = data
        key = message.get("key", {})
        remote_jid = key.get("remoteJid", "")
        from_me = key.get("fromMe", False)
        message_id = key.get("id", "")

        if from_me:
            emoji_logger.webhook_process("Mensagem própria ignorada")
            return

        phone = remote_jid.split("@")[0] if "@" in remote_jid else remote_jid

        if "@g.us" in remote_jid:
            emoji_logger.webhook_process(
                f"Mensagem de grupo ignorada: {remote_jid}"
            )
            return

        emoji_logger.webhook_process(f"Processando mensagem de {phone}")
        message_content = extract_message_content(message)

        if not message_content:
            emoji_logger.system_warning(f"Mensagem sem conteúdo de {phone}")
            logger.debug(f"Payload completo: {message}")
            return

        emoji_logger.evolution_receive(
            phone, "text", preview=message_content[:100]
        )

        if not await redis_client.check_rate_limit(
            f"message:{phone}", max_requests=10, window_seconds=60
        ):
            emoji_logger.system_warning(f"Rate limit excedido para {phone}")
            await evolution_client.send_text_message(
                phone,
                "⚠️ Você está enviando muitas mensagens. "
                "Por favor, aguarde um momento.",
                delay=1
            )
            return

        if settings.enable_message_buffer:
            buffer = get_message_buffer_instance()
            await buffer.add_message(
                phone=phone,
                content=message_content,
                message_data=message
            )
        else:
            await process_message_with_agent(
                phone=phone,
                message_content=message_content,
                original_message=message,
                message_id=message_id
            )

    except Exception as e:
        emoji_logger.system_error("Webhook Message Processing", str(e))
        logger.exception("Erro detalhado no processamento:")


async def process_message_with_agent(
    phone: str,
    message_content: str,
    original_message: Dict[str, Any],
    message_id: str
):
    """Processa mensagem com o agente AGENTIC SDR"""
    from app.integrations.supabase_client import supabase_client
    media_data = await _handle_media_message(original_message)
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

    if not lead:
        lead = await supabase_client.create_lead({
            "phone_number": phone,
            "current_stage": "INITIAL_CONTACT",
            "qualification_status": "PENDING",
            "interested": True,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
        emoji_logger.supabase_insert("leads", 1, phone=phone)

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
            conversation_id=conversation["id"]
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

    response_text = await agentic.process_message(
        message=message_content,
        execution_context=execution_context
    )

    final_response = extract_final_response(response_text)
    
    if final_response:
        await evolution_client.send_text_message(phone, final_response)
    else:
        emoji_logger.system_warning(
            "A resposta final estava vazia, não enviando mensagem."
        )
