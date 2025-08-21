"""
Conversation Monitor - Monitoramento de conversas e agendamento de follow-ups
Sistema SIMPLES e FUNCIONAL para detectar inatividade e agendar reengajamento
ZERO complexidade, MÁXIMA eficiência
"""

from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import asyncio
from app.utils.logger import emoji_logger
from app.config import settings
from app.integrations.supabase_client import SupabaseClient
from app.integrations.redis_client import redis_client

class ConversationMonitor:
    """
    Monitor de conversas para follow-up automático
    Detecta leads inativos e agenda reengajamento inteligente
    """
    
    def __init__(self):
        """Inicializa o monitor de conversas"""
        self.db = SupabaseClient()
        self.redis = redis_client
        self.is_monitoring = False
        
    async def initialize(self):
        """Inicializa o monitor de conversas e inicia monitoramento em background"""
        try:
            if not self.redis.redis_client:
                await self.redis.connect()

            emoji_logger.system_ready("📊 ConversationMonitor inicializado com persistência Redis")
            self.is_monitoring = True
            
            # Iniciar monitoramento em background
            asyncio.create_task(self._monitor_loop())
            
            emoji_logger.system_info("✅ ConversationMonitor: Loop de monitoramento iniciado")
        except Exception as e:
            emoji_logger.system_error("ConversationMonitor", f"Erro ao inicializar: {e}")
    
    async def register_message(self, 
                              phone: str, 
                              is_from_user: bool,
                              lead_info: Optional[Dict[str, Any]] = None):
        """
        Registra uma mensagem na conversa usando Redis para persistência.
        
        Args:
            phone: Número do telefone
            is_from_user: True se mensagem do usuário, False se do bot
            lead_info: Informações do lead (opcional)
        """
        try:
            clean_phone = self._normalize_phone(phone)
            
            active_key = f"monitor:active:{clean_phone}"
            status_key = f"monitor:status:{clean_phone}"
            ttl = int(timedelta(days=7).total_seconds())

            await self.redis.set(active_key, datetime.now().isoformat(), ttl=ttl)
            
            if is_from_user:
                await self.redis.set(status_key, 'active', ttl=ttl)
                emoji_logger.system_debug(f"📨 Conversa ativa registrada no Redis: {clean_phone[:8]}...")
            else:
                emoji_logger.system_debug(f"🤖 Resposta do bot registrada no Redis: {clean_phone[:8]}...")
                
        except Exception as e:
            emoji_logger.system_error("ConversationMonitor", f"Erro ao registrar mensagem no Redis: {e}")
    
    def _normalize_phone(self, phone: str) -> str:
        """
        Normaliza o número do telefone
        """
        clean_phone = ''.join(filter(str.isdigit, phone))
        if not clean_phone.startswith('55'):
            clean_phone = '55' + clean_phone
        return clean_phone
    
    async def _monitor_loop(self):
        """Loop de monitoramento em background - executa a cada 60 segundos"""
        while self.is_monitoring:
            try:
                await self._check_inactive_conversations()
                await asyncio.sleep(60)
            except Exception as e:
                emoji_logger.system_error("ConversationMonitor", f"Erro no monitor loop: {e}")
                await asyncio.sleep(60)
    
    async def _check_inactive_conversations(self):
        """Verifica conversas inativas no Redis e agenda follow-ups."""
        try:
            now = datetime.now()
            
            async for key in self.redis.redis_client.scan_iter("monitor:active:*"):
                phone = key.split(":")[-1]
                
                last_message_iso = await self.redis.get(key)
                if not last_message_iso:
                    continue

                last_message_time = datetime.fromisoformat(last_message_iso)
                inactive_time = now - last_message_time
                
                status_key = f"monitor:status:{phone}"
                current_status = await self.redis.get(status_key) or 'active'
                
                if inactive_time > timedelta(minutes=30) and current_status != 'followup_30min_sent':
                    await self._schedule_followup(phone, 'IMMEDIATE_REENGAGEMENT', last_message_iso)
                    await self.redis.set(status_key, 'followup_30min_sent')
                    emoji_logger.system_info(f"⏰ Follow-up 30min agendado via Redis: {phone[:8]}...")
                
                elif inactive_time > timedelta(hours=24) and current_status != 'followup_24h_sent':
                    await self._schedule_followup(phone, 'DAILY_NURTURING', last_message_iso)
                    await self.redis.set(status_key, 'followup_24h_sent')
                    emoji_logger.system_info(f"📅 Follow-up 24h agendado via Redis: {phone[:8]}...")

        except Exception as e:
            emoji_logger.system_error("ConversationMonitor", f"Erro ao verificar conversas inativas no Redis: {e}")
    
    async def _schedule_followup(self, phone: str, followup_type: str, inactive_since_iso: str):
        """
        Agenda um follow-up no banco de dados
        """
        try:
            lead = await self.db.get_lead_by_phone(phone)
            
            if lead:
                followup_data = {
                    'lead_id': lead['id'],
                    'phone_number': phone,
                    'type': 'reengagement',
                    'follow_up_type': followup_type,
                    'scheduled_at': datetime.now().isoformat(),
                    'status': 'pending',
                    'message': '',
                    'priority': 'medium',
                    'attempt': 0,
                    'metadata': {
                        'source': 'conversation_monitor',
                        'inactive_since': inactive_since_iso,
                        'original_type': followup_type
                    }
                }
                
                await self.db.create_follow_up(followup_data)
                emoji_logger.system_info(f"✅ Follow-up agendado no banco: {followup_type} para {phone[:8]}...")
            else:
                emoji_logger.system_warning(f"⚠️ Lead não encontrado para agendar follow-up: {phone[:8]}...")
                
        except Exception as e:
            emoji_logger.system_error("ConversationMonitor", f"Erro ao agendar follow-up: {e}")
    
    async def shutdown(self):
        """Desliga o monitor de conversas"""
        self.is_monitoring = False
        emoji_logger.system_info("🛑 ConversationMonitor desligado")

# Singleton pattern - instância única global
_conversation_monitor = None

def get_conversation_monitor() -> ConversationMonitor:
    """
    Retorna a instância singleton do ConversationMonitor
    """
    global _conversation_monitor
    if _conversation_monitor is None:
        _conversation_monitor = ConversationMonitor()
    return _conversation_monitor