"""
CRM Service 100% REAL - Kommo API
ZERO simulação, MÁXIMA simplicidade
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
import asyncio
import aiohttp
import json
import random
from functools import wraps
from app.utils.logger import emoji_logger
from app.config import settings
from app.services.rate_limiter import wait_for_kommo

def async_retry_with_backoff(max_retries: int = 3, initial_delay: float = 1.0, max_delay: float = 30.0, backoff_factor: float = 2.0):
    """
    Decorator para retry assíncrono com backoff exponencial
    ZERO complexidade, MÁXIMA resiliência
    
    Args:
        max_retries: Número máximo de tentativas
        initial_delay: Delay inicial em segundos
        max_delay: Delay máximo em segundos
        backoff_factor: Fator de multiplicação do delay
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            delay = initial_delay
            
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        # Adiciona jitter para evitar thundering herd
                        jitter = random.uniform(0, delay * 0.1)
                        sleep_time = min(delay + jitter, max_delay)
                        
                        emoji_logger.service_warning(
                            f"Tentativa {attempt + 1}/{max_retries} falhou: {e}. Aguardando {sleep_time:.1f}s..."
                        )
                        await asyncio.sleep(sleep_time)
                        delay = min(delay * backoff_factor, max_delay)
                    else:
                        emoji_logger.service_error(f"Todas as {max_retries} tentativas falharam: {e}")
                except Exception as e:
                    # Para outros erros, não fazer retry
                    raise e
            
            # Se chegou aqui, todas as tentativas falharam
            if last_exception:
                raise last_exception
        
        return wrapper
    return decorator

class CRMServiceReal:
    """
    Serviço REAL de CRM - Kommo API
    SIMPLES e FUNCIONAL - 100% real
    """
    
    def __init__(self):
        self.is_initialized = False
        self.base_url = settings.kommo_base_url or "https://leonardofvieira00.kommo.com"
        self.access_token = settings.kommo_long_lived_token
        self.pipeline_id = int(settings.kommo_pipeline_id or 11672895)  # Garantir que é int
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        self.session = None
        self._session_timeout = aiohttp.ClientTimeout(total=30)  # 30s timeout
        
        # Cache SIMPLES de estágios (evita buscar toda vez)
        self._stages_cache = None
        self._cache_ttl = 3600  # 1 hora de cache
        self._cache_timestamp = None
        
        # IDs dos campos customizados VALIDADOS e TESTADOS (2025-08-13)
        # Todos os campos abaixo foram testados e validados na API do Kommo
        self.custom_fields = {
            # ===== CAMPOS VALIDADOS E FUNCIONAIS =====
            "phone": 392802,          # WhatsApp (text) ✅ TESTADO
            "whatsapp": 392802,       # Alias para phone ✅ TESTADO
            "bill_value": 392804,     # Valor Conta Energia (numeric) ✅ TESTADO
            "valor_conta": 392804,    # Alias para bill_value ✅ TESTADO
            "solution_type": 392808,  # Solução Solar (select) ✅ TESTADO
            "solucao_solar": 392808,  # Alias para solution_type ✅ TESTADO
            "calendar_link": 395520,  # Link do evento no Google Calendar (url) ✅ TESTADO
            "google_calendar": 395520, # Alias para calendar_link ✅ TESTADO
            
            # ===== CAMPOS DE OUTRAS ENTIDADES (NÃO USAR EM LEADS) =====
            # "location": 152429,     # Endereço (textarea) - COMPANIES apenas, não LEADS
            
            # ===== CAMPOS REMOVIDOS (CAUSAVAM ERRO OU NÃO EXISTEM) =====
            # "conversation_id": 392860,  # Removido por conflitos
            # "score": None,              # Removido - causava erro 400
            # "email": None,              # Não existe campo email customizado em LEADS
            # "property_type": None,      # Não existe campo tipo de propriedade
            "conversation_id": 392860     # Mantendo para compatibilidade
        }
        
        # Mapeamento UNIFICADO de estágios para IDs do Kommo
        # Aceita tanto chaves em inglês quanto português
        self.stage_map = {
            # QUALIFICAÇÃO
            "QUALIFICATION": 89709589,
            "QUALIFICACAO": 89709589,
            "QUALIFICADO": 89709589,
            "QUALIFIED": 89709589,
            
            # AGENDAMENTO
            "SCHEDULE": 89709591,
            "AGENDAMENTO": 89709591,
            "MEETING_SCHEDULED": 89709595,
            "REUNIAO_AGENDADA": 89709595,
            "REUNIÃO AGENDADA": 89709595,
            
            # EM NEGOCIAÇÃO
            "NEGOTIATION": 89709593,
            "NEGOCIACAO": 89709593,
            "EM_NEGOCIACAO": 89709593,
            "EM NEGOCIAÇÃO": 89709593,
            
            # FECHADO
            "CLOSED": 89709597,
            "FECHADO": 89709597,
            "CONVERTED": 89709597,
            "CONVERTIDO": 89709597,
            
            # NÃO INTERESSADO
            "NOT_INTERESTED": 89709599,
            "NAO_INTERESSADO": 89709599,
            "NÃO INTERESSADO": 89709599,
            
            # ATENDIMENTO HUMANO
            "HUMAN_HANDOFF": 90421387,
            "ATENDIMENTO_HUMANO": 90421387,
        }
        
        # Mapeamento de valores do campo SELECT "Solução Solar" (ID: 392808)
        # IMPORTANTE: Usar enum_id, não o texto!
        # Valores REAIS validados em 13/08/2025 via API Kommo
        self.solution_type_values = {
            "usina própria": 326358,
            "usina propria": 326358,
            "fazenda solar": 326360,
            "consórcio": 326362,
            "consorcio": 326362,
            "consultoria": 326364,
            "não definido": 326366,
            "nao definido": 326366,
            "aluguel de lote": 1078618,  # ID correto do Kommo
            "compra com desconto": 1078620,  # ID correto do Kommo
            "usina investimento": 1078622  # ID correto do Kommo
        }
        
        # Opções do campo solution_type (select) - VALIDADAS
        self.solution_type_options = {
            "Usina Própria": 326358,
            "Fazenda Solar": 326360,
            "Consórcio": 326362,
            "Consultoria": 326364,
            "Não Definido": 326366,
            "Aluguel de Lote": 1078618,
            "Compra com Desconto": 1078620,
            "Usina Investimento": 1078622
        }
        
    async def initialize(self):
        """Inicializa conexão REAL com Kommo CRM e busca IDs dinamicamente"""
        if self.is_initialized:
            return
        
        try:
            # 🔧 Criar sessão HTTP com timeout e connector configurado
            connector = aiohttp.TCPConnector(
                limit=10,  # Max 10 conexões simultâneas
                limit_per_host=5,  # Max 5 por host
                ttl_dns_cache=300,  # Cache DNS por 5min
                use_dns_cache=True,
            )
            
            self.session = aiohttp.ClientSession(
                connector=connector,
                timeout=self._session_timeout
            )
            
            # Testar conexão com a API
            # Aplicar rate limiting antes da requisição
            await wait_for_kommo()
            
            async with self.session.get(
                f"{self.base_url}/api/v4/account",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    account = await response.json()
                    emoji_logger.service_ready(
                        f"✅ Kommo CRM conectado: {account.get('name', 'CRM')}"
                    )
                    
                    # Buscar campos customizados dinamicamente
                    await self._fetch_custom_fields()
                    
                    # Buscar estágios do pipeline dinamicamente
                    await self._fetch_pipeline_stages()
                    
                    self.is_initialized = True
                else:
                    raise Exception(f"Erro ao conectar: {response.status}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao conectar Kommo: {e}")
            if self.session:
                await self._close_session_safely()
            raise
    
    async def _fetch_custom_fields(self):
        """Busca IDs dos campos customizados dinamicamente"""
        try:
            # Aplicar rate limiting
            await wait_for_kommo()
            
            async with self.session.get(
                f"{self.base_url}/api/v4/leads/custom_fields",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    fields = await response.json()
                    
                    # Mapear campos pelo nome (baseado nos campos reais do Kommo)
                    field_mapping = {
                        "whatsapp": "phone",
                        "telefone": "phone",
                        "phone": "phone",
                        "valor conta energia": "bill_value",
                        "valor_conta_energia": "bill_value",
                        "valor da conta": "bill_value",
                        "valor conta": "bill_value",
                        "solução solar": "solution_type",
                        "solucao solar": "solution_type",
                        "tipo de solução": "solution_type",
                        "link do evento no google calendar": "calendar_link",
                        "link do evento": "calendar_link",
                        "google calendar": "calendar_link",
                        "calendario": "calendar_link",
                        "local da instalação": "location",
                        "local_da_instalação": "location",
                        "localização": "location",
                        "endereço": "location",
                        "score qualificação": "score",
                        "score_qualificação": "score",
                        "score": "score",
                        "id conversa": "conversation_id",
                        "id_conversa": "conversation_id"
                    }
                    
                    # Atualizar mapeamento de campos
                    for field in fields.get("_embedded", {}).get("custom_fields", []):
                        field_name_lower = field.get("name", "").lower()
                        for key, mapped_name in field_mapping.items():
                            if key in field_name_lower:
                                self.custom_fields[mapped_name] = field.get("id")
                                emoji_logger.system_debug(f"Campo mapeado: {mapped_name} -> {field.get('id')}")
                                break
                    
                    emoji_logger.service_info(f"📊 {len(self.custom_fields)} campos customizados mapeados")
        except Exception as e:
            emoji_logger.service_warning(f"Erro ao buscar campos customizados: {e}")
            # Manter os IDs padrão se falhar
    
    async def _fetch_pipeline_stages(self):
        """Busca estágios do pipeline dinamicamente COM CACHE SIMPLES"""
        try:
            # Verificar cache primeiro
            import time
            current_time = time.time()
            
            if (self._stages_cache and 
                self._cache_timestamp and 
                (current_time - self._cache_timestamp) < self._cache_ttl):
                emoji_logger.system_debug("📦 Usando cache de estágios")
                self.stage_map = self._stages_cache
                return
            
            emoji_logger.system_debug("🔄 Buscando estágios do Kommo...")
            
            # Buscar estágios do Kommo
            # Aplicar rate limiting
            await wait_for_kommo()
            
            async with self.session.get(
                f"{self.base_url}/api/v4/leads/pipelines",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    pipelines = await response.json()
                    
                    # Encontrar o pipeline correto
                    for pipeline in pipelines.get("_embedded", {}).get("pipelines", []):
                        if pipeline.get("id") == self.pipeline_id:
                            # Criar mapa de estágios
                            self.stage_map = {}
                            for status in pipeline.get("_embedded", {}).get("statuses", []):
                                stage_name = status.get("name", "").lower()
                                stage_id = status.get("id")
                                
                                # Mapear variações do nome
                                self.stage_map[stage_name] = stage_id
                                self.stage_map[stage_name.replace(" ", "_")] = stage_id
                                self.stage_map[stage_name.upper()] = stage_id
                                
                                # Adicionar versões sem acentos para compatibilidade
                                import unicodedata
                                stage_name_normalized = unicodedata.normalize('NFKD', stage_name)
                                stage_name_no_accents = ''.join([c for c in stage_name_normalized if not unicodedata.combining(c)])
                                
                                self.stage_map[stage_name_no_accents] = stage_id
                                self.stage_map[stage_name_no_accents.replace(" ", "_")] = stage_id
                                
                                # Adicionar mapeamentos específicos conhecidos PT/EN
                                if "não interessado" in stage_name:
                                    self.stage_map["nao_interessado"] = stage_id
                                    self.stage_map["NAO_INTERESSADO"] = stage_id
                                    self.stage_map["NOT_INTERESTED"] = stage_id
                                elif "reunião agendada" in stage_name:
                                    self.stage_map["reuniao_agendada"] = stage_id
                                    self.stage_map["REUNIAO_AGENDADA"] = stage_id
                                    self.stage_map["MEETING_SCHEDULED"] = stage_id
                                elif "em qualificação" in stage_name:
                                    self.stage_map["em_qualificacao"] = stage_id
                                    self.stage_map["EM_QUALIFICACAO"] = stage_id
                                    self.stage_map["QUALIFICATION"] = stage_id
                                elif "qualificado" in stage_name:
                                    self.stage_map["qualificado"] = stage_id
                                    self.stage_map["QUALIFICADO"] = stage_id
                                    self.stage_map["QUALIFIED"] = stage_id
                                elif "fechado" in stage_name:
                                    self.stage_map["fechado"] = stage_id
                                    self.stage_map["FECHADO"] = stage_id
                                    self.stage_map["CLOSED"] = stage_id
                                elif "agendamento" in stage_name:
                                    self.stage_map["agendamento"] = stage_id
                                    self.stage_map["AGENDAMENTO"] = stage_id
                                    self.stage_map["SCHEDULE"] = stage_id
                                elif "atendimento humano" in stage_name:
                                    self.stage_map["atendimento_humano"] = stage_id
                                    self.stage_map["ATENDIMENTO_HUMANO"] = stage_id
                                    self.stage_map["HUMAN_HANDOFF"] = stage_id
                            
                            # Atualizar cache
                            self._stages_cache = self.stage_map
                            self._cache_timestamp = current_time
                            
                            emoji_logger.service_info(f"📊 {len(self.stage_map)} estágios mapeados")
                            break
        except Exception as e:
            emoji_logger.service_warning(f"Erro ao buscar estágios do pipeline: {e}")
            # Manter mapeamento padrão se falhar
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def create_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria lead REAL no Kommo"""
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar dados do lead para Kommo
            kommo_lead = {
                "name": lead_data.get("name", "Lead sem nome"),
                "responsible_user_id": 11031887,  # ID do usuário responsável (Leonardo)
                "pipeline_id": self.pipeline_id,
                "status_id": 89709589,  # ID do estágio inicial (QUALIFICAÇÃO)
                "_embedded": {
                    "tags": [
                        {
                            "name": "SDR_IA"
                        }
                    ]
                }
            }
            
            # Adicionar campos customizados se disponíveis
            custom_fields = []
            
            # Telefone/WhatsApp
            if lead_data.get("phone"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("phone", 392802),  # ID padrão se não encontrado
                    "values": [
                        {
                            "value": lead_data["phone"]
                        }
                    ]
                })
            
            # Valor da conta
            if lead_data.get("bill_value"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("bill_value", 392804),
                    "values": [
                        {
                            "value": lead_data["bill_value"]
                        }
                    ]
                })
            
            # Tipo de solução
            if lead_data.get("chosen_flow"):
                solution_key = lead_data["chosen_flow"].lower()
                enum_id = self.solution_type_values.get(solution_key)
                if enum_id:
                    custom_fields.append({
                        "field_id": self.custom_fields.get("solution_type", 392808),
                        "values": [
                            {
                                "enum_id": enum_id
                            }
                        ]
                    })
            
            # Link do Google Calendar
            if lead_data.get("google_event_link"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("calendar_link", 395520),
                    "values": [
                        {
                            "value": lead_data["google_event_link"]
                        }
                    ]
                })
            
            # Adicionar campos customizados ao lead
            if custom_fields:
                kommo_lead["custom_fields_values"] = custom_fields
            
            emoji_logger.system_event(f"🏷️ Nome do lead para Kommo: '{kommo_lead['name']}'")
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Criar lead no Kommo
            async with self.session.post(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                json=[kommo_lead]  # API espera array
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    lead_id = result.get("_embedded", {}).get("leads", [{}])[0].get("id")
                    
                    emoji_logger.crm_event(
                        f"✅ Lead CRIADO no Kommo: {kommo_lead['name']} - ID: {lead_id}"
                    )
                    
                    return {
                        "success": True,
                        "lead_id": lead_id,
                        "message": "Lead criado com sucesso no CRM"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro na criação do lead: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao criar lead no Kommo: {e}")
            return {
                "success": False,
                "message": f"Erro ao criar lead no CRM: {e}"
            }
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def update_lead(self, lead_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza lead REAL no Kommo"""
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar dados de atualização
            kommo_update = {}
            
            # Nome (se fornecido)
            if update_data.get("name"):
                kommo_update["name"] = update_data["name"]
            
            # Estágio (se fornecido)
            if update_data.get("current_stage"):
                stage_name = update_data["current_stage"].upper().replace(" ", "_")
                stage_id = self.stage_map.get(stage_name)
                if stage_id:
                    kommo_update["status_id"] = stage_id
            
            # Campos customizados
            custom_fields = []
            
            # Valor da conta
            if "bill_value" in update_data:
                custom_fields.append({
                    "field_id": self.custom_fields.get("bill_value", 392804),
                    "values": [
                        {
                            "value": update_data["bill_value"]
                        }
                    ]
                })
            
            # Tipo de solução
            if update_data.get("chosen_flow"):
                solution_key = update_data["chosen_flow"].lower()
                enum_id = self.solution_type_values.get(solution_key)
                if enum_id:
                    custom_fields.append({
                        "field_id": self.custom_fields.get("solution_type", 392808),
                        "values": [
                            {
                                "enum_id": enum_id
                            }
                        ]
                    })
            
            # Link do Google Calendar
            if update_data.get("google_event_link"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("calendar_link", 395520),
                    "values": [
                        {
                            "value": update_data["google_event_link"]
                        }
                    ]
                })
            
            # Adicionar campos customizados à atualização
            if custom_fields:
                kommo_update["custom_fields_values"] = custom_fields
            
            # Se não há dados para atualizar, retornar sucesso
            if not kommo_update:
                return {
                    "success": True,
                    "message": "Nenhum dado para atualizar"
                }
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Atualizar lead no Kommo
            async with self.session.patch(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                json={
                    "update": [{
                        "id": int(lead_id),
                        **kommo_update
                    }]
                }
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    
                    emoji_logger.crm_event(
                        f"✅ Lead ATUALIZADO no Kommo: {lead_id}"
                    )
                    
                    return {
                        "success": True,
                        "message": "Lead atualizado com sucesso no CRM"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro na atualização do lead: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao atualizar lead no Kommo: {e}")
            return {
                "success": False,
                "message": f"Erro ao atualizar lead no CRM: {e}"
            }
    
    async def create_or_update_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria ou atualiza lead REAL no Kommo
        Método direto para criar/atualizar lead no Kommo (alias para create_lead)
        Usado pelo KommoAutoSyncService
        """
        # Verificar se lead já existe (por telefone)
        if lead_data.get("phone"):
            existing_lead = await self.get_lead_by_phone(lead_data["phone"])
            if existing_lead and existing_lead.get("id"):
                # Atualizar lead existente
                update_result = await self.update_lead(existing_lead["id"], lead_data)
                if update_result.get("success"):
                    return {
                        "success": True,
                        "lead_id": existing_lead["id"],
                        "message": "Lead atualizado com sucesso",
                        "created": False
                    }
        
        # Criar novo lead
        return await self.create_lead(lead_data)
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def get_lead_by_id(self, lead_id: str) -> Optional[Dict[str, Any]]:
        """Busca lead REAL no Kommo por ID"""
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Aplicar rate limiting
            await wait_for_kommo()
            
            async with self.session.get(
                f"{self.base_url}/api/v4/leads/{lead_id}",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    lead = await response.json()
                    return lead
                elif response.status == 404:
                    return None
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro ao buscar lead: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao buscar lead no Kommo: {e}")
            return None
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def get_lead_by_phone(self, phone: str) -> Optional[Dict[str, Any]]:
        """Busca lead REAL no Kommo por telefone"""
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Buscar leads com o telefone específico
            async with self.session.get(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                params={
                    "query": phone
                }
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    leads = result.get("_embedded", {}).get("leads", [])
                    
                    # Retornar primeiro lead encontrado
                    if leads:
                        return leads[0]
                    return None
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro ao buscar lead por telefone: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao buscar lead por telefone no Kommo: {e}")
            return None
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def update_lead_stage(self, lead_id: str, stage_name: str, notes: str = "") -> Dict[str, Any]:
        """
        Atualiza o estágio de um lead no Kommo CRM com mapeamento unificado
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Normalizar nome do estágio (remover espaços e converter para maiúsculas)
            normalized_stage = stage_name.strip().upper().replace(" ", "_")
            
            # Verificar se estágio existe no mapeamento
            stage_id = self.stage_map.get(normalized_stage)
            
            if not stage_id:
                # Tentar encontrar com variações
                for key, value in self.stage_map.items():
                    if normalized_stage in key or key in normalized_stage:
                        stage_id = value
                        break
            
            if not stage_id:
                raise ValueError(f"Estágio '{stage_name}' não encontrado no mapeamento")
            
            # Preparar dados para atualização
            update_data = {
                "status_id": stage_id,
                "updated_at": int(datetime.now().timestamp())
            }
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Atualizar no Kommo
            async with self.session.patch(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                json={
                    "update": [{
                        "id": int(lead_id),
                        **update_data
                    }]
                }
            ) as response:
                if response.status == 200:
                    response_data = await response.json()
                    
                    emoji_logger.crm_event(
                        f"✅ Lead {lead_id} movido para estágio '{stage_name}' (ID: {stage_id})"
                    )
                    
                    return {
                        "success": True,
                        "message": f"Lead movido para estágio {stage_name}",
                        "stage_id": stage_id,
                        "lead_id": lead_id
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro na atualização do estágio: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao atualizar estágio do lead {lead_id}: {e}")
            return {
                "success": False,
                "message": f"Erro ao atualizar estágio: {e}",
                "lead_id": lead_id
            }
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def update_fields(self, lead_id: str, fields_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Atualiza campos customizados de um lead no Kommo
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar campos customizados
            custom_fields = []
            
            for field_name, field_value in fields_dict.items():
                # Mapear nome do campo para ID
                field_id = self.custom_fields.get(field_name)
                
                if field_id:
                    # Preparar valor do campo
                    field_data = {
                        "field_id": field_id,
                        "values": []
                    }
                    
                    # Tratar diferentes tipos de valores
                    if field_value is not None:
                        if isinstance(field_value, (int, float)):
                            field_data["values"].append({"value": field_value})
                        elif isinstance(field_value, str):
                            # Verificar se é um campo do tipo enum (select)
                            if field_name in ["solution_type", "solucao_solar"]:
                                # Procurar enum_id correspondente
                                enum_id = self.solution_type_values.get(field_value.lower())
                                if enum_id:
                                    field_data["values"].append({"enum_id": enum_id})
                                else:
                                    # Se não encontrar enum_id, usar valor como string
                                    field_data["values"].append({"value": field_value})
                            else:
                                field_data["values"].append({"value": field_value})
                        else:
                            # Para outros tipos, converter para string
                            field_data["values"].append({"value": str(field_value)})
                    
                    custom_fields.append(field_data)
            
            # Se não há campos para atualizar, retornar sucesso
            if not custom_fields:
                return {
                    "success": True,
                    "message": "Nenhum campo para atualizar"
                }
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Atualizar campos no Kommo
            async with self.session.patch(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                json={
                    "update": [{
                        "id": int(lead_id),
                        "custom_fields_values": custom_fields
                    }]
                }
            ) as response:
                if response.status == 200:
                    emoji_logger.crm_event(
                        f"✅ Campos atualizados para lead {lead_id}: {list(fields_dict.keys())}"
                    )
                    
                    return {
                        "success": True,
                        "message": "Campos atualizados com sucesso"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro na atualização de campos: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao atualizar campos do lead {lead_id}: {e}")
            return {
                "success": False,
                "message": f"Erro ao atualizar campos: {e}",
                "lead_id": lead_id
            }
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def add_tags_to_lead(self, lead_id: str, tags: List[str]) -> Dict[str, Any]:
        """
        Adiciona tags REAIS ao lead no Kommo
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar tags
            tag_data = []
            for tag in tags:
                tag_data.append({"name": tag})
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Adicionar tags no Kommo
            async with self.session.patch(
                f"{self.base_url}/api/v4/leads",
                headers=self.headers,
                json={
                    "update": [{
                        "id": int(lead_id),
                        "_embedded": {
                            "tags": tag_data
                        }
                    }]
                }
            ) as response:
                if response.status == 200:
                    emoji_logger.crm_event(
                        f"✅ Tags adicionadas ao lead {lead_id}: {tags}"
                    )
                    
                    return {
                        "success": True,
                        "message": "Tags adicionadas com sucesso"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro ao adicionar tags: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao adicionar tags ao lead {lead_id}: {e}")
            return {
                "success": False,
                "message": f"Erro ao adicionar tags: {e}",
                "lead_id": lead_id
            }
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def add_note_to_lead(self, lead_id: str, note_text: str) -> Dict[str, Any]:
        """
        Adiciona nota ao lead no Kommo
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar dados da nota
            note_data = {
                "add": [{
                    "element_id": int(lead_id),
                    "element_type": 2,  # 2 para leads
                    "note_type": 4,  # 4 para notas de texto
                    "text": note_text,
                    "created_by": 11031887  # ID do usuário (Leonardo)
                }]
            }
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Adicionar nota no Kommo
            async with self.session.post(
                f"{self.base_url}/api/v4/leads/notes",
                headers=self.headers,
                json=note_data
            ) as response:
                if response.status == 200:
                    emoji_logger.crm_note(
                        f"📝 Nota adicionada ao lead {lead_id}"
                    )
                    
                    return {
                        "success": True,
                        "message": "Nota adicionada com sucesso"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro ao adicionar nota: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao adicionar nota ao lead {lead_id}: {e}")
            return {
                "success": False,
                "message": f"Erro ao adicionar nota: {e}",
                "lead_id": lead_id
            }
    
    @async_retry_with_backoff(max_retries=3, initial_delay=1.0, max_delay=10.0)
    async def create_task(self, lead_id: str, task_text: str, complete_till: datetime) -> Dict[str, Any]:
        """
        Cria tarefa REAL no Kommo
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Preparar dados da tarefa
            task_data = {
                "add": [{
                    "element_id": int(lead_id),
                    "element_type": 2,  # 2 para leads
                    "task_type_id": 1,  # 1 para tarefas gerais
                    "text": task_text,
                    "complete_till": int(complete_till.timestamp()),
                    "responsible_user_id": 11031887  # ID do usuário (Leonardo)
                }]
            }
            
            # Aplicar rate limiting
            await wait_for_kommo()
            
            # Criar tarefa no Kommo
            async with self.session.post(
                f"{self.base_url}/api/v4/tasks",
                headers=self.headers,
                json=task_data
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    task_id = result.get("_embedded", {}).get("tasks", [{}])[0].get("id")
                    
                    emoji_logger.crm_event(
                        f"✅ Tarefa criada para lead {lead_id}: {task_id}"
                    )
                    
                    return {
                        "success": True,
                        "task_id": task_id,
                        "message": "Tarefa criada com sucesso"
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Erro ao criar tarefa: {response.status} - {error_text}")
                    
        except Exception as e:
            emoji_logger.service_error(f"Erro ao criar tarefa para lead {lead_id}: {e}")
            return {
                "success": False,
                "message": f"Erro ao criar tarefa: {e}",
                "lead_id": lead_id
            }
    
    async def health_check(self) -> bool:
        """Verifica saúde do serviço"""
        try:
            if not self.is_initialized:
                await self.initialize()
            
            # Testar conexão com a API
            await wait_for_kommo()
            
            async with self.session.get(
                f"{self.base_url}/api/v4/account",
                headers=self.headers
            ) as response:
                return response.status == 200
                
        except:
            return False
    
    async def _close_session_safely(self):
        """Fecha sessão HTTP com segurança"""
        try:
            if self.session:
                await self.session.close()
                self.session = None
                emoji_logger.service_info("🔌 Sessão CRM fechada com segurança")
        except Exception as e:
            emoji_logger.service_warning(f"Aviso ao fechar sessão CRM: {e}")
    
    async def close(self):
        """Fecha conexão com o CRM"""
        await self._close_session_safely()