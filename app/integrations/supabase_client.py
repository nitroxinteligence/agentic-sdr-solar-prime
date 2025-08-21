"""
Cliente Supabase para o SDR IA SolarPrime
Gerencia todas as operações com o banco de dados
"""
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from uuid import UUID, uuid4

from supabase import create_client, Client
from loguru import logger
from app.utils.logger import emoji_logger
import asyncio

from app.config import settings


class SupabaseClient:
    """Cliente para interação com Supabase"""
    
    def __init__(self):
        """Inicializa o cliente Supabase"""
        self.client: Client = create_client(
            supabase_url=settings.supabase_url,
            supabase_key=settings.supabase_service_key
        )
        # Cliente inicializado (sem logs repetitivos)
    
    async def test_connection(self) -> bool:
        """Testa conexão com o Supabase"""
        try:
            # Tenta fazer uma query simples
            result = self.client.table('leads').select("id").limit(1).execute()
            # Conexão OK (sem log)
            return True
        except Exception as e:
            logger.error(f"Erro de conexão Supabase: {str(e)}")
            return False
    
    # ============= LEADS =============
    
    async def create_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria um novo lead"""
        try:
            # Adiciona timestamps
            lead_data['created_at'] = datetime.now().isoformat()
            lead_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('leads').insert(lead_data).execute()
            
            if result.data:
                # Lead criado com sucesso
                return result.data[0]
            
            raise Exception("Erro ao criar lead")
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao criar lead: {str(e)}", table="leads")
            raise
    
    async def get_lead_by_phone(self, phone: str) -> Optional[Dict[str, Any]]:
        """Busca lead por telefone"""
        try:
            result = self.client.table('leads').select("*").eq('phone_number', phone).execute()
            
            if result.data:
                return result.data[0]
            
            return None
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao buscar lead: {str(e)}", table="leads")
            return None
    
    async def update_lead(self, lead_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza dados do lead"""
        try:
            update_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('leads').update(update_data).eq('id', lead_id).execute()
            
            if result.data:
                # Lead atualizado com sucesso
                return result.data[0]
            
            raise Exception("Erro ao atualizar lead")
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao atualizar lead: {str(e)}", table="leads")
            raise
    
    async def get_qualified_leads(self) -> List[Dict[str, Any]]:
        """Retorna leads qualificados"""
        try:
            result = self.client.table('leads').select("*").eq(
                'qualification_status', 'QUALIFIED'
            ).execute()
            
            return result.data or []
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao buscar leads qualificados: {str(e)}", table="leads")
            return []
    
    # ============= CONVERSATIONS =============
    
    async def get_or_create_conversation(self, phone: str, lead_id: Optional[str] = None) -> Dict[str, Any]:
        """Busca ou cria uma conversa para o telefone"""
        try:
            # Primeiro tenta buscar conversa existente
            conversation = await self.get_conversation_by_phone(phone)
            
            if conversation:
                return conversation
            
            # Se não existe, cria nova
            return await self.create_conversation(phone, lead_id)
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao obter/criar conversa: {str(e)}", table="conversations")
            raise
    
    async def create_conversation(self, phone: str, lead_id: Optional[str] = None) -> Dict[str, Any]:
        """Cria uma nova conversa"""
        try:
            # Gerar session_id único para a conversa
            session_id = f"session_{uuid4().hex}"
            
            conversation_data = {
                'phone_number': phone,
                'lead_id': lead_id,
                'session_id': session_id,  # Campo obrigatório
                'status': 'ACTIVE',
                # Campos removidos na otimização do schema:
                # 'channel': 'whatsapp',  # Removido - campo não existe mais
                # 'sentiment': 'neutro',   # Removido - campo não existe mais
                'is_active': True,
                'total_messages': 0,
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            
            result = self.client.table('conversations').insert(conversation_data).execute()
            
            if result.data:
                # Conversa criada com sucesso
                return result.data[0]
            
            raise Exception("Erro ao criar conversa")
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao criar conversa: {str(e)}", table="conversations")
            raise
    
    async def get_conversation_by_phone(self, phone: str) -> Optional[Dict[str, Any]]:
        """Busca conversa por telefone"""
        try:
            result = self.client.table('conversations').select("*").eq(
                'phone_number', phone
            ).execute()
            
            if result.data:
                return result.data[0]
            
            return None
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao buscar conversa: {str(e)}", table="conversations")
            return None
    
    async def update_conversation(self, conversation_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza dados da conversa"""
        try:
            update_data['updated_at'] = datetime.now().isoformat()
            # Removido last_message_at que não existe na tabela
            
            result = self.client.table('conversations').update(update_data).eq(
                'id', conversation_id
            ).execute()
            
            if result.data:
                return result.data[0]
            
            raise Exception("Erro ao atualizar conversa")
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao atualizar conversa: {str(e)}", table="conversations")
            raise
    
    async def get_conversation_by_phone(self, phone: str) -> Optional[Dict[str, Any]]:
        """
        Busca dados da conversa por número de telefone
        
        Args:
            phone: Número de telefone do lead
            
        Returns:
            Dict com dados da conversa ou None se não encontrado
        """
        try:
            # Buscar lead pelo telefone
            lead_result = self.client.table('leads').select('id').eq('phone_number', phone).execute()
            
            if not lead_result.data:
                return None
                
            lead_id = lead_result.data[0]['id']
            
            # Buscar conversa associada ao lead
            conversation_result = self.client.table('conversations').select(
                'id, messages, emotional_state, current_stage, qualification_score, created_at, updated_at'
            ).eq('lead_id', lead_id).execute()
            
            if conversation_result.data:
                return conversation_result.data[0]
                
            return None
            
        except Exception as e:
            logger.error(f"Erro ao buscar conversa por telefone {phone}: {str(e)}")
            return None
    
    async def get_conversation_emotional_state(self, conversation_id: str) -> str:
        """
        Obtém estado emocional atual da conversa
        """
        try:
            result = self.client.table('conversations').select('emotional_state').eq(
                'id', conversation_id
            ).execute()
            
            if result.data:
                return result.data[0].get('emotional_state', 'neutro')
            
            return 'neutro'
            
        except Exception as e:
            logger.error(f"Erro ao obter estado emocional: {str(e)}")
            return 'neutro'
    
    async def update_conversation_emotional_state(self, conversation_id: str, emotional_state: str) -> None:
        """Atualiza o estado emocional da conversa com validação"""
        try:
            # Validar estado antes de salvar
            valid_states = ['ENTUSIASMADA', 'CURIOSA', 'CONFIANTE', 'DUVIDOSA', 'NEUTRA']
            
            if emotional_state not in valid_states:
                emoji_logger.system_warning(
                    f"Estado emocional inválido: {emotional_state}, usando NEUTRA como fallback"
                )
                emotional_state = 'NEUTRA'
            
            await self.update_conversation(
                conversation_id,
                {'emotional_state': emotional_state}
            )
            emoji_logger.system_debug(f"Estado emocional atualizado para: {emotional_state}")
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao atualizar estado emocional: {str(e)}", table="conversations")
    
    # ============= MESSAGES =============
    
    async def save_message(self, message_data: Dict[str, Any]) -> Dict[str, Any]:
        """Salva mensagem no banco"""
        try:
            message_data['created_at'] = datetime.now().isoformat()
            
            result = self.client.table('messages').insert(message_data).execute()
            
            if result.data:
                # Incrementa contador de mensagens na conversa
                if message_data.get('conversation_id'):
                    await self._increment_message_count(message_data['conversation_id'])
                
                return result.data[0]
            
            raise Exception("Erro ao salvar mensagem")
            
        except Exception as e:
            emoji_logger.supabase_error(f"Erro ao salvar mensagem: {str(e)}", table="messages")
            raise
    
    async def get_conversation_messages(
        self,
        conversation_id: str,
        limit: int = 200  # 🔥 CORREÇÃO: Aumentar para 200 mensagens
    ) -> List[Dict[str, Any]]:
        """Retorna mensagens de uma conversa com contexto expandido"""
        try:
            # 🔥 MELHORIA: Buscar mensagens mais recentes primeiro, depois reverter
            result = self.client.table('messages').select("*").eq(
                'conversation_id', conversation_id
            ).order('created_at', desc=True).limit(limit).execute()
            
            # Reverter para ordem cronológica após buscar
            if result.data:
                result.data.reverse()
            
            return result.data or []
            
        except Exception as e:
            logger.error(f"Erro ao buscar mensagens: {str(e)}")
            return []
    
    async def _increment_message_count(self, conversation_id: str):
        """Incrementa contador de mensagens na conversa"""
        try:
            # Busca conversa atual
            conv = self.client.table('conversations').select("total_messages").eq(
                'id', conversation_id
            ).execute()
            
            if conv.data:
                current_count = conv.data[0].get('total_messages', 0)
                
                # Atualiza contador
                self.client.table('conversations').update({
                    'total_messages': current_count + 1,
                    'updated_at': datetime.now().isoformat()  # Usar updated_at em vez de last_message_at
                }).eq('id', conversation_id).execute()
                
        except Exception as e:
            logger.error(f"Erro ao incrementar contador: {str(e)}")
    
    # ============= FOLLOW-UPS =============
    
    async def create_follow_up(self, follow_up_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria um follow-up"""
        try:
            follow_up_data['created_at'] = datetime.now().isoformat()
            follow_up_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('follow_ups').insert(follow_up_data).execute()
            
            if result.data:
                logger.info(f"Follow-up criado: {result.data[0]['id']}")
                return result.data[0]
            
            raise Exception("Erro ao criar follow-up")
            
        except Exception as e:
            logger.error(f"Erro ao criar follow-up: {str(e)}")
            raise
    
    async def get_pending_follow_ups(self) -> List[Dict[str, Any]]:
        """Retorna follow-ups pendentes"""
        try:
            now = datetime.now().isoformat()
            
            result = self.client.table('follow_ups').select("*").eq(
                'status', 'pending'
            ).lte('scheduled_at', now).order('priority', desc=True).execute()
            
            return result.data or []
            
        except Exception as e:
            logger.error(f"Erro ao buscar follow-ups: {str(e)}")
            return []
    
    async def update_follow_up_status(
        self,
        follow_up_id: str,
        status: str,
        executed_at: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Atualiza status do follow-up"""
        try:
            update_data = {
                'status': status,
                'updated_at': datetime.now().isoformat()
            }
            
            if executed_at:
                update_data['executed_at'] = executed_at.isoformat()
            
            result = self.client.table('follow_ups').update(update_data).eq(
                'id', follow_up_id
            ).execute()
            
            if result.data:
                return result.data[0]
            
            raise Exception("Erro ao atualizar follow-up")
            
        except Exception as e:
            logger.error(f"Erro ao atualizar follow-up: {str(e)}")
            raise
    
    async def update_follow_up_status_with_compensation(
        self,
        follow_up_id: str,
        status: str,
        executed_at: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Atualiza status do follow-up com mecanismo de compensação
        
        Args:
            follow_up_id: ID do follow-up
            status: Novo status
            executed_at: Data de execução
            
        Returns:
            Dict com resultado da operação
        """
        try:
            # Armazenar status original para possível rollback
            original_status = None
            original_executed_at = None
            
            # Buscar dados atuais do follow-up para possível rollback
            try:
                current_follow_up = self.client.table('follow_ups').select('*').eq(
                    'id', follow_up_id
                ).execute()
                
                if current_follow_up.data:
                    original_status = current_follow_up.data[0].get('status')
                    original_executed_at = current_follow_up.data[0].get('executed_at')
            except Exception as e:
                logger.warning(f"Aviso: Não foi possível obter status original do follow-up {follow_up_id}: {e}")
            
            # Atualizar status do follow-up
            update_data = {
                'status': status,
                'updated_at': datetime.now().isoformat()
            }
            
            if executed_at:
                update_data['executed_at'] = executed_at.isoformat()
            
            result = self.client.table('follow_ups').update(update_data).eq(
                'id', follow_up_id
            ).execute()
            
            if result.data:
                return {
                    "success": True,
                    "data": result.data[0],
                    "message": "Follow-up atualizado com sucesso",
                    "follow_up_id": follow_up_id,
                    "original_status": original_status,
                    "new_status": status
                }
            
            return {
                "success": False,
                "message": "Erro ao atualizar follow-up",
                "follow_up_id": follow_up_id
            }
            
        except Exception as e:
            logger.error(f"Erro ao atualizar follow-up {follow_up_id} com compensação: {str(e)}")
            return {
                "success": False,
                "message": f"Erro ao atualizar follow-up: {e}",
                "follow_up_id": follow_up_id
            }
    
    async def _rollback_follow_up_status(
        self,
        follow_up_id: str,
        original_status: str,
        original_executed_at: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Realiza rollback do status de um follow-up
        
        Args:
            follow_up_id: ID do follow-up
            original_status: Status original
            original_executed_at: Data de execução original
            
        Returns:
            Dict com resultado da operação de rollback
        """
        try:
            # Preparar dados de rollback
            rollback_data = {
                'status': original_status,
                'updated_at': datetime.now().isoformat()
            }
            
            if original_executed_at:
                rollback_data['executed_at'] = original_executed_at
            
            # Reverter status no banco
            result = self.client.table('follow_ups').update(rollback_data).eq(
                'id', follow_up_id
            ).execute()
            
            if result.data:
                return {
                    "success": True,
                    "message": "Rollback de status realizado com sucesso"
                }
            
            return {
                "success": False,
                "message": "Erro ao realizar rollback de status"
            }
            
        except Exception as e:
            logger.error(f"Erro ao realizar rollback do follow-up {follow_up_id}: {str(e)}")
            return {
                "success": False,
                "message": f"Erro no rollback: {e}"
            }
    
    # ============= KNOWLEDGE BASE =============
    
    async def apply_database_indexes(self):
        """
        Apply database indexes for improved query performance
        """
        try:
            # Index creation queries
            index_queries = [
                # Index on follow_ups.scheduled_at for faster retrieval of pending follow-ups
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_scheduled_at 
                ON follow_ups (scheduled_at);
                """,
                
                # Composite index on follow_ups.status and follow_ups.scheduled_at 
                # for efficient querying of pending follow-ups
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_status_scheduled_at 
                ON follow_ups (status, scheduled_at);
                """,
                
                # Index on follow_ups.lead_id for faster lookup of follow-ups by lead
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_lead_id 
                ON follow_ups (lead_id);
                """,
                
                # Index on leads.phone_number for faster lookup of leads by phone
                """
                CREATE INDEX IF NOT EXISTS idx_leads_phone_number 
                ON leads (phone_number);
                """,
                
                # Index on leads_qualifications.lead_id for faster lookup of qualifications by lead
                """
                CREATE INDEX IF NOT EXISTS idx_leads_qualifications_lead_id 
                ON leads_qualifications (lead_id);
                """,
                
                # Index on conversations.lead_id for faster lookup of conversations by lead
                """
                CREATE INDEX IF NOT EXISTS idx_conversations_lead_id 
                ON conversations (lead_id);
                """,
                
                # Index on conversations.updated_at for faster lookup of recent conversations
                """
                CREATE INDEX IF NOT EXISTS idx_conversations_updated_at 
                ON conversations (updated_at);
                """
            ]
            
            # Apply each index creation query
            for i, query in enumerate(index_queries, 1):
                try:
                    # Execute the raw SQL query
                    self.client.execute_sql(query)
                    logger.info(f"✅ Database index {i}/{len(index_queries)} applied successfully")
                except Exception as e:
                    logger.warning(f"⚠️ Failed to apply database index {i}: {e}")
                    # Continue with other indexes even if one fails
                    continue
            
            logger.info("🎉 All database indexes applied successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to apply database indexes: {e}")
            return False
    
    async def add_knowledge(self, knowledge_data: Dict[str, Any]) -> Dict[str, Any]:
        """Adiciona item à base de conhecimento"""
        try:
            knowledge_data['created_at'] = datetime.now().isoformat()
            knowledge_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('knowledge_base').insert(knowledge_data).execute()
            
            if result.data:
                logger.info(f"Conhecimento adicionado: {result.data[0]['id']}")
                return result.data[0]
            
            raise Exception("Erro ao adicionar conhecimento")
            
        except Exception as e:
            logger.error(f"Erro ao adicionar conhecimento: {str(e)}")
            raise
    
    # ============= ANALYTICS =============
    
    async def log_event(self, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Registra evento de analytics"""
        try:
            event_data['timestamp'] = datetime.now().isoformat()
            event_data['created_at'] = datetime.now().isoformat()
            
            result = self.client.table('analytics').insert(event_data).execute()
            
            if result.data:
                return result.data[0]
            
            raise Exception("Erro ao registrar evento")
            
        except Exception as e:
            logger.error(f"Erro ao registrar evento: {str(e)}")
            raise
    
    async def get_daily_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas do dia"""
        try:
            today_start = datetime.now().replace(hour=0, minute=0, second=0).isoformat()
            
            # Total de leads do dia
            leads = self.client.table('leads').select("id", count='exact').gte(
                'created_at', today_start
            ).execute()
            
            # Leads qualificados do dia
            qualified = self.client.table('leads').select("id", count='exact').gte(
                'created_at', today_start
            ).eq('qualification_status', 'QUALIFIED').execute()
            
            # Conversas ativas
            active_convs = self.client.table('conversations').select("id", count='exact').eq(
                'status', 'ACTIVE'
            ).execute()
            
            # Reuniões agendadas hoje - campo agora está em leads_qualifications
            meetings = self.client.table('leads_qualifications').select("id", count='exact').gte(
                'meeting_scheduled_at', today_start
            ).execute()
            
            return {
                'date': datetime.now().date().isoformat(),
                'total_leads': leads.count if leads else 0,
                'qualified_leads': qualified.count if qualified else 0,
                'active_conversations': active_convs.count if active_convs else 0,
                'meetings_scheduled': meetings.count if meetings else 0
            }
            
        except Exception as e:
            logger.error(f"Erro ao obter estatísticas: {str(e)}")
            return {
                'date': datetime.now().date().isoformat(),
                'total_leads': 0,
                'qualified_leads': 0,
                'active_conversations': 0,
                'meetings_scheduled': 0
            }
    
    # ============= SESSION MANAGEMENT =============
    
    # NOTA: Métodos agent_sessions removidos - arquitetura agora é stateless
    # A tabela agent_sessions foi removida no schema otimizado
    # Mantemos o sistema 100% stateless conforme design v0.3
    
    # ============= LEAD QUALIFICATIONS =============
    
    async def create_lead_qualification(self, qualification_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria uma qualificação de lead quando uma reunião é agendada
        
        Args:
            qualification_data: Dados da qualificação incluindo:
                - lead_id: ID do lead (obrigatório)
                - qualification_status: Status (default: 'QUALIFIED')
                - score: Pontuação de 0-100 (default: 80 para reunião agendada)
                - criteria: Critérios em formato JSON
                - notes: Notas sobre a qualificação
                
        Returns:
            Dados da qualificação criada
        """
        try:
            # Valores padrão para reunião agendada
            if 'qualification_status' not in qualification_data:
                qualification_data['qualification_status'] = 'QUALIFIED'
            
            if 'score' not in qualification_data:
                qualification_data['score'] = 80  # Score alto por ter agendado reunião
            
            if 'criteria' not in qualification_data:
                qualification_data['criteria'] = {
                    'meeting_scheduled': True,
                    'interest_level': 'high',
                    'decision_maker': True
                }
            
            if 'notes' not in qualification_data:
                qualification_data['notes'] = 'Lead qualificado - Reunião agendada com sucesso'
            
            # Adicionar timestamps
            qualification_data['qualified_at'] = datetime.now().isoformat()
            qualification_data['created_at'] = datetime.now().isoformat()
            qualification_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('leads_qualifications').insert(qualification_data).execute()
            
            if result.data:
                logger.info(f"✅ Qualificação criada para lead {qualification_data['lead_id']}")
                return result.data[0]
            
            raise Exception("Erro ao criar qualificação")
            
        except Exception as e:
            logger.error(f"Erro ao criar qualificação: {str(e)}")
            raise
    
    async def close(self):
        """Fecha conexão com Supabase"""
        # Supabase client não precisa de close explícito
        # Cliente encerrado
    
    async def test_connection(self) -> bool:
        """Testa a conexão com o Supabase"""
        try:
            # Faz uma query simples para testar
            response = self.client.table("leads").select("id").limit(1).execute()
            return True
        except Exception as e:
            logger.error(f"Erro ao testar conexão com Supabase: {e}")
            return False
    
    async def save_qualification(self, qualification_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Salva resultado de qualificação"""
        try:
            # Adicionar timestamps
            qualification_data['created_at'] = datetime.now().isoformat()
            qualification_data['updated_at'] = datetime.now().isoformat()
            
            result = self.client.table('leads_qualifications').insert(qualification_data).execute()
            
            if result.data:
                logger.info(f"✅ Qualificação salva para lead {qualification_data['lead_id']}")
                return result.data[0]
            
            raise Exception("Erro ao salvar qualificação")
            
        except Exception as e:
            logger.error(f"Erro ao salvar qualificação: {str(e)}")
            raise
    
    async def apply_database_indexes(self):
        """
        Apply database indexes for improved query performance
        """
        try:
            # Index creation queries
            index_queries = [
                # Index on follow_ups.scheduled_at for faster retrieval of pending follow-ups
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_scheduled_at 
                ON follow_ups (scheduled_at);
                """,
                
                # Composite index on follow_ups.status and follow_ups.scheduled_at 
                # for efficient querying of pending follow-ups
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_status_scheduled_at 
                ON follow_ups (status, scheduled_at);
                """,
                
                # Index on follow_ups.lead_id for faster lookup of follow-ups by lead
                """
                CREATE INDEX IF NOT EXISTS idx_follow_ups_lead_id 
                ON follow_ups (lead_id);
                """,
                
                # Index on leads.phone_number for faster lookup of leads by phone
                """
                CREATE INDEX IF NOT EXISTS idx_leads_phone_number 
                ON leads (phone_number);
                """,
                
                # Index on leads_qualifications.lead_id for faster lookup of qualifications by lead
                """
                CREATE INDEX IF NOT EXISTS idx_leads_qualifications_lead_id 
                ON leads_qualifications (lead_id);
                """,
                
                # Index on conversations.lead_id for faster lookup of conversations by lead
                """
                CREATE INDEX IF NOT EXISTS idx_conversations_lead_id 
                ON conversations (lead_id);
                """,
                
                # Index on conversations.updated_at for faster lookup of recent conversations
                """
                CREATE INDEX IF NOT EXISTS idx_conversations_updated_at 
                ON conversations (updated_at);
                """
            ]
            
            # Apply each index creation query
            for i, query in enumerate(index_queries, 1):
                try:
                    # Execute the raw SQL query
                    self.client.execute_sql(query)
                    logger.info(f"✅ Database index {i}/{len(index_queries)} applied successfully")
                except Exception as e:
                    logger.warning(f"⚠️ Failed to apply database index {i}: {e}")
                    # Continue with other indexes even if one fails
                    continue
            
            logger.info("🎉 All database indexes applied successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to apply database indexes: {e}")
            return False
    
    async def get_latest_qualification(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Obtém última qualificação do lead"""
        try:
            response = self.client.table("leads_qualifications")\
                .select("*")\
                .eq("lead_id", lead_id)\
                .order("created_at", desc=True)\
                .limit(1)\
                .execute()
            
            if response.data:
                return response.data[0]
            return None
            
        except Exception as e:
            logger.error(f"Erro ao obter qualificação: {e}")
            return None
    
    async def get_lead_by_id(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Busca lead por ID"""
        try:
            response = self.client.table("leads").select("*").eq("id", lead_id).execute()
            
            if response.data:
                return response.data[0]
            return None
            
        except Exception as e:
            logger.error(f"Erro ao buscar lead por ID: {e}")
            return None

    async def get_recent_followup_count(self, lead_id: str, since: datetime) -> int:
        """Conta o número de follow-ups enviados a um lead desde uma data específica."""
        try:
            result = self.client.table('follow_ups').select('id', count='exact').eq('lead_id', lead_id).gte('created_at', since.isoformat()).execute()
            return result.count
        except Exception as e:
            logger.error(f"Erro ao contar follow-ups recentes para o lead {lead_id}: {e}")
            return 0

    async def apply_database_indexes(self):
        """
        Apply database indexes for improved query performance
        """
        try:
            # Since we can't execute raw SQL directly, we'll log the recommended indexes
            # These should be created manually in the Supabase dashboard or via migration
            
            recommended_indexes = [
                "CREATE INDEX IF NOT EXISTS idx_follow_ups_scheduled_at ON follow_ups (scheduled_at);",
                "CREATE INDEX IF NOT EXISTS idx_follow_ups_status_scheduled_at ON follow_ups (status, scheduled_at);",
                "CREATE INDEX IF NOT EXISTS idx_follow_ups_lead_id ON follow_ups (lead_id);",
                "CREATE INDEX IF NOT EXISTS idx_leads_phone_number ON leads (phone_number);",
                "CREATE INDEX IF NOT EXISTS idx_leads_qualifications_lead_id ON leads_qualifications (lead_id);",
                "CREATE INDEX IF NOT EXISTS idx_conversations_lead_id ON conversations (lead_id);",
                "CREATE INDEX IF NOT EXISTS idx_conversations_updated_at ON conversations (updated_at);"
            ]
            
            logger.info("📋 Recommended database indexes (should be created manually in Supabase):")
            for i, index_sql in enumerate(recommended_indexes, 1):
                logger.info(f"  {i}. {index_sql}")
            
            logger.info("🎉 Database index recommendations logged successfully!")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to generate database index recommendations: {e}")
            return False


# Singleton global
supabase_client = SupabaseClient()