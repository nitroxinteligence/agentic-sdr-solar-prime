"""
FollowUp Worker - Processa tarefas da fila de follow-ups do Redis
"""

import asyncio
from typing import Dict, Any

from app.integrations.redis_client import redis_client
from app.integrations.supabase_client import SupabaseClient
from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.utils.logger import emoji_logger
from loguru import logger


class FollowUpWorker:
    """
    Worker que consome tarefas da fila de follow-ups e as executa.
    """

    def __init__(self):
        self.redis = redis_client
        self.db = SupabaseClient()
        self.running = False
        self.agent = AgenticSDRStateless()

    async def start(self):
        """Inicia o worker e o loop de consumo da fila."""
        if self.running:
            logger.warning("Follow-up worker já está rodando.")
            return

        await self.agent.initialize()
        self.running = True
        emoji_logger.system_ready("FollowUp Worker")
        asyncio.create_task(self._consume_loop())

    async def stop(self):
        """Para o worker."""
        self.running = False
        logger.info("Follow-up worker parado.")

    async def _consume_loop(self):
        """Loop principal que consome tarefas da fila do Redis."""
        while self.running:
            try:
                task_payload = await self.redis.dequeue(
                    "followup_tasks", timeout=10
                )
                if task_payload:
                    await self._process_task(task_payload)
            except Exception as e:
                emoji_logger.system_error(
                    "FollowUp Worker", f"Erro no loop de consumo: {e}"
                )
                await asyncio.sleep(5)

    async def _process_task(self, task_payload: Dict[str, Any]):
        """
        Processa uma única tarefa de follow-up.
        """
        followup_id = task_payload.get("followup_id")
        if not followup_id:
            logger.error("Task de follow-up sem ID, descartando.")
            return

        lock_key = f"followup_exec:{followup_id}"
        if not await self.redis.acquire_lock(lock_key, ttl=300):
            logger.warning(
                f"Execução do follow-up {followup_id} já em andamento, pulando."
            )
            return

        try:
            emoji_logger.followup_event(
                f"🚀 Processando tarefa de follow-up: {followup_id}"
            )

            message_content = await self._generate_intelligent_followup_message(
                task_payload
            )

            from app.integrations.evolution import evolution_client
            send_result = await evolution_client.send_text_message(
                phone=task_payload["phone_number"],
                message=message_content
            )

            if send_result and send_result.get("key", {}).get("id"):
                await self.db.update_follow_up_status(followup_id, 'executed')
                emoji_logger.system_success(
                    f"✅ Follow-up {followup_id} executado e enviado com sucesso."
                )
            else:
                await self.db.update_follow_up_status(followup_id, 'failed')
                emoji_logger.system_error(
                    "FollowUp Worker",
                    f"Falha ao enviar mensagem para o follow-up {followup_id}."
                )

        except Exception as e:
            emoji_logger.system_error(
                "FollowUp Worker",
                f"Erro ao processar tarefa {followup_id}: {e}"
            )
            await self.db.update_follow_up_status(followup_id, 'failed')
        finally:
            await self.redis.release_lock(lock_key)

    async def _generate_intelligent_followup_message(
            self, task_payload: Dict[str, Any]
    ) -> str:
        """
        Usa o AgenticSDRStateless para gerar uma mensagem de follow-up.
        """
        lead_id = task_payload.get("lead_id")
        followup_type = task_payload.get("followup_type", "CUSTOM")

        if not lead_id:
            emoji_logger.system_error(
                "FollowUp Worker",
                f"Task {task_payload.get('followup_id')} não contém 'lead_id'."
            )
            return "Não foi possível gerar a mensagem de follow-up."

        lead_info = await self.db.get_lead_by_id(lead_id)
        conversation_history = await self.db.get_conversation_messages(
            lead_info.get('conversation_id')
        ) if lead_info else []

        execution_context = {
            "conversation_history": conversation_history,
            "lead_info": lead_info or {},
            "phone": task_payload.get("phone_number"),
            "conversation_id": (
                lead_info.get('conversation_id') if lead_info else None
            ),
        }

        prompt = (
            f"Gere uma mensagem de follow-up do tipo '{followup_type}' para "
            f"este lead, com base no nosso histórico de conversa."
        )

        response_text = await self.agent._generate_response(
            message=prompt,
            context={},
            lead_info=lead_info,
            media_context="",
            conversation_history=conversation_history,
            execution_context=execution_context,
            is_followup=True
        )

        from app.api.webhooks import extract_final_response
        return extract_final_response(response_text)


async def main():
    """Função principal para iniciar o worker."""
    worker = FollowUpWorker()
    await worker.start()
    while worker.running:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
