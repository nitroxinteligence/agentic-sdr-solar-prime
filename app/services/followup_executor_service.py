"""
FollowUp Scheduler Service - Enfileira Follow-ups para Execução
Este serviço agora APENAS enfileira tarefas no Redis, não as executa.
"""

import asyncio
from datetime import datetime, timedelta, timezone

from app.integrations.supabase_client import SupabaseClient
from app.config import settings
from app import config
from app.utils.logger import emoji_logger
from app.integrations.redis_client import redis_client
from app.enums import FollowUpStatus
from loguru import logger


class FollowUpSchedulerService:
    """
    Serviço agendador de follow-ups.
    Verifica o banco de dados por follow-ups pendentes e os enfileira no Redis.
    """

    def __init__(self):
        self.db = SupabaseClient()
        self.redis = redis_client
        self.running = False
        self.check_interval = 1800  # 30 minutos (reduzir duplicação com FollowUpWorker)

    async def start(self):
        if self.running:
            logger.warning("Agendador de follow-ups já está rodando.")
            return
        self.running = True
        
        # Verifica se Redis está disponível
        redis_available = await self._check_redis_availability()
        if redis_available:
            emoji_logger.system_ready("FollowUp Scheduler (Redis Mode)")
        else:
            emoji_logger.system_ready("FollowUp Scheduler (Database Mode)")
            
        asyncio.create_task(self._scheduling_loop())

    async def stop(self):
        self.running = False
        logger.info("Agendador de follow-ups parado.")

    async def _scheduling_loop(self):
        while self.running:
            try:
                # Só executa se Redis estiver disponível
                # Se Redis não estiver disponível, o FollowUpWorker faz polling direto do banco
                redis_available = await self._check_redis_availability()
                if redis_available:
                    await self.enqueue_pending_followups()
                else:
                    # Redis indisponível - FollowUpWorker está fazendo polling direto
                    emoji_logger.system_info(
                        "📋 Redis indisponível - FollowUpWorker está fazendo polling direto do banco"
                    )
                    
                await asyncio.sleep(self.check_interval)
            except Exception as e:
                logger.error(f"❌ Erro no loop de agendamento: {e}")
                await asyncio.sleep(60)

    async def enqueue_pending_followups(self):
        """
        Busca follow-ups pendentes e os enfileira no Redis.
        """
        try:
            now = datetime.now(timezone.utc)
            pending_followups = await self.db.get_pending_follow_ups()
            if not pending_followups:
                return
            logger.info(
                f"📋 {len(pending_followups)} follow-ups pendentes encontrados."
            )
            for followup in pending_followups:
                lead_id = followup.get('lead_id')
                if lead_id:
                    one_week_ago = now - timedelta(days=7)
                    count = await self.db.get_recent_followup_count(
                        lead_id, one_week_ago
                    )
                    if count >= settings.max_follow_up_attempts:
                        emoji_logger.system_warning(
                            f"🚫 Limite de follow-ups atingido para o lead {lead_id}."
                        )
                        await self.db.update_follow_up_status(
                            followup['id'], FollowUpStatus.CANCELLED.value
                        )
                        continue
                # Usa locks e enfileiramento no Redis
                lock_key = f"followup_enqueue:{followup['id']}"
                if await self.redis.acquire_lock(lock_key, ttl=60):
                    try:
                        task_payload = {
                            "task_type": "execute_followup",
                            "followup_id": followup['id'],
                            "lead_id": followup['lead_id'],
                            "phone_number": followup['phone_number'],
                            "followup_type": followup.get(
                                'follow_up_type', config.FOLLOW_UP_TYPES[6]  # CUSTOM
                            ),
                            "message": followup.get('message', ''),
                            "enqueued_at": now.isoformat()
                        }
                        await self.redis.enqueue("followup_tasks", task_payload)
                        await self.db.update_follow_up_status(
                            followup['id'], 'queued'
                        )
                        emoji_logger.followup_event(
                            f"✅ Follow-up {followup['id']} enfileirado no Redis."
                        )
                    except Exception as e:
                        logger.error(
                            f"❌ Erro ao enfileirar follow-up {followup['id']}: {e}"
                        )
                        await self.redis.release_lock(lock_key)
                else:
                    logger.warning(
                        f"⚠️ Follow-up {followup['id']} já está sendo processado."
                    )
        except Exception as e:
            logger.error(f"❌ Erro ao enfileirar follow-ups: {e}")

    async def _check_redis_availability(self) -> bool:
        """Verifica se o Redis está disponível."""
        try:
            return await self.redis.ping()
        except Exception:
            return False

    async def force_enqueue_followups(self):
        """Força o enfileiramento imediato de follow-ups pendentes."""
        logger.info("🔄 Forçando enfileiramento de follow-ups...")
        await self.enqueue_pending_followups()
        logger.info("✅ Processo de enfileiramento concluído.")
