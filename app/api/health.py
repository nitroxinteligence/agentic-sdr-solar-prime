"""
Health Check API - Endpoints de saúde do sistema
"""
from fastapi import APIRouter
from datetime import datetime
from loguru import logger

from app.integrations.supabase_client import supabase_client
from app.integrations.evolution import evolution_client
from app.integrations.redis_client import redis_client
from app.agents.agentic_sdr_stateless import AgenticSDRStateless

router = APIRouter()


@router.get("/")
async def health_check():
    """Health check básico"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "SDR IA SolarPrime"
    }


@router.get("/health")
async def health_endpoint():
    """Endpoint /health para compatibilidade"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "SDR IA SolarPrime"
    }


@router.get("/live")
async def liveness():
    """Liveness probe para Kubernetes"""
    return {"status": "alive"}


@router.get("/ready")
async def readiness():
    """Readiness probe - verifica se o serviço está pronto"""
    try:
        # Instanciar agente para verificação
        agent = AgenticSDRStateless()
        await agent.initialize()

        checks = {
            "supabase": await supabase_client.test_connection(),
            "evolution": await evolution_client.test_connection(),
            "agent": agent.is_initialized,
            "redis": await redis_client.ping()
        }
        is_ready = all(checks.values())
        return {
            "ready": is_ready,
            "checks": checks,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Erro no readiness check: {e}")
        return {
            "ready": False,
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


@router.get("/metrics")
async def metrics():
    """Métricas do sistema para monitoramento"""
    try:
        metrics_data = {
            "timestamp": datetime.now().isoformat(),
            "counters": {},
            "gauges": {},
            "histograms": {}
        }

        # Obtém métricas do Redis se disponível
        if await redis_client.ping():
            # Contadores
            messages_processed = await redis_client.get_counter(
                "messages_processed"
            )
            metrics_data["counters"]["messages_processed"] = messages_processed
            leads_created = await redis_client.get_counter("leads_created")
            metrics_data["counters"]["leads_created"] = leads_created
            meetings_scheduled = await redis_client.get_counter(
                "meetings_scheduled"
            )
            metrics_data["counters"]["meetings_scheduled"] = meetings_scheduled

            # Gauges (valores atuais)
            connection_status = await redis_client.get(
                "whatsapp:connection_status"
            )
            if connection_status:
                is_open = connection_status.get("state") == "open"
                metrics_data["gauges"]["whatsapp_connected"] = (
                    1 if is_open else 0
                )

        # Obtém estatísticas do banco se disponível
        if await supabase_client.test_connection():
            try:
                stats = await supabase_client.get_daily_stats()
                metrics_data["gauges"]["leads_today"] = stats.get(
                    "leads_today", 0
                )
                metrics_data["gauges"]["conversations_active"] = stats.get(
                    "conversations_active", 0
                )
            except Exception:
                pass

        return metrics_data

    except Exception as e:
        logger.error(f"Erro ao obter métricas: {e}")
        return {
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


@router.get("/dependencies")
async def check_dependencies():
    """Verifica status de todas as dependências"""
    dependencies = {}

    # Supabase
    try:
        connected = await supabase_client.test_connection()
        dependencies["supabase"] = {
            "status": "healthy" if connected else "unhealthy",
            "type": "database"
        }
    except Exception as e:
        dependencies["supabase"] = {
            "status": "unhealthy",
            "error": str(e),
            "type": "database"
        }

    # Evolution API
    try:
        connected = await evolution_client.test_connection()
        dependencies["evolution_api"] = {
            "status": "healthy" if connected else "unhealthy",
            "type": "whatsapp"
        }
    except Exception as e:
        dependencies["evolution_api"] = {
            "status": "unhealthy",
            "error": str(e),
            "type": "whatsapp"
        }

    # Redis
    try:
        await redis_client.connect()
        if await redis_client.ping():
            dependencies["redis"] = {
                "status": "healthy",
                "type": "cache"
            }
        else:
            dependencies["redis"] = {
                "status": "unhealthy",
                "type": "cache"
            }
    except Exception as e:
        dependencies["redis"] = {
            "status": "unhealthy",
            "error": str(e),
            "type": "cache"
        }

    # Google Calendar (funciona mas sem sync com Supabase)
    try:
        from app.config import settings
        if settings.google_service_account_email:
            dependencies["google_calendar"] = {
                "status": "configured",
                "type": "calendar",
                "message": "Funcionando sem sync Supabase"
            }
        else:
            dependencies["google_calendar"] = {
                "status": "not_configured",
                "type": "calendar"
            }
    except Exception:
        dependencies["google_calendar"] = {
            "status": "not_configured",
            "type": "calendar"
        }

    # Kommo CRM (se configurado)
    try:
        from app.config import settings
        if settings.KOMMO_LONG_LIVED_TOKEN:
            dependencies["kommo_crm"] = {
                "status": "configured",
                "type": "crm"
            }
        else:
            dependencies["kommo_crm"] = {
                "status": "not_configured",
                "type": "crm"
            }
    except Exception:
        dependencies["kommo_crm"] = {
            "status": "not_configured",
            "type": "crm"
        }

    # Determina status geral
    all_healthy = all(
        dep.get("status") in ["healthy", "configured"]
        for dep in dependencies.values()
    )

    return {
        "status": "healthy" if all_healthy else "degraded",
        "dependencies": dependencies,
        "timestamp": datetime.now().isoformat()
    }


@router.get("/info")
async def service_info():
    """Informações sobre o serviço"""
    from app.config import settings

    return {
        "service": "SDR IA SolarPrime",
        "version": "0.2.0",
        "environment": settings.ENVIRONMENT,
        "agent": "Helen Vieira",
        "company": "Solar Prime Boa Viagem",
        "features": {
            "whatsapp": True,
            "ai_qualification": True,
            "google_calendar": bool(settings.GOOGLE_SERVICE_ACCOUNT_PATH),
            "kommo_crm": bool(settings.KOMMO_LONG_LIVED_TOKEN),
            "follow_up": True,
            "reports": True
        },
        "business_hours": {
            "start": settings.BUSINESS_HOURS_START,
            "end": settings.BUSINESS_HOURS_END,
            "timezone": settings.TIMEZONE
        }
    }


# ============================================================================
# ENDPOINTS TEMPORÁRIOS PARA CORREÇÃO DO AGENTE
# ============================================================================

@router.get("/debug-clear-pauses")
async def debug_clear_pauses():
    """TEMPORÁRIO: Limpa pausas via GET para facilitar teste no navegador"""
    try:
        if not redis_client.redis_client:
            await redis_client.connect()
        
        if not redis_client.redis_client:
            return {"error": "Redis não disponível", "status": "failed"}
        
        # Buscar todas as pausas ativas
        handoff_keys = await redis_client.redis_client.keys("lead:pause:*")
        not_interested_keys = await redis_client.redis_client.keys("lead:not_interested:*")
        
        cleared_handoff = 0
        cleared_not_interested = 0
        
        # Limpar pausas handoff
        for key in handoff_keys:
            phone = key.replace("lead:pause:", "")
            if await redis_client.clear_human_handoff_pause(phone):
                cleared_handoff += 1
        
        # Limpar pausas not_interested  
        for key in not_interested_keys:
            phone = key.replace("lead:not_interested:", "")
            if await redis_client.clear_not_interested_pause(phone):
                cleared_not_interested += 1
        
        result = {
            "status": "success",
            "message": "🧹 PAUSAS REMOVIDAS COM SUCESSO!",
            "cleared": {
                "handoff_pauses": cleared_handoff,
                "not_interested_pauses": cleared_not_interested,
                "total": cleared_handoff + cleared_not_interested
            },
            "next_steps": [
                "1. Envie uma mensagem real no WhatsApp",
                "2. Verifique se o agente responde normalmente",
                "3. Monitore os logs para confirmar funcionamento"
            ]
        }
        
        logger.info(f"🧹 CORREÇÃO APLICADA: {result}")
        return result
        
    except Exception as e:
        error_msg = f"Erro ao limpar pausas: {e}"
        logger.error(error_msg)
        return {"error": error_msg, "status": "failed"}


@router.get("/debug-check-pauses")
async def debug_check_pauses():
    """TEMPORÁRIO: Verifica pausas ativas via GET"""
    try:
        if not redis_client.redis_client:
            await redis_client.connect()
        
        if not redis_client.redis_client:
            return {"error": "Redis não disponível", "status": "failed"}
        
        # Buscar pausas ativas
        handoff_keys = await redis_client.redis_client.keys("lead:pause:*")
        not_interested_keys = await redis_client.redis_client.keys("lead:not_interested:*")
        
        handoff_phones = [key.replace("lead:pause:", "") for key in handoff_keys]
        not_interested_phones = [key.replace("lead:not_interested:", "") for key in not_interested_keys]
        
        total = len(handoff_keys) + len(not_interested_keys)
        
        result = {
            "status": "success",
            "active_pauses": {
                "handoff": {
                    "count": len(handoff_phones),
                    "phones": handoff_phones[:10]  # Mostrar apenas primeiros 10
                },
                "not_interested": {
                    "count": len(not_interested_phones),
                    "phones": not_interested_phones[:10]  # Mostrar apenas primeiros 10
                },
                "total": total
            },
            "message": f"📊 {total} pausas ativas encontradas" if total > 0 else "✅ Nenhuma pausa ativa",
            "blocked_phones": {
                "558182556406": "Verifique se este número específico está pausado"
            }
        }
        
        return result
        
    except Exception as e:
        error_msg = f"Erro ao verificar pausas: {e}"
        logger.error(error_msg)
        return {"error": error_msg, "status": "failed"}


@router.get("/debug-test-followup")
async def debug_test_followup():
    """TEMPORÁRIO: Testa valores válidos para follow_up type"""
    try:
        from app.config import FOLLOW_UP_TYPES
        from app.integrations.supabase_client import supabase_client
        
        # Testar inserção com cada tipo
        test_results = {}
        
        for follow_type in FOLLOW_UP_TYPES:
            try:
                # Dados mínimos para teste
                test_data = {
                    "lead_id": "00000000-0000-0000-0000-000000000000",  # UUID fake
                    "phone_number": "5581999999999",
                    "message": f"Teste {follow_type}",
                    "scheduled_at": "2025-01-01T12:00:00Z",
                    "status": "pending",
                    "type": follow_type,
                    "follow_up_type": "CUSTOM",
                    "created_at": "2025-01-01T12:00:00Z",
                    "updated_at": "2025-01-01T12:00:00Z",
                    "priority": "medium",
                    "attempts": 0
                }
                
                # Tentar inserir (vai falhar mas mostra o erro)
                result = await supabase_client.create_follow_up(test_data)
                test_results[follow_type] = {"status": "success", "result": "OK"}
                
            except Exception as e:
                error_msg = str(e)
                if "follow_ups_type_check" in error_msg:
                    test_results[follow_type] = {
                        "status": "constraint_error", 
                        "error": "Valor não aceito pela constraint"
                    }
                else:
                    test_results[follow_type] = {
                        "status": "other_error", 
                        "error": error_msg[:100]
                    }
        
        return {
            "status": "test_completed",
            "follow_up_types_config": FOLLOW_UP_TYPES,
            "test_results": test_results,
            "summary": {
                "total_types": len(FOLLOW_UP_TYPES),
                "constraint_errors": len([r for r in test_results.values() if r["status"] == "constraint_error"]),
                "valid_types": len([r for r in test_results.values() if r["status"] == "success"])
            }
        }
        
    except Exception as e:
        return {"error": f"Erro no teste: {e}", "status": "failed"}
