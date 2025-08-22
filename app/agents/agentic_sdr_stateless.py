"""
AgenticSDR Stateless - Arquitetura ZERO complexidade para produção
Cada requisição é completamente isolada e independente
Não há estado compartilhado entre conversas
"""

from typing import Dict, Any
from datetime import datetime, timedelta
import pytz
import re

from app.core.model_manager import ModelManager
from app.core.multimodal_processor import MultimodalProcessor
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
from app.services.conversation_monitor import get_conversation_monitor
from app.utils.logger import emoji_logger
from app.core.response_formatter import response_formatter

# Importar serviços diretamente
from app.services.calendar_service_100_real import CalendarServiceReal
from app.services.crm_service_100_real import CRMServiceReal
from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.knowledge_service import KnowledgeService


class AgenticSDRStateless:
    """
    SDR Agent STATELESS - Cada requisição é isolada
    Sem singleton, sem estado compartilhado
    100% thread-safe e multi-tenant
    """

    def __init__(self):
        """Inicializa apenas os módulos (stateless)"""
        self.model_manager = ModelManager()
        self.multimodal = MultimodalProcessor()
        self.lead_manager = LeadManager()
        self.context_analyzer = ContextAnalyzer()
        self.conversation_monitor = get_conversation_monitor()

        self.calendar_service = CalendarServiceReal()
        self.crm_service = CRMServiceReal()
        self.followup_service = FollowUpServiceReal()
        self.knowledge_service = KnowledgeService()

        self.is_initialized = False

    async def initialize(self):
        """Inicialização dos módulos assíncronos"""
        if self.is_initialized:
            return

        emoji_logger.system_start("AgenticSDR Stateless")

        try:
            self.model_manager.initialize()
            self.multimodal.initialize()
            self.lead_manager.initialize()
            self.context_analyzer.initialize()
            await self.conversation_monitor.initialize()
            try:
                await self.calendar_service.initialize()
            except Exception as e:
                emoji_logger.system_warning(
                    f"Falha ao inicializar CalendarService: {e}. "
                    f"O agente continuará sem funcionalidades de calendário."
                )
            await self.crm_service.initialize()
            await self.followup_service.initialize()

            self.is_initialized = True
            emoji_logger.system_ready(
                "✅ AgenticSDR Stateless inicializado!",
                modules=[
                    "ModelManager", "MultimodalProcessor",
                    "LeadManager", "ContextAnalyzer", "CalendarService",
                    "CRMService", "FollowUpService"
                ]
            )

        except Exception as e:
            emoji_logger.system_error(
                "AgenticSDRStateless",
                error=f"Erro na inicialização: {e}"
            )
            raise

    async def process_message(
            self,
            message: str,
            execution_context: Dict[str, Any]
    ) -> tuple[str, Dict[str, Any]]:
        """
        Processa mensagem com contexto isolado
        """
        if not self.is_initialized:
            await self.initialize()

        emoji_logger.agentic_start(
            f"Processando (stateless): {message[:100]}..."
        )

        conversation_history = execution_context.get(
            "conversation_history", []
        )
        lead_info = execution_context.get("lead_info", {})
        phone = execution_context.get("phone")
        conversation_id = execution_context.get("conversation_id")
        media_data = execution_context.get("media")

        if phone:
            await self.conversation_monitor.register_message(
                phone=phone,
                is_from_user=True,
                lead_info=lead_info
            )

        if conversation_history and conversation_history[-1]['role'] == 'assistant':
            last_assistant_message = conversation_history[-1]['content'].lower()
            # Se a última mensagem foi uma pergunta sobre agendamento, e o usuário respondeu positivamente
            if any(q in last_assistant_message for q in ["marcar uma reunião", "quando podemos marcar", "quando você estaria disponível"]):
                if any(a in message.lower() for a in ["pode ser", "sim", "claro", "pode", "ok"]):
                    # Força o contexto para agendamento
                    context['conversation_stage'] = 'agendamento'
                    emoji_logger.system_info("Sanity Check: Forçando estágio de agendamento.")

        try:
            # 1. PROCESSAR MÍDIA (SE EXISTIR)
            user_message_content = [
                {"type": "text", "text": message}
            ]
            if media_data:
                # A mídia já vem em base64 do webhook
                media_content = media_data.get("content") or media_data.get("data", "")
                media_type = media_data.get("type", "image") # Default to image if not specified
                mime_type = media_data.get("mime_type", "image/jpeg") # Default to jpeg

                if "base64," in media_content:
                    media_content = media_content.split("base64,")[1]

                # Estrutura genérica para qualquer tipo de mídia
                user_message_content.append({
                    "type": "media",
                    "media_data": {
                        "mime_type": mime_type,
                        "content": media_content
                    }
                })
                emoji_logger.multimodal_event(f"📎 Mídia do tipo {mime_type} adicionada de forma genérica ao prompt.")

            # 2. ATUALIZAR HISTÓRICO
            user_message = {
                "role": "user",
                "content": user_message_content,
                "timestamp": datetime.now().isoformat()
            }
            conversation_history.append(user_message)

            # Extrair texto da mídia para análise de contexto, se necessário
            # Isso é feito de forma assíncrona para não bloquear a resposta principal
            if media_data:
                media_result = await self.multimodal.process_media(media_data)
                if media_result.get("success"):
                    extracted_bill_value = media_result.get("analysis", {}).get("bill_value")
                    if extracted_bill_value:
                        lead_info['bill_value'] = extracted_bill_value
                        emoji_logger.system_info(f"Valor da conta R${extracted_bill_value} extraído e injetado no lead_info.")
                else:
                    emoji_logger.system_warning(f"Falha na extração de texto da mídia: {media_result.get('message')}")

            # 3. EXECUTAR ANÁLISES COM DADOS ATUALIZADOS
            new_lead_info = self.lead_manager.extract_lead_info(
                conversation_history,
                existing_lead_info=lead_info
            )

            lead_changes = self._detect_lead_changes(lead_info, new_lead_info)
            if lead_changes:
                from app.integrations.supabase_client import supabase_client
                lead_id_to_update = lead_info.get("id")
                if lead_id_to_update:
                    await supabase_client.update_lead(lead_id_to_update, lead_changes)
                    emoji_logger.system_info("Estado do lead sincronizado com o banco de dados.", changes=lead_changes)

            lead_info.update(new_lead_info)

            # 4. SINCRONIZAR CRM
            if lead_info.get("name") and not lead_info.get("kommo_lead_id"):
                try:
                    kommo_response = await self.crm_service.create_lead(lead_info)
                    if kommo_response.get("success"):
                        new_kommo_id = kommo_response.get("lead_id")
                        lead_info["kommo_lead_id"] = new_kommo_id
                        await supabase_client.update_lead(lead_info["id"], {"kommo_lead_id": new_kommo_id})
                        emoji_logger.team_crm(f"Lead criado no Kommo com ID: {new_kommo_id}")
                except Exception as e:
                    emoji_logger.system_error("Falha ao criar lead no Kommo", error=str(e))

            # 5. GERAR RESPOSTA
            context = self.context_analyzer.analyze_context(
                conversation_history,
                lead_info
            )

            response = await self._generate_response(
                message,
                context,
                lead_info,
                conversation_history,
                execution_context
            )

            assistant_message = {
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().isoformat()
            }

            if phone:
                await self.conversation_monitor.register_message(
                    phone=phone,
                    is_from_user=False,
                    lead_info=lead_info
                )

            emoji_logger.system_success(
                f"Resposta gerada: {response[:100]}..."
            )
            return response_formatter.ensure_response_tags(response), lead_info

        except Exception as e:
            import traceback
            emoji_logger.system_error(
                "AgenticSDRStateless",
                error=f"Erro: {e}"
            )
            emoji_logger.system_error(
                "AgenticSDRStateless",
                error=f"Traceback: {traceback.format_exc()}"
            )
            return (
                "<RESPOSTA_FINAL>Desculpe, tive um problema aqui. "
                "Pode repetir?</RESPOSTA_FINAL>",
                lead_info
            )

    async def _execute_post_scheduling_workflow(
            self,
            schedule_result: dict,
            lead_info: dict,
            context: dict
    ):
        """
        Executa o workflow pós-agendamento de forma robusta.
        """
        kommo_lead_id = lead_info.get("kommo_lead_id")
        if not kommo_lead_id:
            emoji_logger.service_warning(
                "Kommo lead ID não encontrado. "
                "Pulando workflow pós-agendamento."
            )
            return

        try:
            await self._execute_single_tool(
                "crm.update_stage",
                {"stage": "reuniao_agendada"},
                lead_info,
                context
            )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao atualizar estágio no CRM: {e}"
            )

        try:
            google_event_link = schedule_result.get("link")
            if google_event_link:
                await self._execute_single_tool(
                    "crm.update_field",
                    {"field": "calendar_link", "value": google_event_link},
                    lead_info,
                    context
                )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao salvar link do evento no CRM: {e}"
            )

        try:
            meeting_time_str = schedule_result.get("start_time")
            if meeting_time_str:
                meeting_time = datetime.fromisoformat(
                    meeting_time_str.replace("Z", "+00:00")
                )
                now = datetime.now(pytz.utc)

                if meeting_time > now + timedelta(hours=24):
                    reminder_24h_msg = (
                        f"Oi {lead_info.get('name', '')}! Passando para "
                        f"confirmar nossa reunião de amanhã às "
                        f"{meeting_time.strftime('%H:%M')}. "
                        f"Está tudo certo para você?"
                    )
                    await self._execute_single_tool(
                        "followup.schedule",
                        {"hours": 24, "message": reminder_24h_msg},
                        lead_info,
                        context
                    )

                if meeting_time > now + timedelta(hours=2):
                    reminder_2h_msg = (
                        f"{lead_info.get('name', '')}, nossa reunião é "
                        f"daqui a 2 horas! Te esperamos às "
                        f"{meeting_time.strftime('%H:%M')}!"
                    )
                    await self._execute_single_tool(
                        "followup.schedule",
                        {"hours": 2, "message": reminder_2h_msg},
                        lead_info,
                        context
                    )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao agendar follow-ups de lembrete: {e}"
            )

        try:
            await self._execute_single_tool(
                "crm.update_stage",
                {"stage": "reuniao_agendada"},
                lead_info,
                context
            )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao atualizar estágio no CRM: {e}"
            )

        try:
            google_event_link = schedule_result.get("link")
            if google_event_link:
                await self._execute_single_tool(
                    "crm.update_field",
                    {"field": "calendar_link", "value": google_event_link},
                    lead_info,
                    context
                )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao salvar link do evento no CRM: {e}"
            )

        try:
            meeting_time_str = schedule_result.get("start_time")
            if meeting_time_str:
                meeting_time = datetime.fromisoformat(
                    meeting_time_str.replace("Z", "+00:00")
                )
                now = datetime.now(pytz.utc)

                if meeting_time > now + timedelta(hours=24):
                    reminder_24h_msg = (
                        f"Oi {lead_info.get('name', '')}! Passando para "
                        f"confirmar nossa reunião de amanhã às "
                        f"{meeting_time.strftime('%H:%M')}. "
                        f"Está tudo certo para você?"
                    )
                    await self._execute_single_tool(
                        "followup.schedule",
                        {"hours": 24, "message": reminder_24h_msg},
                        lead_info,
                        context
                    )

                if meeting_time > now + timedelta(hours=2):
                    reminder_2h_msg = (
                        f"{lead_info.get('name', '')}, nossa reunião é "
                        f"daqui a 2 horas! Te esperamos às "
                        f"{meeting_time.strftime('%H:%M')}!"
                    )
                    await self._execute_single_tool(
                        "followup.schedule",
                        {"hours": 2, "message": reminder_2h_msg},
                        lead_info,
                        context
                    )
        except Exception as e:
            emoji_logger.system_error(
                "Post-scheduling workflow",
                f"Falha ao agendar follow-ups de lembrete: {e}"
            )

        emoji_logger.system_success(
            "✅ Workflow pós-agendamento executado com as devidas "
            "tratativas de erro."
        )

    async def _parse_and_execute_tools(
            self,
            response: str,
            lead_info: dict,
            context: dict
    ) -> dict:
        """
        Parse e executa tool calls na resposta do agente.
        """
        tool_pattern = r'\[TOOL:\s*([^|\]]+?)\s*(?:\|\s*([^\]]*))?\]'
        tool_matches = re.findall(tool_pattern, response)

        if not tool_matches:
            return {}

        tool_results = {}

        for match in tool_matches:
            service_method = match[0].strip()
            params_str = match[1].strip() if len(
                match) > 1 and match[1] else ""

            params = {}
            if params_str:
                param_pairs = params_str.split('|')
                for pair in param_pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        params[key.strip()] = value.strip()

            try:
                result = await self._execute_single_tool(
                    service_method, params, lead_info, context
                )
                tool_results[service_method] = result
                emoji_logger.system_success(
                    f"✅ Tool executado: {service_method}"
                )
            except Exception as e:
                tool_results[service_method] = {"error": str(e)}
                emoji_logger.system_error(
                    "Tool execution error",
                    error=f"❌ Erro no tool {service_method}: {e}"
                )

        return tool_results

    async def _execute_single_tool(
            self,
            service_method: str,
            params: dict,
            lead_info: dict,
            context: dict
    ):
        """Executa um tool específico"""
        parts = service_method.split('.')
        if len(parts) != 2:
            raise ValueError(f"Formato inválido: {service_method}")

        service_name, method_name = parts

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
                    # CRIA UM REGISTRO DE QUALIFICAÇÃO COM O ID DO EVENTO
                    event_id = result.get("google_event_id")
                    if event_id and lead_info.get("id"):
                        from app.integrations.supabase_client import supabase_client
                        qualification_data = {
                            "lead_id": lead_info["id"],
                            "qualification_status": "QUALIFIED",
                            "google_event_id": event_id,
                            "meeting_scheduled_at": result.get("start_time"),
                            "notes": "Reunião agendada pelo agente de IA."
                        }
                        await supabase_client.create_lead_qualification(qualification_data)
                        emoji_logger.system_info(f"Registro de qualificação criado para o evento: {event_id}")

                    await self._execute_post_scheduling_workflow(
                        result,
                        lead_info,
                        context
                    )
                return result
            elif method_name == "suggest_times":
                return await self.calendar_service.suggest_times(lead_info)
            elif method_name == "cancel_meeting":
                from app.integrations.supabase_client import supabase_client
                latest_qualification = await supabase_client.get_latest_qualification(lead_info["id"])
                meeting_id = params.get("meeting_id") or (latest_qualification and latest_qualification.get("google_event_id"))
                
                if not meeting_id:
                    raise ValueError(
                        "ID da reunião não encontrado para cancelamento."
                    )
                return await self.calendar_service.cancel_meeting(meeting_id)
            elif method_name == "reschedule_meeting":
                from app.integrations.supabase_client import supabase_client
                latest_qualification = await supabase_client.get_latest_qualification(lead_info["id"])
                meeting_id = params.get("meeting_id") or (latest_qualification and latest_qualification.get("google_event_id"))
                date = params.get("date")
                time = params.get("time")
                if not meeting_id:
                    raise ValueError(
                        "ID da reunião não encontrado para reagendamento."
                    )
                return await self.calendar_service.reschedule_meeting(
                    meeting_id=meeting_id,
                    date=date,
                    time=time,
                    lead_info=lead_info
                )

        elif service_name == "crm":
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
                    return await self.crm_service.update_lead(
                        lead_info.get("kommo_lead_id"),
                        {"custom_fields_values": [{"field_id": self.crm_service.custom_fields.get(field_name), "values": [{"value": field_value}]}]}
                    )

        elif service_name == "followup":
            if method_name == "schedule":
                hours = int(params.get("hours", 24))
                message = params.get(
                    "message",
                    "Oi! Tudo bem? Ainda tem interesse em energia solar?"
                )
                return await self.followup_service.schedule_followup(
                    phone_number=lead_info.get("phone_number"),
                    message=message,
                    delay_hours=hours,
                    lead_info=lead_info
                )

        elif service_name == "knowledge":
            if method_name == "search":
                query = params.get("query")
                if not query:
                    raise ValueError("O parâmetro 'query' é obrigatório para a busca na base de conhecimento.")
                return await self.knowledge_service.search_knowledge_base(query)

        raise ValueError(f"Tool não reconhecido: {service_method}")

    async def _generate_response(
        self,
        message: str,
        context: dict,
        lead_info: dict,
        conversation_history: list,
        execution_context: dict,
        is_followup: bool = False
    ) -> str:
        """Gera a resposta do agente usando o ModelManager."""
        
        # Carrega o prompt do sistema diretamente
        try:
            with open("app/prompts/prompt-agente.md", "r", encoding="utf-8") as f:
                system_prompt = f.read()
        except FileNotFoundError:
            system_prompt = "Você é um assistente de vendas."

        # Constrói o prompt do usuário com contexto, mas sem achatar o histórico
        user_prompt_context = (
            f"Data e Hora Atuais: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"=== Informações do Lead ===\n{lead_info}\n\n"
            f"=== Contexto da Conversa ===\n{context}\n\n"
        )

        if is_followup:
            user_prompt_context += f"=== Tarefa de Follow-up ===\n{message}\n"
        else:
            user_prompt_context += f"=== Instrução ===\nCom base em todo o histórico e contexto, gere a próxima resposta para o usuário.\n"

        # O histórico já contém a mensagem do usuário com a mídia.
        # Adicionamos o contexto como a ÚLTIMA mensagem do usuário para dar-lhe peso.
        # A API espera uma lista de dicionários.
        
        # Limpa o conteúdo de texto simples do histórico para evitar duplicação
        history_for_model = []
        for msg in conversation_history:
            if isinstance(msg['content'], list): # Mensagem multimodal
                history_for_model.append(msg)
            else: # Mensagem de texto
                # Mantém apenas a última mensagem de texto do usuário se for a mais recente
                if msg['role'] == 'user':
                    # A mensagem de texto já foi adicionada ao user_message_content
                    pass
                else:
                    history_for_model.append(msg)

        # A última mensagem do usuário já está formatada com a mídia.
        # Agora, vamos garantir que o contexto seja adicionado corretamente.
        # A melhor abordagem é injetar o contexto no final do prompt do sistema
        # ou como uma mensagem de sistema separada, mas vamos manter simples por enquanto.
        
        final_system_prompt = f"{system_prompt}\n\n{user_prompt_context}"

        response_text = await self.model_manager.get_response(
            messages=conversation_history, # Envia o histórico completo
            system_prompt=final_system_prompt
        )

        if response_text:
            tool_results = await self._parse_and_execute_tools(
                response_text, lead_info, context
            )
            if tool_results:
                # Adiciona os resultados das ferramentas ao histórico para a chamada final
                tool_results_str = "\n".join(
                    [f"Tool {tool}: {result}" for tool, result in tool_results.items()]
                )
                
                final_instruction = (
                    f"=== Resposta do Modelo e Uso de Ferramentas ===\n"
                    f"Resposta do modelo: {response_text}\n"
                    f"Resultados das ferramentas: {tool_results_str}\n\n"
                    f"=== Instrução Final ===\n"
                    f"Com base nos resultados das ferramentas, gere a resposta final para o usuário."
                )
                
                conversation_history.append({"role": "assistant", "content": response_text})
                conversation_history.append({"role": "user", "content": final_instruction})

                response_text = await self.model_manager.get_response(
                    messages=conversation_history,
                    system_prompt=final_system_prompt
                )
        
        return response_text or "Não consegui gerar uma resposta no momento."

    def _detect_lead_changes(self, old_info: dict, new_info: dict) -> dict:
        """Detecta mudanças nas informações do lead."""
        changes = {}
        for key, value in new_info.items():
            if value and value != old_info.get(key):
                changes[key] = value
        return changes

    async def _sync_lead_changes(self, changes: dict, phone: str, lead_info: dict):
        """Sincroniza as mudanças do lead com o CRM."""
        if not self.crm_service.is_initialized:
            await self.crm_service.initialize()
            
        kommo_lead_id = lead_info.get("kommo_lead_id")
        if not kommo_lead_id:
            # Se não houver ID do Kommo, talvez criar um novo lead aqui
            return

        update_data = {}
        for key, value in changes.items():
            if key == "name":
                update_data["name"] = value
            elif key == "bill_value":
                update_data["bill_value"] = value
            elif key == "chosen_flow":
                update_data["chosen_flow"] = value
        
        if update_data:
            await self.crm_service.update_lead(kommo_lead_id, update_data)
