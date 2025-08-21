"""
FollowUp Scheduler Service - Enfileira Follow-ups para Execução
Este serviço agora APENAS enfileira tarefas no Redis, não as executa.
"""

import asyncio
import logging
from datetime import datetime, timedelta, timezone
from typing import Dict, Any

from app.integrations.supabase_client import SupabaseClient
from app.config import settings
from app.utils.logger import emoji_logger
from app.integrations.redis_client import redis_client

logger = logging.getLogger(__name__)

class FollowUpSchedulerService:
    """
    Serviço agendador de follow-ups.
    Verifica o banco de dados por follow-ups pendentes e os enfileira no Redis para serem processados por um worker.
    """
    
    def __init__(self):
        self.db = SupabaseClient()
        self.redis = redis_client
        self.running = False
        self.check_interval = 15  # segundos

    async def start(self):
        if self.running:
            logger.warning("Agendador de follow-ups já está rodando.")
            return
            
        self.running = True
        emoji_logger.system_ready("FollowUp Scheduler")
        asyncio.create_task(self._scheduling_loop())
        
    async def stop(self):
        self.running = False
        logger.info("Agendador de follow-ups parado.")
        
    async def _scheduling_loop(self):
        while self.running:
            try:
                await self.enqueue_pending_followups()
                await asyncio.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"❌ Erro no loop de agendamento de follow-ups: {e}")
                await asyncio.sleep(60)

    async def enqueue_pending_followups(self):
        """
        Busca follow-ups pendentes, aplica regras de negócio (como anti-spam) e os enfileira no Redis.
        """
        try:
            now = datetime.now(timezone.utc)
            pending_followups = await self.db.get_pending_follow_ups()

            if not pending_followups:
                return

            logger.info(f"📋 {len(pending_followups)} follow-ups pendentes encontrados para enfileirar.")
            
            for followup in pending_followups:
                # ANTI-SPAM: Verificar se o lead já recebeu muitos follow-ups recentemente
                lead_id = followup.get('lead_id')
                if lead_id:
                    one_week_ago = now - timedelta(days=7)
                    recent_followups_count = await self.db.get_recent_followup_count(lead_id, one_week_ago)
                    
                    if recent_followups_count >= settings.max_follow_up_attempts:
                        emoji_logger.system_warning(f"🚫 Limite de follow-ups (spam) atingido para o lead {lead_id}. Cancelando.")
                        await self.db.update_follow_up_status(followup['id'], 'cancelled')
                        continue # Pula para o próximo follow-up

                lock_key = f"followup_enqueue:{followup['id']}"
                if await self.redis.acquire_lock(lock_key, ttl=60):
                    try:
                        task_payload = {
                            "task_type": "execute_followup",
                            "followup_id": followup['id'],
                            "lead_id": followup['lead_id'],
                            "phone_number": followup['phone_number'],
                            "followup_type": followup.get('follow_up_type', 'CUSTOM'),
                            "enqueued_at": now.isoformat()
                        }
                        
                        await self.redis.enqueue("followup_tasks", task_payload)
                        await self.db.update_follow_up_status(followup['id'], 'queued')
                        
                        emoji_logger.followup_event(f"✅ Follow-up {followup['id']} enfileirado para execução.")
                    except Exception as e:
                        logger.error(f"❌ Erro ao enfileirar follow-up {followup['id']}: {e}")
                        await self.redis.release_lock(lock_key)
                else:
                    logger.warning(f"⚠️ Follow-up {followup['id']} já está sendo processado, pulando.")

        except Exception as e:
            logger.error(f"❌ Erro ao processar e enfileirar follow-ups pendentes: {e}")

    async def force_enqueue_followups(self):
        """Força o enfileiramento imediato de follow-ups pendentes."""
        logger.info("🔄 Forçando enfileiramento imediato de follow-ups...")
        await self.enqueue_pending_followups()
        logger.info("✅ Processo de enfileiramento concluído.")