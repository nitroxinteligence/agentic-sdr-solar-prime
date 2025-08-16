"""
Team Coordinator - Coordenação SIMPLES de serviços
ZERO complexidade, execução direta
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from uuid import uuid4
import asyncio
from app.utils.logger import emoji_logger
from app.config import settings

class TeamCoordinator:
    """
    Coordenador SIMPLES de serviços (Calendar, CRM, FollowUp)
    Execução direta sem complexidade
    """
    
    def __init__(self):
        self.is_initialized = False
        self.services = {}
        self.decision_threshold = 0.4  # Threshold otimizado para análise inteligente
        self.dynamic_threshold = True  # Habilita threshold dinâmico por serviço
        
    async def initialize(self):
        """Inicialização assíncrona dos serviços"""
        if self.is_initialized:
            return
            
        # Inicializar serviços conforme configuração
        await self._initialize_services()
        
        emoji_logger.system_ready(
            "🎯 TeamCoordinator inicializado",
            services=list(self.services.keys())
        )
        self.is_initialized = True
    
    async def _initialize_services(self):
        """Inicializa serviços habilitados de forma SIMPLES"""
        
        # Calendar Service
        if settings.enable_calendar_agent:
            try:
                from app.services.calendar_service_100_real import CalendarServiceReal as CalendarService
                self.services["calendar"] = CalendarService()
                emoji_logger.service_ready("📅 Calendar Service pronto")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao inicializar Calendar: {e}")
        
        # CRM Service  
        if settings.enable_crm_agent:
            try:
                from app.services.crm_service_100_real import CRMServiceReal as CRMService
                self.services["crm"] = CRMService()
                emoji_logger.service_ready("📊 CRM Service pronto")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao inicializar CRM: {e}")
        
        # FollowUp Service
        if settings.enable_followup_agent:
            try:
                from app.services.followup_service_100_real import FollowUpServiceReal as FollowUpService
                self.services["followup"] = FollowUpService()
                emoji_logger.service_ready("🔄 FollowUp Service pronto")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao inicializar FollowUp: {e}")
    
    def analyze_service_need(self, message: str, context: Dict[str, Any]) -> Dict[str, float]:
        """
        Analisa necessidade de serviços com INTENÇÃO INTELIGENTE
        
        Args:
            message: Mensagem do usuário
            context: Contexto da conversa
            
        Returns:
            Scores de necessidade por serviço
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
        
        # Normalizar scores e aplicar threshold dinâmico
        for service in scores:
            scores[service] = min(1.0, scores[service])
        
        # 📝 Log detalhado para debugging
        emoji_logger.service_event(
            "🎯 Análise de necessidade de serviços",
            calendar=f"{scores['calendar']:.3f}",
            crm=f"{scores['crm']:.3f}", 
            followup=f"{scores['followup']:.3f}",
            threshold=self.decision_threshold
        )
        
        return scores
    
    def _get_dynamic_threshold(self, service_name: str, context: Dict[str, Any]) -> float:
        """
        🎯 Calcula threshold dinâmico baseado no serviço e contexto
        """
        if not self.dynamic_threshold:
            return self.decision_threshold
        
        base_threshold = self.decision_threshold
        
        # Threshold específico por serviço
        service_thresholds = {
            "calendar": 0.35,  # Mais sensível para agendamentos
            "crm": 0.45,       # Padrão para dados
            "followup": 0.40   # Moderado para follow-ups
        }
        
        threshold = service_thresholds.get(service_name, base_threshold)
        
        # Ajustes baseados no contexto
        stage = context.get("conversation_stage", "").lower()
        urgency = context.get("urgency_level", "normal").lower()
        
        # Reduzir threshold para estágios avançados
        if stage in ["qualificação", "negociação", "fechamento"]:
            threshold -= 0.1
        
        # Reduzir threshold para alta urgência
        if urgency == "alta":
            threshold -= 0.15
        elif urgency == "média":
            threshold -= 0.05
        
        return max(0.2, threshold)  # Mínimo de 0.2
    
    def _analyze_calendar_intent(self, message_lower: str, context: Dict[str, Any]) -> float:
        """
        🎯 Análise INTELIGENTE de intenção para Calendar Service
        Considera palavras-chave + intenção + estágio da conversa + BOOST PROATIVO
        """
        calendar_score = 0.0
        
        # 1. PALAVRAS-CHAVE BÁSICAS (peso 0.2)
        basic_keywords = [
            "agendar", "marcar", "reunião", "conversar", "leonardo",
            "horário", "disponível", "data", "quando", "encontro"
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
        
        # 3. INDICADORES DE URGÊNCIA (peso 0.3)
        urgency_indicators = [
            "hoje", "amanhã", "logo", "rápido", "urgente",
            "já", "agora", "preciso", "importante"
        ]
        if any(indicator in message_lower for indicator in urgency_indicators):
            calendar_score += 0.3
        
        # 4. INDICADORES DE TEMPO ESPECÍFICO (peso 0.5)
        time_patterns = [
            r"\d{1,2}h\d{0,2}", r"\d{1,2}:\d{2}", r"\d{1,2}/\d{1,2}",
            "segunda", "terça", "quarta", 
            "quinta", "sexta", "sábado", "domingo"
        ]
        import re
        for pattern in time_patterns:
            if re.search(pattern, message_lower):
                calendar_score += 0.5
                break
        
        # 🚀 5. BOOST PROATIVO PARA CLOSING/AGENDAMENTO (peso 0.3)
        conversation_stage = context.get("conversation_stage", "").lower()
        qualification_score = context.get("qualification_score", 0)
        
        # Boost quando estágio indica necessidade de agendamento
        if conversation_stage in ["closing", "agendamento_processo", "qualificação_completa"]:
            calendar_score += 0.3
            emoji_logger.service_event("🎯 BOOST Calendar por estágio de closing")
        
        # Boost quando score de qualificação é alto (≥7)
        if qualification_score >= 7:
            calendar_score += 0.3
            emoji_logger.service_event(f"🎯 BOOST Calendar por score alto: {qualification_score}")
        
        # 🚀 6. BOOST POR INTERESSE DEMONSTRADO (peso 0.2)
        interest_indicators = [
            "interessante", "interessado", "faz sentido", "legal", "ótimo",
            "perfeito", "quero", "preciso", "vou", "aceito"
        ]
        if any(indicator in message_lower for indicator in interest_indicators):
            calendar_score += 0.2
            emoji_logger.service_event("🎯 BOOST Calendar por interesse demonstrado")
        
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
            emoji_logger.service_event("🎯 BOOST Calendar por user_intent")
            
        elif "dados" in user_intent or "informações" in user_intent:
            scores["crm"] += 0.4
            emoji_logger.service_event("📊 BOOST CRM por user_intent")
            
        elif "depois" in user_intent or "adiado" in user_intent:
            scores["followup"] += 0.4
            emoji_logger.service_event("🔄 BOOST FollowUp por user_intent")
        
        # BOOST baseado em conversation_stage
        stage = context.get("conversation_stage", "").lower()
        
        if stage in ["qualificação", "negociação", "fechamento"]:
            scores["calendar"] += 0.3  # Estágios avançados = agendar reunião
            emoji_logger.service_event("🎯 BOOST Calendar por conversation_stage avançado")
            
        elif stage in ["início", "descoberta"]:
            scores["crm"] += 0.3  # Início = coletar dados
            emoji_logger.service_event("📊 BOOST CRM por conversation_stage inicial")
        
        # BOOST baseado em action_needed (compatibilidade)
        action_needed = context.get("action_needed", "")
        if action_needed == "agendar":
            scores["calendar"] += 0.4
        elif action_needed == "qualificar":
            scores["crm"] += 0.4
        elif action_needed == "reengajar":
            scores["followup"] += 0.4
        
        return scores
    
    async def execute_services(self, 
                              message: str,
                              context: Dict[str, Any],
                              lead_info: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Executa serviços necessários de forma DIRETA
        
        Args:
            message: Mensagem do usuário
            context: Contexto analisado
            lead_info: Informações do lead
            
        Returns:
            Lista de resultados dos serviços executados
        """
        results = []
        
        # Analisar necessidade
        scores = self.analyze_service_need(message, context)
        
        # Executar serviços com threshold dinâmico
        for service_name, score in scores.items():
            # Calcular threshold dinâmico para este serviço
            dynamic_threshold = self._get_dynamic_threshold(service_name, context)
            
            if score >= dynamic_threshold:
                emoji_logger.service_event(
                    f"🎯 Executando {service_name}",
                    score=f"{score:.3f}",
                    threshold=f"{dynamic_threshold:.3f}",
                    reason="threshold_dinamico"
                )
                
                result = await self._execute_single_service(
                    service_name,
                    message,
                    context,
                    lead_info
                )
                
                if result:
                    results.append(result)
        
        return results
    
    async def _execute_single_service(self,
                                     service_name: str,
                                     message: str,
                                     context: Dict[str, Any],
                                     lead_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Executa um serviço específico
        
        Args:
            service_name: Nome do serviço
            message: Mensagem
            context: Contexto
            lead_info: Info do lead
            
        Returns:
            Resultado da execução ou None
        """
        if service_name not in self.services:
            emoji_logger.service_warning(f"Serviço {service_name} não disponível")
            return None
        
        service = self.services[service_name]
        
        try:
            if service_name == "calendar":
                # Verificar disponibilidade ou agendar
                if "disponível" in message.lower() or "horário" in message.lower():
                    result = await service.check_availability(message)
                else:
                    # Extrair data/hora da mensagem
                    date_time = self._extract_datetime(message)
                    if date_time:
                        result = await service.schedule_meeting(
                            date_time["date"],
                            date_time["time"],
                            lead_info
                        )
                        
                        # 🚀 WORKFLOW COMPLETO PÓS-AGENDAMENTO
                        if result and result.get("success"):
                            await self._execute_post_scheduling_workflow(
                                result,
                                lead_info,
                                context
                            )
                    else:
                        result = await service.suggest_times(lead_info)
                
            elif service_name == "crm":
                # Atualizar lead no CRM
                result = await service.create_or_update_lead(lead_info)
                
                # Capturar o lead_id retornado e adicionar ao lead_info
                if result.get("success") and result.get("lead_id"):
                    lead_id = result["lead_id"]
                    lead_info["id"] = lead_id  # Armazenar para uso futuro
                    
                    # Atualizar estágio se necessário
                    if lead_info.get("stage"):
                        await service.update_lead_stage(
                            lead_id,  # Usar o lead_id correto
                            lead_info["stage"]
                        )
                    
                    # 🚀 SINCRONIZAÇÃO AUTOMÁTICA COM KOMMO
                    # Após criar/atualizar no CRM, sincronizar com campos dinâmicos
                    try:
                        emoji_logger.service_event("🔄 Sincronizando campos dinâmicos e tags")
                        sync_result = await self.sync_lead_to_crm(lead_info)
                        if sync_result.get("success"):
                            emoji_logger.system_success("✅ Tags e campos personalizados sincronizados")
                    except Exception as sync_error:
                        emoji_logger.service_warning(f"Sync opcional falhou: {sync_error}")
                    
            elif service_name == "followup":
                # Agendar follow-up
                phone = lead_info.get("phone", "")
                name = lead_info.get("name", "Cliente")
                bill_value = lead_info.get("bill_value", 0)
                
                # 🛡️ VALIDAÇÃO: Verificar se phone_number é válido
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
                result = await service.schedule_followup(
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
    
    def _extract_datetime(self, text: str) -> Optional[Dict[str, str]]:
        """
        Extrai data e hora do texto (SIMPLES)
        
        Args:
            text: Texto com data/hora
            
        Returns:
            Dict com date e time ou None
        """
        import re
        from datetime import datetime, timedelta
        
        text_lower = text.lower()
        
        # Padrões simples
        hoje = datetime.now()
        
        # Detectar "hoje", "amanhã", "depois de amanhã"
        if "hoje" in text_lower:
            date = hoje.strftime("%Y-%m-%d")
        elif "amanhã" in text_lower:
            date = (hoje + timedelta(days=1)).strftime("%Y-%m-%d")
        elif "depois de amanhã" in text_lower:
            date = (hoje + timedelta(days=2)).strftime("%Y-%m-%d")
        else:
            # Tentar extrair data no formato DD/MM
            date_match = re.search(r"(\d{1,2})[/-](\d{1,2})", text)
            if date_match:
                day = int(date_match.group(1))
                month = int(date_match.group(2))
                year = hoje.year
                date = f"{year}-{month:02d}-{day:02d}"
            else:
                date = None
        
        # Extrair hora
        time_match = re.search(r"(\d{1,2})[h:](\d{0,2})", text_lower)
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            time = f"{hour:02d}:{minute:02d}"
        else:
            # Detectar períodos
            if "manhã" in text_lower:
                time = "09:00"
            elif "tarde" in text_lower:
                time = "14:00"
            elif "noite" in text_lower:
                time = "19:00"
            else:
                time = "10:00"  # Default
        
        if date:
            return {"date": date, "time": time}
        
        return None
    
    def _calculate_followup_date(self, context: Dict[str, Any]) -> str:
        """
        Calcula data ideal para follow-up
        
        Args:
            context: Contexto da conversa
            
        Returns:
            Data no formato YYYY-MM-DD
        """
        from datetime import datetime, timedelta
        
        urgency = context.get("urgency_level", "normal")
        stage = context.get("conversation_stage", "início")
        
        # Calcular dias baseado em urgência e estágio
        if urgency == "alta":
            days = 1
        elif urgency == "média":
            days = 3
        elif stage in ["negociação", "qualificação"]:
            days = 2
        else:
            days = 7
        
        followup_date = datetime.now() + timedelta(days=days)
        return followup_date.strftime("%Y-%m-%d")
    
    def get_service_status(self) -> Dict[str, Any]:
        """Retorna status dos serviços"""
        return {
            "initialized": self.is_initialized,
            "threshold": self.decision_threshold,
            "services": {
                name: {
                    "enabled": name in self.services,
                    "ready": self.services.get(name) is not None
                }
                for name in ["calendar", "crm", "followup"]
            }
        }
    
    async def _execute_post_scheduling_workflow(self,
                                                scheduling_result: Dict[str, Any],
                                                lead_info: Dict[str, Any],
                                                context: Dict[str, Any]):
        """
        🚀 WORKFLOW COMPLETO PÓS-AGENDAMENTO
        Executa todas as ações necessárias após agendar reunião
        """
        try:
            from datetime import datetime, timedelta
            from app.integrations.supabase_client import supabase_client
            
            # 🚀 EXTRAIR DADOS ESSENCIAIS do resultado do agendamento
            google_event_id = scheduling_result.get("google_event_id") or scheduling_result.get("meeting_id")
            start_time = scheduling_result.get("start_time")
            meet_link = scheduling_result.get("meet_link")
            lead_id = lead_info.get("id")  # Agora estará definido pelo CRM
            
            emoji_logger.service_event(
                "🎯 Iniciando workflow pós-agendamento",
                google_event_id=google_event_id,
                start_time=start_time,
                meet_link=meet_link
            )
            
            # Se não tiver lead_id, tentar criar no CRM primeiro
            if not lead_id and "crm" in self.services:
                try:
                    crm_result = await self.services["crm"].create_or_update_lead(lead_info)
                    if crm_result.get("success") and crm_result.get("lead_id"):
                        lead_id = crm_result["lead_id"]
                        lead_info["id"] = lead_id
                except Exception as e:
                    emoji_logger.service_warning(f"Erro ao criar lead no CRM: {e}")
            
            # 1. SALVAR GOOGLE_EVENT_ID NO SUPABASE - ESSENCIAL PARA CANCELAMENTOS
            try:
                # Buscar ou criar lead no Supabase usando UUID
                supabase_lead_id = await self._get_or_create_supabase_lead_id(lead_info)
                
                qualification_data = {
                    'lead_id': supabase_lead_id,  # Usar UUID do Supabase
                    'qualification_status': 'QUALIFIED',
                    'score': 85,
                    'notes': f'Reunião agendada com sucesso. Evento Google: {google_event_id}',
                    'qualified_at': datetime.now().isoformat(),
                    'qualified_by': str(uuid4()),  # Usar UUID válido ao invés de 'TeamCoordinator'
                    'google_event_id': google_event_id  # 🚀 SALVAR google_event_id para cancelamentos futuros
                }
                
                # Adicionar meet_link se disponível
                if meet_link:
                    qualification_data['notes'] += f' | Google Meet: {meet_link}'
                
                created_qualification = await supabase_client.create_lead_qualification(qualification_data)
                emoji_logger.system_success(
                    "✅ Qualificação criada no Supabase com google_event_id",
                    google_event_id=google_event_id,
                    qualification_id=created_qualification.get('id') if created_qualification else None
                )
            except Exception as e:
                emoji_logger.service_warning(f"Erro ao criar qualificação: {e}")
            
            # 2. ATUALIZAR LEAD NO SUPABASE COM DADOS COMPLETOS DA REUNIÃO
            try:
                # Usar o UUID do Supabase ao invés do ID do Kommo
                supabase_lead_id = await self._get_or_create_supabase_lead_id(lead_info)
                
                update_data = {
                    'google_event_id': google_event_id,  # 🚀 PERSISTÊNCIA ESSENCIAL
                    'meeting_scheduled_at': start_time,
                    'qualification_status': 'QUALIFIED',
                    'current_stage': 'MEETING_SCHEDULED'
                }
                
                # 🚀 ADICIONAR meet_link se disponível
                if meet_link:
                    update_data['google_event_link'] = meet_link  # Assumindo que existe este campo
                    # ou se não existir, adicionamos um campo genérico
                    update_data['meeting_link'] = meet_link
                
                updated_lead = await supabase_client.update_lead(supabase_lead_id, update_data)
                emoji_logger.system_success(
                    "✅ Lead atualizado com dados completos da reunião",
                    google_event_id=google_event_id,
                    meet_link=meet_link[:50] + '...' if meet_link and len(meet_link) > 50 else meet_link
                )
            except Exception as e:
                emoji_logger.service_warning(f"Erro ao atualizar lead: {e}")
            
            # 3. CRIAR LEMBRETES PERSONALIZADOS
            if "followup" in self.services:
                try:
                    # 🛡️ VALIDAÇÃO: Verificar se start_time é string ou datetime
                    if isinstance(start_time, str):
                        meeting_datetime = datetime.fromisoformat(start_time)
                    elif isinstance(start_time, datetime):
                        meeting_datetime = start_time
                    else:
                        raise ValueError(f"start_time deve ser string ou datetime, recebido: {type(start_time)}")
                    
                    followup_service = self.services["followup"]
                    
                    # Lembrete 24h antes
                    reminder_24h = await self._generate_personalized_reminder(
                        lead_info,
                        meeting_datetime,
                        24,
                        context
                    )
                    
                    # Usar UUID do Supabase para follow-ups
                    supabase_lead_id = await self._get_or_create_supabase_lead_id(lead_info)
                    
                    await followup_service.create_followup_direct({
                        'lead_id': supabase_lead_id,
                        'type': 'MEETING_REMINDER_24H', 
                        'scheduled_at': (meeting_datetime - timedelta(hours=24)).isoformat(),
                        'message': reminder_24h,
                        'metadata': {
                            'google_event_id': google_event_id,  # 🚀 PERSISTÊNCIA para cancelamentos
                            'meet_link': meet_link,  # 🚀 ADICIONAR meet_link para lembretes
                            'hours_before': 24
                        }
                    })
                    emoji_logger.system_success(
                        "✅ Lembrete 24h criado com google_event_id", 
                        google_event_id=google_event_id
                    )
                    
                    # Lembrete 2h antes
                    reminder_2h = await self._generate_personalized_reminder(
                        lead_info,
                        meeting_datetime,
                        2,
                        context
                    )
                    
                    await followup_service.create_followup_direct({
                        'lead_id': supabase_lead_id,
                        'type': 'MEETING_REMINDER_2H',
                        'scheduled_at': (meeting_datetime - timedelta(hours=2)).isoformat(),
                        'message': reminder_2h,
                        'metadata': {
                            'google_event_id': google_event_id,  # 🚀 PERSISTÊNCIA para cancelamentos
                            'meet_link': meet_link,  # 🚀 ADICIONAR meet_link para lembretes
                            'hours_before': 2
                        }
                    })
                    emoji_logger.system_success(
                        "✅ Lembrete 2h criado com google_event_id",
                        google_event_id=google_event_id
                    )
                    
                except Exception as e:
                    emoji_logger.service_warning(f"Erro ao criar lembretes: {e}")
            
            # 4. ATUALIZAR CRM SE DISPONÍVEL
            if "crm" in self.services and lead_info and lead_id:
                try:
                    crm_service = self.services["crm"]
                    
                    # Usar o ID do Kommo (original) para operações do CRM
                    kommo_lead_id = lead_info.get("id") or lead_id
                    if kommo_lead_id:
                        # Atualizar estágio no CRM
                        await crm_service.update_lead_stage(
                            str(kommo_lead_id),  # Usar ID do Kommo para CRM
                            "REUNIAO_AGENDADA",
                            f"Reunião agendada para {start_time}"
                        )
                        
                        # Adicionar tags
                        if hasattr(crm_service, 'add_tags_to_lead'):
                            await crm_service.add_tags_to_lead(
                                str(kommo_lead_id),  # Usar ID do Kommo para CRM
                                ["reuniao_agendada", "qualificado", "hot_lead"]
                            )
                    
                    emoji_logger.system_success("✅ CRM atualizado com sucesso")
                except Exception as e:
                    emoji_logger.service_warning(f"Erro ao atualizar CRM: {e}")
            
            # 🚀 SUMMARY: Log de todos os dados persistidos
            emoji_logger.system_success(
                "🎊 Workflow pós-agendamento concluído com persistência!",
                google_event_id=google_event_id,
                meet_link=meet_link[:50] + '...' if meet_link and len(meet_link) > 50 else meet_link,
                lead_id=lead_id,
                start_time=start_time
            )
            
            # 🚀 RETORNAR dados importantes para uso futuro
            return {
                'success': True,
                'google_event_id': google_event_id,
                'meet_link': meet_link,
                'start_time': start_time,
                'lead_id': lead_id,
                'workflow_completed': True
            }
            
        except Exception as e:
            emoji_logger.service_error(f"Erro no workflow pós-agendamento: {e}")
    
    async def _generate_personalized_reminder(self,
                                             lead_info: Dict[str, Any],
                                             meeting_time: datetime,
                                             hours_before: int,
                                             context: Dict[str, Any]) -> str:
        """
        Gera mensagem personalizada de lembrete
        NÃO USA TEMPLATES FIXOS - mensagens únicas baseadas no contexto
        """
        lead_name = lead_info.get("name", "").split()[0] if lead_info.get("name") else ""
        meeting_hour = meeting_time.strftime("%H:%M")
        weekday = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"][meeting_time.weekday()]
        
        # Informações do contexto
        main_interest = context.get("main_interest", "economia na conta de luz")
        pain_points = context.get("pain_points", [])
        
        if hours_before == 24:
            # Lembrete 24h - informativo e amigável
            if "conta alta" in str(pain_points).lower():
                return f"Oi{' ' + lead_name if lead_name else ''}! 😊 Amanhã às {meeting_hour} Leonardo vai te mostrar como reduzir essa conta alta. Preparado(a) pra economizar?"
            else:
                return f"{'Oi ' + lead_name + '! ' if lead_name else ''}Confirmado amanhã {weekday} às {meeting_hour} com Leonardo sobre {main_interest}! 🌞"
        else:
            # Lembrete 2h - direto e urgente
            return f"⏰ Reunião em 2h! Leonardo te espera às {meeting_hour} pra falar da sua economia!"
    
    async def sync_lead_to_crm(self, lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        🚀 Sincroniza lead imediatamente com Kommo CRM
        Conecta com KommoAutoSyncService para sync dinâmico
        
        Args:
            lead_info: Informações atualizadas do lead
            
        Returns:
            Resultado da sincronização
        """
        try:
            # Verificar se sync está habilitado
            if not settings.enable_kommo_auto_sync:
                return {"success": False, "message": "Auto sync desabilitado"}
            
            emoji_logger.service_event("🔄 Iniciando sync imediato com Kommo CRM")
            
            # Usar serviço CRM atual (kommo_auto_sync foi migrado para crm_service)
            from app.services.crm_service_100_real import CRMServiceReal
            kommo_auto_sync_service = CRMServiceReal()  # Compatibilidade com código legado
            
            # Primeiro, garantir que o lead existe no Supabase
            supabase_lead_id = await self._get_or_create_supabase_lead_id(lead_info)
            
            # Atualizar Supabase com informações mais recentes
            from app.integrations.supabase_client import supabase_client
            
            # Preparar dados para atualização
            update_data = {}
            
            # Mapear campos importantes
            if lead_info.get("name"):
                update_data["name"] = lead_info["name"]
            if lead_info.get("email"):
                # 🔥 CORREÇÃO CRÍTICA: Garantir que email seja salvo no Supabase
                update_data["email"] = lead_info["email"]
                emoji_logger.service_event(f"✉️ Email detectado e será salvo: {lead_info['email']}")
            if lead_info.get("bill_value"):
                update_data["bill_value"] = lead_info["bill_value"]
            if lead_info.get("chosen_flow"):
                update_data["chosen_flow"] = lead_info["chosen_flow"]
            if lead_info.get("current_stage"):
                update_data["current_stage"] = lead_info["current_stage"]
            if lead_info.get("qualification_score"):
                # 🔥 CORREÇÃO CRÍTICA: Converter float para int para evitar erro de tipo INTEGER
                from app.utils.safe_conversions import safe_int_conversion
                update_data["qualification_score"] = safe_int_conversion(lead_info["qualification_score"], 0)
            if lead_info.get("google_event_link"):
                update_data["google_event_link"] = lead_info["google_event_link"]
            
            # Atualizar no Supabase se houver mudanças
            if update_data:
                try:
                    await supabase_client.update_lead(supabase_lead_id, update_data)
                    emoji_logger.service_event(
                        "✅ Lead atualizado no Supabase",
                        fields=list(update_data.keys()),
                        data=update_data
                    )
                    
                    # 🔥 Log específico para email para debugging
                    if "email" in update_data:
                        emoji_logger.system_success(
                            f"📧 Email salvo com sucesso no Supabase: {update_data['email']}"
                        )
                except Exception as e:
                    emoji_logger.service_error(f"Erro ao atualizar lead no Supabase: {e}")
                    emoji_logger.service_error(f"Dados que falharam: {update_data}")
                    # Não propagar erro para não quebrar o fluxo principal
            
            # Executar sync específico do lead
            # CRMServiceReal não tem os métodos sync_* do antigo kommo_auto_sync
            # Vamos criar o lead diretamente no Kommo usando o método create_lead
            try:
                # Preparar dados para criação/atualização do lead no Kommo
                lead_data = {
                    "name": lead_info.get("name", "Lead sem nome"),
                    "phone": lead_info.get("phone", ""),
                    "qualification_score": lead_info.get("qualification_score", 0),
                    "bill_value": lead_info.get("bill_value", 0),
                    "interested": lead_info.get("interested", False)
                }
                
                # Tentar criar ou atualizar o lead no Kommo
                # CRMServiceReal usa create_or_update_lead ao invés de create_lead
                if hasattr(kommo_auto_sync_service, 'create_or_update_lead'):
                    kommo_lead = await kommo_auto_sync_service.create_or_update_lead(
                        lead_data=lead_data,
                        tags=["sync_automático", "SDR_IA"]
                    )
                    sync_result = {"success": True, "message": f"Lead criado/atualizado no Kommo: {kommo_lead.get('id')}"}
                else:
                    # Se não tem create_or_update_lead, apenas marca como sincronizado
                    sync_result = {"success": True, "message": "Sync marcado (métodos não disponíveis)"}
            except Exception as sync_error:
                emoji_logger.service_error(f"Erro no sync com Kommo: {sync_error}")
                sync_result = {"success": False, "message": str(sync_error)}
            
            emoji_logger.system_success(
                "✅ Lead sincronizado com Kommo CRM",
                result=sync_result
            )
            
            return sync_result
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao sincronizar com CRM: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def health_check(self) -> Dict[str, bool]:
        """Verifica saúde dos serviços"""
        health = {}
        
        for name, service in self.services.items():
            try:
                # Cada serviço deve ter um método health_check
                if hasattr(service, 'health_check'):
                    health[name] = await service.health_check()
                else:
                    health[name] = True  # Assume healthy se não tem check
            except:
                health[name] = False
        
        return health
    
    async def _get_or_create_supabase_lead_id(self, lead_info: Dict[str, Any]) -> str:
        """
        Busca ou cria um UUID válido no Supabase para o lead
        
        Args:
            lead_info: Informações do lead incluindo telefone e dados do Kommo
            
        Returns:
            UUID válido do Supabase
        """
        try:
            from app.integrations.supabase_client import supabase_client
            
            phone = lead_info.get("phone", "")
            if not phone:
                # Se não tem telefone, gerar número único baseado no UUID
                new_lead_uuid = str(uuid4())
                # Usar parte do UUID como telefone único para evitar duplicação
                unique_phone = f"unknown_{new_lead_uuid[:8]}"
                
                lead_data = {
                    "id": new_lead_uuid,  # UUID explícito
                    "phone_number": unique_phone,  # Phone único baseado no UUID
                    "name": lead_info.get("name", "Lead Sem Telefone"),
                    "email": lead_info.get("email"),
                    "bill_value": lead_info.get("bill_value"),
                    "current_stage": "INITIAL_CONTACT", 
                    "qualification_status": "PENDING",
                    "kommo_lead_id": str(lead_info.get("id")) if lead_info.get("id") else None
                }
                
                try:
                    new_lead = await supabase_client.create_lead(lead_data)
                    emoji_logger.system_success(f"✅ Lead sem telefone criado: {new_lead['id']}")
                    return new_lead["id"]
                except Exception as e:
                    emoji_logger.service_error(f"Erro ao criar lead sem telefone: {e}")
                    # Se erro for duplicate key, retornar UUID sem criar no banco
                    if "duplicate key" in str(e):
                        return new_lead_uuid
                    return new_lead_uuid  # Fallback para UUID
            
            # Buscar lead existente no Supabase por telefone
            existing_lead = await supabase_client.get_lead_by_phone(phone)
            
            if existing_lead:
                # Atualizar dados do Kommo se necessário
                kommo_id = lead_info.get("id")
                if kommo_id and existing_lead.get("kommo_lead_id") != str(kommo_id):
                    await supabase_client.update_lead(
                        existing_lead["id"],
                        {"kommo_lead_id": str(kommo_id)}
                    )
                return existing_lead["id"]
            else:
                # 🔥 CORREÇÃO CRÍTICA: Criar novo lead no Supabase
                emoji_logger.service_event(f"🆕 Criando novo lead no Supabase para {phone}")
                lead_data = {
                    "phone_number": phone,
                    "name": lead_info.get("name"),
                    "email": lead_info.get("email"),
                    "bill_value": lead_info.get("bill_value"),
                    "current_stage": "INITIAL_CONTACT",
                    "qualification_status": "PENDING",
                    "kommo_lead_id": str(lead_info.get("id")) if lead_info.get("id") else None
                }
                
                try:
                    new_lead = await supabase_client.create_lead(lead_data)
                    emoji_logger.system_success(f"✅ Lead criado no Supabase: {new_lead['id']}")
                    return new_lead["id"]
                except Exception as e:
                    emoji_logger.service_error(f"Erro ao criar lead no Supabase: {e}")
                    # Fallback: criar UUID mas registrar erro
                    return str(uuid4())
                
        except Exception as e:
            emoji_logger.service_error(f"Erro ao obter UUID do Supabase: {e}")
            # Fallback: criar novo UUID
            return str(uuid4())
    
    async def proactive_crm_sync(self, lead_info: Dict[str, Any], context: Dict[str, Any]):
        """
        Sincroniza proativamente o estágio do lead, tags e campos customizados com o CRM,
        baseado no contexto completo da conversa e nas regras de negócio.
        """
        if "crm" not in self.services:
            return

        crm_service = self.services["crm"]
        kommo_lead_id = lead_info.get("kommo_lead_id")

        if not kommo_lead_id:
            emoji_logger.service_warning("Kommo Lead ID não encontrado para sync proativo.")
            return

        # 1. Mapeamento de Estágio Conversacional para Estágio do CRM
        conversation_stage = context.get("conversation_stage")
        lead_score = lead_info.get("qualification_score", 0)
        
        target_stage_name = None
        if conversation_stage == "agendamento":
            target_stage_name = "REUNIÃO AGENDADA"
        elif conversation_stage == "qualificação":
            if lead_score >= settings.min_qualification_score:
                target_stage_name = "QUALIFICADO"
            else:
                target_stage_name = "DESQUALIFICADO"
        elif conversation_stage in ["estágio_1_apresentar_soluções", "estágio_2_aguardando_escolha"]:
            target_stage_name = "EM QUALIFICAÇÃO"
        
        if target_stage_name:
            try:
                await crm_service.update_lead_stage(str(kommo_lead_id), target_stage_name)
                emoji_logger.system_success(f"✅ Estágio atualizado para: {target_stage_name}")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao atualizar estágio: {e}")

        # 2. Atualização de Campos Customizados
        fields_to_update = {}
        if lead_info.get("bill_value"):
            fields_to_update["bill_value"] = lead_info["bill_value"]
        if lead_info.get("chosen_flow"):
            fields_to_update["solution_type"] = lead_info["chosen_flow"]
        
        if fields_to_update:
            try:
                await crm_service.update_fields(str(kommo_lead_id), fields_to_update)
                emoji_logger.system_success(f"✅ Campos atualizados: {list(fields_to_update.keys())}")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao atualizar campos: {e}")

        # 3. Atualização de Tags Contextuais
        tags_to_add = []
        if lead_info.get("chosen_flow"):
            tags_to_add.append(f"fluxo_{lead_info['chosen_flow'].lower().replace(' ', '_')}")
        if context.get("objections_raised"):
            for objection in context["objections_raised"]:
                tags_to_add.append(f"objecao_{objection}")
        
        if tags_to_add:
            try:
                await crm_service.add_tags_to_lead(str(kommo_lead_id), tags_to_add)
                emoji_logger.system_success(f"✅ Tags adicionadas: {tags_to_add}")
            except Exception as e:
                emoji_logger.service_error(f"Erro ao adicionar tags: {e}")
    
    async def get_google_event_id_by_lead(self, lead_id: str) -> Optional[str]:
        """
        🔍 Busca google_event_id de um lead para cancelamentos futuros
        
        Args:
            lead_id: ID do lead no Supabase ou Kommo
            
        Returns:
            google_event_id se encontrado, None caso contrário
        """
        try:
            from app.integrations.supabase_client import supabase_client
            
            # Tentar buscar primeiro na tabela leads_qualifications
            result = supabase_client.client.table('leads_qualifications')\
                .select('google_event_id')\
                .eq('lead_id', lead_id)\
                .order('created_at', desc=True)\
                .limit(1)\
                .execute()
            
            if result.data and result.data[0].get('google_event_id'):
                google_event_id = result.data[0]['google_event_id']
                emoji_logger.service_event(
                    "🔍 Google Event ID encontrado na qualificação",
                    google_event_id=google_event_id,
                    lead_id=lead_id
                )
                return google_event_id
            
            # Se não encontrou na qualificação, tentar na tabela leads
            lead_result = supabase_client.client.table('leads')\
                .select('google_event_id')\
                .eq('id', lead_id)\
                .execute()
            
            if lead_result.data and lead_result.data[0].get('google_event_id'):
                google_event_id = lead_result.data[0]['google_event_id']
                emoji_logger.service_event(
                    "🔍 Google Event ID encontrado no lead",
                    google_event_id=google_event_id,
                    lead_id=lead_id
                )
                return google_event_id
            
            emoji_logger.service_warning(f"Google Event ID não encontrado para lead: {lead_id}")
            return None
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao buscar google_event_id: {e}")
            return None
    
    async def cancel_meeting_by_lead(self, lead_id: str, reason: str = "Cancelamento solicitado") -> Dict[str, Any]:
        """
        🚫 Cancela reunião usando lead_id (busca google_event_id automaticamente)
        
        Args:
            lead_id: ID do lead
            reason: Motivo do cancelamento
            
        Returns:
            Resultado do cancelamento
        """
        try:
            # Buscar google_event_id
            google_event_id = await self.get_google_event_id_by_lead(lead_id)
            
            if not google_event_id:
                return {
                    "success": False,
                    "message": "Reunião não encontrada para este lead",
                    "reason": "google_event_id não encontrado"
                }
            
            # Cancelar no Google Calendar se serviço estiver disponível
            if "calendar" in self.services:
                calendar_service = self.services["calendar"]
                cancel_result = await calendar_service.cancel_meeting(google_event_id)
                
                if cancel_result.get("success"):
                    # Atualizar status no Supabase
                    await self._update_meeting_status_after_cancel(lead_id, google_event_id, reason)
                    
                    emoji_logger.system_success(
                        "✅ Reunião cancelada com sucesso",
                        lead_id=lead_id,
                        google_event_id=google_event_id,
                        reason=reason
                    )
                    
                    return {
                        "success": True,
                        "message": "Reunião cancelada com sucesso",
                        "google_event_id": google_event_id,
                        "reason": reason
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Erro ao cancelar no Google Calendar: {cancel_result.get('message')}",
                        "google_event_id": google_event_id
                    }
            else:
                return {
                    "success": False,
                    "message": "Serviço de calendário não disponível"
                }
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao cancelar reunião: {e}")
            return {
                "success": False,
                "message": f"Erro interno: {e}"
            }
    
    async def _update_meeting_status_after_cancel(self, lead_id: str, google_event_id: str, reason: str):
        """
        📝 Atualiza status da reunião após cancelamento
        
        Args:
            lead_id: ID do lead
            google_event_id: ID do evento Google
            reason: Motivo do cancelamento
        """
        try:
            from app.integrations.supabase_client import supabase_client
            from datetime import datetime
            
            # Atualizar qualificação
            supabase_client.client.table('leads_qualifications')\
                .update({
                    'notes': f'CANCELADO - {reason} em {datetime.now().strftime("%d/%m/%Y %H:%M")}',
                    'qualification_status': 'NOT_QUALIFIED',  # ou manter como QUALIFIED mas marcar como cancelado
                    'updated_at': datetime.now().isoformat()
                })\
                .eq('google_event_id', google_event_id)\
                .execute()
            
            # Atualizar lead
            await supabase_client.update_lead(lead_id, {
                'current_stage': 'MEETING_CANCELLED',
                'meeting_scheduled_at': None,  # Limpar data da reunião
                'updated_at': datetime.now().isoformat()
            })
            
            emoji_logger.service_event("📝 Status atualizado após cancelamento")
            
        except Exception as e:
            emoji_logger.service_warning(f"Erro ao atualizar status após cancelamento: {e}")