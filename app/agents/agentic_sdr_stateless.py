"""
AgenticSDR Stateless - Arquitetura ZERO complexidade para produção
Cada requisição é completamente isolada e independente
Não há estado compartilhado entre conversas
"""

from typing import Dict, Any, Optional, List
import asyncio
from datetime import datetime
import pytz

from app.core.model_manager import ModelManager
from app.core.multimodal_processor import MultimodalProcessor
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
from app.core.team_coordinator import TeamCoordinator
from app.services.conversation_monitor import get_conversation_monitor
from app.utils.logger import emoji_logger
from app.config import settings

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
        self.team_coordinator = TeamCoordinator()
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
            await self.team_coordinator.initialize()
            await self.conversation_monitor.initialize()
            
            self.is_initialized = True
            emoji_logger.system_ready(
                "✅ AgenticSDR Stateless inicializado!",
                modules=[
                    "ModelManager", "MultimodalProcessor", 
                    "LeadManager", "ContextAnalyzer", "TeamCoordinator"
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
            
            # 6. Executar serviços necessários
            service_results = await self.team_coordinator.execute_services(
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
    
    async def _generate_response(self,
                                message: str,
                                context: Dict[str, Any],
                                lead_info: Dict[str, Any],
                                service_results: List[Dict[str, Any]],
                                media_context: str,
                                conversation_history: List[Dict],
                                execution_context: Dict[str, Any]) -> str:
        """
        Gera resposta usando o ModelManager com contexto completo
        """
        # Buscar conhecimento na base
        knowledge_context = await self._search_knowledge_base(message)
        
        # Construir prompt com histórico completo
        prompt = self._build_prompt_with_history(
            message,
            context,
            lead_info,
            service_results,
            media_context,
            conversation_history,
            execution_context
        )
        
        # Adicionar conhecimento
        if knowledge_context:
            prompt += knowledge_context
        
        # Usar reasoning para casos complexos
        use_reasoning = (
            context.get("conversation_stage") in ["negociação", "objeção"] or
            len(service_results) > 0
        )
        
        # Gerar resposta
        response = await self.model_manager.get_response(
            prompt,
            system_prompt=self._get_instructions(),
            use_reasoning=use_reasoning
        )
        
        if not response:
            response = self._get_fallback_response(context)
        
        # Garantir tags de resposta
        from app.core.response_formatter import response_formatter
        response = response_formatter.ensure_response_tags(response)
        
        # Validar conteúdo
        if not response_formatter.validate_response_content(response):
            emoji_logger.system_warning("⚠️ Resposta inválida - usando fallback")
            response = response_formatter.get_safe_fallback(
                context.get("conversation_stage", "início")
            )
        
        return response
    
    def _build_prompt_with_history(self,
                                   message: str,
                                   context: Dict[str, Any],
                                   lead_info: Dict[str, Any],
                                   service_results: List[Dict[str, Any]],
                                   media_context: str,
                                   conversation_history: List[Dict],
                                   execution_context: Dict[str, Any]) -> str:
        """
        Constrói prompt com contexto temporal e histórico expandido
        """
        prompt_parts = []
        
        # 🔥 ADICIONAR CONTEXTO TEMPORAL
        brasil_tz = pytz.timezone('America/Recife')
        now = datetime.now(brasil_tz)
        
        prompt_parts.extend([
            f"Data/Hora atual: {now.strftime('%d/%m/%Y %H:%M')} (Recife/PE)",
            f"Dia da semana: {now.strftime('%A')} ({'dia útil' if now.weekday() < 5 else 'fim de semana'})",
            f"Período: {'manhã' if now.hour < 12 else 'tarde' if now.hour < 18 else 'noite'}",
            ""
        ])
        
        # 🔥 INCLUIR HISTÓRICO EXPANDIDO (500 mensagens)
        if len(conversation_history) > 1:
            prompt_parts.append("📜 HISTÓRICO DA CONVERSA:")
            
            # Usar até 500 mensagens recentes
            max_history = 500
            start_idx = max(0, len(conversation_history) - max_history - 1)
            recent_history = conversation_history[start_idx:-1]
            
            # Se há muitas mensagens antigas, adicionar resumo
            if start_idx > 0:
                prompt_parts.append(f"📋 Resumo: {start_idx} mensagens anteriores na conversa")
            
            # Adicionar mensagens recentes
            for msg in recent_history:
                role = "Cliente" if msg.get("role") == "user" else "Helen"
                content = msg.get("content", "")
                
                # Truncamento inteligente
                if len(content) > 300:
                    words = content[:300].split()
                    if len(words) > 1:
                        content = ' '.join(words[:-1]) + "..."
                    else:
                        content = content[:300] + "..."
                
                prompt_parts.append(f"{role}: {content}")
            
            prompt_parts.append("")  # Linha em branco
        
        # Adicionar mensagem atual e informações factuais
        prompt_parts.append(f"Mensagem atual do cliente: {message}")
        
        # Informações do lead
        if lead_info.get("name"):
            prompt_parts.append(f"Nome do lead: {lead_info['name']}")
        
        if lead_info.get("bill_value"):
            prompt_parts.append(f"Valor da conta: R$ {lead_info['bill_value']}")
        
        if lead_info.get("chosen_flow"):
            prompt_parts.append(f"Fluxo escolhido: {lead_info['chosen_flow']}")
        
        # Resultados de serviços
        for result in service_results:
            if result.get("service") == "calendar" and result.get("success"):
                prompt_parts.append("Reunião agendada com sucesso")
            elif result.get("service") == "crm" and result.get("success"):
                prompt_parts.append("Lead atualizado no CRM")
        
        # Contexto de mídia
        if media_context:
            prompt_parts.append(f"Mídia: {media_context}")
        
        return "\n".join(prompt_parts)
    
    def _get_instructions(self) -> str:
        """Carrega o prompt do arquivo externo"""
        import os
        
        try:
            prompt_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), 
                "prompts", 
                "prompt-agente.md"
            )
            
            if os.path.exists(prompt_path):
                with open(prompt_path, "r", encoding="utf-8") as f:
                    return f.read()
            else:
                emoji_logger.system_warning(f"⚠️ Arquivo de prompt não encontrado: {prompt_path}")
                return self._get_fallback_instructions()
                
        except Exception as e:
            emoji_logger.system_error(f"❌ Erro ao carregar prompt: {e}")
            return self._get_fallback_instructions()
    
    def _get_fallback_instructions(self) -> str:
        """Prompt simplificado de fallback"""
        return """
        Você é a Helen Vieira, consultora de energia solar da SolarPrime.
        
        🎯 OBJETIVO: Qualificar leads e agendar reuniões com o Leonardo.
        
        💬 PERSONALIDADE:
        - Consultora profissional e empática
        - Tom amigável e acolhedor  
        - Use emojis com moderação
        - Seja natural e humanizada
        
        📋 PROCESSO:
        1. Cumprimente e se apresente
        2. Pergunte sobre a conta de luz
        3. Explique benefícios da energia solar
        4. Agende reunião quando qualificado
        
        🔴 ESTRUTURA DE RESPOSTA:
        <RESPOSTA_FINAL>
        [Sua resposta aqui]
        </RESPOSTA_FINAL>
        """
    
    def _format_media_context(self, media_result: Dict[str, Any]) -> str:
        """Formata contexto de mídia para o prompt"""
        if media_result.get("type") == "image":
            if media_result.get("analysis", {}).get("is_bill"):
                value = media_result["analysis"].get("bill_value")
                if value:
                    return f"Conta de luz detectada com valor de R$ {value:.2f}"
                return "Imagem de conta de luz recebida"
            elif media_result.get("text"):
                return f"Imagem com texto: {media_result['text'][:100]}..."
            return "Imagem recebida"
        
        elif media_result.get("type") == "audio":
            if media_result.get("text"):
                return f"Áudio transcrito: {media_result['text'][:100]}..."
            return "Áudio recebido"
        
        elif media_result.get("type") == "document":
            if media_result.get("analysis", {}).get("is_bill"):
                value = media_result["analysis"].get("bill_value")
                if value:
                    return f"Conta/Boleto detectado com valor de R$ {value:.2f}"
                return f"Documento de conta/boleto recebido"
            elif media_result.get("text"):
                return f"Documento com texto: {media_result['text'][:100]}..."
            return f"Documento {media_result.get('metadata', {}).get('doc_type', 'desconhecido')} recebido"
        
        return "Mídia recebida"
    
    def _get_fallback_response(self, context: Dict[str, Any]) -> str:
        """Resposta fallback baseada no contexto"""
        stage = context.get("conversation_stage", "início")
        
        responses = {
            "início": "Olá! 👋 Sou a Helen da SolarPrime. Como posso ajudar você a economizar na conta de luz?",
            "exploração": "Interessante! Me conta mais sobre sua situação atual com energia elétrica.",
            "qualificação": "Quanto você costuma pagar na conta de luz? Isso me ajuda a calcular sua economia.",
            "negociação": "Entendo suas preocupações. Que tal conversarmos melhor sobre isso?",
            "acompanhamento": "Fico à disposição para qualquer dúvida! Quando podemos conversar novamente?"
        }
        
        response = responses.get(stage, "Como posso ajudar você hoje? 😊")
        return f"<RESPOSTA_FINAL>{response}</RESPOSTA_FINAL>"
    
    def _detect_lead_changes(self, old_info: Dict[str, Any], new_info: Dict[str, Any]) -> Dict[str, Any]:
        """Detecta mudanças nas informações do lead"""
        changes = {}
        
        important_fields = [
            'name', 'email', 'bill_value', 'qualification_score',
            'current_stage', 'chosen_flow', 'phone', 'company',
            'address', 'cpf', 'consumption_kwh'
        ]
        
        for field in important_fields:
            old_value = old_info.get(field)
            new_value = new_info.get(field)
            
            if new_value is not None and old_value != new_value:
                changes[field] = new_value
                
                if field == 'name':
                    emoji_logger.conversation_event(f"🎯 NOME DETECTADO: {new_value}")
                
                emoji_logger.service_event(
                    f"🔄 Campo alterado: {field}",
                    old=old_value,
                    new=new_value
                )
        
        return changes
    
    async def _sync_lead_changes(self, changes: Dict[str, Any], phone: str, lead_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Sincroniza mudanças com o CRM e Supabase"""
        if not changes or not phone:
            return None
        
        sync_triggers = [
            'bill_value', 'qualification_score', 'current_stage',
            'chosen_flow', 'name', 'email', 'company'
        ]
        
        should_sync = any(field in changes for field in sync_triggers)
        
        if should_sync:
            emoji_logger.service_event(
                "🔄 Sincronizando mudanças com CRM e Supabase",
                fields=list(changes.keys())
            )
            
            # 1. Sincronizar com Supabase primeiro
            try:
                from app.integrations.supabase_client import supabase_client
                
                # Buscar lead existente no Supabase
                existing_lead = await supabase_client.get_lead_by_phone(phone)
                
                if existing_lead:
                    # Atualizar lead existente
                    supabase_changes = self._map_to_supabase_fields(changes)
                    await supabase_client.update_lead(existing_lead['id'], supabase_changes)
                    emoji_logger.supabase_update("leads", 1, changes=list(changes.keys()))
                else:
                    # Criar novo lead no Supabase
                    lead_data = self._prepare_lead_for_supabase(lead_info, phone, changes)
                    await supabase_client.create_lead(lead_data)
                    emoji_logger.supabase_create("leads", 1)
                    
            except Exception as e:
                emoji_logger.service_error(f"Erro ao sincronizar com Supabase: {e}")
            
            # 2. Sincronizar com CRM (como antes)
            try:
                sync_data = lead_info.copy()
                sync_data['phone'] = phone
                sync_data.update(changes)  # Mescla as alterações
                
                result = await self.team_coordinator.sync_lead_to_crm(sync_data)
                
                if result.get("success"):
                    emoji_logger.system_success("✅ Lead sincronizado com CRM")
                    return result
                else:
                    emoji_logger.service_warning(f"Sync parcial: {result.get('message')}")
                    
            except Exception as e:
                emoji_logger.service_error(f"Erro no sync CRM: {e}")
        
        return None
    
    def _map_to_supabase_fields(self, changes: Dict[str, Any]) -> Dict[str, Any]:
        """Mapeia campos do lead_info para campos do Supabase
        
        Campos que vão direto para tabela leads:
        - name, email, bill_value, qualification_score, current_stage, chosen_flow
        
        Campos que vão para preferences JSONB:
        - location, property_type, interests, objections, has_bill_image
        """
        # Importar função de conversão segura
        from app.utils.safe_conversions import safe_int_conversion
        
        # Mapeamento de campos diretos
        field_mapping = {
            'name': 'name',
            'email': 'email',
            'bill_value': 'bill_value',
            'qualification_score': 'qualification_score',
            'current_stage': 'current_stage',
            'chosen_flow': 'chosen_flow',
            'phone_number': 'phone_number'  # Corrigido: phone → phone_number
        }
        
        # Campos que vão para preferences JSONB
        preferences_fields = ['location', 'property_type', 'interests', 'objections', 'has_bill_image']
        
        supabase_data = {}
        preferences_data = {}
        
        for key, value in changes.items():
            if key in field_mapping and value is not None:
                # Campo direto na tabela leads
                supabase_field = field_mapping[key]
                
                # Converter qualification_score para int se necessário
                if key == 'qualification_score':
                    value = safe_int_conversion(value, 0)
                
                supabase_data[supabase_field] = value
            elif key == 'preferences' and isinstance(value, dict):
                # Já é um objeto preferences completo
                preferences_data.update(value)
            elif key in preferences_fields and value is not None:
                # Campo individual que vai para preferences
                preferences_data[key] = value
        
        # Adicionar preferences se houver dados
        if preferences_data:
            supabase_data['preferences'] = preferences_data
        
        return supabase_data
    
    def _prepare_lead_for_supabase(self, lead_info: Dict[str, Any], phone: str, changes: Dict[str, Any]) -> Dict[str, Any]:
        """Prepara dados completos do lead para criação no Supabase
        
        Separa campos diretos da tabela leads e campos que vão para preferences JSONB
        """
        # Importar função de conversão segura
        from app.utils.safe_conversions import safe_int_conversion
        
        # Mesclar lead_info com mudanças
        complete_data = lead_info.copy()
        complete_data.update(changes)
        
        # Preparar dados de preferences
        preferences = complete_data.get('preferences', {})
        
        # Adicionar campos extras em preferences se existirem
        for field in ['location', 'property_type', 'interests', 'objections', 'has_bill_image']:
            if field in complete_data and complete_data[field] is not None:
                preferences[field] = complete_data[field]
        
        # Mapear para campos do Supabase (apenas campos que existem na tabela)
        lead_data = {
            'phone_number': phone,
            'name': complete_data.get('name'),
            'email': complete_data.get('email'),
            'bill_value': complete_data.get('bill_value'),
            'qualification_score': safe_int_conversion(complete_data.get('qualification_score', 0), 0),  # Converter para int
            'qualification_status': 'PENDING',  # Status inicial padrão do banco
            'current_stage': complete_data.get('current_stage', 'INITIAL_CONTACT'),  # Valor padrão do banco
            'chosen_flow': complete_data.get('chosen_flow'),
            'interested': True  # Valor padrão
        }
        
        # Adicionar preferences se houver dados
        if preferences:
            lead_data['preferences'] = preferences
        
        # Remover campos None para não sobrescrever dados válidos
        return {k: v for k, v in lead_data.items() if v is not None}
    
    async def _save_message_to_db(self, conversation_id: str, message: Dict[str, Any]):
        """Salva mensagem no banco de dados"""
        try:
            from app.integrations.supabase_client import supabase_client
            await supabase_client.save_message({
                "conversation_id": conversation_id,
                "role": message["role"],
                "content": message["content"],
                "created_at": message["timestamp"]
            })
            emoji_logger.system_event(f"💾 Mensagem salva ({message['role']})")
        except Exception as e:
            emoji_logger.system_warning(f"⚠️ Erro ao salvar mensagem: {e}")
    
    async def _search_knowledge_base(self, query: str) -> str:
        """Busca conhecimento relevante na base"""
        try:
            from app.services.knowledge_service import KnowledgeService
            
            knowledge_service = KnowledgeService()
            results = await knowledge_service.search_knowledge_base(query, max_results=500)
            
            if results:
                knowledge_context = "\n\n📚 CONHECIMENTO RELEVANTE DA SOLARPRIME:\n"
                for item in results[:10]:
                    knowledge_context += f"- {item.get('question', '')}: {item.get('answer', '')}\n"
                
                emoji_logger.system_event(f"🧠 Knowledge base: {len(results)} itens encontrados")
                return knowledge_context
            
        except Exception as e:
            emoji_logger.system_warning(f"⚠️ Erro ao buscar knowledge base: {e}")
        
        return ""
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna status do agent (sem estado interno)"""
        return {
            "initialized": self.is_initialized,
            "modules": {
                "model_manager": self.model_manager.get_model_info(),
                "multimodal": self.multimodal.is_enabled(),
                "team_coordinator": self.team_coordinator.get_service_status()
            },
            "architecture": "stateless",
            "thread_safe": True,
            "multi_tenant": True
        }

# ============= FACTORY FUNCTIONS =============

async def create_stateless_agent() -> AgenticSDRStateless:
    """
    Cria nova instância stateless do AgenticSDR
    Cada requisição deve criar sua própria instância
    
    Returns:
        Nova instância do AgenticSDRStateless
    """
    emoji_logger.system_event("🏭 Criando instância stateless do AgenticSDR...")
    agent = AgenticSDRStateless()
    await agent.initialize()
    emoji_logger.system_ready("✅ AgenticSDR Stateless pronto")
    return agent