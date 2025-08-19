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
        # Removido TeamCoordinator
        self.conversation_monitor = get_conversation_monitor()
        
        # SEM ESTADO INTERNO!
        # Cada requisição traz seu próprio contexto
        self.is_initialized = False
        
    async def initialize(self):
        """Inicialização dos módulos assíncronos"""
        if self.is_initialized:
            return
        
        emoji_logger.system_event("🚀 Inicializando AgenticSDR Stateless...")
        
        try:
            # Inicializar módulos
            self.model_manager.initialize()
            self.multimodal.initialize()
            self.lead_manager.initialize()
            self.context_analyzer.initialize()
            # TeamCoordinator removido - não precisa inicializar
            await self.conversation_monitor.initialize()
            
            self.is_initialized = True
            emoji_logger.system_ready(
                "✅ AgenticSDR Stateless inicializado!",
                modules=[
                    "ModelManager", "MultimodalProcessor", 
                    "LeadManager", "ContextAnalyzer"
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
            
            # 6. Executar serviços necessários diretamente (sem TeamCoordinator)
            service_results = await self._execute_services_directly(
                message,
                context,
                lead_info
            )
            
            # 7. Gerar resposta com contexto completo
            response = await self._generate_response(
                message,
                context,
                lead_info,
                service_results,
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
    
    async def _execute_services_directly(self,
                                       message: str,
                                       context: Dict[str, Any],
                                       lead_info: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Executa serviços necessários diretamente sem TeamCoordinator
        Esta é a nova abordagem mais simples e direta
        """
        results = []
        
        # Analisar necessidade de serviços com lógica similar ao TeamCoordinator
        service_needs = self._analyze_service_needs(message, context)
        
        # Executar serviços necessários
        for service_name, need_score in service_needs.items():
            # Threshold otimizado (similar ao TeamCoordinator)
            if need_score >= 0.4:
                emoji_logger.service_event(
                    f"🎯 Executando {service_name} diretamente",
                    score=f"{need_score:.3f}",
                    threshold="0.4"
                )
                
                result = await self._execute_single_service_directly(
                    service_name,
                    message,
                    context,
                    lead_info
                )
                
                if result:
                    results.append(result)
        
        return results
    
    def _analyze_service_needs(self, message: str, context: Dict[str, Any]) -> Dict[str, float]:
        """
        Analisa necessidade de serviços com INTENÇÃO INTELIGENTE
        Baseado na lógica do TeamCoordinator mas simplificada
        """
        scores = {
            "calendar": 0.0,
            "crm": 0.0,
            "followup": 0.0
        }
        
        message_lower = message.lower()
        
        # 🎯 CALENDAR - Análise de Intenção Aprimorada
        calendar_score = self._analyze_calendar_intent(message_lower, context)
        scores["calendar"] = calendar_score
        
        # 📊 CRM - Análise de Intenção para Dados
        crm_score = self._analyze_crm_intent(message_lower, context)
        scores["crm"] = crm_score
        
        # 🔄 FOLLOWUP - Análise de Intenção para Reengajamento
        followup_score = self._analyze_followup_intent(message_lower, context)
        scores["followup"] = followup_score
        
        # 🚀 BOOST INTELIGENTE baseado em user_intent e conversation_stage
        scores = self._apply_intelligent_boost(scores, context)
        
        # Normalizar scores
        for service in scores:
            scores[service] = min(1.0, scores[service])
        
        return scores
    
    def _analyze_calendar_intent(self, message_lower: str, context: Dict[str, Any]) -> float:
        """
        🎯 Análise INTELIGENTE de intenção para Calendar Service
        Simplificada do TeamCoordinator
        """
        calendar_score = 0.0
        
        # 1. PALAVRAS-CHAVE BÁSICAS (peso 0.2)
        basic_keywords = [
            "agendar", "marcar", "reunião", "conversar", "leonardo",
            "horário", "disponível", "data", "quando", "encontro",
            "pode ser", "poderia ser", "da pra ser", "dá pra ser"
        ]
        keyword_matches = sum(1 for kw in basic_keywords if kw in message_lower)
        calendar_score += min(0.4, keyword_matches * 0.2)  # Max 0.4 de keywords
        
        # 2. INTENÇÕES FORTES (peso 0.4)
        strong_intent_phrases = [
            "quero agendar", "vamos marcar", "podemos conversar",
            "falar com leonardo", "marcar reunião", "que horário",
            "estou disponível", "quando posso", "vamos falar"
        ]
        for phrase in strong_intent_phrases:
            if phrase in message_lower:
                calendar_score += 0.4
                break
        
        # 3. INDICADORES DE URGÊNCIA E TEMPO (peso 0.4)
        urgency_indicators = [
            "hoje", "amanhã", "logo", "rápido", "urgente",
            "já", "agora", "preciso", "importante"
        ]
        # Indicadores específicos de flexibilidade temporal
        time_flexibility_indicators = [
            "amanhã pode", "pode ser amanhã", "amanhã da", "amanhã dá"
        ]
        
        urgency_match = any(indicator in message_lower for indicator in urgency_indicators)
        flexibility_match = any(indicator in message_lower for indicator in time_flexibility_indicators)
        
        if flexibility_match:
            calendar_score += 0.5  # Peso maior para flexibilidade temporal específica
        elif urgency_match:
            calendar_score += 0.4  # Peso aumentado para urgência geral
        
        # 4. INDICADORES DE TEMPO ESPECÍFICO (peso 0.5)
        time_patterns = [
            r"\d{1,2}h\d{0,2}", r"\d{1,2}:\d{2}", r"\d{1,2}/\d{1,2}",
            "segunda", "terça", "quarta", 
            "quinta", "sexta", "sábado", "domingo"
        ]
        # Padrões de hora simplificados
        simple_time_patterns = [
            r"\d{1,2}h", r"as \d{1,2}", r"às \d{1,2}", 
            r"pode ser \d{1,2}", r"pode ser as \d{1,2}"
        ]
        
        import re
        time_detected = False
        
        # Verificar padrões de tempo específicos
        for pattern in time_patterns:
            if re.search(pattern, message_lower):
                calendar_score += 0.5
                time_detected = True
                break
        
        # Verificar padrões de hora simplificados
        if not time_detected:
            for pattern in simple_time_patterns:
                if re.search(pattern, message_lower):
                    calendar_score += 0.6  # Peso maior para padrões contextuais
                    break
        
        # 🚀 BOOST PROATIVO PARA CLOSING/AGENDAMENTO
        conversation_stage = context.get("conversation_stage", "").lower()
        qualification_score = context.get("qualification_score", 0)
        
        # Boost quando estágio indica necessidade de agendamento
        if conversation_stage in ["closing", "agendamento_processo", "qualificação_completa"]:
            calendar_score += 0.3
        
        # Boost quando score de qualificação é alto (≥7)
        if qualification_score >= 7:
            calendar_score += 0.3
        
        # 🚀 BOOST POR INTERESSE DEMONSTRADO
        interest_indicators = [
            "interessante", "interessado", "faz sentido", "legal", "ótimo",
            "perfeito", "quero", "preciso", "vou", "aceito"
        ]
        
        # 🚀 BOOST POR CONTEXTO DE AGENDAMENTO CONVERSACIONAL
        contextual_scheduling_phrases = [
            "pode ser", "da pra", "dá pra", "consigo", "posso", 
            "tudo bem", "ok", "sim", "claro", "perfeito"
        ]
        
        if any(indicator in message_lower for indicator in interest_indicators):
            calendar_score += 0.2
        
        # Boost adicional para frases contextuais de agendamento
        if any(phrase in message_lower for phrase in contextual_scheduling_phrases):
            # Verificar se há indicador temporal na mesma mensagem
            has_time_context = any(time_word in message_lower for time_word in 
                                 ["amanhã", "hoje", "depois", "manhã", "tarde", "noite"] + 
                                 [str(i)+"h" for i in range(6, 24)])
            
            if has_time_context:
                calendar_score += 0.3  # Boost significativo para contexto temporal + flexibilidade
        
        return min(1.0, calendar_score)
    
    def _analyze_crm_intent(self, message_lower: str, context: Dict[str, Any]) -> float:
        """
        📊 Análise INTELIGENTE de intenção para CRM Service
        """
        crm_score = 0.0
        
        # Palavras-chave de dados pessoais/empresa
        data_keywords = [
            "nome", "telefone", "email", "empresa", "conta",
            "valor", "consumo", "kwh", "endereço", "cpf", "cnpj"
        ]
        keyword_matches = sum(1 for kw in data_keywords if kw in message_lower)
        crm_score += min(0.6, keyword_matches * 0.25)
        
        # Intenções de fornecer dados
        data_providing_phrases = [
            "meu nome é", "me chamo", "minha empresa", "nossa conta",
            "pagamos", "gastamos", "consumimos", "nosso endereço"
        ]
        for phrase in data_providing_phrases:
            if phrase in message_lower:
                crm_score += 0.4
                break
        
        return min(1.0, crm_score)
    
    def _analyze_followup_intent(self, message_lower: str, context: Dict[str, Any]) -> float:
        """
        🔄 Análise INTELIGENTE de intenção para FollowUp Service
        """
        followup_score = 0.0
        
        # Palavras-chave de adiamento/reengajamento
        followup_keywords = [
            "lembrar", "retornar", "voltar", "depois", "pensar",
            "aguardar", "futuro", "próxima", "acompanhar", "ligar"
        ]
        keyword_matches = sum(1 for kw in followup_keywords if kw in message_lower)
        followup_score += min(0.4, keyword_matches * 0.2)
        
        # Intenções de adiamento
        postpone_phrases = [
            "vou pensar", "preciso conversar", "não posso agora",
            "talvez depois", "outra hora", "me ligue", "entre em contato"
        ]
        for phrase in postpone_phrases:
            if phrase in message_lower:
                followup_score += 0.6
                break
        
        return min(1.0, followup_score)
    
    def _apply_intelligent_boost(self, scores: Dict[str, float], context: Dict[str, Any]) -> Dict[str, float]:
        """
        🚀 Aplica boost inteligente baseado em user_intent e conversation_stage
        """
        # BOOST baseado em user_intent (do contexto analisado)
        user_intent = context.get("user_intent", "").lower()
        
        if "agendar" in user_intent or "reunião" in user_intent:
            scores["calendar"] += 0.4
        elif "dados" in user_intent or "informações" in user_intent:
            scores["crm"] += 0.4
        elif "depois" in user_intent or "adiado" in user_intent:
            scores["followup"] += 0.4
        
        # BOOST baseado em conversation_stage
        stage = context.get("conversation_stage", "").lower()
        
        if stage in ["qualificação", "negociação", "fechamento"]:
            scores["calendar"] += 0.3  # Estágios avançados = agendar reunião
        elif stage in ["início", "descoberta"]:
            scores["crm"] += 0.3  # Início = coletar dados
        
        # BOOST baseado em action_needed (compatibilidade)
        action_needed = context.get("action_needed", "")
        if action_needed == "agendar":
            scores["calendar"] += 0.4
        elif action_needed == "qualificar":
            scores["crm"] += 0.4
        elif action_needed == "reengajar":
            scores["followup"] += 0.4
        
        return scores
    
    async def _execute_single_service_directly(self,
                                             service_name: str,
                                             message: str,
                                             context: Dict[str, Any],
                                             lead_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Executa um serviço específico diretamente sem TeamCoordinator
        Esta é a nova abordagem mais simples e direta
        """
        try:
            if service_name == "calendar":
                # Instanciar CalendarService diretamente
                calendar_service = CalendarServiceReal()
                await calendar_service.initialize()
                
                # Verificar disponibilidade ou agendar
                if "disponível" in message.lower() or "horário" in message.lower():
                    result = await calendar_service.check_availability(message)
                else:
                    # Extrair data/hora da mensagem com contexto
                    conversation_history = context.get("conversation_history", [])
                    date_time = self._extract_datetime(message, conversation_history)
                    if date_time:
                        result = await calendar_service.schedule_meeting(
                            date_time["date"],
                            date_time["time"],
                            lead_info
                        )
                        
                        # Workflow completo pós-agendamento
                        if result and result.get("success"):
                            await self._execute_post_scheduling_workflow(
                                result,
                                lead_info,
                                context
                            )
                    else:
                        result = await calendar_service.suggest_times(lead_info)
                
            elif service_name == "crm":
                # Instanciar CRMService diretamente
                crm_service = CRMServiceReal()
                await crm_service.initialize()
                
                # Atualizar lead no CRM
                result = await crm_service.create_or_update_lead(lead_info)
                
                # Capturar o lead_id retornado e adicionar ao lead_info
                if result.get("success") and result.get("lead_id"):
                    lead_id = result["lead_id"]
                    lead_info["id"] = lead_id  # Armazenar para uso futuro
                    
                    # Atualizar estágio se necessário
                    if lead_info.get("stage"):
                        await crm_service.update_lead_stage(
                            lead_id,  # Usar o lead_id correto
                            lead_info["stage"]
                        )
                    
                    # Sincronização automática com Kommo
                    try:
                        emoji_logger.service_event("🔄 Sincronizando campos dinâmicos e tags")
                        sync_result = await self._sync_lead_to_crm(lead_info)
                        if sync_result.get("success"):
                            emoji_logger.system_success("✅ Tags e campos personalizados sincronizados")
                    except Exception as sync_error:
                        emoji_logger.service_warning(f"Sync opcional falhou: {sync_error}")
                
            elif service_name == "followup":
                # Instanciar FollowUpService diretamente
                followup_service = FollowUpServiceReal()
                
                # Agendar follow-up
                phone = lead_info.get("phone", "")
                name = lead_info.get("name", "Cliente")
                bill_value = lead_info.get("bill_value", 0)
                
                # Validação: Verificar se phone_number é válido
                if not phone or phone.strip() == "":
                    emoji_logger.service_warning("Phone number vazio - follow-up não agendado")
                    result = {
                        "success": False,
                        "error": "Phone number is required for follow-up"
                    }
                    return None
                
                # Gerar mensagem personalizada para follow-up
                message = f"Oi {name}! Helen da SolarPrime aqui. "
                message += f"Vou entrar em contato com você em breve para continuarmos nossa conversa sobre energia solar. "
                if bill_value > 0:
                    message += f"Já preparei uma análise especial para sua conta de R$ {bill_value}. "
                message += "Até logo! ☀️"
                
                # Calcular delay em horas baseado no contexto
                urgency = context.get("urgency_level", "normal")
                if urgency == "alta":
                    delay_hours = 24
                elif urgency == "média":
                    delay_hours = 72
                else:
                    delay_hours = 168  # 7 dias
                
                # Chamar com argumentos corretos
                result = await followup_service.schedule_followup(
                    phone_number=phone,
                    message=message,
                    delay_hours=delay_hours,
                    lead_info=lead_info
                )
            
            else:
                result = None
            
            if result and result.get("success"):
                emoji_logger.service_event(
                    f"✅ {service_name} executado com sucesso",
                    result=result.get("message", "")
                )
                return {
                    "service": service_name,
                    "success": True,
                    "data": result
                }
            
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao executar {service_name}: {e}"
            )
        
        return None
    
    async def _parse_and_execute_tools(self, response: str, lead_info: dict, context: dict) -> dict:
        """
        Parse e executa tool calls na resposta do agente
        Formato: [TOOL: service.method | param=value | param2=value2]
        """
        
        tool_pattern = r'\[TOOL:\s*([^|]+?)(?:\s*\|\s*([^\]]+))?\]'
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
            # Instanciar CalendarService diretamente
            calendar_service = CalendarServiceReal()
            await calendar_service.initialize()
            
            if method_name == "check_availability":
                return await calendar_service.check_availability(
                    context.get("message", "")
                )
            elif method_name == "schedule_meeting":
                return await calendar_service.schedule_meeting(
                    date=params.get("date"),
                    time=params.get("time"),
                    lead_info={
                        **lead_info,
                        "email": params.get("email", lead_info.get("email"))
                    }
                )
            elif method_name == "suggest_times":
                return await calendar_service.suggest_times(lead_info)
            elif method_name == "cancel_meeting":
                meeting_id = params.get("meeting_id")
                if not meeting_id:
                    raise ValueError("meeting_id é obrigatório para cancelar reunião")
                return await calendar_service.cancel_meeting(meeting_id)
            elif method_name == "reschedule_meeting":
                meeting_id = params.get("meeting_id")
                date = params.get("date")
                time = params.get("time")
                if not meeting_id:
                    raise ValueError("meeting_id é obrigatório para reagendar reunião")
                return await calendar_service.reschedule_meeting(
                    meeting_id=meeting_id,
                    date=date,
                    time=time,
                    lead_info=lead_info
                )
        
        # CRM tools
        elif service_name == "crm":
            # Instanciar CRMService diretamente
            crm_service = CRMServiceReal()
            await crm_service.initialize()
            
            if method_name == "update_stage":
                stage = params.get("stage", "").lower()
                return await crm_service.update_lead_stage(
                    lead_info.get("kommo_lead_id"),
                    stage
                )
            elif method_name == "update_field":
                field_name = params.get("field")
                field_value = params.get("value")
                if field_name and field_value:
                    return await crm_service.update_fields(
                        lead_info.get("kommo_lead_id"),
                        {field_name: field_value}
                    )
        
        # Follow-up tools
        elif service_name == "followup":
            # Instanciar FollowUpService diretamente
            followup_service = FollowUpServiceReal()
            
            if method_name == "schedule":
                hours = int(params.get("hours", 24))
                message = params.get("message", "Oi! Tudo bem? Ainda tem interesse em energia solar?")
                return await followup_service.schedule_followup(
                    phone_number=lead_info.get("phone"),
                    message=message,
                    delay_hours=hours,
                    lead_info=lead_info
                )
        
        raise ValueError(f"Tool não reconhecido: {service_method}")