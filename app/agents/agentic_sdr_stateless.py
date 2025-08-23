"""
AgenticSDR Stateless - Arquitetura ZERO complexidade para produção
Cada requisição é completamente isolada e independente
Não há estado compartilhado entre conversas
"""

from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import pytz
import re

from app.integrations.supabase_client import supabase_client
from app.core.model_manager import ModelManager
from app.core.multimodal_processor import MultimodalProcessor
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
from app.services.conversation_monitor import get_conversation_monitor
from app.utils.logger import emoji_logger
from app.core.response_formatter import response_formatter
from app.utils.time_utils import get_period_of_day
from app.config import settings

# Importar serviços diretamente
from app.services.calendar_service_100_real import CalendarServiceReal
from app.services.crm_service_100_real import CRMServiceReal
from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.knowledge_service import KnowledgeService
from app.services.crm_sync_service import crm_sync_service


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
            import traceback
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
        Processa mensagem com contexto isolado, orquestrando o fluxo de trabalho.
        """
        if not self.is_initialized:
            await self.initialize()

        emoji_logger.agentic_start(f"Processando (stateless): {message[:100]}...")

        try:
            # Etapa 1: Preparar o contexto da execução
            conversation_history = execution_context.get("conversation_history", [])
            lead_info = execution_context.get("lead_info", {})
            phone = execution_context.get("phone")

            await self.conversation_monitor.register_message(phone=phone, is_from_user=True, lead_info=lead_info)

            # Etapa 2: Atualizar histórico e contexto do lead
            conversation_history, lead_info = await self._update_context(message, conversation_history, lead_info, execution_context.get("media"))

            # Etapa 3: Sincronizar com serviços externos (CRM)
            lead_info = await self._sync_external_services(lead_info)

            # Etapa 3.5: Sincronizar dados de tags e campos com o CRM
            await self._sync_crm_data(lead_info, conversation_history)

            # Etapa 4: Determinar a estratégia de resposta (Bypass ou LLM)
            user_intent = self.context_analyzer._extract_intent(message)
            if user_intent in ["reagendamento", "cancelamento", "agendamento"]:
                response = await self._handle_intent_bypass(user_intent, message, lead_info)
            else:
                response = await self._generate_llm_response(message, lead_info, conversation_history, execution_context)

            # Etapa 5: Finalizar e registrar a resposta
            await self.conversation_monitor.register_message(phone=phone, is_from_user=False, lead_info=lead_info)
            emoji_logger.system_success(f"Resposta gerada: {response[:100]}...")
            return response_formatter.ensure_response_tags(response), lead_info

        except Exception as e:
            import traceback
            emoji_logger.system_error(
                "AgenticSDRStateless",
                error=f"Erro: {e}",
                traceback=traceback.format_exc()
            )
            return (
                "<RESPOSTA_FINAL>Desculpe, tive um problema aqui. "
                "Pode repetir?</RESPOSTA_FINAL>",
                execution_context.get("lead_info", {})
            )

    async def _update_context(self, message: str, conversation_history: list, lead_info: dict, media_data: dict) -> tuple[list, dict]:
        """Prepara a mensagem do usuário, atualiza o histórico e enriquece as informações do lead."""
        # 1. PROCESSAR MÍDIA (SE EXISTIR)
        user_message_content = [{"type": "text", "text": message}]
        if media_data:
            if media_data.get("type") == "error":
                raise ValueError(media_data.get("content", "Erro ao processar mídia."))

            media_content = media_data.get("content") or media_data.get("data", "")
            mime_type = media_data.get("mimetype", "application/octet-stream")
            if "base64," in media_content:
                media_content = media_content.split("base64,")[1]
            user_message_content.append({
                "type": "media",
                "media_data": {"mime_type": mime_type, "content": media_content}
            })
            emoji_logger.multimodal_event(f"📎 Mídia do tipo {mime_type} adicionada.")

            media_result = await self.multimodal.process_media(media_data)
            if media_result.get("success"):
                extracted_bill_value = media_result.get("analysis", {}).get("bill_value")
                if extracted_bill_value:
                    lead_info['bill_value'] = extracted_bill_value
                    emoji_logger.system_info(f"Valor da conta R${extracted_bill_value} extraído e injetado no lead_info.")
            else:
                emoji_logger.system_warning(f"Falha na extração de texto da mídia: {media_result.get('message')}")

        # 2. ATUALIZAR HISTÓRICO
        user_message = {"role": "user", "content": user_message_content, "timestamp": datetime.now().isoformat()}
        conversation_history.append(user_message)

        # 3. EXECUTAR ANÁLISES DE LEAD
        new_lead_info = self.lead_manager.extract_lead_info(conversation_history, existing_lead_info=lead_info)
        lead_changes = self._detect_lead_changes(lead_info, new_lead_info)
        if lead_changes:
            from app.integrations.supabase_client import supabase_client
            lead_id_to_update = lead_info.get("id")
            if lead_id_to_update:
                await supabase_client.update_lead(lead_id_to_update, lead_changes)
                emoji_logger.system_info("Estado do lead sincronizado com o banco de dados.", changes=lead_changes)
        lead_info.update(new_lead_info)

        return conversation_history, lead_info

    async def _sync_external_services(self, lead_info: dict) -> dict:
        """Sincroniza informações do lead com serviços externos como o CRM."""
        if lead_info.get("name") and not lead_info.get("kommo_lead_id"):
            try:
                from app.integrations.supabase_client import supabase_client
                kommo_response = await self.crm_service.create_lead(lead_info)
                if kommo_response.get("success"):
                    new_kommo_id = kommo_response.get("lead_id")
                    lead_info["kommo_lead_id"] = new_kommo_id
                    await supabase_client.update_lead(lead_info["id"], {"kommo_lead_id": new_kommo_id})
                    emoji_logger.team_crm(f"Lead criado no Kommo com ID: {new_kommo_id}")
            except Exception as e:
                emoji_logger.system_error("Falha ao criar lead no Kommo", error=str(e))
        return lead_info

    async def _sync_crm_data(self, lead_info: dict, conversation_history: list):
        """Gera e envia atualizações de campos e tags para o CRM."""
        if not lead_info.get("kommo_lead_id"):
            emoji_logger.system_debug("CRM Sync: Pulando, lead sem kommo_lead_id.")
            return

        update_payload = crm_sync_service.get_update_payload(
            lead_info=lead_info,
            conversation_history=conversation_history
        )

        if update_payload:
            try:
                await self.crm_service.update_lead(
                    lead_id=str(lead_info["kommo_lead_id"]),
                    update_data=update_payload
                )
                emoji_logger.system_info("CRM Sync: Dados do lead atualizados no Kommo.", payload=update_payload)
            except Exception as e:
                emoji_logger.system_error("CRM Sync: Falha ao atualizar dados no Kommo.", error=str(e))

    async def _handle_intent_bypass(self, user_intent: str, message: str, lead_info: dict) -> str:
        """Lida com intenções que podem ser resolvidas sem o fluxo principal do LLM."""
        emoji_logger.system_info(f"Intenção '{user_intent}' detectada. Usando fluxo de bypass.")
        tool_name, tool_params = "", {}
        if user_intent == "reagendamento":
            tool_name = "calendar.reschedule_meeting"
        elif user_intent == "cancelamento":
            tool_name = "calendar.cancel_meeting"
        elif user_intent == "agendamento":
            tool_name = "calendar.check_availability"
            date, _ = self._extract_schedule_details(message)
            if date:
                tool_params['date_request'] = date

        params_str = " | ".join([f"{k}={v}" for k, v in tool_params.items()])
        tool_call_string = f"[TOOL: {tool_name}{' | ' + params_str if params_str else ''}]"
        
        context = {"message": message}
        tool_results = await self._parse_and_execute_tools(tool_call_string, lead_info, context)

        if not tool_results:
            return "Não consegui processar sua solicitação no momento. Pode tentar novamente?"

        result = next(iter(tool_results.values()), {})
        if result.get("success"):
            if "available_slots" in result:
                slots = result['available_slots']
                date_str = datetime.strptime(result['date'], '%Y-%m-%d').strftime('%d/%m/%Y')
                return f"Perfeito! Para o dia {date_str}, tenho os seguintes horários disponíveis: {', '.join(slots)}. Qual prefere?" if slots else f"Poxa, não tenho horários disponíveis para o dia {date_str}. Podemos tentar outro dia?"
            return result.get("message", "Sua solicitação foi processada com sucesso.")
        else:
            return f"Desculpe, tive um problema ao processar sua solicitação: {result.get('message', 'erro desconhecido')}. Podemos tentar de outra forma?"

    async def _generate_llm_response(self, message: str, lead_info: dict, conversation_history: list, execution_context: dict) -> str:
        """Executa o fluxo normal de geração de resposta com o LLM."""
        context = {}  # Contexto pode ser enriquecido aqui se necessário
        return await self._generate_response(
            message=message,
            context=context,
            lead_info=lead_info,
            conversation_history=conversation_history,
            execution_context=execution_context
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

        emoji_logger.system_success(
            "✅ Workflow pós-agendamento executado com as devidas "
            "tratativas de erro."
        )

        # Agendar lembretes de reunião
        meeting_date_time = datetime.fromisoformat(schedule_result["start_time"])
        lead_email = lead_info.get("email")
        lead_name = lead_info.get("name", "")
        meet_link = schedule_result.get("meet_link", "")

        # Lembrete de 24 horas
        message_24h = (
            f"Oi {lead_name}! Tudo bem? Passando para confirmar sua reunião de amanhã às "
            f"{meeting_date_time.strftime('%H:%M')} com o Leonardo. Aqui está o link da reunião: "
            f"{meet_link} Está tudo certo para você?"
        )
        await self.followup_service.schedule_followup(
            phone_number=lead_info["phone_number"],
            message=message_24h,
            delay_hours=24,
            lead_info=lead_info
        )
        emoji_logger.followup_event(f"Lembrete de 24h agendado para {lead_name}.")

        # Lembrete de 2 horas
        message_2h = (
            f"{lead_name}, Sua reunião com o Leonardo é daqui a 2 horas! Te esperamos às "
            f"{meeting_date_time.strftime('%H:%M')}! Link: {meet_link}"
        )
        await self.followup_service.schedule_followup(
            phone_number=lead_info["phone_number"],
            message=message_2h,
            delay_hours=2,
            lead_info=lead_info
        )
        emoji_logger.followup_event(f"Lembrete de 2h agendado para {lead_name}.")

    async def _parse_and_execute_tools(
            self,
            response: str,
            lead_info: dict,
            context: dict
    ) -> dict:
        """
        Parse e executa tool calls na resposta do agente.
        """
        emoji_logger.system_debug(f"Raw LLM response before tool parsing: {response}")
        tool_pattern = r'\[TOOL:\s*([^|\]]+?)\s*(?:\|\s*([^\]]*))?\]'
        tool_matches = []
        try:
            tool_matches = re.findall(tool_pattern, response)
        except re.error as e:
            emoji_logger.system_error(
                "Tool parsing error",
                error=f"Erro de regex ao parsear tools: {e}. Resposta: {response[:200]}..."
            )
            return {} # Retorna vazio se a regex falhar

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
                date_req = params.get("date_request", "")
                return await self.calendar_service.check_availability(
                    date_req
                )
            elif method_name == "schedule_meeting":
                result = await self.calendar_service.schedule_meeting(
                    date=params.get("date"),
                    time=params.get("time"),
                    lead_info={
                        **lead_info,
                        "email": params.get("email", lead_info.get("email")),
                    }
                )
                if result and result.get("success"):
                    # CRIA UM REGISTRO DE QUALIFICAÇÃO COM O ID DO EVENTO
                    event_id = result.get("google_event_id")
                    if event_id and lead_info.get("id"):
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
                latest_qualification = await supabase_client.get_latest_qualification(lead_info["id"])
                meeting_id = params.get("meeting_id") or (latest_qualification and latest_qualification.get("google_event_id"))
                
                if not meeting_id:
                    raise ValueError(
                        "ID da reunião não encontrado para cancelamento."
                    )
                return await self.calendar_service.cancel_meeting(meeting_id)
            elif method_name == "reschedule_meeting":
                # Lógica robusta: Ignora o meeting_id do LLM e busca sempre do Supabase.
                latest_qualification = await supabase_client.get_latest_qualification(lead_info.get("id"))
                meeting_id = latest_qualification.get("google_event_id") if latest_qualification else None
                
                if not meeting_id:
                    raise ValueError("Não foi encontrada uma reunião ativa para reagendar.")

                # Extrai a nova data/hora da mensagem do usuário se não estiver nos parâmetros
                # Lógica de reagendamento mais inteligente e contextual
                user_message = context.get("message", "")
                new_date, new_time = self._extract_schedule_details(user_message)

                # Se o usuário não especificar uma nova data, reutiliza a data da reunião original
                if not new_date:
                    original_start_str = latest_qualification.get("meeting_scheduled_at")
                    if original_start_str:
                        original_datetime = datetime.fromisoformat(original_start_str)
                        new_date = original_datetime.strftime('%Y-%m-%d')
                
                # Se mesmo assim não tivermos data ou hora, a extração falhou
                if not new_date or not new_time:
                    return {
                        "success": False,
                        "message": "Não consegui entender a nova data e hora. Poderia informar o dia e o horário desejado, por favor?"
                    }

                return await self.calendar_service.reschedule_meeting(
                    meeting_id=meeting_id,
                    date=new_date,
                    time=new_time,
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
        """Gera a resposta do agente usando o ModelManager com injeção de contexto robusta."""
        import json

        # 1. Carrega o prompt do sistema (persona) e injeta o contexto de data/hora.
        system_prompt = "Você é um assistente de vendas." # Fallback inicial
        try:
            with open("app/prompts/prompt-agente.md", "r", encoding="utf-8") as f:
                system_prompt = f.read()
        except FileNotFoundError:
            emoji_logger.system_warning("Arquivo de prompt principal não encontrado. Usando fallback.")

        # Injeção de Contexto Temporal
        tz = pytz.timezone(settings.timezone)
        now = datetime.now(tz)
        current_date_str = now.strftime('%Y-%m-%d %H:%M')
        days_map = {0: "Segunda-feira", 1: "Terça-feira", 2: "Quarta-feira", 3: "Quinta-feira", 4: "Sexta-feira", 5: "Sábado", 6: "Domingo"}
        day_of_week_pt = days_map[now.weekday()]
        
        date_context = f"<contexto_temporal>\nA data e hora atuais são: {current_date_str} ({day_of_week_pt}).\n</contexto_temporal>\n\n"
        system_prompt_with_context = date_context + system_prompt

        # 2. Prepara as mensagens para o modelo.
        if is_followup:
            # Para follow-ups, a 'message' é um prompt completo e contextual.
            messages_for_model = [{"role": "user", "content": message}]
        else:
            messages_for_model = list(conversation_history)

        # Limita o histórico para as últimas 200 mensagens para evitar sobrecarga de contexto
        if len(messages_for_model) > 200:
            emoji_logger.system_warning(
                "Histórico longo detectado, truncando para as últimas 200 mensagens.",
                original_size=len(messages_for_model)
            )
            messages_for_model = messages_for_model[-30:]

        # VERIFICAÇÃO CRÍTICA: Garantir que não estamos enviando conteúdo vazio.
        if not messages_for_model or not any(msg.get("content") for msg in messages_for_model):
            emoji_logger.model_error(
                "Tentativa de chamar o modelo com conteúdo vazio.",
                history_len=len(conversation_history),
                is_followup=is_followup
            )
            return "<RESPOSTA_FINAL>Não consegui processar sua solicitação no momento.</RESPOSTA_FINAL>"

        # 3. Primeira chamada ao modelo para obter a resposta inicial (que pode conter tools).
        response_text = await self.model_manager.get_response(
            messages=messages_for_model,
            system_prompt=system_prompt_with_context
        )

        if response_text:
            # 5. Analisa e executa ferramentas, se houver.
            tool_results = await self._parse_and_execute_tools(
                response_text, lead_info, context
            )
            if tool_results:
                # 6. Se ferramentas foram usadas, faz uma segunda chamada ao modelo com os resultados.
                tool_results_str = "\n".join(
                    [f"- {tool}: {result}" for tool, result in tool_results.items()]
                )

                final_instruction = (
                    f"""=== RESULTADO DAS FERRAMENTAS ===
Sua resposta inicial foi: 
'{response_text}'
As seguintes ferramentas foram executadas com estes resultados:
{tool_results_str}

=== INSTRUÇÃO FINAL ===
Com base nos resultados das ferramentas, gere a resposta final, clara e amigável para o usuário. Siga TODAS as regras do seu prompt de sistema. Não inclua mais chamadas de ferramentas. Apenas a resposta final."""
                )

                # Adiciona a resposta do assistente (com tools) e a instrução final ao histórico
                messages_for_final_response = list(messages_for_model)
                messages_for_final_response.append({"role": "assistant", "content": response_text})
                messages_for_final_response.append({"role": "user", "content": final_instruction})

                response_text = await self.model_manager.get_response(
                    messages=messages_for_final_response,
                    system_prompt=system_prompt_with_context # Reutiliza o mesmo system_prompt com contexto
                )

        return response_text or "Não consegui gerar uma resposta no momento."

    def _detect_lead_changes(self, old_info: dict, new_info: dict) -> dict:
        """Detecta mudanças nas informações do lead."""
        changes = {}
        for key, value in new_info.items():
            if value and value != old_info.get(key):
                changes[key] = value
        return changes

    def _extract_schedule_details(self, message: str) -> (Optional[str], Optional[str]):
        """Extrai data e hora de uma mensagem usando dateparser."""
        import dateparser
        from app.config import settings
        import pytz

        # Configurações para o dateparser entender português e o contexto futuro
        parser_settings = {
            'PREFER_DATES_FROM': 'future',
            'TIMEZONE': settings.timezone,
            'RETURN_AS_TIMEZONE_AWARE': True
        }
        
        # A biblioteca dateparser parseia a string inteira para encontrar a data/hora
        parsed_datetime = dateparser.parse(message, languages=['pt'], settings=parser_settings)

        if parsed_datetime:
            # Garante que o objeto datetime tenha timezone antes de formatar
            tz = pytz.timezone(settings.timezone)
            if parsed_datetime.tzinfo is None:
                parsed_datetime = tz.localize(parsed_datetime)
            
            date_str = parsed_datetime.strftime('%Y-%m-%d')
            time_str = parsed_datetime.strftime('%H:%M')
            return date_str, time_str
        
        return None, None

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
