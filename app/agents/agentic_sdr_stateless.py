"""
AgenticSDR Stateless - Arquitetura ZERO complexidade para produção
Cada requisição é completamente isolada e independente
Não há estado compartilhado entre conversas
"""

from typing import Dict, Any, Optional, List
import asyncio
from datetime import datetime
import pytz
import re

from app.core.model_manager import ModelManager
from app.core.multimodal_processor import MultimodalProcessor
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
# Removido TeamCoordinator - vamos instanciar serviços diretamente
from app.services.conversation_monitor import get_conversation_monitor
from app.utils.logger import emoji_logger
from app.config import settings

# Importar serviços diretamente
from app.services.calendar_service_100_real import CalendarServiceReal
from app.services.crm_service_100_real import CRMServiceReal
from app.services.followup_service_100_real import FollowUpServiceReal

class AgenticSDRStateless:
    """
    SDR Agent STATELESS - Cada requisição é isolada
    Sem singleton, sem estado compartilhado
    100% thread-safe e multi-tenant
    """
    
    def __init__(self):
        """Inicializa apenas os módulos (stateless)"""
        # Módulos stateless
        self.model_manager = ModelManager()
        self.multimodal = MultimodalProcessor()
        self.lead_manager = LeadManager()
        self.context_analyzer = ContextAnalyzer()
        self.conversation_monitor = get_conversation_monitor()

        # Serviços
        self.calendar_service = CalendarServiceReal()
        self.crm_service = CRMServiceReal()
        self.followup_service = FollowUpServiceReal()
        
        # SEM ESTADO INTERNO!
        # Cada requisição traz seu próprio contexto
        self.is_initialized = False
        
    async def initialize(self):
        """Inicialização dos módulos assíncronos"""
        if self.is_initialized:
            return
        
        emoji_logger.system_event("🚀 Inicializando AgenticSDR Stateless...")
        
        try:
            # Inicializar módulos e serviços
            self.model_manager.initialize()
            self.multimodal.initialize()
            self.lead_manager.initialize()
            self.context_analyzer.initialize()
            await self.conversation_monitor.initialize()
            try:
                await self.calendar_service.initialize()
            except Exception as e:
                emoji_logger.system_warning(f"Falha ao inicializar CalendarService: {e}. O agente continuará sem funcionalidades de calendário.")
            await self.crm_service.initialize()
            await self.followup_service.initialize()
            
            self.is_initialized = True
            emoji_logger.system_ready(
                "✅ AgenticSDR Stateless inicializado!",
                modules=[
                    "ModelManager", "MultimodalProcessor", 
                    "LeadManager", "ContextAnalyzer", "CalendarService", "CRMService", "FollowUpService"
                ]
            )
            
        except Exception as e:
            emoji_logger.system_error("AgenticSDRStateless", error=f"Erro na inicialização: {e}")
            raise
    
    async def process_message(self, 
                             message: str, 
                             execution_context: Dict[str, Any]) -> str:
        """
        Processa mensagem com contexto isolado
        
        Args:
            message: Mensagem do usuário
            execution_context: Contexto completo da execução incluindo:
                - conversation_history: Histórico completo
                - lead_info: Informações do lead
                - phone: Número do telefone
                - conversation_id: ID da conversa
                - media: Dados de mídia se houver
                - timestamp: Data/hora atual
            
        Returns:
            Resposta do agent
        """
        if not self.is_initialized:
            await self.initialize()
        
        emoji_logger.conversation_event(f"💬 Processando (stateless): {message[:100]}...")
        
        # Extrair dados do contexto de execução
        conversation_history = execution_context.get("conversation_history", [])
        lead_info = execution_context.get("lead_info", {})
        phone = execution_context.get("phone")
        conversation_id = execution_context.get("conversation_id")
        media_data = execution_context.get("media")
        
        # Registrar mensagem no monitor
        if phone:
            await self.conversation_monitor.register_message(
                phone=phone,
                is_from_user=True,
                lead_info=lead_info
            )
        
        try:
            # 1. Processar mídia se houver
            media_context = ""
            if media_data:
                media_result = await self.multimodal.process_media(media_data)
                if media_result.get("success"):
                    media_context = self._format_media_context(media_result)
                    emoji_logger.multimodal_event("📎 Mídia processada com sucesso")
            
            # 2. Adicionar mensagem atual ao histórico
            user_message = {
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            }
            conversation_history.append(user_message)
            
            # 2.1 Salvar mensagem no banco se tiver ID
            if conversation_id and phone:
                await self._save_message_to_db(conversation_id, user_message)
            
            # 3. Analisar contexto
            context = self.context_analyzer.analyze_context(
                conversation_history,
                message
            )
            
            # 4. Extrair informações do lead
            new_lead_info = self.lead_manager.extract_lead_info(conversation_history)
            
            # 5. Detectar mudanças e sincronizar
            lead_changes = self._detect_lead_changes(lead_info, new_lead_info)
            if lead_changes and phone:
                await self._sync_lead_changes(lead_changes, phone, lead_info)
            
            # Atualizar lead_info com novas informações
            lead_info.update(new_lead_info)
            
            # 6. Gerar resposta com contexto completo
                        # 6. Gerar resposta com contexto completo
            response = await self._generate_response(
                message,
                context,
                lead_info,
                media_context,
                conversation_history,
                execution_context
            )
            
            # 8. Salvar resposta no banco
            assistant_message = {
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().isoformat()
            }
            
            if conversation_id and phone:
                await self._save_message_to_db(conversation_id, assistant_message)
            
            # 9. Registrar resposta no monitor
            if phone:
                await self.conversation_monitor.register_message(
                    phone=phone,
                    is_from_user=False,
                    lead_info=lead_info
                )
            
            emoji_logger.conversation_event(f"✅ Resposta gerada: {response[:100]}...")
            return response
            
        except Exception as e:
            import traceback
            emoji_logger.system_error("AgenticSDRStateless", error=f"Erro: {e}")
            emoji_logger.system_error("AgenticSDRStateless", error=f"Traceback: {traceback.format_exc()}")
            return "Desculpe, tive um problema ao processar sua mensagem. Pode repetir? 🤔"
    
    async def _execute_post_scheduling_workflow(self, schedule_result: dict, lead_info: dict, context: dict):
        """
        Executa o workflow pós-agendamento de forma robusta, com tratamento de erro individual.
        """
        kommo_lead_id = lead_info.get("kommo_lead_id")
        if not kommo_lead_id:
            emoji_logger.service_warning("Kommo lead ID não encontrado. Pulando workflow pós-agendamento.")
            return

        # 1. Atualizar estágio no CRM
        try:
            await self._execute_single_tool(
                "crm.update_stage", {"stage": "reuniao_agendada"}, lead_info, context
            )
        except Exception as e:
            emoji_logger.system_error("Post-scheduling workflow", f"Falha ao atualizar estágio no CRM: {e}")
            # Continua a execução mesmo em caso de falha

        # 2. Salvar link do evento no CRM
        try:
            google_event_link = schedule_result.get("link")
            if google_event_link:
                await self._execute_single_tool(
                    "crm.update_field", {"field": "calendar_link", "value": google_event_link}, lead_info, context
                )
        except Exception as e:
            emoji_logger.system_error("Post-scheduling workflow", f"Falha ao salvar link do evento no CRM: {e}")
            # Continua a execução

        # 3. Agendar follow-ups de lembrete
        try:
            meeting_time_str = schedule_result.get("start_time")
            if meeting_time_str:
                meeting_time = datetime.fromisoformat(meeting_time_str.replace("Z", "+00:00"))
                now = datetime.now(pytz.utc)

                # Lembrete de 24h
                if meeting_time > now + timedelta(hours=24):
                    reminder_24h_msg = f"Oi {lead_info.get('name', '')}! Passando para confirmar nossa reunião de amanhã às {meeting_time.strftime('%H:%M')}. Está tudo certo para você?"
                    await self._execute_single_tool(
                        "followup.schedule", {"hours": 24, "message": reminder_24h_msg}, lead_info, context
                    )

                # Lembrete de 2h
                if meeting_time > now + timedelta(hours=2):
                    reminder_2h_msg = f"{lead_info.get('name', '')}, nossa reunião é daqui a 2 horas! Te esperamos às {meeting_time.strftime('%H:%M')}!"
                    await self._execute_single_tool(
                        "followup.schedule", {"hours": 2, "message": reminder_2h_msg}, lead_info, context
                    )
        except Exception as e:
            emoji_logger.system_error("Post-scheduling workflow", f"Falha ao agendar follow-ups de lembrete: {e}")
            # Finaliza o workflow aqui, mas o erro foi logado

        emoji_logger.system_success("✅ Workflow pós-agendamento executado com as devidas tratativas de erro.")

    async def _parse_and_execute_tools(self, response: str, lead_info: dict, context: dict) -> dict:
        """
        Parse e executa tool calls na resposta do agente
        Formato: [TOOL: service.method | param=value | param2=value2]
        """
        
        tool_pattern = r'\[TOOL:\s*([^|\]]+?)\s*(?:\|\s*([^\]]*))?\]'
        tool_matches = re.findall(tool_pattern, response)
        
        if not tool_matches:
            return {}
        
        tool_results = {}
        
        for match in tool_matches:
            service_method = match[0].strip()
            params_str = match[1].strip() if len(match) > 1 and match[1] else ""
            
            # Parse dos parâmetros
            params = {}
            if params_str:
                param_pairs = params_str.split('|')
                for pair in param_pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        params[key.strip()] = value.strip()
            
            # Executar o tool
            try:
                result = await self._execute_single_tool(
                    service_method, params, lead_info, context
                )
                tool_results[service_method] = result
                emoji_logger.system_success(f"✅ Tool executado: {service_method}")
            except Exception as e:
                tool_results[service_method] = {"error": str(e)}
                emoji_logger.system_error("Tool execution error", error=f"❌ Erro no tool {service_method}: {e}")
        
        return tool_results

    async def _execute_single_tool(self, service_method: str, params: dict, lead_info: dict, context: dict):
        """Executa um tool específico"""
        
        parts = service_method.split('.')
        if len(parts) != 2:
            raise ValueError(f"Formato inválido: {service_method}")
        
        service_name, method_name = parts
        
        # Calendar tools
        if service_name == "calendar":
            if method_name == "check_availability":
                return await self.calendar_service.check_availability(
                    context.get("message", "")
                )
            elif method_name == "schedule_meeting":
                result = await self.calendar_service.schedule_meeting(
                    date=params.get("date"),
                    time=params.get("time"),
                    lead_info={
                        **lead_info,
                        "email": params.get("email", lead_info.get("email"))
                    }
                )
                if result and result.get("success"):
                    await self._execute_post_scheduling_workflow(result, lead_info, context)
                return result
            elif method_name == "suggest_times":
                return await self.calendar_service.suggest_times(lead_info)
            elif method_name == "cancel_meeting":
                meeting_id = params.get("meeting_id")
                if not meeting_id:
                    raise ValueError("meeting_id é obrigatório para cancelar reunião")
                return await self.calendar_service.cancel_meeting(meeting_id)
            elif method_name == "reschedule_meeting":
                meeting_id = params.get("meeting_id")
                date = params.get("date")
                time = params.get("time")
                if not meeting_id:
                    raise ValueError("meeting_id é obrigatório para reagendar reunião")
                return await self.calendar_service.reschedule_meeting(
                    meeting_id=meeting_id,
                    date=date,
                    time=time,
                    lead_info=lead_info
                )
        
        # CRM tools
        elif service_name == "crm":
            # ALIAS: Aceitar "update_stage" do prompt e mapear para "update_lead_stage"
            if method_name == "update_stage":
                stage = params.get("stage", "").lower()
                return await self.crm_service.update_lead_stage(
                    lead_info.get("kommo_lead_id"),
                    stage
                )
            elif method_name == "update_field":
                field_name = params.get("field")
                field_value = params.get("value")
                if field_name and field_value:
                    return await self.crm_service.update_fields(
                        lead_info.get("kommo_lead_id"),
                        {field_name: field_value}
                    )
        
        # Follow-up tools
        elif service_name == "followup":
            if method_name == "schedule":
                hours = int(params.get("hours", 24))
                message = params.get("message", "Oi! Tudo bem? Ainda tem interesse em energia solar?")
                return await self.followup_service.schedule_followup(
                    phone_number=lead_info.get("phone_number"),
                    message=message,
                    delay_hours=hours,
                    lead_info=lead_info
                )
        
        raise ValueError(f"Tool não reconhecido: {service_method}")