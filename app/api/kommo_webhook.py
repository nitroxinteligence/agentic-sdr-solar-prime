"""
Webhook para receber eventos do Kommo CRM
"""
from fastapi import APIRouter, Request
from loguru import logger
from datetime import datetime

router = APIRouter(prefix="/webhook/kommo", tags=["kommo"])


@router.post("/events")
async def kommo_webhook(request: Request):
    """
    Recebe eventos do Kommo CRM
    """
    try:
        content_type = request.headers.get("content-type", "")

        if "application/json" in content_type:
            try:
                data = await request.json()
            except Exception:
                body = await request.body()
                data = ({"raw_data": body.decode('utf-8', errors='ignore')}
                        if body else {"event": "empty_body"})
        elif "application/x-www-form-urlencoded" in content_type:
            form_data = await request.form()
            data = dict(form_data)
        else:
            body = await request.body()
            data = ({"raw_data": body.decode('utf-8', errors='ignore')}
                    if body else {"event": "ping"})

        if data != {"event": "ping"}:
            logger.debug(f"📥 Evento Kommo recebido: {data}")

        if isinstance(data, dict):
            event_type = (
                data.get('event_type') or data.get('event') or 'unknown'
            )
            if event_type in [
                'lead.created', 'lead.updated', 'lead.status_changed'
            ]:
                logger.info(f"📌 Evento Kommo importante: {event_type}")

        return {"status": "ok", "received_at": datetime.now().isoformat()}

    except Exception as e:
        logger.error(f"❌ Erro inesperado no webhook Kommo: {e}")
        return {"status": "ok", "error_handled": True}


@router.post("/")
async def kommo_webhook_root(request: Request):
    """
    Rota alternativa para receber eventos (caso o Kommo não use /events)
    """
    try:
        data = await request.json()
        logger.info(f"📥 Evento Kommo recebido na rota raiz: {data}")
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"❌ Erro: {e}")
        return {"status": "error"}
