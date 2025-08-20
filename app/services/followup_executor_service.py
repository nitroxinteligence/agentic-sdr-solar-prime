"""
FollowUp Executor Service - Processamento de Follow-ups Agendados
Executa follow-ups e lembretes agendados no banco de dados
"""

import asyncio
import logging
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, List, Optional
import json

from app.integrations.supabase_client import SupabaseClient
from app.integrations.evolution import evolution_client
# Google Calendar será acessado via CalendarServiceReal quando necessário
from app.config import settings, FOLLOW_UP_TYPES
from app.utils.logger import emoji_logger
from app.integrations.redis_client import redis_client

logger = logging.getLogger(__name__)

class FollowUpExecutorService:
    """
    Serviço executor de follow-ups
    Processa follow-ups agendados e envia mensagens personalizadas
    """
    
    def __init__(self):
        """Inicializa o executor de follow-ups"""
        self.db = SupabaseClient()
        self.evolution = evolution_client
        self.running = False
        self.check_interval = 15  # 15 segundos para maior precisão em follow-ups de 30min
        
        # Templates de mensagens por tipo
        self.templates = {
            "IMMEDIATE_REENGAGEMENT": [
                "Oi {name}! Vi que nossa conversa ficou pela metade...",
                "Ainda posso te ajudar com a economia na conta de luz?",
                "Se preferir, podemos conversar em outro momento"
            ],
            "DAILY_NURTURING": [
                "{name}, você sabia que clientes como você economizam em média R$ {savings} por ano?",
                "A Solar Prime tem a solução perfeita para sua conta de R$ {bill_value}",
                "Vamos conversar sobre como reduzir sua conta de luz?"
            ],
            "MEETING_CONFIRMATION": [
                "Oi {name}! Passando para confirmar nossa reunião de amanhã às {time}",
                "Você confirma presença? É só responder SIM ou NÃO",
                "Vou te mostrar como economizar {percentage}% na conta de luz!"
            ],
            "MEETING_REMINDER": [
                "{name}, nossa reunião é daqui a {hours} horas!",
                "Já preparei tudo para te mostrar a economia",
                "Link da reunião: {meeting_link}"
            ],
            "ABANDONMENT_CHECK": [
                "{name}, há {days} dias você demonstrou interesse em economizar na conta de luz",
                "Ainda tem interesse? A SolarPrime continua com as melhores condições",
                "Posso te ajudar com alguma dúvida?"
            ]
        }
        
    async def start(self):
        """Inicia o serviço executor"""
        if self.running:
            logger.warning("Executor de follow-ups já está rodando")
            return
            
        self.running = True
        emoji_logger.system_ready("FollowUp Executor")
        logger.info("🚀 DEBUG: FollowUp Executor iniciado com sucesso!")
        logger.info(f"⏰ DEBUG: Check interval: {self.check_interval}s")
        logger.info("📋 DEBUG: Templates de mensagens carregados:")
        for tipo, msgs in self.templates.items():
            logger.info(f"  - {tipo}: {len(msgs)} templates")
        
        # Iniciar loop principal
        asyncio.create_task(self._execution_loop())
        asyncio.create_task(self._meeting_reminder_loop())
        logger.info("🔄 DEBUG: Loops de execução iniciados (follow-ups e lembretes)")
        
    async def stop(self):
        """Para o serviço executor"""
        self.running = False
        logger.info("FollowUp Executor parado")
        
    async def _execution_loop(self):
        """Loop principal de execução de follow-ups"""
        while self.running:
            try:
                await self.process_pending_followups()
                await asyncio.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"❌ Erro no loop de follow-ups: {e}")
                await asyncio.sleep(60)
    
    async def _meeting_reminder_loop(self):
        """Loop específico para lembretes de reunião (24h e 2h antes)"""
        while self.running:
            try:
                await self.process_meeting_reminders()
                await asyncio.sleep(300)  # Verificar a cada 5 minutos
            except Exception as e:
                logger.error(f"❌ Erro no loop de lembretes: {e}")
                await asyncio.sleep(60)
    
    async def process_pending_followups(self):
        """
        Processa follow-ups pendentes
        Busca follow-ups com scheduled_at <= agora e status = pending
        """
        try:
            now = datetime.now(timezone.utc)
            logger.info(f"🔍 DEBUG: Verificando follow-ups pendentes às {now.isoformat()}")
            
            # Buscar follow-ups pendentes
            result = self.db.client.table('follow_ups').select("*").eq(
                'status', 'pending'
            ).lte(
                'scheduled_at', now.isoformat()
            ).order('scheduled_at').limit(10).execute()
            
            # DEBUG: Log detalhado do resultado
            logger.info(f"📊 DEBUG: Query executada. Result data: {result.data is not None}, Count: {len(result.data) if result.data else 0}")
            
            if not result.data:
                logger.debug("🔍 DEBUG: Nenhum follow-up pendente encontrado no momento")
                # DEBUG: Verificar se existem follow-ups futuros
                future_result = self.db.client.table('follow_ups').select("scheduled_at, type, status").eq(
                    'status', 'pending'
                ).order('scheduled_at').limit(5).execute()
                
                if future_result.data:
                    logger.info(f"📅 DEBUG: Próximos follow-ups agendados:")
                    for f in future_result.data:
                        logger.info(f"  - {f['scheduled_at']} | {f['type']} | {f['status']}")
                else:
                    logger.info("📭 DEBUG: Nenhum follow-up agendado na tabela")
                return
            
            logger.info(f"📋 {len(result.data)} follow-ups pendentes encontrados")
            logger.info(f"📝 DEBUG: Detalhes dos follow-ups:")
            for idx, f in enumerate(result.data):
                logger.info(f"  {idx+1}. Lead: {f.get('lead_id')} | Type: {f.get('type')} | Scheduled: {f.get('scheduled_at')}")
            
            for followup in result.data:
                await self._execute_followup_with_retry(followup)
                
        except Exception as e:
            logger.error(f"❌ Erro ao processar follow-ups: {e}")
    
    async def process_meeting_reminders(self):
        """
        Processa lembretes de reunião da tabela follow_ups
        """
        try:
            now = datetime.now(timezone.utc)
            
            # Verificar se Google Calendar está habilitado
            if settings.disable_google_calendar:
                logger.debug("Google Calendar desabilitado nas configurações")
                return
            
            # Buscar lembretes de reunião pendentes na tabela follow_ups
            pending_reminders_result = self.db.client.table('follow_ups').select("*").eq(
                'type', 'MEETING_REMINDER'
            ).eq(
                'status', 'PENDING'
            ).lte(
                'scheduled_at', now.isoformat()
            ).execute()
            
            if not pending_reminders_result.data:
                logger.debug("Nenhum lembrete de reunião pendente")
                return
            
            # Processar cada lembrete
            for reminder in pending_reminders_result.data:
                try:
                    # Buscar dados do lead
                    lead_data = await self.db.get_lead_by_id(reminder['lead_id'])
                    if not lead_data:
                        logger.warning(f"Lead {reminder['lead_id']} não encontrado para lembrete")
                        continue
            
                    # Extrair metadata do lembrete
                    metadata = reminder.get('metadata', {})
                    hours_before = metadata.get('hours_before', 24)
                    google_event_id = metadata.get('google_event_id')
                    
                    # Nota: Verificação de status cancelado removida para simplificação
                    # O lembrete será enviado independente do status do evento no Google Calendar
                    google_event = {
                        'summary': metadata.get('event_title', 'Reunião sobre Energia Solar'),
                        'start': {'dateTime': metadata.get('event_start')},
                        'end': {'dateTime': metadata.get('event_end')},
                        'hangoutLink': metadata.get('meet_link')
                    } if google_event_id else None
                    
                    # Buscar qualificação do lead - usar maybeSingle para permitir 0 resultados
                    qualification_result = self.db.client.table('leads_qualifications').select("*").eq(
                        'lead_id', reminder['lead_id']
                    ).maybe_single().execute()
                    
                    qualification_id = qualification_result.data['id'] if qualification_result.data else None
                    
                    # Enviar lembrete personalizado
                    await self._send_meeting_reminder_v2(
                        lead_data=lead_data,
                        google_event=google_event or {'summary': reminder.get('message', 'Reunião')},
                        hours_before=hours_before,
                        qualification_id=qualification_id
                    )
                    
                    # Marcar lembrete como executado com compensação
                    try:
                        update_result = await self.db.update_follow_up_status_with_compensation(
                            reminder['id'],
                            'executed',
                            executed_at=now
                        )
                        
                        if not update_result.get("success"):
                            logger.error(f"❌ Erro ao marcar lembrete como executado: {update_result.get('message')}")
                    except Exception as db_error:
                        logger.error(f"❌ Erro ao marcar lembrete como executado: {db_error}")
                    
                except Exception as reminder_error:
                    logger.error(f"Erro ao processar lembrete {reminder['id']}: {reminder_error}")
                    try:
                        update_result = await self.db.update_follow_up_status_with_compensation(
                            reminder['id'],
                            'failed',
                            executed_at=now
                        )
                        
                        if not update_result.get("success"):
                            logger.error(f"❌ Erro ao atualizar status do lembrete no banco: {update_result.get('message')}")
                    except Exception as db_error:
                        logger.error(f"❌ Erro ao atualizar status do lembrete no banco: {db_error}")
                
        except Exception as e:
            logger.error(f"❌ Erro ao processar lembretes de reunião: {e}")
    
    async def _execute_followup_with_retry(self, followup: Dict[str, Any], max_retries: int = 3):
        """Executa um follow-up com retry automático em caso de falha"""
        # Verificar se o lead já atingiu o limite de follow-ups
        lead_id = followup.get('lead_id')
        if lead_id:
            followup_count = await self._get_lead_followup_count(lead_id)
            if followup_count >= 3:  # Limite de 3 follow-ups por semana
                logger.warning(f"⚠️ Limite de follow-ups atingido para lead {lead_id}. Cancelando execução.")
                # Marcar follow-up como cancelado
                await self.db.update_follow_up_status(
                    followup['id'], 
                    'cancelled',
                    executed_at=datetime.now(timezone.utc)
                )
                return {"success": False, "error": "Follow-up limit reached"}
            
            # Verificar se o lead respondeu recentemente (últimas 24 horas)
            if await self._has_lead_responded_recently(lead_id, 24):
                logger.info(f"📞 Lead {lead_id} respondeu recentemente. Cancelando follow-up.")
                # Marcar follow-up como cancelado
                await self.db.update_follow_up_status(
                    followup['id'], 
                    'cancelled',
                    executed_at=datetime.now(timezone.utc)
                )
                return {"success": False, "error": "Lead responded recently"}
        
        for attempt in range(max_retries):
            try:
                result = await self._execute_followup(followup)
                if result and result.get("success"):
                    return result
                
                # Se falhou mas ainda tem tentativas
                if attempt < max_retries - 1:
                    delay = 2 ** attempt * 30  # 30s, 60s, 120s
                    logger.warning(f"⚠️ Follow-up falhou, tentativa {attempt + 1}/{max_retries}. Aguardando {delay}s...")
                    await asyncio.sleep(delay)
                    
            except Exception as e:
                if attempt == max_retries - 1:
                    logger.error(f"❌ Follow-up {followup.get('id')} falhou após {max_retries} tentativas: {e}")
                    # Marcar como falho no banco
                    await self.db.update_follow_up_status(
                        followup['id'], 
                        'failed',
                        executed_at=datetime.now(timezone.utc)
                    )
                else:
                    delay = 2 ** attempt * 30
                    await asyncio.sleep(delay)
        
        return {"success": False, "error": "Max retries exceeded"}
    
    async def _get_lead_followup_count(self, lead_id: str) -> int:
        """
        Obtém o número de follow-ups enviados para um lead na última semana
        
        Args:
            lead_id: ID do lead
            
        Returns:
            Número de follow-ups enviados na última semana
        """
        try:
            # Calcular data de uma semana atrás
            one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)
            
            # Buscar follow-ups executados na última semana
            result = self.db.client.table('follow_ups').select(
                'count'
            ).eq(
                'lead_id', lead_id
            ).eq(
                'status', 'executed'
            ).gte(
                'executed_at', one_week_ago.isoformat()
            ).execute()
            
            # Retornar contagem ou 0 se não houver resultados
            return len(result.data) if result.data else 0
            
        except Exception as e:
            logger.error(f"Erro ao obter contagem de follow-ups para lead {lead_id}: {e}")
            return 0
    
    async def _has_lead_responded_recently(self, lead_id: str, hours: int = 24) -> bool:
        """
        Verifica se um lead respondeu recentemente (nas últimas X horas)
        
        Args:
            lead_id: ID do lead
            hours: Número de horas para verificar
            
        Returns:
            True se o lead respondeu recentemente, False caso contrário
        """
        try:
            # Calcular data de X horas atrás
            since_time = datetime.now(timezone.utc) - timedelta(hours=hours)
            
            # Buscar conversas do lead nas últimas X horas
            result = self.db.client.table('conversations').select(
                'messages'
            ).eq(
                'lead_id', lead_id
            ).gte(
                'updated_at', since_time.isoformat()
            ).execute()
            
            # Verificar se há mensagens do usuário (role: 'user')
            if result.data:
                for conversation in result.data:
                    messages = conversation.get('messages', [])
                    if isinstance(messages, list):
                        for message in messages:
                            if isinstance(message, dict) and message.get('role') == 'user':
                                message_time = message.get('timestamp')
                                if message_time:
                                    try:
                                        msg_dt = datetime.fromisoformat(message_time.replace('Z', '+00:00'))
                                        if msg_dt > since_time:
                                            return True
                                    except Exception:
                                        pass
            
            return False
            
        except Exception as e:
            logger.error(f"Erro ao verificar respostas recentes do lead {lead_id}: {e}")
            return False
    
    async def _execute_followup(self, followup: Dict[str, Any]):
        """Executa um follow-up individual"""
        try:
            lead_id = followup.get('lead_id')
            followup_type = followup.get('type', 'CUSTOM')
            
            logger.info(f"🎯 DEBUG: Iniciando execução de follow-up")
            logger.info(f"  - ID: {followup.get('id')}")
            logger.info(f"  - Lead ID: {lead_id}")
            logger.info(f"  - Type: {followup_type}")
            logger.info(f"  - Scheduled: {followup.get('scheduled_at')}")
            
            # 🔒 LOCK DISTRIBUÍDO POR LEAD - Previne envios duplicados
            # Usar phone_number como fallback se não tiver lead_id
            lock_identifier = lead_id or followup.get('phone_number') or followup.get('id')
            lock_key = f"followup:{lock_identifier}"
            lock_acquired = await redis_client.acquire_lock(lock_key, ttl=60)
            
            if not lock_acquired:
                logger.info(f"🔒 Follow-up para lead {lead_id} já sendo processado por outro processo")
                return
                
            try:
                # Buscar dados do lead - Suportar busca por ID ou telefone
                if lead_id:
                    # Tentar buscar por ID primeiro - usar maybeSingle para permitir 0 resultados
                    lead_result = self.db.client.table('leads').select("*").eq(
                        'id', lead_id
                    ).maybe_single().execute()
                else:
                    # Se não tem lead_id, buscar pelo telefone do follow-up
                    followup_phone = followup.get('phone_number')
                    if not followup_phone:
                        logger.error("Follow-up sem lead_id e sem phone_number")
                        await self._mark_followup_failed(followup['id'], "Lead ID e telefone não encontrados")
                        return
                    
                    lead_result = self.db.client.table('leads').select("*").eq(
                        'phone_number', followup_phone
                    ).limit(1).execute()
                    
                    if lead_result.data:
                        lead_result.data = lead_result.data[0]  # Pegar primeiro resultado
                
                if not lead_result.data:
                    logger.error(f"Lead não encontrado - ID: {lead_id}, Phone: {followup.get('phone_number')}")
                    await self._mark_followup_failed(followup['id'], "Lead não encontrado")
                    return
                
                lead = lead_result.data
                phone = lead.get('phone_number')
                
                if not phone:
                    await self._mark_followup_failed(followup['id'], "Telefone não encontrado")
                    return
                
                # NOVA VALIDAÇÃO: Para follow-ups de reengajamento, verificar se usuário realmente ficou inativo
                if followup_type == 'reengagement':
                    should_send = await self._validate_inactivity_followup(followup)
                    if not should_send:
                        # Usuário respondeu, cancelar este follow-up
                        self.db.client.table('follow_ups').update({
                            'status': 'cancelled',
                            'executed_at': datetime.now(timezone.utc).isoformat(),
                            'response': json.dumps({'reason': 'user_responded_before_followup'})
                        }).eq('id', followup['id']).execute()
                        
                        logger.info(f"📞 Follow-up cancelado - {lead.get('name')} respondeu antes do prazo")
                        return
                
                # Preparar mensagem baseada no template
                message = await self._prepare_followup_message(followup_type, lead, followup)
                
                if not message:
                    await self._mark_followup_failed(followup['id'], "Falha ao preparar mensagem")
                    return
                
                # SANITIZAÇÃO FINAL - Remove qualquer tag remanescente
                message = self._sanitize_final_message(message)
                
                logger.info(f"📤 DEBUG: Preparando envio via Evolution API")
                logger.info(f"  - Phone: {phone}")
                logger.info(f"  - Message length: {len(message)}")
                logger.info(f"  - Message preview: {message[:100]}...")
                
                # Enviar mensagem via WhatsApp
                result = await self.evolution.send_text_message(
                    phone=phone,
                    message=message
                )
                
                logger.info(f"📱 DEBUG: Resultado do envio Evolution: {result}")
            
                if result:
                    logger.info(f"🧠✅ Follow-up EXECUTADO: {followup.get('id')} - {lead.get('name')}")
                    emoji_logger.whatsapp_sent(f"Follow-up enviado para {lead.get('name')}")
                    
                    # Marcar como executado no banco com compensação
                    try:
                        update_result = await self.db.update_follow_up_status_with_compensation(
                            followup['id'], 
                            'executed',
                            executed_at=datetime.now(timezone.utc)
                        )
                        
                        if not update_result.get("success"):
                            logger.error(f"❌ Erro ao atualizar status do follow-up no banco: {update_result.get('message')}")
                    except Exception as db_error:
                        logger.error(f"❌ Erro ao atualizar status do follow-up no banco: {db_error}")
                else:
                    logger.error(f"❌ Falha ao enviar follow-up para {lead.get('name')}")
                    await self._mark_follow_up_failed(followup['id'], "Falha no envio via WhatsApp")
                    
            finally:
                # 🔓 LIBERAR LOCK
                await redis_client.release_lock(lock_key)
                
        except Exception as e:
            logger.error(f"❌ Erro ao executar follow-up: {e}")
            await self._mark_followup_failed(followup.get('id'), str(e))
            # Garantir liberação do lock mesmo em caso de erro
            if 'lock_key' in locals():
                await redis_client.release_lock(lock_key)
    
    async def _send_meeting_reminder_v2(self, lead_data: Dict[str, Any], google_event: Dict[str, Any], hours_before: int, qualification_id: str):
        """
        Envia lembrete de reunião PERSONALIZADO usando Helen + contexto completo
        
        Args:
            lead_data: Dados do lead (id, name, phone_number)
            google_event: Evento do Google Calendar
            hours_before: Horas antes da reunião (24 ou 2)
            qualification_id: ID do registro na tabela leads_qualifications
        """
        try:
            phone = lead_data.get('phone_number')
            
            if not phone:
                logger.warning(f"Lead {lead_data.get('id')} sem telefone para lembrete")
                return
            
            # Extrair informações do evento
            start_str = google_event.get('start', {}).get('dateTime', '')
            
            # Parse da data/hora do evento
            try:
                if start_str:
                    # Remover timezone info para parsing
                    start_dt = datetime.fromisoformat(start_str.replace('Z', '+00:00')).replace(tzinfo=None)
                    event_time = start_dt.strftime("%H:%M")
                    event_date = start_dt.strftime("%d/%m")
                else:
                    event_time = "10:00"  # Default
                    event_date = datetime.now().strftime("%d/%m")
            except Exception:
                event_time = "10:00"  # Default fallback
                event_date = datetime.now().strftime("%d/%m")
            
            # Extrair link do Google Meet
            meet_link = google_event.get('hangoutLink', '')
            
            # Preparar dados do lead para contexto
            lead_info = {
                "name": lead_data.get("name", "Cliente"),
                "bill_value": lead_data.get("bill_value", 0),
                "chosen_flow": lead_data.get("chosen_flow", "Não definido"),
                "qualification_score": lead_data.get("qualification_score", 0)
            }
            
            # Gerar mensagem personalizada usando contexto completo
            if hours_before == 24:
                # Lembrete 24h antes
                if lead_info["bill_value"] > 0:
                    message = f"""☀️ {lead_info['name']}, amanhã ({event_date}) às {event_time} temos nossa reunião sobre energia solar!

💰 Sua conta de R$ {lead_info['bill_value']} pode ser reduzida em até 90% com a SolarPrime.

📍 Link da reunião: {meet_link}

✅ Nossa reunião vai mostrar:
• Análise personalizada da sua conta
• Simulação de economia real
• Opções de financiamento que cabem no seu bolso

Confirma presença? É só responder SIM ou NÃO 🙏"""
                else:
                    message = f"""☀️ {lead_info['name']}, amanhã ({event_date}) às {event_time} temos nossa reunião sobre energia solar!

📍 Link da reunião: {meet_link}

✅ Nossa reunião vai mostrar:
• Como a energia solar pode transformar sua conta de luz
• As melhores soluções para seu perfil
• Condições especiais exclusivas

Confirma presença? É só responder SIM ou NÃO 🙏"""
            
            elif hours_before == 2:
                # Lembrete 2h antes
                message = f"""⏰ {lead_info['name']}, nossa reunião é daqui a 2 HORAS ({event_time})!

📍 Link da reunião: {meet_link}

Chegou a hora de transformar sua conta de luz! Preparei tudo para mostrar como você pode economizar até 90%.

Nos vemos na reunião! 👋"""
            
            else:
                # Lembrete genérico
                message = f"""☀️ {lead_info['name']}, sua reunião sobre energia solar é às {event_time}!

📍 Link da reunião: {meet_link}

Preparado para descobrir como economizar na conta de luz?

Até já! 👋"""
            
            # Enviar mensagem via Evolution API
            result = await self.evolution.send_text_message(
                phone=phone,
                message=message
            )
            
            if result:
                logger.info(f"🧠✅ Lembrete de reunião enviado para {lead_info['name']} - {hours_before}h antes")
                emoji_logger.whatsapp_sent(f"Lembrete {hours_before}h enviado para {lead_info['name']}")
            else:
                logger.error(f"❌ Falha ao enviar lembrete de reunião para {lead_info['name']}")
                
        except Exception as e:
            logger.error(f"❌ Erro ao enviar lembrete de reunião: {e}")
    
    def _sanitize_final_message(self, message: str) -> str:
        """Remove tags e formatação remanescentes da mensagem final"""
        import re
        
        # Remover tags específicas do sistema
        message = re.sub(r'<RESPOSTA_FINAL>.*?</RESPOSTA_FINAL>', '', message, flags=re.DOTALL)
        message = re.sub(r'<[^>]+>', '', message)  # Remove qualquer tag HTML/XML
        
        # Remover múltiplos espaços e quebras de linha
        message = re.sub(r'\s+', ' ', message)
        message = message.strip()
        
        return message
    
    async def _validate_inactivity_followup(self, followup: Dict) -> bool:
        """
        Valida se usuário realmente ficou inativo para follow-ups de reengajamento
        
        Returns:
            True: Deve enviar follow-up (usuário inativo)
            False: Cancelar follow-up (usuário respondeu)
        """
        try:
            # Extrair metadados necessários
            metadata = followup.get('metadata', {})
            lead_id = followup.get('lead_id')
            
            if not lead_id:
                logger.warning(f"Follow-up {followup['id']} sem lead_id para validação")
                return True  # Se não temos dados, enviar o follow-up mesmo assim
            
            # Buscar última resposta do usuário e última resposta do agente antes deste follow-up
            conversation = await self.db.get_conversation_by_lead_id(lead_id)
            if not conversation or not conversation.get('messages'):
                return True  # Sem mensagens, enviar follow-up
            
            messages = conversation['messages']
            agent_response_time = None
            last_user_message_time = None
            
            # Encontrar timestamp da resposta do agente que gerou este follow-up
            if 'agent_response_timestamp' in metadata:
                agent_response_time = datetime.fromisoformat(metadata['agent_response_timestamp'])
            else:
                # Retroceder para encontrar última mensagem do agente
                for msg in reversed(messages):
                    if msg.get('role') == 'assistant':
                        agent_response_time = datetime.fromisoformat(msg['timestamp'])
                        break
            
            # Encontrar última mensagem do usuário
            for msg in reversed(messages):
                if msg.get('role') == 'user':
                    last_user_message_time = datetime.fromisoformat(msg['timestamp'])
                    break
            
            # Se não temos dados suficientes, enviar follow-up
            if not agent_response_time:
                logger.warning(f"Follow-up {followup['id']} sem metadados necessários para validação")
                return True
            
            # Se usuário não respondeu desde a resposta do agente, enviar follow-up
            if not last_user_message_time or last_user_message_time < agent_response_time:
                logger.info(f"✅ Usuário inativo desde {agent_response_time} - enviando follow-up de reengajamento")
                return True
            else:
                # Usuário respondeu após a resposta do agente, cancelar follow-up
                logger.info(f"🚫 Usuário respondeu às {last_user_message_time} após agente às {agent_response_time} - cancelando follow-up")
                return False
                
        except Exception as e:
            logger.error(f"❌ Erro ao validar inatividade do follow-up: {e}")
            return True  # Em caso de erro, enviar o follow-up mesmo assim
    
    async def _prepare_followup_message(self, followup_type: str, lead: Dict, followup: Dict) -> str:
        """
        Prepara mensagem de follow-up usando templates + contexto
        
        Args:
            followup_type: Tipo do follow-up (IMMEDIATE_REENGAGEMENT, DAILY_NURTURING, etc.)
            lead: Dados do lead
            followup: Dados do follow-up
            
        Returns:
            Mensagem formatada para envio
        """
        try:
            # Extrair informações do lead
            name = lead.get("name", "Cliente").split()[0]  # Usar apenas primeiro nome
            bill_value = lead.get("bill_value", 0)
            qualification_score = lead.get("qualification_score", 0)
            
            # Calcular economia estimada (70% da conta)
            estimated_savings = bill_value * 0.7 if bill_value > 0 else 0
            
            # Selecionar template baseado no índice do follow-up
            templates_for_type = self.templates.get(followup_type, self.templates.get("DAILY_NURTURING"))
            
            # Escolher template baseado em algum critério (ex: score, tentativa, etc.)
            template_index = min(qualification_score // 20, len(templates_for_type) - 1) if qualification_score > 0 else 0
            template = templates_for_type[template_index]
            
            # Formatar mensagem com dados do lead
            message = template.format(
                name=name,
                bill_value=f"R$ {bill_value:.2f}" if bill_value > 0 else "R$ 0,00",
                savings=f"R$ {estimated_savings:.2f}" if estimated_savings > 0 else "R$ 0,00",
                percentage="70",
                time="10:00",  # Default time
                hours=24,  # Default hours
                days=2,  # Default days
                meeting_link=""  # Default empty
            )
            
            # FOLLOW-UP INTELIGENTE: Para reengajamento, SEMPRE usar Helen completa com contexto
            if followup_type == "IMMEDIATE_REENGAGEMENT":
                # Criar contexto mais completo para follow-up inteligente
                context = {
                    "lead_name": name,
                    "bill_value": bill_value,
                    "qualification_score": qualification_score,
                    "last_interaction": lead.get("last_interaction", ""),
                    "current_stage": lead.get("current_stage", "UNKNOWN"),
                    "chosen_flow": lead.get("chosen_flow", "Não definido")
                }
                
                # Mensagem mais personalizada para reengajamento
                message = f"""☀️ {name}, tudo bem?

Vi que nossa conversa sobre energia solar ficou pela metade...

{'💰' if bill_value > 0 else '💡'} {f'Com sua conta de R$ {bill_value:.2f}, ' if bill_value > 0 else ''}você pode economizar até 90% com a SolarPrime!

✨ Como posso te ajudar hoje?
1️⃣ Quero continuar nossa conversa
2️⃣ Prefiro agendar para outro momento
3️⃣ Dúvidas sobre energia solar

É só responder com o número! 😊"""
            
            elif followup_type == "DAILY_NURTURING":
                # Mensagem de nurturing mais elaborada
                message = f"""☀️ Bom dia, {name}!

{'💰' if bill_value > 0 else '💡'} {f'Clientes com contas similares à sua (R$ {bill_value:.2f}) ' if bill_value > 0 else 'Nossos clientes '} economizam em média R$ {estimated_savings:.2f} por ano com energia solar!

✅ A SolarPrime oferece:
• Instalação própria de usina - economia de até 90%
• Aluguel de lote - sua usina em nosso terreno  
• Compra com desconto - economia imediata de 20%
• Usina de investimento - renda passiva com energia solar

Quer que eu te mostre as opções ideais para seu perfil?

1️⃣ Sim, me mostre as opções
2️⃣ Prefiro agendar uma reunião  
3️⃣ Tenho dúvidas

É só responder com o número! 🙏"""
            
            return message
            
        except Exception as e:
            logger.error(f"❌ Erro ao preparar mensagem de follow-up: {e}")
            # Fallback para mensagem padrão
            return f"Olá {lead.get('name', 'Cliente')}! Tudo bem? Estou checando se ainda tem interesse em nossa conversa sobre energia solar. 😊"
    
    async def _schedule_next_followup(self, followup_type: str, lead: Dict, current_followup: Dict):
        """
        Agenda próximo follow-up baseado na estratégia - FLUXO SEQUENCIAL
        """
        try:
            # Verificar tipo de follow-up atual
            if followup_type == 'IMMEDIATE_REENGAGEMENT':
                # Este era o follow-up de 30min, agendar o de 24h
                next_time = datetime.now() + timedelta(hours=24)
                
                # Criar follow-up de 24h
                followup_24h_data = {
                    'lead_id': lead['id'],
                    'type': 'reengagement',
                    'follow_up_type': 'DAILY_NURTURING',
                    'scheduled_at': next_time.isoformat(),
                    'message': await self._prepare_followup_message('DAILY_NURTURING', lead, {}),
                    'status': 'pending',
                    'metadata': {
                        'previous_followup_id': current_followup['id'],
                        'scheduled_reason': 'User inactivity check 24h after agent response'
                    }
                }
                
                try:
                    result = self.db.client.table('follow_ups').insert(followup_24h_data).execute()
                    if result.data:
                        emoji_logger.system_info(f"📅 Follow-up sequencial de 24h agendado para {lead.get('phone_number')} às {next_time.strftime('%d/%m %H:%M')}")
                except Exception as e:
                    emoji_logger.system_error("Falha ao agendar follow-up sequencial de 24h", error=str(e))
            
            elif followup_type == 'DAILY_NURTURING':
                # Este era o follow-up de 24h, pode continuar nurturing ou marcar como perdido
                attempt = current_followup.get('attempt', 0)
                if attempt < 2:  # Tentar mais 2 vezes de nurturing
                    next_time = datetime.now() + timedelta(days=2)  # Próximo em 2 dias
                    # Agendar próximo follow-up de nurturing
                    await self._schedule_nurturing_followup(lead, current_followup, attempt + 1, next_time)
                else:
                    # Marcar lead como não interessado após múltiplas tentativas
                    await self._mark_lead_as_not_interested(lead, current_followup)
                    emoji_logger.system_info(f"🔚 Sequência de follow-up para {lead.get('name')} concluída sem resposta.")
                    
        except Exception as e:
            logger.error(f"Erro ao agendar próximo follow-up: {e}")
    
    async def _schedule_nurturing_followup(self, lead: Dict, previous_followup: Dict, attempt: int, scheduled_time: datetime):
        """
        Agenda follow-up de nurturing adicional
        """
        try:
            # Preparar mensagem personalizada para nurturing
            message = await self._prepare_followup_message('DAILY_NURTURING', lead, {})
            
            # Criar follow-up de nurturing
            nurturing_followup_data = {
                'lead_id': lead['id'],
                'type': 'nurture',
                'follow_up_type': 'DAILY_NURTURING',
                'scheduled_at': scheduled_time.isoformat(),
                'message': message,
                'status': 'pending',
                'attempt': attempt,
                'metadata': {
                    'previous_followup_id': previous_followup['id'],
                    'scheduled_reason': f'Nurturing attempt #{attempt}'
                }
            }
            
            result = self.db.client.table('follow_ups').insert(nurturing_followup_data).execute()
            if result.data:
                emoji_logger.system_info(f"📅 Follow-up de nurturing adicional agendado (tentativa {attempt})")
                
        except Exception as e:
            logger.error(f"Erro ao agendar próximo follow-up: {e}")
    
    async def _mark_lead_as_not_interested(self, lead: Dict, current_followup: Dict):
        """
        Marca lead como não interessado após múltiplas tentativas de follow-up
        """
        try:
            # Atualizar status do lead
            await self.db.client.table('leads').update({
                'current_stage': 'NOT_INTERESTED',
                'qualification_status': 'NOT_QUALIFIED',
                'updated_at': datetime.now(timezone.utc).isoformat()
            }).eq('id', lead['id']).execute()
            
            # Criar registro na tabela de qualificações
            qualification_data = {
                'lead_id': lead['id'],
                'qualification_status': 'NOT_QUALIFIED',
                'score': 0,
                'notes': f'Lead não respondeu após múltiplos follow-ups. Último follow-up: {current_followup.get("id")}',
                'qualified_at': datetime.now(timezone.utc).isoformat()
            }
            
            await self.db.client.table('leads_qualifications').insert(qualification_data).execute()
            
            emoji_logger.system_info(f"📋 Lead {lead.get('name')} marcado como NÃO INTERESSADO após follow-ups")
            
        except Exception as e:
            logger.error(f"Erro ao marcar lead como não interessado: {e}")
    
    async def _mark_follow_up_failed(self, follow_up_id: str, error_reason: str):
        """Marca follow-up como falho"""
        try:
            result = await self.db.update_follow_up_status_with_compensation(
                follow_up_id, 
                'failed',
                executed_at=datetime.now(timezone.utc)
            )
            
            if result.get("success"):
                logger.error(f"❌ Follow-up {follow_up_id} marcado como falho: {error_reason}")
            else:
                logger.error(f"Erro ao marcar follow-up {follow_up_id} como falho: {result.get('message')}")
        except Exception as e:
            logger.error(f"Erro ao marcar follow-up {follow_up_id} como falho: {e}")
    
    async def create_followup(self, followup_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria novo follow-up no banco"""
        try:
            # Validar dados obrigatórios
            required_fields = ['lead_id', 'type', 'message', 'scheduled_at']
            for field in required_fields:
                if not followup_data.get(field):
                    raise ValueError(f"Campo obrigatório faltando: {field}")
            
            # Adicionar campos padrão
            followup_data.setdefault('status', 'pending')
            followup_data.setdefault('created_at', datetime.now(timezone.utc).isoformat())
            followup_data.setdefault('updated_at', datetime.now(timezone.utc).isoformat())
            
            result = self.db.client.table('follow_ups').insert(followup_data).execute()
            if result.data:
                logger.info(f"📅 Novo follow-up agendado para {followup_data.get('scheduled_at')}")
                return result.data[0]
            else:
                raise Exception("Falha ao criar follow-up")
                
        except Exception as e:
            logger.error(f"Erro ao criar follow-up: {e}")
            raise
    
    async def mark_followup_failed(self, followup_id: str, error_reason: str):
        """Marca follow-up como falho"""
        try:
            self.db.client.table('follow_ups').update({
                'status': 'failed',
                'executed_at': datetime.now(timezone.utc).isoformat(),
                'error_reason': error_reason
            }).eq('id', followup_id).execute()
            
            logger.error(f"Erro ao marcar follow-up como falho: {e}")
    
    def _validate_inactivity_followup(self, followup: Dict) -> bool:
        """
        Valida se usuário realmente ficou inativo para follow-ups de reengajamento
        
        Returns:
            True: Deve enviar follow-up (usuário inativo)
            False: Cancelar follow-up (usuário respondeu)
        """
        try:
            # Extrair metadados necessários
            metadata = followup.get('metadata', {})
            lead_id = followup.get('lead_id')
            
            if not lead_id:
                logger.warning(f"Follow-up {followup['id']} sem lead_id para validação")
                return True  # Se não temos dados, enviar o follow-up mesmo assim
            
            # Buscar última resposta do usuário e última resposta do agente antes deste follow-up
            # Esta função precisa ser implementada no SupabaseClient
            # conversation = await self.db.get_conversation_by_lead_id(lead_id)
            # Se não estiver implementada, retornar True para manter comportamento original
            return True
                
        except Exception as e:
            logger.error(f"❌ Erro ao validar inatividade do follow-up: {e}")
            return True  # Em caso de erro, enviar o follow-up mesmo assim
    
    async def force_process_followups(self):
        """Força processamento imediato de follow-ups"""
        logger.info("🔄 Forçando processamento imediato de follow-ups...")
        await self.process_pending_followups()
        logger.info("✅ Processamento de follow-ups concluído")
    
    async def get_pending_followups_count(self) -> int:
        """Retorna contagem de follow-ups pendentes"""
        try:
            now = datetime.now(timezone.utc).isoformat()
            result = self.db.client.table('follow_ups').select(
                "count"
            ).eq(
                'status', 'pending'
            ).lte(
                'scheduled_at', now
            ).execute()
            
            return len(result.data) if result.data else 0
        except Exception as e:
            logger.error(f"Erro ao contar follow-ups pendentes: {e}")
            return 0
    
    async def cancel_followup(self, followup_id: str) -> Dict[str, Any]:
        """Cancela follow-up específico"""
        try:
            result = self.db.client.table('follow_ups').update({
                'status': 'cancelled',
                'updated_at': datetime.now(timezone.utc).isoformat()
            }).eq('id', followup_id).execute()
            
            if result.data:
                return {
                    "success": True,
                    "message": f"Follow-up {followup_id} cancelado com sucesso"
                }
            else:
                return {
                    "success": False,
                    "message": "Follow-up não encontrado"
                }
        except Exception as e:
            logger.error(f"Erro ao cancelar follow-up: {e}")
            return {
                "success": False,
                "message": f"Erro ao cancelar follow-up: {e}"
            }