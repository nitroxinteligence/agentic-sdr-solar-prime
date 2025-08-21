"""
Webhooks API - Recebe eventos externos (WhatsApp, Kommo)
Processa mensagens recebidas e eventos do CRM
"""

from datetime import datetime, timezone
from typing import Dict, Any, Optional
import json
import asyncio
import re

from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
from loguru import logger

from app.config import settings
from app.utils.logger import emoji_logger
from app.integrations.supabase_client import SupabaseClient
from app.integrations.redis_client import redis_client
from app.integrations.evolution import evolution_client
from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.services.message_buffer import MessageBuffer
from app.utils.agno_media_detection import AGNOMediaDetector

router = APIRouter(prefix="/webhook", tags=["webhooks"])  # Mudado para /webhook (sem 's')

# REMOVIDO: Instância global do AGENTIC SDR - agora criamos nova instância por requisição

# Instâncias dos serviços de mensagem
message_buffer = None
message_splitter = None

# Instância do detector AGNO para validação de mídia
agno_detector = AGNOMediaDetector()

# FUNÇÕES AUXILIARES DE WEBHOOK (REIMPLEMENTADAS)

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

async def _handle_media_message(message: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Lida com o download e processamento de mídia."""
    # Esta função pode ser expandida para baixar e processar mídia
    return None

async def process_connection_update(data: Dict[str, Any]):
    """Processa atualizações de status da conexão."""
    status = data.get("status")
    emoji_logger.system_info(f"Connection status update: {status}")
    await redis_client.set("whatsapp:connection_status", status)

async def process_qrcode_update(data: Dict[str, Any]):
    """Processa atualizações de QR code."""
    emoji_logger.system_info("QR code updated. Scan required.")
    # Lógica para notificar sobre o QR code pode ser adicionada aqui

async def process_message_update(data: Dict[str, Any]):
    """Processa atualizações de status de mensagem (enviada, lida, etc.)."""
    update = data.get("update", {})
    status = update.get("status")
    msg_id = update.get("key", {}).get("id")
    if status and msg_id:
        emoji_logger.system_debug(f"Message {msg_id} status updated to {status}")

async def process_presence_update(data: Dict[str, Any]):
    """Processa atualizações de presença (digitando, online, etc.)."""
    remote_jid = data.get("remoteJid")
    presence = data.get("presence")
    if remote_jid and presence:
        emoji_logger.system_debug(f"Presence update from {remote_jid}: {presence}")

# FIM DAS FUNÇÕES AUXILIARES


def sanitize_final_response(text: str) -> str:
    """
    Sanitiza agressivamente o texto final para garantir conformidade total 
    com as regras de formatação do WhatsApp, removendo todo o markdown e emojis.
    
    Args:
        text: Texto a ser sanitizado
        
    Returns:
        Texto limpo sem formatação incorreta
    """
    if not isinstance(text, str):
        return ""

    # 1. Remover emojis (padrão Unicode abrangente)
    emoji_pattern = re.compile("["
                               u"\U0001f600-\U0001f64f"  # emoticons
                               u"\U0001f300-\U0001f5ff"  # symbols & pictographs
                               u"\U0001f680-\U0001f6ff"  # transport & map symbols
                               u"\U0001f1e0-\U0001f1ff"  # flags (ios)
                               u"\u2600-\u26ff"          # miscellaneous symbols
                               u"\u2700-\u27bf"          # dingbats
                               u"\u2300-\u23ff"          # misc technical
                               u"\ufe0f"                # variation selector
                               u"\u200d"                # zero width joiner
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    # 2. Remover todo o markdown (negrito duplo, itálico, etc.)
    # Remove **, *, _, __, ~, `, etc.
    text = re.sub(r'\*{2,}', '', text)  # Remove ** (markdown duplo)
    text = re.sub(r'[_~`]', '', text)   # Remove outros markdowns

    # 3. Remover enumerações e juntar linhas
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove padrões como "1. ", "- ", "* " no início da linha
        cleaned_line = re.sub(r'^\s*\d+\.\s*|^\s*[-*]\s*', '', line.strip())
        if cleaned_line:
            cleaned_lines.append(cleaned_line)
    
    text = ' '.join(cleaned_lines)

    # 4. Remover espaços duplos e limpar
    text = ' '.join(text.split())
    text = text.strip()
    
    # VERIFICAÇÃO FINAL DE SEGURANÇA
    if not text or text.lower() == "none":
        emoji_logger.system_error("Sanitize", f"⚠️ sanitize_final_response resultaria em vazio/None")
        return "Oi! Como posso ajudar você hoje? 😊"
    
    return text

def extract_final_response(full_response: str) -> str:
    """
    Extrai apenas a resposta final das tags <RESPOSTA_FINAL>
    
    Args:
        full_response: Resposta completa do LLM incluindo raciocínio
        
    Returns:
        Apenas o conteúdo dentro das tags RESPOSTA_FINAL
    """
    # Log adicional para debug
    emoji_logger.system_info(f"🔎 extract_final_response recebeu: tipo={type(full_response)}, tamanho={len(full_response) if full_response else 0}, primeiros 200 chars: {full_response[:200] if full_response else 'VAZIO'}")
    
    try:
        # Busca o conteúdo entre as tags - aceita variações
        patterns = [
            r'<RESPOSTA_FINAL>(.*?)</RESPOSTA_FINAL>',
            r'<RESPOSTAFINAL>(.*?)</RESPOSTAFINAL>',
            r'<RESPOSTA[_ ]FINAL[>:](.*?)$'  # Para casos onde a tag não fecha
        ]
        
        match = None
        for pattern in patterns:
            match = re.search(pattern, full_response, re.DOTALL | re.IGNORECASE)
            if match:
                break
        
        if match:
            # Extrai e limpa o conteúdo
            final_response = match.group(1).strip()
            
            # LIMPEZA EXTRA: Remover qualquer tag ou lixo que vazou
            final_response = re.sub(r'<[^>]*>', '', final_response)  # Remove tags HTML/XML
            final_response = re.sub(r'</?\w+[^>]*>', '', final_response)  # Remove tags malformadas
            final_response = re.sub(r'^\s*[.,:;]*\s*', '', final_response)  # Remove pontuação inicial
            final_response = final_response.strip()
            
            emoji_logger.system_debug(f"✅ Resposta final extraída e limpa: {final_response[:50]}...")
            
            # 🚨 VALIDAÇÃO DE SEGURANÇA: Verificar se está pedindo dados proibidos
            forbidden_terms = [
                'cpf', 'c.p.f', 'cadastro de pessoa', 'documento',
                'rg', 'r.g', 'identidade', 'cnh', 'c.n.h',
                'carteira de motorista', 'carteira de identidade',
                'dados bancários', 'conta bancária', 'senha',
                'cartão de crédito', 'dados do cartão'
            ]
            
            response_lower = final_response.lower()
            
            # CORREÇÃO: Usar regex para detectar palavras completas, não substrings
            contains_forbidden = False
            for term in forbidden_terms:
                # \b marca limites de palavra para evitar falsos positivos
                pattern = r'\b' + re.escape(term) + r'\b'
                if re.search(pattern, response_lower):
                    contains_forbidden = True
                    break
            
            if contains_forbidden:
                emoji_logger.system_warning("🚨 ALERTA: Resposta contém solicitação de dados proibidos!")
                emoji_logger.system_warning(f"Resposta bloqueada: {final_response[:100]}...")
                
                # Retornar resposta segura
                safe_response = "Ótimo! Para eu fazer uma proposta personalizada de economia, preciso apenas saber o valor da sua conta de luz. Quanto você está pagando em média?"
                emoji_logger.system_debug(f"✅ Resposta substituída por versão segura")
                return safe_response
            
            # VERIFICAÇÃO FINAL: Nunca retornar None ou vazio
            if not final_response or final_response.strip() == "" or final_response.strip().lower() == "none":
                emoji_logger.system_error("Extract", f"⚠️ extract_final_response retornaria vazio/None: '{final_response}'")
                return "Oi! Como posso ajudar você com energia solar? ☀️"
            
            return final_response
        else:
            # 🚨 CORREÇÃO CRÍTICA: NUNCA retornar conteúdo bruto ou raciocínio interno
            emoji_logger.system_error("extract_final_response", "🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO")
            emoji_logger.system_error("extract_final_response", f"📝 Conteúdo original (primeiros 200 chars): {full_response[:200]}...")
            
            # ✅ RESPOSTA SEGURA: fallback controlado que não vaza raciocínio
            safe_fallback = "Oi! Me dê só um minutinho que já te respondo!"
            
            emoji_logger.system_warning(f"🔒 Usando resposta segura para evitar vazamento de raciocínio interno")
            return safe_fallback
                
    except Exception as e:
        emoji_logger.system_error("extract_final_response", f"🚨 ERRO CRÍTICO ao extrair resposta: {e}")
        emoji_logger.system_error("extract_final_response", f"📝 Conteúdo que causou erro (primeiros 200 chars): {full_response[:200] if full_response else 'None'}...")
        
        # 🚨 CORREÇÃO CRÍTICA: NUNCA retornar resposta completa em caso de erro
        # ✅ RESPOSTA SEGURA: fallback de emergência que não vaza raciocínio
        emergency_fallback = "Oi! Me dê só um momento que já te retorno! 🔧"
        
        emoji_logger.system_warning(f"🔒 Usando resposta de emergência para evitar vazamento em caso de erro")
        return emergency_fallback

def detect_media_format(media_data: Any) -> str:
    """
    Detecta o formato da mídia recebida
    
    Args:
        media_data: Dados da mídia em qualquer formato
        
    Returns:
        Tipo do formato: 'base64', 'data_url', 'url', 'bytes', 'unknown'
    """
    if media_data is None:
        return 'unknown'
    
    if isinstance(media_data, str):
        # Verifica se é uma data URL
        if media_data.startswith("data:"):
            logger.info("Formato detectado: Data URL")
            return 'data_url'
        # Verifica se é uma URL HTTP/HTTPS
        elif media_data.startswith(("http://", "https://")):
            logger.info("Formato detectado: URL para download")
            return 'url'
        # Se é uma string longa, provavelmente é base64
        elif len(media_data) > 50:  # Threshold reduzido para pegar thumbnails pequenos
            # Tenta validar se é base64 válido
            try:
                # Tenta decodificar um pequeno pedaço para verificar
                import base64 as b64
                test_sample = media_data[:100] if len(media_data) >= 100 else media_data
                test = b64.b64decode(test_sample)
                logger.info("Formato detectado: Base64 válido")
                return 'base64'
            except:
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
    """
    Extrai o base64 de uma data URL
    
    Args:
        data_url: Data URL completa (ex: data:image/jpeg;base64,...)
        
    Returns:
        Apenas a parte base64
    """
    if ";base64," in data_url:
        return data_url.split(";base64,")[1]
    return data_url

# REMOVIDO: Cache global do agente - causava deadlock com múltiplas mensagens
# _cached_agent = None
# _agent_lock = asyncio.Lock()

async def create_agent_with_context(phone: str, conversation_id: str = None) -> tuple:
    """
    Cria agente stateless com contexto completo carregado
    
    Args:
        phone: Número do telefone
        conversation_id: ID da conversa (opcional)
        
    Returns:
        Tupla (agent, execution_context)
    """
    emoji_logger.webhook_process("🏭 Criando agente stateless com contexto...")
    
    try:
        # Carregar histórico e informações em paralelo
        from app.integrations.supabase_client import supabase_client
        
        # Carregar dados em paralelo
        lead_data = await supabase_client.get_lead_by_phone(phone)
        
        conversation_history = []
        if conversation_id:
            conversation_history = await supabase_client.get_conversation_messages(conversation_id, limit=500)
        
        # Criar contexto de execução completo
        execution_context = {
            "phone": phone,
            "lead_info": lead_data or {},
            "conversation_id": conversation_id,
            "conversation_history": conversation_history or [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Criar agente conforme configuração (stateless ou singleton)
        use_stateless = settings.use_stateless_mode
        
        if use_stateless:
            agent = AgenticSDRStateless()
            await agent.initialize()
        else:
            # For singleton, we should have a global instance
            # For now, let's just create a new instance
            agent = AgenticSDRStateless()
            await agent.initialize()
        
        emoji_logger.system_ready(
            "✅ Agente stateless criado com contexto",
            history_count=len(conversation_history),
            lead_name=lead_data.get('name') if lead_data else 'Não identificado'
        )
        
        return agent, execution_context
        
    except Exception as e:
        emoji_logger.system_error("Webhook", f"Erro ao criar agente com contexto: {e}")
        raise

def get_message_buffer_instance():
    """Obtém instância do Message Buffer (deve ser inicializado no startup)"""
    from app.services.message_buffer import get_message_buffer
    buffer = get_message_buffer()
    if buffer is None:
        # Fallback para criação se não inicializado (não deveria acontecer)
        logger.warning("Message Buffer não foi inicializado no startup!")
        buffer = MessageBuffer(
            timeout=settings.message_buffer_timeout,
            max_size=10
        )
        set_message_buffer(buffer)
    return buffer

def get_message_splitter_instance():
    """Obtém instância do Message Splitter (deve ser inicializado no startup)"""
    from app.services.message_splitter import get_message_splitter
    splitter = get_message_splitter()
    if splitter is None:
        # Fallback para criação se não inicializado (não deveria acontecer)
        logger.warning("Message Splitter não foi inicializado no startup!")
        splitter = MessageSplitter(
            max_length=settings.message_max_length,
            add_indicators=settings.message_add_indicators
        )
        set_message_splitter(splitter)
    return splitter

@router.post("/whatsapp/{event_type}")
async def whatsapp_dynamic_webhook(
    event_type: str,
    request: Request,
    background_tasks: BackgroundTasks
):
    """
    Webhook dinâmico para eventos específicos do WhatsApp
    Captura URLs como /webhook/whatsapp/messages-upsert
    """
    try:
        # Converter event_type de kebab-case para UPPER_SNAKE_CASE
        # Ex: messages-upsert -> MESSAGES_UPSERT
        event = event_type.upper().replace("-", "_")
        
        # Recebe dados do webhook
        data = await request.json()
        
        # Log do evento recebido
        emoji_logger.webhook_receive(f"/whatsapp/{event_type}", "evolution-api", event=event)
        
        # Processa eventos específicos baseado no tipo
        if event == "MESSAGES_UPSERT":
            # Nova mensagem recebida - passar apenas o 'data' interno
            # Evolution API v2: event está no nível superior, dados em 'data'
            actual_data = data.get("data", data)  # Pega 'data' se existir, senão usa o próprio data
            background_tasks.add_task(
                process_new_message,
                actual_data
            )
            
        elif event == "CONNECTION_UPDATE":
            # Status da conexão mudou
            await process_connection_update(data)
            
        elif event == "QRCODE_UPDATED":
            # QR Code atualizado
            await process_qrcode_update(data)
            
        elif event == "MESSAGES_UPDATE":
            # Status de mensagem atualizado (entregue, lida, etc)
            await process_message_update(data)
            
        elif event == "PRESENCE_UPDATE":
            # Status de presença (online, digitando, etc)
            await process_presence_update(data)
            
        elif event == "CHATS_UPDATE":
            # Atualização de chats
            logger.info(f"Chat update recebido: {data}")
            # TODO: Implementar processamento de chats_update se necessário
            
        elif event == "CONTACTS_UPDATE":
            # Atualização de contatos
            logger.info(f"Contacts update recebido: {data}")
            # TODO: Implementar processamento de contacts_update se necessário
        
        else:
            logger.warning(f"Evento não reconhecido: {event}")
            
        return {"status": "ok", "event": event}
        
    except Exception as e:
        emoji_logger.system_error(f"Webhook WhatsApp {event_type}", str(e))
        # Não lança exceção para não travar o webhook
        return {"status": "error", "message": str(e)}

@router.post("/evolution")
async def evolution_webhook(
    request: Request,
    background_tasks: BackgroundTasks
):
    """
    Webhook principal da Evolution API
    Recebe todos os eventos do WhatsApp
    """
    try:
        # Recebe dados do webhook
        data = await request.json()
        
        # Log do evento recebido
        event = data.get("event")
        instance = data.get("instance")
        
        emoji_logger.webhook_receive("/evolution", "evolution-api", event=event, instance=instance)
        
        # Processa eventos específicos
        if event == "MESSAGES_UPSERT":
            # Nova mensagem recebida - Evolution API v2
            actual_data = data.get("data", data)
            background_tasks.add_task(
                process_new_message,
                actual_data
            )
            
        elif event == "CONNECTION_UPDATE":
            # Status da conexão mudou
            await process_connection_update(data.get("data", {}))
            
        elif event == "QRCODE_UPDATED":
            # QR Code atualizado
            await process_qrcode_update(data.get("data", {}))
            
        elif event == "MESSAGES_UPDATE":
            # Status de mensagem atualizado (entregue, lida, etc)
            await process_message_update(data.get("data", {}))
            
        elif event == "PRESENCE_UPDATE":
            # Status de presença (online, digitando, etc)
            await process_presence_update(data.get("data", {}))
            
        return {"status": "ok", "event": event}
        
    except Exception as e:
        emoji_logger.system_error("Webhook Evolution", str(e))
        raise HTTPException(status_code=500, detail=str(e))

async def process_new_message(data: Dict[str, Any]):
    """
    Processa nova mensagem recebida
    
    Args:
        data: Dados da mensagem (Evolution API v2)
    """
    try:
        emoji_logger.webhook_process("Iniciando processamento de nova mensagem")
        
        # Evolution API v2: mensagem vem diretamente em 'data'
        # Não é mais um array 'messages', é um objeto direto
        if not data:
            emoji_logger.system_warning("Payload vazio")
            return
        
        # A mensagem ESTÁ diretamente no data (não em data.messages)
        message = data
        emoji_logger.webhook_process(f"Mensagem extraída: {message.get('key', {}).get('id', 'unknown')}")
        
        # Informações básicas
        key = message.get("key", {})
        remote_jid = key.get("remoteJid", "")
        from_me = key.get("fromMe", False)
        message_id = key.get("id", "")
        
        # Ignora mensagens enviadas por nós
        if from_me:
            emoji_logger.webhook_process("Mensagem própria ignorada")
            return
        
        # Extrai número do telefone
        phone = remote_jid.split("@")[0] if "@" in remote_jid else remote_jid
        
        # Verifica se é grupo
        is_group = "@g.us" in remote_jid
        if is_group:
            # Por enquanto, ignora mensagens de grupo
            emoji_logger.webhook_process(f"Mensagem de grupo ignorada: {remote_jid}")
            return
        
        emoji_logger.webhook_process(f"Processando mensagem de {phone}")
        
        # Extrai conteúdo da mensagem
        message_content = extract_message_content(message)
        
        if not message_content:
            emoji_logger.system_warning(f"Mensagem sem conteúdo de {phone}")
            # Log do payload para debug
            logger.debug(f"Payload completo: {message}")
            return
        
        emoji_logger.evolution_receive(phone, "text", preview=message_content[:100])
        
        # Verifica rate limit
        if not await redis_client.check_rate_limit(
            f"message:{phone}",
            max_requests=10,
            window_seconds=60
        ):
            emoji_logger.system_warning(f"Rate limit excedido para {phone}")
            await evolution_client.send_text_message(
                phone,
                "⚠️ Você está enviando muitas mensagens. Por favor, aguarde um momento.",
                delay=1
            )
            return
        
        # Se o buffer está habilitado, adiciona mensagem ao buffer
        if settings.enable_message_buffer:
            buffer = get_message_buffer_instance()
            
            # Adiciona mensagem ao buffer (sem callback complexo)
            await buffer.add_message(
                phone=phone,
                content=message_content,
                message_data=message
            )
            # O buffer chama process_message_with_agent internamente quando pronto
        else:
            # Processa imediatamente sem buffer
            await process_message_with_agent(
                phone=phone,
                message_content=message_content,
                original_message=message,
                message_id=message_id
            )
            
    except Exception as e:
        emoji_logger.system_error("Webhook Message Processing", str(e))
        logger.exception("Erro detalhado no processamento:")
        # Não lança exceção para não travar o webhook

async def process_message_with_agent(
    phone: str,
    message_content: str,
    original_message: Dict[str, Any],
    message_id: str
):
    """
    Processa mensagem com o agente AGENTIC SDR
    
    Args:
        phone: Número do telefone
        message_content: Conteúdo da mensagem (pode ser combinado)
        original_message: Dados originais da mensagem
        message_id: ID da mensagem
    """
    # Preparar mídia se houver
    media_data = await _handle_media_message(original_message)
    if media_data and media_data.get("error"):
        # Se houver erro no processamento da mídia, informa o usuário e encerra.
        await evolution_client.send_text_message(phone, media_data["error"])
        return
        
    # PARALELIZAÇÃO MÁXIMA: Busca lead + conversa em paralelo com tratamento de erros
    lead_task = asyncio.create_task(supabase_client.get_lead_by_phone(phone))
    conversation_task = asyncio.create_task(supabase_client.get_conversation_by_phone(phone))
    # Agente stateless será criado depois, não precisa pré-carregar
    
    # Aguarda todas as tasks com tratamento de erros
    results = await asyncio.gather(
        lead_task,
        conversation_task,
        return_exceptions=True
    )
    
    # Processar resultados com tratamento de erros
    lead_result, conv_result = results
    
    # Verificar lead
    if isinstance(lead_result, Exception):
        emoji_logger.system_error("Lead Fetch", f"Erro ao buscar lead: {lead_result}")
        lead = None
    else:
        lead = lead_result
    
    if not lead:
        # Cria novo lead
        lead = await supabase_client.create_lead({
            "phone_number": phone,
            "current_stage": "INITIAL_CONTACT",
            "qualification_status": "PENDING", 
            "interested": True,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        })
        emoji_logger.supabase_insert("leads", 1, phone=phone)
    
    # Preparar dados da mensagem enquanto busca conversa
    message_data = {
        "content": message_content,
        "role": "user",
        "sender": "user",
        "media_data": {
            "message_id": message_id,
            "raw_data": original_message
        }
    }
    
    # Verificar conversa
    if isinstance(conv_result, Exception):
        emoji_logger.system_error("Conversation Fetch", f"Erro ao buscar conversa: {conv_result}")
        conversation = None
    else:
        conversation = conv_result
    
    if not conversation:
        conversation = await supabase_client.create_conversation(phone, lead["id"])
    
    # VALIDAÇÃO CRÍTICA: Garantir que conversation existe e tem ID válido
    if not conversation or not isinstance(conversation, dict) or "id" not in conversation:
        emoji_logger.system_error("Conversation Validation", f"Conversa inválida criada/buscada: {conversation}")
        raise ValueError(f"Conversa inválida: {conversation}")
    
    # Log para debug
    emoji_logger.system_info(f"Conversa validada - ID: {conversation['id']}, Phone: {phone}")
    
    # OTIMIZAÇÃO: Executar em PARALELO - salvar mensagem + cache
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
    
    # Executar tarefas em paralelo
    await asyncio.gather(*save_tasks, return_exceptions=True)
    
    # Criar agente stateless com contexto completo
    emoji_logger.webhook_process("Criando AGENTIC SDR Stateless...")
    
    try:
        agentic, execution_context = await create_agent_with_context(
            phone=phone,
            conversation_id=conversation["id"]
        )
        emoji_logger.webhook_process("AGENTIC SDR Stateless pronto para uso")
    except Exception as e:
        emoji_logger.system_error("Agent Creation", f"Erro ao criar agente: {e}")
        raise HTTPException(status_code=503, detail="Agente temporariamente indisponível")
    
    # REMOVIDO: Não simular tempo de leitura quando usuário envia mensagem
    # Isso estava causando typing aparecer quando não deveria
    
    # VALIDAÇÃO CRÍTICA: Garantir conversation_id antes de processar
    if not conversation or not conversation.get("id"):
        emoji_logger.system_error("WEBHOOK", f"❌ Conversation inválida! Lead: {lead}, Phone: {phone}")
        # Tentar criar nova conversa como fallback
        try:
            conversation = await supabase_client.create_conversation(phone, lead["id"] if lead else None)
            emoji_logger.system_info(f"✅ Nova conversa criada: {conversation.get('id', 'N/A')}")
        except Exception as conv_error:
            emoji_logger.system_error("WEBHOOK", f"❌ Falha ao criar conversa: {conv_error}")
            return
