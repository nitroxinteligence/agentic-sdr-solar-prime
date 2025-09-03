# app/services/followup_manager.py

from typing import Dict, Any
from datetime import datetime, timedelta
from app.utils.logger import emoji_logger
from app.integrations.supabase_client import supabase_client
from app.config import settings, FOLLOW_UP_TYPES

class FollowUpManagerService:
    """
    Gerencia a lógica de agendamento de follow-ups, centralizando
    as regras de negócio e limites.
    """

    def __init__(self):
        self.db = supabase_client

    async def handle_conversation_inactivity(
        self,
        lead_id: str,
        phone_number: str,
        inactive_since: datetime,
        current_status: str
    ) -> None:
        """
        Verifica a inatividade da conversa e agenda follow-ups de reengajamento
        se os limites permitirem.
        """
        now = datetime.now()
        inactive_time = now - inactive_since

        # Lógica para follow-up de 30 minutos
        if inactive_time > timedelta(minutes=30) and current_status != 'followup_30min_sent':
            await self._schedule_reengagement_followup(
                lead_id, phone_number, FOLLOW_UP_TYPES[0], inactive_since.isoformat()
            )
            # Atualizar status no Redis para evitar agendamentos duplicados
            # Isso será feito no ConversationMonitor, que chamará este serviço

        # Lógica para follow-up de 24 horas
        elif inactive_time > timedelta(hours=24) and current_status != 'followup_24h_sent':
            await self._schedule_reengagement_followup(
                lead_id, phone_number, FOLLOW_UP_TYPES[1], inactive_since.isoformat()
            )
            # Atualizar status no Redis

        # Lógica para desqualificação automática após 48 horas
        elif inactive_time > timedelta(hours=48) and current_status != 'followup_48h_sent':
            await self._schedule_disqualification_followup(
                lead_id, phone_number, inactive_since.isoformat()
            )

    async def _schedule_reengagement_followup(
        self,
        lead_id: str,
        phone_number: str,
        followup_type: str,
        inactive_since_iso: str
    ) -> None:
        """
        Agenda um follow-up de reengajamento no banco de dados, respeitando o limite.
        """
        one_week_ago = datetime.now() - timedelta(days=7)
        count = await self.db.get_recent_followup_count(lead_id, one_week_ago)

        if count >= settings.max_follow_up_attempts:
            emoji_logger.system_warning(
                f"🚫 Limite de follow-ups atingido para o lead {lead_id}. Tipo: {followup_type}"
            )
            # Não agendar, mas registrar que o limite foi atingido
            return

        followup_data = {
            'lead_id': lead_id,
            'phone_number': phone_number,
            'type': 'reengagement',
            'follow_up_type': followup_type,
            'scheduled_at': datetime.now().isoformat(), # Agendado para agora, worker vai pegar
            'status': 'pending',
            'message': '', # A mensagem será gerada pelo worker
            'priority': 'medium',
            'attempt': count + 1,
            'metadata': {
                'source': 'followup_manager',
                'inactive_since': inactive_since_iso,
                'original_type': followup_type
            }
        }

        try:
            await self.db.create_follow_up(followup_data)
            emoji_logger.followup_event(
                f"✅ Follow-up agendado: {followup_type} para {phone_number[:8]}... (Tentativa {count + 1})"
            )
        except Exception as e:
            emoji_logger.system_error(
                "FollowUpManagerService", f"Erro ao criar follow-up no DB: {e}"
            )

    async def _schedule_disqualification_followup(
        self,
        lead_id: str,
        phone_number: str,
        inactive_since: str
    ):
        """Agenda desqualificação automática após 48h sem resposta"""
        try:
            from app.services.followup_service_100_real import FollowUpServiceReal
            
            followup_service = FollowUpServiceReal()
            
            # Calcula o tempo restante até completar 48h desde a última interação
            inactive_since_dt = datetime.fromisoformat(inactive_since)
            hours_since_inactive = (datetime.now() - inactive_since_dt).total_seconds() / 3600
            delay_hours = max(0, 48 - hours_since_inactive)
            
            # Agenda follow-up de desqualificação para o momento correto (48h após última interação)
            await followup_service.schedule_followup(
                phone_number=phone_number,
                message="DISQUALIFY_LEAD",  # Mensagem especial para desqualificação
                delay_hours=delay_hours,  # Tempo correto até 48h
                followup_type=FOLLOW_UP_TYPES[5],
                lead_id=lead_id,
                context={
                    "inactive_since": inactive_since,
                    "reason": "48h_no_response",
                    "action": "disqualify_to_nao_interessado"
                }
            )
            
            # Atualizar status no Redis
            await self.redis_client.set(
                f"conversation_status:{phone_number}",
                'followup_48h_disqualified',
                ex=86400 * 7  # 7 dias
            )
            
            emoji_logger.system_warning(
                f"🚫 Desqualificação automática agendada para {phone_number} após 48h sem resposta"
            )
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao agendar desqualificação automática: {e}"
            )

# Instância singleton
followup_manager_service = FollowUpManagerService()
