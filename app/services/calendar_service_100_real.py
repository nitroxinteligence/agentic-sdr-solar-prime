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
                calendar = self.service.calendars().get(
                    calendarId=self.calendar_id
                ).execute()
                emoji_logger.service_ready(
                    f"Google Calendar conectado via OAuth: "
                    f"{calendar.get('summary', 'Calendar')}"
                )
            else:
                calendar_list = self.service.calendarList().list().execute()
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
            result = await redis_client.redis_client.eval(
                lua_script, keys=[lock_key], args=[lock_value]
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
                created_event = self.service.events().insert(
                    calendarId=self.calendar_id,
                    body=event_data,
                    conferenceDataVersion=1,
                    sendUpdates='all' if event_data.get('attendees') else 'none'
                ).execute()
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
            events_result = self.service.events().list(
                calendarId=self.calendar_id, timeMin=time_min,
                timeMax=time_max, singleEvents=True, orderBy='startTime'
            ).execute()
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
            event = {
                'summary': (
                    f'☀️ Reunião SolarPrime com '
                    f'{lead_info.get("name", "Cliente")}'
                ),
                'description': (
                    "Detalhes da apresentação sobre economia com energia solar."
                ),
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
                "start_time": meeting_datetime.isoformat(),
                "date": date, "time": time,
                "link": created_event.get('htmlLink'), "meet_link": meet_link,
                "attendees": [att['email'] for att in event['attendees']],
                "message": (
                    f"✅ Reunião confirmada para {date} às {time}."
                ), "real": True
            }
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
            self.service.events().delete(
                calendarId=self.calendar_id, eventId=meeting_id
            ).execute()
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
    async def get_event(self, event_id: str) -> Optional[Dict[str, Any]]:
        """Busca um evento específico no Google Calendar pelo ID."""
        if not self.is_initialized:
            await self.initialize()
        try:
            return self.service.events().get(
                calendarId=self.calendar_id, eventId=event_id
            ).execute()
        except HttpError as e:
            if e.resp.status == 404:
                return None
            raise

    async def health_check(self) -> bool:
        """Verifica saúde do serviço"""
        try:
            if not self.is_initialized:
                await self.initialize()
            return self.service.calendars().get(
                calendarId=self.calendar_id
            ).execute() is not None
        except Exception:
            return False
