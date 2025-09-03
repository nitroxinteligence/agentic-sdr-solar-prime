"""
Conversation Monitor - Monitoramento de conversas e agendamento de follow-ups
Sistema SIMPLES e FUNCIONAL para detectar inatividade e agendar reengajamento
ZERO complexidade, MÁXIMA eficiência
"""

from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import asyncio
from app.utils.logger import emoji_logger
from app.integrations.supabase_client import SupabaseClient # Manter para get_lead_by_phone
from app.integrations.redis_client import redis_client
from app.services.followup_manager import followup_manager_service


class ConversationMonitor:
    """
    Monitor de conversas para follow-up automático
    """

    def __init__(self):
        """Inicializa o monitor de conversas"""
        self.db = SupabaseClient() # Manter para buscar lead_info
        self.redis = redis_client
        self.is_monitoring = False

    async def initialize(self):
        """Inicializa o monitor de conversas e inicia monitoramento"""
        try:
            if not self.redis.redis_client:
                await self.redis.connect()
            emoji_logger.system_ready("📊 ConversationMonitor inicializado")
            self.is_monitoring = True
            asyncio.create_task(self._monitor_loop())
            emoji_logger.system_info("✅ ConversationMonitor: Loop iniciado")
        except Exception as e:
            emoji_logger.system_error(
                "ConversationMonitor", f"Erro na verificação: {e}"
            )

    async def register_message(
        self,
        phone: str,
        is_from_user: bool,
        lead_info: Optional[Dict[str, Any]] = None
    ):
        """
        Registra uma mensagem na conversa usando Redis com fallback para Supabase.
        """
        try:
            clean_phone = self._normalize_phone(phone)
            
            # Tentar usar Redis primeiro
            if self.redis.redis_client:
                active_key = f"monitor:active:{clean_phone}"
                status_key = f"monitor:status:{clean_phone}"
                ttl = int(timedelta(days=7).total_seconds())
                await self.redis.set(
                    active_key, datetime.now().isoformat(), ttl=ttl
                )
                if is_from_user:
                    await self.redis.set(status_key, 'active', ttl=ttl)
                    emoji_logger.system_debug(
                        f"📨 Conversa ativa registrada no Redis: {clean_phone[:8]}..."
                    )
                else:
                    emoji_logger.system_debug(
                        f"🤖 Resposta do bot registrada no Redis: {clean_phone[:8]}..."
                    )
            else:
                # Fallback para Supabase quando Redis não está disponível
                emoji_logger.system_debug(
                    "ConversationMonitor: Redis não disponível, usando fallback Supabase"
                )
                await self._register_message_fallback(clean_phone, is_from_user, lead_info)
                
        except Exception as e:
            emoji_logger.system_error(
                "ConversationMonitor", f"Erro ao registrar mensagem: {e}"
            )
            # Em caso de erro, tentar fallback se ainda não foi usado
            if self.redis.redis_client:
                try:
                    await self._register_message_fallback(clean_phone, is_from_user, lead_info)
                except Exception as fallback_error:
                    emoji_logger.system_error(
                        "ConversationMonitor", f"Erro no fallback: {fallback_error}"
                    )

    async def _register_message_fallback(
        self, 
        clean_phone: str, 
        is_from_user: bool, 
        lead_info: Optional[Dict[str, Any]] = None
    ):
        """Fallback para registrar mensagem usando Supabase quando Redis não está disponível"""
        try:
            # Buscar ou criar conversa no Supabase
            conversation = self.db.client.table('conversations').select(
                "id, phone_number, lead_id, status"
            ).eq('phone_number', clean_phone).execute()
            
            current_time = datetime.now().isoformat()
            
            if conversation.data:
                # Atualizar conversa existente
                conversation_id = conversation.data[0]['id']
                self.db.client.table('conversations').update({
                    'updated_at': current_time,
                    'status': 'ACTIVE' if is_from_user else conversation.data[0]['status']
                }).eq('id', conversation_id).execute()
                
                emoji_logger.system_debug(
                    f"📨 Conversa atualizada no Supabase: {clean_phone[:8]}..."
                )
            else:
                # Criar nova conversa se não existir
                lead_id = None
                if lead_info and 'id' in lead_info:
                    lead_id = lead_info['id']
                else:
                    # Tentar buscar lead pelo telefone
                    lead = self.db.get_lead_by_phone(clean_phone)
                    if lead:
                        lead_id = lead.get('id')
                
                self.db.client.table('conversations').insert({
                    'phone_number': clean_phone,
                    'lead_id': lead_id,
                    'status': 'ACTIVE',
                    'created_at': current_time,
                    'updated_at': current_time
                }).execute()
                
                emoji_logger.system_debug(
                    f"📨 Nova conversa criada no Supabase: {clean_phone[:8]}..."
                )
                
        except Exception as e:
            emoji_logger.system_error(
                "ConversationMonitor", f"Erro no fallback de registro: {e}"
            )

    async def _check_inactive_conversations_fallback(self):
        """Fallback para verificar conversas inativas usando apenas o Supabase"""
        try:
            emoji_logger.system_info("ConversationMonitor: Executando verificação de inatividade via Supabase")
            
            # Buscar todas as conversas ativas
            conversations = self.db.client.table('conversations').select(
                "id, phone_number, lead_id, updated_at, followup_status"
            ).eq('status', 'ACTIVE').execute()
            
            if not conversations.data:
                emoji_logger.system_debug("ConversationMonitor: Nenhuma conversa ativa encontrada")
                return
            
            now = datetime.now()
            
            for conversation in conversations.data:
                phone = conversation['phone_number']
                lead_id = conversation['lead_id']
                conversation_id = conversation['id']
                
                # Buscar a última mensagem desta conversa
                last_message = await self.db.get_last_message_by_phone(phone)
                
                if not last_message:
                    emoji_logger.system_debug(f"Monitor: Nenhuma mensagem encontrada para {phone[:8]}...")
                    continue
                
                last_message_time = datetime.fromisoformat(last_message['created_at'])
                inactive_time = now - last_message_time
                
                # Usar o status do Supabase ou 'active' como padrão
                current_status = conversation.get('followup_status', 'active')
                
                # Delegar para o FollowUpManagerService
                await followup_manager_service.handle_conversation_inactivity(
                    lead_id=lead_id,
                    phone_number=phone,
                    inactive_since=last_message_time,
                    current_status=current_status
                )
                
                # Atualizar status no Supabase baseado no tempo de inatividade
                new_status = None
                if inactive_time > timedelta(hours=48) and current_status != 'followup_48h_sent':
                    new_status = 'followup_48h_sent'
                    emoji_logger.system_info(
                        f"🚫 Status Supabase atualizado: followup_48h_sent para {phone[:8]}... (desqualificação)"
                    )
                elif inactive_time > timedelta(hours=24) and current_status != 'followup_24h_sent':
                    new_status = 'followup_24h_sent'
                    emoji_logger.system_info(
                        f"📅 Status Supabase atualizado: followup_24h_sent para {phone[:8]}..."
                    )
                elif inactive_time > timedelta(minutes=30) and current_status != 'followup_30min_sent':
                    new_status = 'followup_30min_sent'
                    emoji_logger.system_info(
                        f"⏰ Status Supabase atualizado: followup_30min_sent para {phone[:8]}..."
                    )
                
                # Atualizar o status no Supabase se necessário
                if new_status:
                    self.db.client.table('conversations').update({
                        'followup_status': new_status,
                        'updated_at': now.isoformat()
                    }).eq('id', conversation_id).execute()
                    
        except Exception as e:
            emoji_logger.system_error(
                "ConversationMonitor", 
                f"Erro no fallback de verificação de inatividade: {e}"
            )

    def _normalize_phone(self, phone: str) -> str:
        """Normaliza o número do telefone"""
        clean_phone = ''.join(filter(str.isdigit, phone))
        if not clean_phone.startswith('55'):
            clean_phone = '55' + clean_phone
        return clean_phone

    async def _monitor_loop(self):
        """Loop de monitoramento em background"""
        while self.is_monitoring:
            try:
                await self._check_inactive_conversations()
                await asyncio.sleep(60)
            except Exception as e:
                emoji_logger.system_error(
                    "ConversationMonitor", f"Erro no loop: {e}"
                )
                await asyncio.sleep(60)

    async def _check_inactive_conversations(self):
        """Verifica conversas inativas e agenda follow-ups."""
        try:
            # Verifica se o Redis está disponível
            if not self.redis.redis_client:
                emoji_logger.system_info("ConversationMonitor: Redis não disponível, usando fallback do Supabase")
                await self._check_inactive_conversations_fallback()
                return
                
            now = datetime.now()
            async for key in self.redis.redis_client.scan_iter(
                "monitor:active:*"
            ):
                phone = key.split(":")[-1]
                last_message_iso = await self.redis.get(key)
                if not last_message_iso:
                    continue
                last_message_time = datetime.fromisoformat(last_message_iso)
                inactive_time = now - last_message_time
                status_key = f"monitor:status:{phone}"
                current_status = await self.redis.get(status_key) or 'active'

                lead = await self.db.get_lead_by_phone(phone)
                if not lead:
                    emoji_logger.system_debug(f"Monitor: Conversa ativa para {phone[:8]}... aguardando criação do lead no DB.")
                    # Não removemos mais a chave, pois é esperado que o lead seja criado em breve.
                    # A chave tem um TTL e expirará naturalmente se o lead nunca for criado.
                    continue

                # Delega a lógica de agendamento para o FollowUpManagerService
                await followup_manager_service.handle_conversation_inactivity(
                    lead_id=lead['id'],
                    phone_number=phone,
                    inactive_since=last_message_time,
                    current_status=current_status
                )

                # Atualiza o status no Redis com base na decisão do FollowUpManagerService
                # A lógica de atualização do status no Redis é movida para cá
                if inactive_time > timedelta(minutes=30) and current_status != 'followup_30min_sent':
                    await self.redis.set(status_key, 'followup_30min_sent')
                    emoji_logger.system_info(
                        f"⏰ Status Redis atualizado: followup_30min_sent para {phone[:8]}..."
                    )
                elif inactive_time > timedelta(hours=24) and current_status != 'followup_24h_sent':
                    await self.redis.set(status_key, 'followup_24h_sent')
                    emoji_logger.system_info(
                        f"📅 Status Redis atualizado: followup_24h_sent para {phone[:8]}..."
                    )
                elif inactive_time > timedelta(hours=48) and current_status != 'followup_48h_sent':
                    await self.redis.set(status_key, 'followup_48h_sent')
                    emoji_logger.system_info(
                        f"🚫 Status Redis atualizado: followup_48h_sent para {phone[:8]}... (desqualificação)"
                    )

        except Exception as e:
            emoji_logger.system_error(
                "ConversationMonitor", f"Erro ao verificar inatividade: {e}"
            )

    async def shutdown(self):
        """Desliga o monitor de conversas"""
        self.is_monitoring = False
        emoji_logger.system_info("🛑 ConversationMonitor desligado")


_conversation_monitor = None


def get_conversation_monitor() -> "ConversationMonitor":
    """Retorna a instância singleton do ConversationMonitor"""
    global _conversation_monitor
    if _conversation_monitor is None:
        _conversation_monitor = ConversationMonitor()
    return _conversation_monitor