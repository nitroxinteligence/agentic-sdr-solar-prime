"""Rotas para webhooks do Google Calendar"""

from fastapi import APIRouter, Request, HTTPException
from typing import Dict, Any
from app.handlers.webhook_handler import webhook_handler
from app.utils.logger import emoji_logger

router = APIRouter(prefix="/webhooks", tags=["webhooks"])


@router.post("/google-calendar")
async def google_calendar_webhook(request: Request) -> Dict[str, Any]:
    """Endpoint para receber webhooks do Google Calendar"""
    try:
        emoji_logger.system_info(
            "🔔 Webhook", "Recebido webhook do Google Calendar"
        )
        
        # Processar o webhook
        result = await webhook_handler.handle_calendar_event(request)
        
        if result.get("success"):
            emoji_logger.system_success(
                "🔔 Webhook", f"Processado com sucesso: {result.get('action')}"
            )
            return {"status": "success", "data": result}
        else:
            emoji_logger.system_warning(
                "🔔 Webhook", f"Erro no processamento: {result.get('error')}"
            )
            return {"status": "error", "error": result.get("error")}
            
    except Exception as e:
        emoji_logger.system_error(
            "🔔 Webhook", f"Erro crítico no webhook: {e}"
        )
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/google-calendar/health")
async def webhook_health_check() -> Dict[str, str]:
    """Health check para o endpoint de webhook"""
    return {"status": "healthy", "service": "google-calendar-webhook"}