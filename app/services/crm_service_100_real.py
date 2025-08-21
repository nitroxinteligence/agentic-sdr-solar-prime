"""
CRM Service 100% REAL - Kommo API
ZERO simulação, MÁXIMA simplicidade
"""

from typing import Dict, Any, Optional
from datetime import datetime
import asyncio
import aiohttp
import json
import random
from functools import wraps
from app.utils.logger import emoji_logger
from app.config import settings
from app.services.rate_limiter import wait_for_kommo
from app.decorators.error_handler import handle_kommo_errors
from app.exceptions import KommoAPIException
from app.integrations.redis_client import redis_client


def async_retry_with_backoff(
    max_retries: int = 3, initial_delay: float = 1.0,
    max_delay: float = 30.0, backoff_factor: float = 2.0
):
    """Decorator para retry assíncrono com backoff exponencial"""
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
                        jitter = random.uniform(0, delay * 0.1)
                        sleep_time = min(delay + jitter, max_delay)
                        emoji_logger.service_warning(
                            f"Tentativa {attempt + 1}/{max_retries} falhou: {e}. "
                            f"Aguardando {sleep_time:.1f}s..."
                        )
                        await asyncio.sleep(sleep_time)
                        delay = min(delay * backoff_factor, max_delay)
                    else:
                        emoji_logger.service_error(
                            f"Todas as {max_retries} tentativas falharam: {e}"
                        )
                except Exception as e:
                    raise e
            if last_exception:
                raise last_exception
        return wrapper
    return decorator


class CRMServiceReal:
    """Serviço REAL de CRM - Kommo API"""

    def __init__(self):
        self.is_initialized = False
        self.base_url = (
            settings.kommo_base_url or "https://leonardofvieira00.kommo.com"
        )
        self.access_token = settings.kommo_long_lived_token
        self.pipeline_id = int(settings.kommo_pipeline_id or 11672895)
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        self._session_timeout = aiohttp.ClientTimeout(total=30)
        self._stages_cache = None
        self._cache_ttl = 3600
        self._cache_timestamp = None
        self.custom_fields = {
            "phone": None, "whatsapp": None, "bill_value": None,
            "valor_conta": None, "solution_type": None,
            "solucao_solar": None, "calendar_link": None,
            "google_calendar": None, "conversation_id": None
        }
        self.stage_map = {}
        self.solution_type_values = {
            "usina própria": 326358, "usina propria": 326358,
            "fazenda solar": 326360, "consórcio": 326362,
            "consorcio": 326362, "consultoria": 326364,
            "não definido": 326366, "nao definido": 326366,
            "aluguel de lote": 1078618, "compra com desconto": 1078620,
            "usina investimento": 1078622
        }
        self.solution_type_options = {
            "Usina Própria": 326358, "Fazenda Solar": 326360,
            "Consórcio": 326362, "Consultoria": 326364,
            "Não Definido": 326366, "Aluguel de Lote": 1078618,
            "Compra com Desconto": 1078620, "Usina Investimento": 1078622
        }

    async def _get_session(self):
        connector = aiohttp.TCPConnector(
            limit=10, limit_per_host=5, ttl_dns_cache=300
        )
        return aiohttp.ClientSession(
            connector=connector, timeout=self._session_timeout
        )

    @handle_kommo_errors(max_retries=3, delay=10.0)
    async def initialize(self):
        """Inicializa conexão REAL com Kommo CRM"""
        if self.is_initialized:
            return
        try:
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.get(
                    f"{self.base_url}/api/v4/account", headers=self.headers
                ) as response:
                    if response.status == 200:
                        account = await response.json()
                        emoji_logger.service_ready(
                            f"✅ Kommo CRM conectado: {account.get('name', 'CRM')}"
                        )
                        await self._fetch_custom_fields()
                        await self._fetch_pipeline_stages()
                        self.is_initialized = True
                    else:
                        error_text = await response.text()
                        raise KommoAPIException(
                            f"Erro ao conectar Kommo: {response.status} - {error_text}",
                            error_code="KOMMO_CONNECTION_ERROR",
                            details={
                                "status_code": response.status,
                                "response": error_text
                            }
                        )
        except Exception as e:
            emoji_logger.service_error(f"Erro ao conectar Kommo: {e}")
            if not isinstance(e, KommoAPIException):
                raise KommoAPIException(
                    f"Erro ao conectar Kommo: {e}",
                    error_code="KOMMO_INITIALIZATION_ERROR",
                    details={"exception": str(e)}
                )
            else:
                raise

    async def _fetch_custom_fields(self):
        """Busca IDs dos campos customizados dinamicamente"""
        try:
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.get(
                    f"{self.base_url}/api/v4/leads/custom_fields",
                    headers=self.headers
                ) as response:
                    if response.status == 200:
                        fields = await response.json()
                        field_mapping = {
                            "whatsapp": "phone", "telefone": "phone",
                            "phone": "phone", "valor conta energia": "bill_value",
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
                            "localização": "location", "endereço": "location",
                            "score qualificação": "score",
                            "score_qualificação": "score", "score": "score",
                            "id conversa": "conversation_id",
                            "id_conversa": "conversation_id"
                        }
                        for field in fields.get(
                                "_embedded", {}
                        ).get("custom_fields", []):
                            field_name_lower = field.get("name", "").lower()
                            for key, mapped_name in field_mapping.items():
                                if key in field_name_lower:
                                    self.custom_fields[mapped_name] = field.get("id")
                                    break
                        emoji_logger.service_info(
                            f"📊 {len(self.custom_fields)} campos customizados mapeados"
                        )
        except Exception as e:
            emoji_logger.service_warning(
                f"Erro ao buscar campos customizados: {e}"
            )
            missing_fields = [
                f for f in [
                    "phone", "bill_value", "solution_type", "calendar_link"
                ] if not self.custom_fields.get(f)
            ]
            if missing_fields:
                raise KommoAPIException(
                    f"Falha ao mapear campos essenciais: {missing_fields}",
                    error_code="KOMMO_FIELD_MAPPING_ERROR"
                )

    async def _fetch_pipeline_stages(self):
        """Busca estágios do pipeline dinamicamente COM CACHE"""
        import time
        if (self._stages_cache and
                (time.time() - self._cache_timestamp) < self._cache_ttl):
            self.stage_map = self._stages_cache
            return
        try:
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.get(
                    f"{self.base_url}/api/v4/leads/pipelines",
                    headers=self.headers
                ) as response:
                    if response.status == 200:
                        pipelines = await response.json()
                        for pipeline in pipelines.get(
                                "_embedded", {}
                        ).get("pipelines", []):
                            if pipeline.get("id") == self.pipeline_id:
                                self.stage_map = {}
                                for status in pipeline.get(
                                        "_embedded", {}
                                ).get("statuses", []):
                                    stage_name = status.get("name", "").lower()
                                    stage_id = status.get("id")
                                    self.stage_map[
                                        stage_name.replace(" ", "_")
                                    ] = stage_id
                                    self.stage_map[stage_name.upper()] = stage_id
                                self._stages_cache = self.stage_map
                                self._cache_timestamp = time.time()
                                emoji_logger.service_info(
                                    f"📊 {len(self.stage_map)} estágios mapeados"
                                )
                                break
        except Exception as e:
            emoji_logger.service_warning(f"Erro ao buscar estágios: {e}")
            missing_stages = [
                s for s in [
                    "QUALIFICATION", "MEETING_SCHEDULED",
                    "NOT_INTERESTED", "HUMAN_HANDOFF"
                ] if not self.stage_map.get(s)
            ]
            if missing_stages:
                raise KommoAPIException(
                    f"Falha ao mapear estágios essenciais: {missing_stages}",
                    error_code="KOMMO_STAGE_MAPPING_ERROR"
                )

    @async_retry_with_backoff()
    @handle_kommo_errors()
    async def create_lead(
            self, lead_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria lead REAL no Kommo"""
        if not self.is_initialized:
            await self.initialize()
        try:
            kommo_lead = {
                "name": lead_data.get("name", "Lead sem nome"),
                "pipeline_id": self.pipeline_id,
                "status_id": 89709589,
                "_embedded": {"tags": [{"name": "SDR_IA"}]}
            }
            custom_fields = []
            if lead_data.get("phone"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("phone", 392802),
                    "values": [{"value": lead_data["phone"]}]
                })
            if lead_data.get("bill_value"):
                custom_fields.append({
                    "field_id": self.custom_fields.get("bill_value", 392804),
                    "values": [{"value": lead_data["bill_value"]}]
                })
            if lead_data.get("chosen_flow"):
                enum_id = self.solution_type_values.get(
                    lead_data["chosen_flow"].lower()
                )
                if enum_id:
                    custom_fields.append({
                        "field_id": self.custom_fields.get(
                            "solution_type", 392808
                        ),
                        "values": [{"enum_id": enum_id}]
                    })
            if lead_data.get("google_event_link"):
                custom_fields.append({
                    "field_id": self.custom_fields.get(
                        "calendar_link", 395520
                    ),
                    "values": [{"value": lead_data["google_event_link"]}]
                })
            if custom_fields:
                kommo_lead["custom_fields_values"] = custom_fields
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.post(
                    f"{self.base_url}/api/v4/leads",
                    headers=self.headers,
                    json=[kommo_lead]
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        lead_id = result.get(
                            "_embedded", {}
                        ).get("leads", [{}])[0].get("id")
                        emoji_logger.crm_event(
                            f"✅ Lead CRIADO no Kommo: {kommo_lead['name']} - "
                            f"ID: {lead_id}"
                        )
                        return {
                            "success": True, "lead_id": lead_id,
                            "message": "Lead criado com sucesso"
                        }
                    else:
                        error_text = await response.text()
                        raise KommoAPIException(
                            f"Erro ao criar lead: {response.status} - {error_text}",
                            error_code="KOMMO_CREATE_LEAD_ERROR",
                            details={
                                "status_code": response.status,
                                "response": error_text
                            }
                        )
        except Exception as e:
            emoji_logger.service_error(f"Erro ao criar lead no Kommo: {e}")
            if not isinstance(e, KommoAPIException):
                raise KommoAPIException(
                    f"Erro ao criar lead: {e}",
                    error_code="KOMMO_CREATE_LEAD_EXCEPTION",
                    details={"exception": str(e)}
                )
            else:
                raise

    @async_retry_with_backoff()
    @handle_kommo_errors()
    async def update_lead(
            self, lead_id: str, update_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Atualiza lead REAL no Kommo"""
        if not self.is_initialized:
            await self.initialize()
        try:
            kommo_update = {}
            if update_data.get("name"):
                kommo_update["name"] = update_data["name"]
            if update_data.get("current_stage"):
                stage_id = self.stage_map.get(
                    update_data["current_stage"].upper().replace(" ", "_")
                )
                if stage_id:
                    kommo_update["status_id"] = stage_id
            custom_fields = []
            if "bill_value" in update_data:
                custom_fields.append({
                    "field_id": self.custom_fields.get("bill_value", 392804),
                    "values": [{"value": update_data["bill_value"]}]
                })
            if update_data.get("chosen_flow"):
                enum_id = self.solution_type_values.get(
                    update_data["chosen_flow"].lower()
                )
                if enum_id:
                    custom_fields.append({
                        "field_id": self.custom_fields.get(
                            "solution_type", 392808
                        ),
                        "values": [{"enum_id": enum_id}]
                    })
            if update_data.get("google_event_link"):
                custom_fields.append({
                    "field_id": self.custom_fields.get(
                        "calendar_link", 395520
                    ),
                    "values": [{"value": update_data["google_event_link"]}]
                })
            if custom_fields:
                kommo_update["custom_fields_values"] = custom_fields
            if not kommo_update:
                return {"success": True, "message": "Nenhum dado para atualizar"}
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.patch(
                    f"{self.base_url}/api/v4/leads",
                    headers=self.headers,
                    json={"update": [{"id": int(lead_id), **kommo_update}]}
                ) as response:
                    if response.status == 200:
                        emoji_logger.crm_event(
                            f"✅ Lead {lead_id} ATUALIZADO no Kommo"
                        )
                        return {
                            "success": True, "message": "Lead atualizado com sucesso"
                        }
                    else:
                        error_text = await response.text()
                        raise KommoAPIException(
                            f"Erro ao atualizar lead: {response.status} - {error_text}",
                            error_code="KOMMO_UPDATE_LEAD_ERROR",
                            details={
                                "status_code": response.status,
                                "response": error_text
                            }
                        )
        except Exception as e:
            emoji_logger.service_error(f"Erro ao atualizar lead no Kommo: {e}")
            if not isinstance(e, KommoAPIException):
                raise KommoAPIException(
                    f"Erro ao atualizar lead: {e}",
                    error_code="KOMMO_UPDATE_LEAD_EXCEPTION",
                    details={"exception": str(e)}
                )
            else:
                raise

    async def create_or_update_lead(
            self, lead_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Cria ou atualiza lead REAL no Kommo, com lock"""
        phone = lead_data.get("phone")
        if not phone:
            return await self.create_lead(lead_data)
        lock_key = f"crm:lead:{phone}"
        if not await redis_client.acquire_lock(lock_key, ttl=30):
            return {
                "success": False, "error": "lock_not_acquired",
                "message": "Operação já em andamento."
            }
        try:
            existing_lead = await self.get_lead_by_phone(phone)
            if existing_lead and existing_lead.get("id"):
                update_result = await self.update_lead(
                    existing_lead["id"], lead_data
                )
                if update_result.get("success"):
                    return {
                        "success": True, "lead_id": existing_lead["id"],
                        "message": "Lead atualizado", "created": False
                    }
                return update_result
            return await self.create_lead(lead_data)
        finally:
            await redis_client.release_lock(lock_key)

    @async_retry_with_backoff()
    @handle_kommo_errors()
    async def get_lead_by_phone(
            self, phone: str
    ) -> Optional[Dict[str, Any]]:
        """Busca lead REAL no Kommo por telefone com cache"""
        if not self.is_initialized:
            await self.initialize()
        clean_phone = ''.join(filter(str.isdigit, phone))
        if not clean_phone.startswith('55'):
            clean_phone = '55' + clean_phone
        cache_key = f"kommo_lead:{clean_phone}"
        cached_lead = await redis_client.get(cache_key)
        if cached_lead:
            return json.loads(cached_lead)
        try:
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.get(
                    f"{self.base_url}/api/v4/leads",
                    headers=self.headers,
                    params={"query": clean_phone}
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        leads = result.get("_embedded", {}).get("leads", [])
                        if leads:
                            lead = leads[0]
                            await redis_client.set(
                                cache_key, json.dumps(lead), ttl=300
                            )
                            return lead
                        return None
                    else:
                        error_text = await response.text()
                        raise KommoAPIException(
                            f"Erro ao buscar lead por telefone: {response.status} - "
                            f"{error_text}",
                            error_code="KOMMO_GET_LEAD_BY_PHONE_ERROR",
                            details={
                                "status_code": response.status,
                                "response": error_text
                            }
                        )
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao buscar lead por telefone {phone}: {e}"
            )
            if not isinstance(e, KommoAPIException):
                raise KommoAPIException(
                    f"Erro ao buscar lead por telefone: {e}",
                    error_code="KOMMO_GET_LEAD_BY_PHONE_EXCEPTION",
                    details={"exception": str(e)}
                )
            else:
                raise

    @handle_kommo_errors()
    async def update_lead_stage(
            self, lead_id: str, stage_name: str, notes: str = ""
    ) -> Dict[str, Any]:
        """Atualiza o estágio de um lead no Kommo"""
        if not self.is_initialized:
            await self.initialize()
        try:
            normalized_stage = stage_name.strip().upper().replace(" ", "_")
            stage_id = self.stage_map.get(normalized_stage)
            if not stage_id:
                raise ValueError(f"Estágio '{stage_name}' não encontrado")
            update_data = {
                "status_id": stage_id,
                "updated_at": int(datetime.now().timestamp())
            }
            await wait_for_kommo()
            async with await self._get_session() as session:
                async with session.patch(
                    f"{self.base_url}/api/v4/leads",
                    headers=self.headers,
                    json={"update": [{"id": int(lead_id), **update_data}]}
                ) as response:
                    if response.status == 200:
                        emoji_logger.crm_event(
                            f"✅ Lead {lead_id} movido para '{stage_name}'"
                        )
                        if notes:
                            await self.add_note_to_lead(lead_id, notes)
                        return {
                            "success": True,
                            "message": f"Lead movido para {stage_name}",
                            "stage_id": stage_id, "lead_id": lead_id
                        }
                    else:
                        error_text = await response.text()
                        raise KommoAPIException(
                            f"Erro ao atualizar estágio: {response.status} - "
                            f"{error_text}",
                            error_code="KOMMO_UPDATE_STAGE_ERROR",
                            details={
                                "status_code": response.status,
                                "response": error_text
                            }
                        )
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao atualizar estágio do lead {lead_id}: {e}"
            )
            if not isinstance(e, KommoAPIException):
                raise KommoAPIException(
                    f"Erro ao atualizar estágio: {e}",
                    error_code="KOMMO_UPDATE_STAGE_EXCEPTION",
                    details={"exception": str(e), "lead_id": lead_id}
                )
            else:
                raise

    async def close(self):
        """Fecha conexão com Kommo CRM"""
        self.is_initialized = False