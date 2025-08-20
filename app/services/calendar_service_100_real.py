"""
Calendar Service - Google Calendar API com OAuth 2.0
Funcionalidades habilitadas: Google Meet + Participantes + Convites
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
import asyncio
import uuid
from googleapiclient.errors import HttpError
from app.utils.logger import emoji_logger
from app.config import settings
from app.integrations.google_oauth_handler import get_oauth_handler
from app.integrations.redis_client import redis_client

class CalendarServiceReal:
    """
    Serviço REAL de calendário - Google Calendar API com OAuth 2.0
    Funcionalidades habilitadas: Google Meet + Participantes + Convites
    """
    
    def __init__(self):
        self.is_initialized = False
        self.calendar_id = settings.google_calendar_id
        self.service = None
        self.oauth_handler = get_oauth_handler()
        
        # 🚨 HORÁRIO COMERCIAL: Segunda a Sexta, 8h às 17h
        self.business_hours = {
            "start_hour": 8,   # 8:00
            "end_hour": 17,    # 17:00
            "weekdays": [0, 1, 2, 3, 4]  # Segunda(0) a Sexta(4)
        }
        
        # Lock timeout in seconds
        self.lock_timeout = 30
        
    async def initialize(self):
        """Inicializa conexão REAL com Google Calendar usando OAuth 2.0"""
        if self.is_initialized:
            return
        
        try:
            # Usar OAuth handler para construir serviço
            self.service = self.oauth_handler.build_calendar_service()
            
            if not self.service:
                emoji_logger.service_error("❌ Não foi possível construir serviço - autorização OAuth necessária")
                raise Exception("OAuth 2.0 não autorizado. Execute /google/auth para autorizar")
            
            # Testar conexão
            if self.calendar_id:
                calendar = self.service.calendars().get(calendarId=self.calendar_id).execute()
                emoji_logger.service_ready(f"✅ Google Calendar conectado via OAuth: {calendar.get('summary', 'Calendar')}")
            else:
                # Usar calendário primário se ID não especificado
                calendar_list = self.service.calendarList().list().execute()
                primary_calendar = next((cal for cal in calendar_list.get('items', []) if cal.get('primary')), None)
                if primary_calendar:
                    self.calendar_id = primary_calendar.get('id')
                    emoji_logger.service_ready(f"✅ Google Calendar conectado via OAuth: {primary_calendar.get('summary', 'Primary Calendar')}")
                else:
                    raise Exception("Nenhum calendário encontrado")
            
            self.is_initialized = True
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao conectar Google Calendar: {e}")
            raise
    
    def is_business_hours(self, datetime_obj: datetime) -> bool:
        """
        Verifica se a data/hora está dentro do horário comercial
        Segunda a Sexta, 8h às 17h
        
        Returns:
            True se está no horário comercial, False caso contrário
        """
        # Verificar dia da semana (0=Segunda, 6=Domingo)
        if datetime_obj.weekday() not in self.business_hours["weekdays"]:
            return False
        
        # Verificar horário (8h às 17h)
        if datetime_obj.hour < self.business_hours["start_hour"] or datetime_obj.hour >= self.business_hours["end_hour"]:
            return False
        
        return True
    
    def get_next_business_day(self, date: datetime) -> datetime:
        """
        Retorna o próximo dia útil disponível
        """
        next_day = date
        while next_day.weekday() not in self.business_hours["weekdays"]:
            next_day += timedelta(days=1)
        return next_day
    
    def format_business_hours_message(self) -> str:
        """
        Retorna mensagem formatada sobre horário comercial
        """
        weekday_names = {
            0: "Segunda", 1: "Terça", 2: "Quarta", 
            3: "Quinta", 4: "Sexta"
        }
        days_str = " a ".join([weekday_names[self.business_hours["weekdays"][0]], 
                               weekday_names[self.business_hours["weekdays"][-1]]])
        
        return f"{days_str}, das {self.business_hours['start_hour']}h às {self.business_hours['end_hour']}h"
    
    async def _acquire_lock(self, lock_key: str) -> bool:
        """
        Adquire um lock distribuído usando Redis
        
        Args:
            lock_key: Chave única para o lock
            
        Returns:
            True se o lock foi adquirido, False caso contrário
        """
        try:
            # Gerar um valor único para o lock (para identificar o proprietário)
            lock_value = str(uuid.uuid4())
            
            # Tentar adquirir o lock com NX (só se não existir) e EX (tempo de expiração)
            result = await redis_client.redis_client.set(
                f"calendar_lock:{lock_key}",
                lock_value,
                nx=True,
                ex=self.lock_timeout
            )
            
            if result:
                # Armazenar o valor do lock para liberação posterior
                self._lock_value = lock_value
                self._lock_key = lock_key
                return True
            else:
                return False
                
        except Exception as e:
            emoji_logger.service_error(f"Erro ao adquirir lock: {e}")
            return False
    
    async def _release_lock(self) -> bool:
        """
        Libera o lock distribuído
        
        Returns:
            True se o lock foi liberado, False caso contrário
        """
        try:
            if not hasattr(self, '_lock_key') or not hasattr(self, '_lock_value'):
                return False
                
            lock_key = f"calendar_lock:{self._lock_key}"
            lock_value = self._lock_value
            
            # Usar um script Lua para liberar o lock apenas se for o proprietário
            # Isso evita liberar o lock de outro processo
            lua_script = """
            if redis.call("get", KEYS[1]) == ARGV[1] then
                return redis.call("del", KEYS[1])
            else
                return 0
            end
            """
            
            result = await redis_client.redis_client.eval(
                lua_script,
                keys=[lock_key],
                args=[lock_value]
            )
            
            # Limpar variáveis do lock
            if hasattr(self, '_lock_key'):
                delattr(self, '_lock_key')
            if hasattr(self, '_lock_value'):
                delattr(self, '_lock_value')
                
            return result == 1
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao liberar lock: {e}")
            return False
    
    async def _schedule_meeting_with_retry(self, event_data: Dict[str, Any], max_retries: int = 3) -> Dict[str, Any]:
        """
        Agenda reunião com retry em caso de conflitos (HttpError 409)
        
        Args:
            event_data: Dados do evento a ser criado
            max_retries: Número máximo de tentativas
            
        Returns:
            Dict com resultado do agendamento
        """
        import random
        
        for attempt in range(max_retries):
            try:
                # Criar evento no Google Calendar
                created_event = self.service.events().insert(
                    calendarId=self.calendar_id,
                    body=event_data,
                    conferenceDataVersion=1,  # Sempre 1 para Google Meet com OAuth
                    sendUpdates='all' if event_data.get('attendees') else 'none'
                ).execute()
                
                return created_event
                
            except HttpError as e:
                status_code = e.resp.status if hasattr(e, 'resp') else 'unknown'
                
                # Se for conflito de horário (409) e ainda tiver tentativas
                if status_code == 409 and attempt < max_retries - 1:
                    # Esperar um tempo aleatório antes de tentar novamente (backoff exponencial)
                    delay = (2 ** attempt) + random.uniform(0, 1)
                    emoji_logger.service_warning(f"⚠️ Conflito de horário detectado, tentando novamente em {delay:.2f}s (tentativa {attempt + 1}/{max_retries})")
                    await asyncio.sleep(delay)
                    continue
                else:
                    # Relançar a exceção se não for 409 ou se já esgotou as tentativas
                    raise e
        
        # Isso não deve ser alcançado, mas está aqui para segurança
        raise Exception("Número máximo de tentativas excedido")
    
    async def _rollback_reschedule(self, 
                                  original_meeting_id: str, 
                                  original_event_data: Optional[Dict[str, Any]], 
                                  lead_info: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Realiza rollback de uma operação de reagendamento que falhou
        
        Args:
            original_meeting_id: ID da reunião original
            original_event_data: Dados do evento original
            lead_info: Informações do lead
            
        Returns:
            Dict com resultado do rollback
        """
        try:
            # Se não temos os dados do evento original, não podemos fazer rollback
            if not original_event_data:
                return {
                    "success": False,
                    "message": "Dados do evento original não disponíveis para rollback"
                }
            
            # Tentar recriar o evento original
            recreated_event = self.service.events().insert(
                calendarId=self.calendar_id,
                body=original_event_data,
                conferenceDataVersion=1,
                sendUpdates='all' if original_event_data.get('attendees') else 'none'
            ).execute()
            
            emoji_logger.service_info(f"✅ Evento recriado no rollback: {recreated_event.get('id')}")
            
            return {
                "success": True,
                "message": "Evento original recriado com sucesso",
                "recreated_event_id": recreated_event.get('id')
            }
            
        except Exception as e:
            emoji_logger.service_error(f"❌ Erro no rollback: {e}")
            return {
                "success": False,
                "message": f"Erro ao recriar evento original: {e}"
            }
    
    async def check_availability(self, date_request: str) -> Dict[str, Any]:
        """
        Verifica disponibilidade REAL no Google Calendar
        """
        if not self.is_initialized:
            await self.initialize()
        
        # Adquirir lock para verificar disponibilidade
        # Usamos um lock mais amplo para evitar race conditions na verificação
        lock_key = f"availability:check"
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning("⚠️ Não foi possível adquirir lock para verificar disponibilidade")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para verificação de disponibilidade"
            }
        
        try:
            # Determinar data baseada no request
            tomorrow = datetime.now() + timedelta(days=1)
            
            # 🚨 VALIDAÇÃO: Ajustar para próximo dia útil se necessário
            if tomorrow.weekday() not in self.business_hours["weekdays"]:
                tomorrow = self.get_next_business_day(tomorrow)
                emoji_logger.service_info(f"📅 Ajustando para próximo dia útil: {tomorrow.strftime('%A, %d/%m')}")
            
            # Buscar eventos do dia
            time_min = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
            time_max = tomorrow.replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + 'Z'
            
            events_result = self.service.events().list(
                calendarId=self.calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = events_result.get('items', [])
            
            # 🚨 HORÁRIO COMERCIAL: Apenas horários dentro do expediente
            all_slots = []
            for hour in range(self.business_hours["start_hour"], self.business_hours["end_hour"]):
                slot_start = tomorrow.replace(hour=hour, minute=0, second=0, microsecond=0)
                slot_end = slot_start + timedelta(hours=1)
                
                # Verificar se está livre
                is_free = True
                for event in events:
                    event_start = event.get('start', {}).get('dateTime')
                    event_end = event.get('end', {}).get('dateTime')
                    
                    if event_start and event_end:
                        # Remover timezone info para comparação
                        event_start_dt = datetime.fromisoformat(event_start.replace('Z', '+00:00')).replace(tzinfo=None)
                        event_end_dt = datetime.fromisoformat(event_end.replace('Z', '+00:00')).replace(tzinfo=None)
                        
                        # Verificar conflito
                        if not (slot_end <= event_start_dt or slot_start >= event_end_dt):
                            is_free = False
                            break
                
                if is_free:
                    all_slots.append(f"{hour:02d}:00")
            
            return {
                "success": True,
                "date": tomorrow.strftime("%d/%m/%Y"),
                "available_slots": all_slots[:5] if all_slots else ["10:00", "14:00", "16:00"],  # Default se vazio
                "message": f"Leonardo tem {len(all_slots)} horários disponíveis para {tomorrow.strftime('%d/%m')}",
                "real": True  # Indicador de que é REAL
            }
            
        except HttpError as e:
            emoji_logger.service_error(f"Erro Google Calendar: {e}")
            return {
                "success": False,
                "message": f"Erro ao verificar disponibilidade: {e}"
            }
        except Exception as e:
            emoji_logger.service_error(f"Erro inesperado: {e}")
            return {
                "success": False,
                "message": "Erro ao processar solicitação"
            }
        finally:
            # Liberar o lock independentemente do resultado
            await self._release_lock()
    
    async def schedule_meeting(self, 
                              date: str, 
                              time: str, 
                              lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Agenda reunião REAL no Google Calendar
        """
        if not self.is_initialized:
            await self.initialize()
        
        # Criar chave única para o lock baseada na data e hora
        lock_key = f"schedule:{date}:{time}"
        
        # Adquirir lock para prevenir race conditions
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning(f"⚠️ Não foi possível adquirir lock para agendamento em {date} às {time}")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para agendamento"
            }
        
        try:
            # Converter data e hora
            meeting_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            meeting_end = meeting_datetime + timedelta(hours=1)
            
            # 🚨 VALIDAÇÃO DE HORÁRIO COMERCIAL
            if not self.is_business_hours(meeting_datetime):
                weekday_names = {
                    5: "sábado", 6: "domingo",
                    0: "segunda-feira", 1: "terça-feira", 2: "quarta-feira",
                    3: "quinta-feira", 4: "sexta-feira"
                }
                
                # Mensagem específica para fim de semana
                if meeting_datetime.weekday() in [5, 6]:
                    emoji_logger.service_warning(f"⚠️ Tentativa de agendar no {weekday_names[meeting_datetime.weekday()]}")
                    
                    # Sugerir próximo dia útil
                    next_business = self.get_next_business_day(meeting_datetime)
                    
                    return {
                        "success": False,
                        "error": "weekend_not_allowed",
                        "message": f"Ops! Não agendamos reuniões aos finais de semana. 🚫

" +
                                  f"O Leonardo atende apenas em dias úteis ({self.format_business_hours_message()}).

" +
                                  f"Que tal {weekday_names[next_business.weekday()]}, {next_business.strftime('%d/%m')}? " +
                                  f"Posso verificar os horários disponíveis para você! 😊",
                        "suggested_date": next_business.strftime("%Y-%m-%d"),
                        "business_hours": self.format_business_hours_message()
                    }
                
                # Mensagem para horário fora do expediente
                elif meeting_datetime.hour < self.business_hours["start_hour"] or meeting_datetime.hour >= self.business_hours["end_hour"]:
                    emoji_logger.service_warning(f"⚠️ Tentativa de agendar às {meeting_datetime.hour}h (fora do expediente)")
                    
                    return {
                        "success": False,
                        "error": "outside_business_hours",
                        "message": f"Ops! Esse horário está fora do nosso expediente. ⏰

" +
                                  f"O Leonardo atende {self.format_business_hours_message()}.

" +
                                  f"Posso verificar os horários disponíveis dentro do expediente para você! 😊",
                        "requested_time": time,
                        "business_hours": self.format_business_hours_message()
                    }
            
            # Se passou na validação, continuar com o agendamento normal
            
            # Criar evento
            event = {
                'summary': f'☀️ Reunião SolarPrime com {lead_info.get("name", "Cliente")}',
                'description': f"""
☀️ REUNIÃO SOLARPRIME - ECONOMIA COM ENERGIA SOLAR

Olá {lead_info.get("name", "")}!

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
☀️ Transformando Sol em Economia
                """,
                'start': {
                    'dateTime': meeting_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'dateTime': meeting_end.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 60},
                        {'method': 'popup', 'minutes': 15},
                    ],
                },
            }
            
            # Adicionar participantes - Com OAuth funciona!
            attendees = []
            if lead_info.get("email"):
                attendees.append(lead_info["email"])
            
            # Adicionar emails adicionais se fornecidos
            if 'attendees' in lead_info:
                if isinstance(lead_info['attendees'], list):
                    attendees.extend(lead_info['attendees'])
                elif isinstance(lead_info['attendees'], str):
                    # Se for string com vários emails separados por vírgula
                    emails = [e.strip() for e in lead_info['attendees'].split(',')]
                    attendees.extend(emails)
            
            # Remover duplicatas
            attendees = list(set(attendees))
            
            # Adicionar participantes ao evento - Com OAuth sempre funciona!
            if attendees:
                event['attendees'] = [{'email': email} for email in attendees]
                emoji_logger.service_info(f"👥 {len(attendees)} participantes serão convidados")
            
            # Adicionar Google Meet - Com OAuth sempre funciona!
            event['conferenceData'] = {
                'createRequest': {
                    'requestId': f'meet-{datetime.now().timestamp()}',
                    'conferenceSolutionKey': {
                        'type': 'hangoutsMeet'
                    }
                }
            }
            emoji_logger.service_info("📹 Google Meet será criado automaticamente")
            
            # Criar evento no Google Calendar com retry em caso de conflitos
            # Com OAuth sempre usa conferenceDataVersion=1 para criar Google Meet
            created_event = await self._schedule_meeting_with_retry(event)
            
            emoji_logger.calendar_event(
                f"✅ Reunião REAL agendada: {created_event.get('id')}"
            )
            
            # Extrair link do Google Meet se criado
            meet_link = None
            if 'conferenceData' in created_event:
                entry_points = created_event['conferenceData'].get('entryPoints', [])
                for entry in entry_points:
                    if entry.get('entryPointType') == 'video':
                        meet_link = entry.get('uri')
                        break
            
            # Mensagem personalizada baseada nas funcionalidades
            features = []
            if meet_link:
                features.append(f"📹 Google Meet: {meet_link}")
            if attendees:
                features.append(f"👥 {len(attendees)} participante(s) convidado(s)")
            
            # Liberar o lock antes de retornar sucesso
            await self._release_lock()
            
            return {
                "success": True,
                "meeting_id": created_event.get('id'),
                "google_event_id": created_event.get('id'),  # 🚀 CORREÇÃO: Adicionar google_event_id
                "start_time": meeting_datetime.isoformat(),  # 🚀 CORREÇÃO: Adicionar start_time
                "date": date,
                "time": time,
                "link": created_event.get('htmlLink'),
                "meet_link": meet_link,
                "attendees": attendees,
                "message": f"✅ Reunião confirmada para {date} às {time}. {' | '.join(features) if features else 'Leonardo foi notificado!'}",
                "real": True
            }
            
        except HttpError as e:
            # 🚀 ROBUSTEZ: Tratamento específico para HttpError
            error_details = e.error_details if hasattr(e, 'error_details') else []
            status_code = e.resp.status if hasattr(e, 'resp') else 'unknown'
            
            if status_code == 403:
                emoji_logger.service_error("❌ Erro de permissão Google Calendar - Verificar OAuth")
                result = {
                    "success": False,
                    "error_code": 403,
                    "message": "Erro de permissão. Necessário reautorizar OAuth",
                    "details": "Verifique as permissões do Google Calendar"
                }
            elif status_code == 404:
                emoji_logger.service_error("❌ Calendário não encontrado")
                result = {
                    "success": False,
                    "error_code": 404,
                    "message": "Calendário não encontrado",
                    "details": f"Calendar ID: {self.calendar_id}"
                }
            elif status_code == 409:
                emoji_logger.service_error("⚠️ Conflito de horário detectado")
                result = {
                    "success": False,
                    "error_code": 409,
                    "message": "Conflito de horário - Horário já ocupado",
                    "details": "Tente outro horário disponível"
                }
            else:
                emoji_logger.service_error(f"❌ Erro Google Calendar [{status_code}]: {e}")
                result = {
                    "success": False,
                    "error_code": status_code,
                    "message": f"Erro Google Calendar: {e}",
                    "details": str(error_details)
                }
        except Exception as e:
            emoji_logger.service_error(f"❌ Erro inesperado ao agendar: {e}")
            result = {
                "success": False,
                "error_code": "unknown",
                "message": f"Erro inesperado: {e}",
                "details": "Erro interno do sistema"
            }
        
        # Liberar o lock em caso de erro
        await self._release_lock()
        
        # Retornar o resultado de erro
        return result
    
    async def cancel_meeting(self, meeting_id: str) -> Dict[str, Any]:
        """Cancela reunião REAL no Google Calendar"""
        if not self.is_initialized:
            await self.initialize()
        
        # Adquirir lock para cancelar a reunião
        lock_key = f"cancel:{meeting_id}"
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning(f"⚠️ Não foi possível adquirir lock para cancelar reunião {meeting_id}")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para cancelamento de reunião"
            }
        
        try:
            self.service.events().delete(
                calendarId=self.calendar_id,
                eventId=meeting_id
            ).execute()
            
            emoji_logger.calendar_event(f"❌ Reunião cancelada: {meeting_id}")
            
            return {
                "success": True,
                "message": "Reunião cancelada com sucesso",
                "meeting_id": meeting_id,
                "real": True
            }
            
        except HttpError as e:
            # 🚀 ROBUSTEZ: Tratamento específico para cancelamento
            status_code = e.resp.status if hasattr(e, 'resp') else 'unknown'
            
            if status_code == 403:
                emoji_logger.service_error("❌ Sem permissão para cancelar evento")
                return {
                    "success": False,
                    "error_code": 403,
                    "message": "Sem permissão para cancelar evento",
                    "details": "Verificar permissões OAuth"
                }
            elif status_code == 404:
                emoji_logger.service_warning("⚠️ Evento já foi cancelado ou não existe")
                return {
                    "success": True,  # Considerar sucesso se já não existe
                    "message": "Evento já foi cancelado ou não existe",
                    "details": f"Event ID: {meeting_id}"
                }
            else:
                emoji_logger.service_error(f"❌ Erro ao cancelar [{status_code}]: {e}")
                return {
                    "success": False,
                    "error_code": status_code,
                    "message": f"Erro ao cancelar: {e}",
                    "details": f"Event ID: {meeting_id}"
                }
        except Exception as e:
            emoji_logger.service_error(f"❌ Erro inesperado ao cancelar: {e}")
            return {
                "success": False,
                "error_code": "unknown",
                "message": f"Erro inesperado: {e}",
                "details": f"Event ID: {meeting_id}"
            }
        finally:
            # Liberar o lock independentemente do resultado
            await self._release_lock()
    
    async def reschedule_meeting(self, 
                                meeting_id: str,
                                date: Optional[str] = None,
                                time: Optional[str] = None,
                                lead_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Reagenda reunião REAL no Google Calendar
        Estratégia: Cancela a reunião existente e cria uma nova
        
        Args:
            meeting_id: ID da reunião existente
            date: Nova data (YYYY-MM-DD ou string natural)
            time: Novo horário (HH:MM)
            lead_info: Informações do lead
            
        Returns:
            Dict com resultado do reagendamento
        """
        if not self.is_initialized:
            await self.initialize()
        
        # Adquirir lock para toda a operação de reagendamento
        lock_key = f"reschedule:{meeting_id}"
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning(f"⚠️ Não foi possível adquirir lock para reagendamento da reunião {meeting_id}")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para reagendamento"
            }
        
        # Variáveis para armazenar o estado da operação
        old_event_cancelled = False
        new_event_created = False
        new_meeting_id = None
        
        try:
            # Primeiro, buscar detalhes da reunião existente
            try:
                existing_event = self.service.events().get(
                    calendarId=self.calendar_id,
                    eventId=meeting_id
                ).execute()
                
                # Extrair informações do evento existente
                existing_summary = existing_event.get('summary', '')
                existing_attendees = existing_event.get('attendees', [])
                existing_description = existing_event.get('description', '')
                
            except HttpError as e:
                if e.resp.status == 404:
                    emoji_logger.service_error(f"❌ Reunião {meeting_id} não encontrada")
                    return {
                        "success": False,
                        "message": "Reunião não encontrada para reagendar",
                        "meeting_id": meeting_id
                    }
                raise
            
            # Cancelar a reunião existente
            cancel_result = await self.cancel_meeting(meeting_id)
            
            if not cancel_result.get("success") and "já foi cancelado" not in cancel_result.get("message", ""):
                return {
                    "success": False,
                    "message": f"Erro ao cancelar reunião anterior: {cancel_result.get('message')}",
                    "meeting_id": meeting_id
                }
            
            # Marcar que o evento antigo foi cancelado
            old_event_cancelled = True
            
            # Preparar informações do lead
            if not lead_info and existing_attendees:
                # Tentar extrair informações dos participantes existentes
                for attendee in existing_attendees:
                    if attendee.get('email') and '@' in attendee.get('email', ''):
                        lead_info = {
                            "email": attendee.get('email'),
                            "name": attendee.get('displayName', 'Cliente')
                        }
                        break
            
            if not lead_info:
                lead_info = {"name": "Cliente", "email": None}
            
            # Criar nova reunião com os novos parâmetros
            schedule_result = await self.schedule_meeting(
                date=date,
                time=time,
                lead_info=lead_info
            )
            
            if schedule_result.get("success"):
                new_event_created = True
                new_meeting_id = schedule_result.get("meeting_id")
                emoji_logger.calendar_event(
                    f"✅ Reunião reagendada: {meeting_id} → {schedule_result.get('meeting_id')}"
                )
                
                return {
                    "success": True,
                    "message": "Reunião reagendada com sucesso",
                    "old_meeting_id": meeting_id,
                    "new_meeting_id": schedule_result.get("meeting_id"),
                    "meeting_link": schedule_result.get("meeting_link"),
                    "datetime": schedule_result.get("datetime"),
                    "real": True
                }
            else:
                # Se falhou ao criar nova reunião, tentar informar o usuário
                emoji_logger.service_error(
                    f"❌ Falha ao criar nova reunião após cancelar {meeting_id}"
                )
                
                return {
                    "success": False,
                    "message": f"Reunião cancelada mas erro ao criar nova: {schedule_result.get('message')}",
                    "old_meeting_id": meeting_id,
                    "details": "A reunião anterior foi cancelada, mas houve erro ao criar a nova"
                }
                
        except Exception as e:
            emoji_logger.service_error(f"❌ Erro ao reagendar reunião: {e}")
            # Tentar rollback se o evento antigo foi cancelado mas o novo não foi criado
            if old_event_cancelled and not new_event_created:
                emoji_logger.service_warning(f"⚠️ Tentando rollback: recriar evento {meeting_id}")
                rollback_result = await self._rollback_reschedule(
                    meeting_id, 
                    existing_event if 'existing_event' in locals() else None,
                    lead_info
                )
                
                if rollback_result.get("success"):
                    emoji_logger.service_info("✅ Rollback realizado com sucesso")
                else:
                    emoji_logger.service_error(f"❌ Falha no rollback: {rollback_result.get('message')}")
            
            return {
                "success": False,
                "message": f"Erro ao reagendar reunião: {e}",
                "meeting_id": meeting_id,
                "rollback_attempted": old_event_cancelled and not new_event_created
            }
        finally:
            # Liberar o lock independentemente do resultado
            await self._release_lock()
    
    async def suggest_times(self, lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """Sugere horários disponíveis REAIS"""
        # Adquirir lock para sugerir horários
        lock_key = "suggest_times"
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning("⚠️ Não foi possível adquirir lock para sugerir horários")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para sugestão de horários"
            }
        
        try:
            availability = await self.check_availability("próximos dias")
            
            if availability.get("success") and availability.get("available_slots"):
                slots = availability["available_slots"][:3]
                
                return {
                    "success": True,
                    "suggested_times": slots,
                    "message": f"Tenho estes horários disponíveis amanhã: {', '.join(slots)}. Qual prefere?",
                    "real": True
                }
            
            return {
                "success": False,
                "message": "Não consegui verificar os horários no momento"
            }
        finally:
            # Liberar o lock independentemente do resultado
            await self._release_lock()
    
    async def check_availability_for_date(self, date_str: str) -> Dict[str, Any]:
        """Verifica disponibilidade para uma data específica"""
        if not self.is_initialized:
            await self.initialize()
        
        # Adquirir lock para verificar disponibilidade
        lock_key = f"availability:date:{date_str}"
        if not await self._acquire_lock(lock_key):
            emoji_logger.service_warning(f"⚠️ Não foi possível adquirir lock para verificar disponibilidade na data {date_str}")
            return {
                "success": False,
                "error": "lock_not_acquired",
                "message": "Sistema ocupado. Por favor, tente novamente em alguns segundos.",
                "details": "Não foi possível adquirir lock para verificação de disponibilidade"
            }
        
        try:
            # Converter string de data para datetime
            from datetime import datetime
            if date_str == "tomorrow" or not date_str:
                target_date = datetime.now() + timedelta(days=1)
            else:
                target_date = datetime.strptime(date_str, "%Y-%m-%d")
            
            # Buscar eventos do dia
            time_min = target_date.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
            time_max = target_date.replace(hour=23, minute=59, second=59, microsecond=0).isoformat() + 'Z'
            
            events_result = self.service.events().list(
                calendarId=self.calendar_id,
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime'
            ).execute()
            
            events = events_result.get('items', [])
            
            # Horários disponíveis (9h às 18h)
            available_slots = []
            for hour in range(9, 18):
                slot_start = target_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                slot_end = slot_start + timedelta(hours=1)
                
                # Verificar se está livre
                is_free = True
                for event in events:
                    event_start = event.get('start', {}).get('dateTime')
                    event_end = event.get('end', {}).get('dateTime')
                    
                    if event_start and event_end:
                        event_start_dt = datetime.fromisoformat(event_start.replace('Z', '+00:00')).replace(tzinfo=None)
                        event_end_dt = datetime.fromisoformat(event_end.replace('Z', '+00:00')).replace(tzinfo=None)
                        
                        if not (slot_end <= event_start_dt or slot_start >= event_end_dt):
                            is_free = False
                            break
                
                if is_free:
                    available_slots.append(f"{hour:02d}:00 - {hour+1:02d}:00")
            
            return {
                "success": True,
                "date": target_date.strftime("%Y-%m-%d"),
                "available_slots": available_slots[:5] if available_slots else ["10:00 - 11:00", "14:00 - 15:00", "16:00 - 17:00"],
                "message": f"Leonardo tem {len(available_slots)} horários disponíveis",
                "real": True
            }
            
        except Exception as e:
            emoji_logger.service_error(f"Erro ao verificar disponibilidade: {e}")
            return {
                "success": False,
                "available_slots": [],
                "message": f"Erro ao verificar disponibilidade: {e}"
            }
        finally:
            # Liberar o lock independentemente do resultado
            await self._release_lock()
    
    async def health_check(self) -> bool:
        """Verifica saúde do serviço"""
        try:
            if not self.is_initialized:
                await self.initialize()
            
            # Testar acesso ao calendário
            calendar = self.service.calendars().get(calendarId=self.calendar_id).execute()
            return calendar is not None
            
        except:
            return False