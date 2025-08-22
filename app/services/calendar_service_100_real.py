"""
Calendar Service - Google Calendar API com OAuth 2.0
Funcionalidades habilitadas: Google Meet + Participantes + Convites
"""

from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import asyncio
import uuid
import random
from googleapiclient.errors import HttpError
from app.utils.logger import emoji_logger
from app.config import settings
from app.integrations.google_oauth_handler import get_oauth_handler
from app.integrations.redis_client import redis_client

from app.decorators.error_handler import async_handle_errors


class CalendarServiceReal:
    """
    Serviço REAL de calendário - Google Calendar API com OAuth 2.0
    """

    def __init__(self):
        self.is_initialized = False
        self.calendar_id = settings.google_calendar_id
        self.service = None
        self.oauth_handler = get_oauth_handler()
        self.business_hours = {
            "start_hour": 8,
            "end_hour": 18,
            "weekdays": [0, 1, 2, 3, 4]
        }
        self.lock_timeout = 30

    @async_handle_errors(retry_policy='google_calendar')
    async def initialize(self):
        """Inicializa conexão REAL com Google Calendar usando OAuth 2.0"""
        if self.is_initialized:
            return
        try:
            self.service = self.oauth_handler.build_calendar_service()
            if not self.service:
                emoji_logger.service_error(
                    "Não foi possível construir serviço - autorização OAuth necessária."
                )
                return

            if self.calendar_id:
                calendar = await asyncio.to_thread(
                    self.service.calendars().get(calendarId=self.calendar_id).execute
                )
                emoji_logger.service_ready(
                    f"Google Calendar conectado via OAuth: "
                    f"{calendar.get('summary', 'Calendar')}"
                )
            else:
                calendar_list = await asyncio.to_thread(
                    self.service.calendarList().list().execute
                )
                primary_calendar = next(
                    (
                        cal for cal in calendar_list.get('items', [])
                        if cal.get('primary')
                    ), None
                )
                if primary_calendar:
                    self.calendar_id = primary_calendar.get('id')
                    emoji_logger.service_ready(
                        f"Google Calendar conectado via OAuth: "
                        f"{primary_calendar.get('summary', 'Primary Calendar')}"
                    )
                else:
                    emoji_logger.service_error(
                        "Nenhum calendário primário encontrado."
                    )
                    return
            self.is_initialized = True
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao conectar Google Calendar: {e}"
            )
            self.is_initialized = False

    def is_business_hours(self, datetime_obj: datetime) -> bool:
        """Verifica se a data/hora está dentro do horário comercial"""
        if datetime_obj.weekday() not in self.business_hours["weekdays"]:
            return False
        if not (self.business_hours["start_hour"] <=
                datetime_obj.hour < self.business_hours["end_hour"]):
            return False
        return True

    def get_next_business_day(self, date: datetime) -> datetime:
        """Retorna o próximo dia útil disponível"""
        next_day = date
        while next_day.weekday() not in self.business_hours["weekdays"]:
            next_day += timedelta(days=1)
        return next_day

    def format_business_hours_message(self) -> str:
        """Retorna mensagem formatada sobre horário comercial"""
        weekday_names = {
            0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta"
        }
        days_str = (
            f"{weekday_names[self.business_hours['weekdays'][0]]} a "
            f"{weekday_names[self.business_hours['weekdays'][-1]]}"
        )
        return (
            f"{days_str}, das {self.business_hours['start_hour']}h às "
            f"{self.business_hours['end_hour']}h"
        )

    async def _acquire_lock(self, lock_key: str) -> bool:
        """Adquire um lock distribuído usando Redis"""
        try:
            lock_value = str(uuid.uuid4())
            result = await redis_client.redis_client.set(
                f"calendar_lock:{lock_key}",
                lock_value,
                nx=True,
                ex=self.lock_timeout
            )
            if result:
                self._lock_value = lock_value
                self._lock_key = lock_key
                return True
            return False
        except Exception as e:
            emoji_logger.service_error(f"Erro ao adquirir lock: {e}")
            return False

    async def _release_lock(self) -> bool:
        """Libera o lock distribuído"""
        try:
            if not hasattr(self, '_lock_key') or not hasattr(self, '_lock_value'):
                return False
            lock_key = f"calendar_lock:{self._lock_key}"
            lock_value = self._lock_value
            lua_script = """
            if redis.call("get", KEYS[1]) == ARGV[1] then
                return redis.call("del", KEYS[1])
            else
                return 0
            end
            """
            # A chamada correta para eval é posicional: script, num_keys, key, arg
            result = await redis_client.redis_client.eval(
                lua_script, 1, lock_key, lock_value
            )
            if hasattr(self, '_lock_key'):
                delattr(self, '_lock_key')
            if hasattr(self, '_lock_value'):
                delattr(self, '_lock_value')
            return result == 1
        except Exception as e:
            emoji_logger.service_error(f"Erro ao liberar lock: {e}")
            return False

    async def _schedule_meeting_with_retry(
            self, event_data: Dict[str, Any], max_retries: int = 3
    ) -> Dict[str, Any]:
        """Agenda reunião com retry em caso de conflitos"""
        import random
        for attempt in range(max_retries):
            try:
                created_event = await asyncio.to_thread(
                    self.service.events().insert(
                        calendarId=self.calendar_id,
                        body=event_data,
                        conferenceDataVersion=1,
                        sendUpdates='all' if event_data.get('attendees') else 'none'
                    ).execute
                )
                return created_event
            except HttpError as e:
                if e.resp.status == 409 and attempt < max_retries - 1:
                    delay = (2 ** attempt) + random.uniform(0, 1)
                    emoji_logger.service_warning(
                        f"⚠️ Conflito de horário, tentando novamente em "
                        f"{delay:.2f}s"
                    )
                    await asyncio.sleep(delay)
                else:
                    raise e
        raise Exception("Número máximo de tentativas excedido")

    @async_handle_errors(retry_policy='google_calendar')
    async def check_availability(self, date_request: str) -> Dict[str, Any]:
        """Verifica disponibilidade REAL no Google Calendar"""
        if not self.is_initialized:
            await self.initialize()
        lock_key = "calendar:availability_check"
        if not await redis_client.acquire_lock(lock_key, ttl=10):
            return {
                "success": False, "error": "lock_not_acquired",
                "message": "Sistema ocupado, tente novamente."
            }
        try:
            tomorrow = self.get_next_business_day(
                datetime.now() + timedelta(days=1)
            )
            time_min = tomorrow.replace(
                hour=0, minute=0, second=0
            ).isoformat() + 'Z'
            time_max = tomorrow.replace(
                hour=23, minute=59, second=59
            ).isoformat() + 'Z'
            events_result = await asyncio.to_thread(
                self.service.events().list(
                    calendarId=self.calendar_id, timeMin=time_min,
                    timeMax=time_max, singleEvents=True, orderBy='startTime'
                ).execute
            )
            events = events_result.get('items', [])
            all_slots = []
            for hour in range(
                    self.business_hours["start_hour"],
                    self.business_hours["end_hour"]
            ):
                slot_start = tomorrow.replace(hour=hour, minute=0, second=0)
                slot_end = slot_start + timedelta(hours=1)
                is_free = all(
                    slot_end <= datetime.fromisoformat(
                        event['start']['dateTime'].replace('Z', '+00:00')
                    ).replace(tzinfo=None) or
                    slot_start >= datetime.fromisoformat(
                        event['end']['dateTime'].replace('Z', '+00:00')
                    ).replace(tzinfo=None)
                    for event in events if 'dateTime' in event.get('start', {})
                )
                if is_free:
                    all_slots.append(f"{hour:02d}:00")
            morning_slots = [s for s in all_slots if "08:00" <= s < "12:00"]
            afternoon_slots = [s for s in all_slots if "13:00" <= s < "18:00"]

            selected_slots = []
            if morning_slots:
                selected_slots.append(random.choice(morning_slots))
            if afternoon_slots:
                selected_slots.append(random.choice(afternoon_slots))
            
            # Adiciona mais um horário se ainda houver espaço e slots disponíveis
            remaining_slots = [s for s in all_slots if s not in selected_slots]
            if len(selected_slots) < 3 and remaining_slots:
                selected_slots.append(random.choice(remaining_slots))

            selected_slots.sort()

            return {
                "success": True, "date": tomorrow.strftime("%Y-%m-%d"),
                "available_slots": selected_slots,
                "message": (
                    f"Leonardo tem {len(selected_slots)} horários para "
                    f"{tomorrow.strftime('%d/%m')}"
                ),
                "real": True
            }
        except Exception as e:
            emoji_logger.service_error(
                f"Erro ao verificar disponibilidade: {e}"
            )
            return {
                "success": False,
                "message": f"Erro ao verificar disponibilidade: {e}"
            }
        finally:
            await redis_client.release_lock(lock_key)

    @async_handle_errors(retry_policy='google_calendar')
    async def schedule_meeting(
            self, date: str, time: str, lead_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Agenda reunião REAL no Google Calendar"""
        if not self.is_initialized:
            await self.initialize()
        lock_key = f"calendar:schedule:{date}:{time}"
        if not await redis_client.acquire_lock(lock_key, ttl=30):
            return {
                "success": False, "error": "lock_not_acquired",
                "message": "Este horário foi agendado. Escolha outro."
            }
        try:
            meeting_datetime = datetime.strptime(
                f"{date} {time}", "%Y-%m-%d %H:%M"
            )
            if not self.is_business_hours(meeting_datetime):
                return {
                    "success": False, "error": "outside_business_hours",
                    "message": (
                        f"Fora do horário comercial: "
                        f"{self.format_business_hours_message()}"
                    )
                }
            meeting_end = meeting_datetime + timedelta(hours=1)
            
            description_template = """☀️ REUNIÃO SOLARPRIME - ECONOMIA COM ENERGIA SOLAR

Olá {lead_name}!

É com grande satisfação que confirmamos nossa reunião para apresentar como a SolarPrime pode transformar sua conta de energia em um investimento inteligente.

Somos líderes no setor de energia solar em Pernambuco, com mais de 12 anos de experiência e milhares de clientes satisfeitos. Nossa missão é democratizar o acesso à energia limpa e proporcionar economia real de até 90% na conta de luz.

✅ O QUE VAMOS APRESENTAR:
• Análise personalizada da sua conta de energia
• Simulação de economia com nossos 4 modelos de negócio
• Opções de financiamento que cabem no seu bolso
• Garantias e benefícios exclusivos SolarPrime
• Retorno do investimento em média de 3 anos

✅ NOSSOS DIFERENCIAIS:
• Instalação própria de usina - economia de até 90%
• Aluguel de lote - sua usina em nosso terreno
• Compra com desconto - economia imediata de 20%
• Usina de investimento - renda passiva com energia solar

Agradecemos pela confiança em escolher a SolarPrime para cuidar da sua economia energética. Leonardo Ferraz, nosso especialista, está ansioso para mostrar como podemos proteger você dos constantes aumentos da energia elétrica.

✨ Desejamos uma excelente reunião e estamos confiantes de que será o início de uma parceria de sucesso!

Atenciosamente,
Equipe SolarPrime
☀️ Transformando Sol em Economia"""

            event_description = description_template.format(lead_name=lead_info.get("name", "Cliente"))

            event = {
                'summary': (
                    f'☀️ Reunião SolarPrime com '
                    f'{lead_info.get("name", "Cliente")}'
                ),
                'description': event_description,
                'start': {
                    'dateTime': meeting_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo'
                },
                'end': {
                    'dateTime': meeting_end.isoformat(),
                    'timeZone': 'America/Sao_Paulo'
                },
                'conferenceData': {
                    'createRequest': {
                        'requestId': f'meet-{uuid.uuid4()}',
                        'conferenceSolutionKey': {'type': 'hangoutsMeet'}
                    }
                },
                'attendees': [
                    {'email': email} for email in set(
                        [lead_info.get("email")] +
                        lead_info.get("attendees", [])
                    ) if email
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 60},
                        {'method': 'popup', 'minutes': 15}
                    ]
                }
            }
            created_event = await self._schedule_meeting_with_retry(event)
            emoji_logger.system_debug(f"Resposta da API do Google (insert): {created_event}")

            meet_link = next(
                (
                    ep['uri'] for ep in created_event.get(
                        'conferenceData', {}
                    ).get('entryPoints', [])
                    if ep.get('entryPointType') == 'video'
                ), None
            )
            return {
                "success": True, "meeting_id": created_event.get('id'),
                "google_event_id": created_event.get('id'),
                "start_time": created_event.get('start', {}).get('dateTime'),
                "date": date, "time": time,
                "link": created_event.get('htmlLink'), "meet_link": meet_link,
                "attendees": [att['email'] for att in event['attendees']],
                "message": (
                    f"✅ Reunião confirmada para {date} às {time}."
                ), "real": True
            }
        except HttpError as e:
            if e.resp.status == 409:
                emoji_logger.service_warning(f"Conflito de agendamento detectado para {date} {time}. Buscando novos horários.")
                availability_result = await self.check_availability("")
                return {
                    "success": False,
                    "error": "conflict",
                    "message": f"O horário {time} no dia {date} já está ocupado.",
                    "available_slots": availability_result.get("available_slots", []),
                    "date": availability_result.get("date")
                }
            else:
                emoji_logger.service_error(f"Erro HTTP não tratado ao agendar: {e}")
                return {"success": False, "message": f"Erro ao agendar: {e}"}
        except Exception as e:
            emoji_logger.service_error(f"Erro ao agendar: {e}")
            return {"success": False, "message": f"Erro ao agendar: {e}"}
        finally:
            await redis_client.release_lock(lock_key)

    @async_handle_errors(retry_policy='google_calendar')
    async def cancel_meeting(self, meeting_id: str) -> Dict[str, Any]:
        """Cancela reunião REAL no Google Calendar"""
        if not self.is_initialized:
            await self.initialize()
        lock_key = f"cancel:{meeting_id}"
        if not await self._acquire_lock(lock_key):
            return {
                "success": False, "error": "lock_not_acquired",
                "message": "Sistema ocupado."
            }
        try:
            await asyncio.to_thread(
                self.service.events().delete(
                    calendarId=self.calendar_id, eventId=meeting_id
                ).execute
            )
            return {
                "success": True, "message": "Reunião cancelada.",
                "meeting_id": meeting_id, "real": True
            }
        except HttpError as e:
            if e.resp.status == 404:
                return {"success": True, "message": "Evento já cancelado."}
            raise
        finally:
            await self._release_lock()

    @async_handle_errors(retry_policy='google_calendar')
    async def reschedule_meeting(
        self, meeting_id: str, date: Optional[str], time: Optional[str], lead_info: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Reagenda uma reunião de forma segura, verificando a disponibilidade primeiro."""
        if not self.is_initialized:
            await self.initialize()
        
        emoji_logger.calendar_event(f"Iniciando reagendamento seguro para a reunião: {meeting_id}")

        try:
            # Passo 1: Obter detalhes do evento original
            original_event = await self.get_event(meeting_id)
            if not original_event:
                return {"success": False, "message": f"Reunião original com ID {meeting_id} não encontrada."}
            
            original_start_str = original_event.get("start", {}).get("dateTime")
            original_datetime = datetime.fromisoformat(original_start_str)
            
            # Define a nova data/hora, usando os dados originais como fallback
            new_date = date or original_datetime.strftime("%Y-%m-%d")
            new_time = time or original_datetime.strftime("%H:%M")
            new_datetime = datetime.strptime(f"{new_date} {new_time}", "%Y-%m-%d %H:%M")
            new_datetime_end = new_datetime + timedelta(hours=1)

            # Passo 2: Verificar se o novo horário está disponível
            emoji_logger.calendar_event(f"Verificando disponibilidade para {new_date} às {new_time}...")
            time_min = new_datetime.isoformat() + 'Z'
            time_max = new_datetime_end.isoformat() + 'Z'
            
            events_result = await asyncio.to_thread(
                self.service.events().list(
                    calendarId=self.calendar_id, timeMin=time_min,
                    timeMax=time_max, singleEvents=True
                ).execute
            )
            conflicting_events = [
                event for event in events_result.get('items', []) 
                if event.get('id') != meeting_id # Ignora o próprio evento que estamos reagendando
            ]

            if conflicting_events:
                emoji_logger.service_warning(f"Conflito detectado. O horário {new_time} de {new_date} não está disponível.")
                suggested_times = await self.check_availability("")
                return {
                    "success": False,
                    "error": "conflict",
                    "message": f"O horário {new_time} de {new_date} já está ocupado. Que tal um destes?",
                    "available_slots": suggested_times.get("available_slots", []),
                    "date": suggested_times.get("date")
                }

            # Passo 3: Se disponível, atualizar o evento existente usando events().update()
            emoji_logger.calendar_event(f"Horário disponível. Atualizando evento {meeting_id}...")
            original_event['start']['dateTime'] = new_datetime.isoformat()
            original_event['end']['dateTime'] = new_datetime_end.isoformat()

            updated_event = await asyncio.to_thread(
                self.service.events().update(
                    calendarId=self.calendar_id,
                    eventId=meeting_id,
                    body=original_event,
                    sendUpdates='all'
                ).execute
            )
            
            emoji_logger.system_success(f"Reunião {meeting_id} reagendada com sucesso para {new_date} às {new_time}.")
            emoji_logger.system_debug(f"Resposta da API (update): {updated_event}")

            meet_link = updated_event.get('hangoutLink')
            return {
                "success": True,
                "meeting_id": updated_event.get('id'),
                "google_event_id": updated_event.get('id'),
                "start_time": updated_event.get('start', {}).get('dateTime'),
                "date": new_date,
                "time": new_time,
                "link": updated_event.get('htmlLink'),
                "meet_link": meet_link,
                "message": f"✅ Reunião reagendada com sucesso para {new_date} às {new_time}."
            }

        except HttpError as e:
            emoji_logger.service_error(f"Erro de API do Google ao reagendar: {e}")
            return {"success": False, "message": f"Erro de API ao reagendar: {e.reason}"}
        except Exception as e:
            emoji_logger.service_error(f"Erro inesperado ao reagendar: {e}")
            return {"success": False, "message": "Ocorreu um erro inesperado durante o reagendamento."}

    @async_handle_errors(retry_policy='google_calendar')
    async def get_event(self, event_id: str) -> Optional[Dict[str, Any]]:
        """Busca um evento específico no Google Calendar pelo ID."""
        if not self.is_initialized:
            await self.initialize()
        try:
            return await asyncio.to_thread(
                self.service.events().get(
                    calendarId=self.calendar_id, eventId=event_id
                ).execute
            )
        except HttpError as e:
            if e.resp.status == 404:
                return None
            raise

    async def health_check(self) -> bool:
        """Verifica saúde do serviço"""
        try:
            if not self.is_initialized:
                await self.initialize()
            
            calendar_info = await asyncio.to_thread(
                self.service.calendars().get(calendarId=self.calendar_id).execute
            )
            return calendar_info is not None
        except Exception:
            return False
