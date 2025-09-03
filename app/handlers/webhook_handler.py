"""Webhook Handler para eventos do Google Calendar"""

from typing import Dict, Any, Optional
from datetime import datetime
from fastapi import Request, HTTPException
import json
import hmac
import hashlib
from app.utils.logger import emoji_logger
from app.integrations.supabase_client import SupabaseClient
from app.config import settings
from app.enums import MeetingStatus


class GoogleCalendarWebhookHandler:
    """Handler para webhooks do Google Calendar"""
    
    def __init__(self):
        self.db = SupabaseClient()
        self.webhook_secret = getattr(settings, 'google_webhook_secret', None)
    
    async def handle_calendar_event(self, request: Request) -> Dict[str, Any]:
        """Processa eventos de webhook do Google Calendar"""
        try:
            # Verificar headers necessários
            resource_id = request.headers.get('X-Goog-Resource-ID')
            resource_state = request.headers.get('X-Goog-Resource-State')
            
            if not resource_id or not resource_state:
                emoji_logger.system_warning(
                    "GoogleWebhook", "Headers obrigatórios ausentes"
                )
                return {"success": False, "error": "missing_headers"}
            
            # Verificar assinatura se configurada
            if self.webhook_secret:
                if not await self._verify_signature(request):
                    raise HTTPException(status_code=401, detail="Invalid signature")
            
            # Processar diferentes tipos de eventos
            if resource_state == 'sync':
                # Evento de sincronização inicial - ignorar
                emoji_logger.system_debug(
                    "GoogleWebhook", "Evento de sincronização recebido"
                )
                return {"success": True, "action": "sync_ignored"}
            
            elif resource_state in ['updated', 'deleted']:
                # Evento de atualização ou cancelamento
                return await self._process_event_change(resource_id, resource_state)
            
            else:
                emoji_logger.system_warning(
                    "GoogleWebhook", f"Estado desconhecido: {resource_state}"
                )
                return {"success": False, "error": "unknown_state"}
                
        except Exception as e:
            emoji_logger.system_error(
                "GoogleWebhook", f"Erro ao processar webhook: {e}"
            )
            return {"success": False, "error": str(e)}
    
    async def _verify_signature(self, request: Request) -> bool:
        """Verifica assinatura do webhook para segurança"""
        try:
            signature = request.headers.get('X-Goog-Signature')
            if not signature:
                return False
            
            body = await request.body()
            expected_signature = hmac.new(
                self.webhook_secret.encode(),
                body,
                hashlib.sha256
            ).hexdigest()
            
            return hmac.compare_digest(signature, expected_signature)
            
        except Exception as e:
            emoji_logger.system_error(
                "GoogleWebhook", f"Erro na verificação de assinatura: {e}"
            )
            return False
    
    async def _process_event_change(self, resource_id: str, state: str) -> Dict[str, Any]:
        """Processa mudanças em eventos do calendário"""
        try:
            # Buscar o evento no Google Calendar para obter detalhes
            from app.services.calendar_service_100_real import CalendarServiceReal
            calendar_service = CalendarServiceReal()
            await calendar_service.initialize()
            
            # Tentar obter o evento
            event_data = await calendar_service.get_event(resource_id)
            
            if not event_data and state == 'deleted':
                # Evento foi deletado - processar cancelamento
                return await self._handle_event_cancellation(resource_id)
            
            elif event_data:
                # Evento ainda existe - verificar status
                event_status = event_data.get('status', '').lower()
                
                if event_status == 'cancelled':
                    return await self._handle_event_cancellation(resource_id)
                elif event_status == 'confirmed':
                    return await self._handle_event_confirmation(resource_id, event_data)
                else:
                    emoji_logger.system_debug(
                        "GoogleWebhook", f"Status do evento: {event_status}"
                    )
                    return {"success": True, "action": "no_action_needed"}
            
            return {"success": True, "action": "event_not_found"}
            
        except Exception as e:
            emoji_logger.system_error(
                "GoogleWebhook", f"Erro ao processar mudança de evento: {e}"
            )
            return {"success": False, "error": str(e)}
    
    async def _handle_event_cancellation(self, event_id: str) -> Dict[str, Any]:
        """Processa cancelamento de evento"""
        try:
            # Buscar lead_qualification pelo google_event_id
            qualification = self.db.client.table('leads_qualifications').select(
                "id, lead_id, google_event_id, meeting_status"
            ).eq('google_event_id', event_id).execute()
            
            if not qualification.data:
                emoji_logger.system_warning(
                    "GoogleWebhook", f"Qualificação não encontrada para evento: {event_id}"
                )
                return {"success": True, "action": "qualification_not_found"}
            
            qualification_data = qualification.data[0]
            qualification_id = qualification_data['id']
            lead_id = qualification_data['lead_id']
            current_status = qualification_data.get('meeting_status')
            
            # Atualizar status para CANCELADO se não estiver já cancelado
            if current_status != MeetingStatus.CANCELLED.value:
                self.db.client.table('leads_qualifications').update({
                    'meeting_status': MeetingStatus.CANCELLED.value,
                    'updated_at': datetime.now().isoformat()
                }).eq('id', qualification_id).execute()
                
                emoji_logger.system_info(
                    f"📅 Reunião cancelada via webhook: Lead {lead_id} - Evento {event_id}"
                )
                
                return {
                    "success": True,
                    "action": "meeting_cancelled",
                    "lead_id": lead_id,
                    "event_id": event_id
                }
            else:
                return {
                    "success": True,
                    "action": "already_cancelled",
                    "lead_id": lead_id
                }
                
        except Exception as e:
            emoji_logger.system_error(
                "GoogleWebhook", f"Erro ao processar cancelamento: {e}"
            )
            return {"success": False, "error": str(e)}
    
    async def _handle_event_confirmation(self, event_id: str, event_data: Dict[str, Any]) -> Dict[str, Any]:
        """Processa confirmação/atualização de evento"""
        try:
            # Buscar lead_qualification pelo google_event_id
            qualification = self.db.client.table('leads_qualifications').select(
                "id, lead_id, google_event_id, meeting_status"
            ).eq('google_event_id', event_id).execute()
            
            if not qualification.data:
                return {"success": True, "action": "qualification_not_found"}
            
            qualification_data = qualification.data[0]
            qualification_id = qualification_data['id']
            lead_id = qualification_data['lead_id']
            current_status = qualification_data.get('meeting_status')
            
            # Atualizar para AGENDADO se estava cancelado
            if current_status == MeetingStatus.CANCELLED.value:
                self.db.client.table('leads_qualifications').update({
                    'meeting_status': MeetingStatus.SCHEDULED.value,
                    'updated_at': datetime.now().isoformat()
                }).eq('id', qualification_id).execute()
                
                emoji_logger.system_info(
                    f"📅 Reunião reconfirmada via webhook: Lead {lead_id} - Evento {event_id}"
                )
                
                return {
                    "success": True,
                    "action": "meeting_reconfirmed",
                    "lead_id": lead_id,
                    "event_id": event_id
                }
            
            return {"success": True, "action": "no_status_change"}
            
        except Exception as e:
            emoji_logger.system_error(
                "GoogleWebhook", f"Erro ao processar confirmação: {e}"
            )
            return {"success": False, "error": str(e)}


# Instância global do handler
webhook_handler = GoogleCalendarWebhookHandler()