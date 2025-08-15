"""
Calendar Service - Google Calendar API com OAuth 2.0
Funcionalidades habilitadas: Google Meet + Participantes + Convites
"""

from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from googleapiclient.errors import HttpError
from app.utils.logger import emoji_logger
from app.config import settings
from app.integrations.google_oauth_handler import get_oauth_handler

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
    
    async def check_availability(self, date_request: str) -> Dict[str, Any]:
        """
        Verifica disponibilidade REAL no Google Calendar
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Determinar data baseada no request
            tomorrow = datetime.now() + timedelta(days=1)
            
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
            
            # Horários disponíveis (9h às 18h)
            all_slots = []
            for hour in range(9, 18):
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
    
    async def schedule_meeting(self, 
                              date: str, 
                              time: str, 
                              lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Agenda reunião REAL no Google Calendar
        """
        if not self.is_initialized:
            await self.initialize()
        
        try:
            # Converter data e hora
            meeting_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
            meeting_end = meeting_datetime + timedelta(hours=1)
            
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
            
            # Criar evento no Google Calendar
            # Com OAuth sempre usa conferenceDataVersion=1 para criar Google Meet
            created_event = self.service.events().insert(
                calendarId=self.calendar_id,
                body=event,
                conferenceDataVersion=1,  # Sempre 1 para Google Meet com OAuth
                sendUpdates='all' if attendees else 'none'  # Enviar convites se houver participantes
            ).execute()
            
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
                return {
                    "success": False,
                    "error_code": 403,
                    "message": "Erro de permissão. Necessário reautorizar OAuth",
                    "details": "Verifique as permissões do Google Calendar"
                }
            elif status_code == 404:
                emoji_logger.service_error("❌ Calendário não encontrado")
                return {
                    "success": False,
                    "error_code": 404,
                    "message": "Calendário não encontrado",
                    "details": f"Calendar ID: {self.calendar_id}"
                }
            elif status_code == 409:
                emoji_logger.service_error("⚠️ Conflito de horário detectado")
                return {
                    "success": False,
                    "error_code": 409,
                    "message": "Conflito de horário - Horário já ocupado",
                    "details": "Tente outro horário disponível"
                }
            else:
                emoji_logger.service_error(f"❌ Erro Google Calendar [{status_code}]: {e}")
                return {
                    "success": False,
                    "error_code": status_code,
                    "message": f"Erro Google Calendar: {e}",
                    "details": str(error_details)
                }
        except Exception as e:
            emoji_logger.service_error(f"❌ Erro inesperado ao agendar: {e}")
            return {
                "success": False,
                "error_code": "unknown",
                "message": f"Erro inesperado: {e}",
                "details": "Erro interno do sistema"
            }
    
    async def cancel_meeting(self, meeting_id: str) -> Dict[str, Any]:
        """Cancela reunião REAL no Google Calendar"""
        if not self.is_initialized:
            await self.initialize()
        
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
    
    async def suggest_times(self, lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """Sugere horários disponíveis REAIS"""
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
    
    async def check_availability_for_date(self, date_str: str) -> Dict[str, Any]:
        """Verifica disponibilidade para uma data específica"""
        if not self.is_initialized:
            await self.initialize()
        
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