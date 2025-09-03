"""Versão debug do AgenticSDR Stateless sem ConversationMonitor"""

from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import pytz
import re
import traceback

from app.integrations.supabase_client import supabase_client
from app.core.model_manager import ModelManager
from app.core.multimodal_processor import MultimodalProcessor
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
# ConversationMonitor removido para debug
# from app.services.conversation_monitor import get_conversation_monitor
from app.utils.logger import emoji_logger
from app.core.response_formatter import response_formatter
from app.utils.time_utils import get_period_of_day
from app.config import settings

from app.services.calendar_service_100_real import CalendarServiceReal
from app.services.crm_service_100_real import CRMServiceReal
from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.knowledge_service import KnowledgeService
from app.services.crm_sync_service import crm_sync_service


class AgenticSDRStatelessDebug:
    """Versão debug do AgenticSDR Stateless sem ConversationMonitor"""

    def __init__(self):
        """Inicializa apenas os módulos (stateless)"""
        self.model_manager = ModelManager()
        self.multimodal = MultimodalProcessor()
        self.lead_manager = LeadManager()
        self.context_analyzer = ContextAnalyzer()
        # ConversationMonitor removido para debug
        # self.conversation_monitor = get_conversation_monitor()

        self.calendar_service = CalendarServiceReal()
        self.crm_service = CRMServiceReal()
        self.followup_service = FollowUpServiceReal()
        self.knowledge_service = KnowledgeService()

    async def initialize(self):
        """Inicializa os serviços"""
        try:
            # Inicializar serviços
            self.model_manager.initialize()
            emoji_logger.system_ready("ModelManager")

            self.multimodal.initialize()
            emoji_logger.system_ready("MultimodalProcessor")

            self.lead_manager.initialize()
            emoji_logger.system_ready("LeadManager")

            self.context_analyzer.initialize()
            emoji_logger.system_ready("🧠 ContextAnalyzer")

            # ConversationMonitor removido para debug
            # await self.conversation_monitor.initialize()

            await self.calendar_service.initialize()
            await self.crm_service.initialize()
            await self.followup_service.initialize()

            modules = [
                'ModelManager',
                'MultimodalProcessor', 
                'LeadManager',
                'ContextAnalyzer',
                'CalendarService',
                'CRMService',
                'FollowUpService'
            ]

            emoji_logger.system_ready(
                "✅ AgenticSDR Stateless DEBUG inicializado!",
                data={"modules": modules}
            )

        except Exception as e:
            emoji_logger.system_error("AgenticSDR", f"Erro na inicialização: {e}")
            raise

    async def process_message(
            self,
            message: str,
            execution_context: Dict[str, Any]
    ) -> tuple[str, Dict[str, Any]]:
        """Processa uma mensagem e retorna resposta + contexto atualizado"""
        try:
            phone = execution_context.get('phone')
            if not phone:
                raise ValueError("Phone é obrigatório no execution_context")

            # Buscar informações do lead
            lead_info = await self.lead_manager.get_or_create_lead(phone)
            if not lead_info:
                raise ValueError(f"Não foi possível obter/criar lead para {phone}")

            # Buscar histórico de conversas
            conversation_history = await supabase_client.get_conversation_history(
                lead_info['id'], limit=10
            )

            # Processar mídia se presente
            media_data = {}
            if execution_context.get('media_url'):
                media_data = await self.multimodal.process_media(
                    execution_context['media_url'],
                    execution_context.get('media_type', 'image')
                )

            # Atualizar contexto
            conversation_history, lead_info = await self._update_context(
                message, conversation_history, lead_info, media_data
            )

            # Sincronizar com serviços externos
            lead_info = await self._sync_external_services(lead_info, phone)

            # Registrar mensagem no monitor de conversas (removido para debug)
            # await self.conversation_monitor.register_message(
            #     phone=phone,
            #     is_from_user=True,
            #     lead_info=lead_info
            # )

            # Gerar resposta
            response = await self._generate_response(
                message, execution_context, lead_info, conversation_history, execution_context
            )

            # Registrar resposta no monitor (removido para debug)
            # await self.conversation_monitor.register_message(
            #     phone=phone,
            #     is_from_user=False,
            #     lead_info=lead_info
            # )

            return response, execution_context

        except Exception as e:
            emoji_logger.system_error("AgenticSDR", f"Erro ao processar mensagem: {e}")
            emoji_logger.system_error("AgenticSDR", f"Traceback: {traceback.format_exc()}")
            return "Desculpe, ocorreu um erro interno. Tente novamente.", execution_context

    # Métodos auxiliares simplificados (apenas os essenciais para o debug)
    async def _update_context(self, message: str, conversation_history: list, lead_info: dict, media_data: dict) -> tuple[list, dict]:
        """Atualiza contexto da conversa"""
        return conversation_history, lead_info

    async def _sync_external_services(self, lead_info: dict, phone: str) -> dict:
        """Sincroniza com serviços externos"""
        return lead_info

    async def _generate_response(
        self,
        message: str,
        context: dict,
        lead_info: dict,
        conversation_history: list,
        execution_context: dict,
        is_followup: bool = False
    ) -> str:
        """Gera resposta simples para debug"""
        return "Sistema funcionando! Esta é uma resposta de debug."


# Instância global para debug
_agentic_sdr_debug = None

def get_agentic_sdr_debug():
    """Retorna instância singleton do AgenticSDR Debug"""
    global _agentic_sdr_debug
    if _agentic_sdr_debug is None:
        _agentic_sdr_debug = AgenticSDRStatelessDebug()
    return _agentic_sdr_debug