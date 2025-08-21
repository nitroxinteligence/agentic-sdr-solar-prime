"""
SDR IA Solar Prime - Aplicação Principal
Powered by AGnO Teams Framework
"""
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from loguru import logger
from app.utils.logger import emoji_logger

from app.config import settings
from app.api import health, webhooks  # teams module not yet implemented
from app.integrations.supabase_client import supabase_client
from app.integrations.redis_client import redis_client
# from app.teams import create_sdr_team  # Removed - using refactored system

# Configuração do logger
logger.add(
    "logs/app.log",
    rotation="1 day",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação
    """
    # Startup
    emoji_logger.system_start("SDR IA Solar Prime v0.3")
    
    try:
        # Conecta ao Redis
        await redis_client.connect()
        emoji_logger.system_ready("Redis")
        
        # Testa conexão com Supabase
        await supabase_client.test_connection()
        emoji_logger.system_ready("Supabase")
        
        # Inicializa Message Buffer
        from app.services.message_buffer import set_message_buffer, MessageBuffer
        from app.config import settings
        
        if settings.enable_message_buffer:
            message_buffer = MessageBuffer(
                timeout=settings.message_buffer_timeout,
                max_size=10
            )
            set_message_buffer(message_buffer)
            emoji_logger.system_ready("Message Buffer", timeout=f"{settings.message_buffer_timeout}s")
        
        # Inicializa Message Splitter
        from app.services.message_splitter import set_message_splitter, MessageSplitter
        
        if settings.enable_message_splitter:
            message_splitter = MessageSplitter(
                max_length=settings.message_max_length,
                add_indicators=settings.message_add_indicators,
                enable_smart_splitting=settings.enable_smart_splitting,
                smart_splitting_fallback=settings.smart_splitting_fallback
            )
            set_message_splitter(message_splitter)
            emoji_logger.system_ready("Message Splitter", max_length=settings.message_max_length)
        
        # Team SDR removido - usando sistema refatorado com módulos centrais
        # Os serviços são inicializados diretamente quando necessário
        emoji_logger.system_ready("Sistema Refatorado", modules="Core + Services")
        
        # Kommo Auto Sync removido - usava sistema antigo de teams
        # Sincronização agora é feita diretamente pelo CRMServiceReal
        
        
        # Inicializa FollowUp Scheduler e Worker
        if settings.enable_follow_up_automation:
            try:
                from app.services.followup_executor_service import FollowUpSchedulerService
                from app.services.followup_worker import FollowUpWorker

                scheduler = FollowUpSchedulerService()
                worker = FollowUpWorker()
                
                await scheduler.start()
                await worker.start()
                
                emoji_logger.system_ready("FollowUp Services (Scheduler & Worker)")
            except Exception as e:
                emoji_logger.system_warning(f"⚠️ FollowUp Services não iniciados: {str(e)}")
        
        # PRÉ-AQUECIMENTO: Instancia o agente para carregar modelos e serviços
        from app.agents.agentic_sdr_stateless import AgenticSDRStateless
        
        agent_mode = "Stateless"
        
        try:
            emoji_logger.system_info(f"🔥 Pré-aquecendo AgenticSDR ({agent_mode})...")
            test_agent = AgenticSDRStateless()
            await test_agent.initialize()
            emoji_logger.system_ready(f"AgenticSDR ({agent_mode})", status="sistema pronto")
        except Exception as e:
            emoji_logger.system_error("AgenticSDR", f"Falha no pré-aquecimento: {e}")
            # Em caso de falha, a aplicação não deve subir para evitar instabilidade
            raise
        
        emoji_logger.system_ready("SDR IA Solar Prime", startup_time=3.0)
        
    except Exception as e:
        emoji_logger.system_error("SDR IA Solar Prime", f"Erro na inicialização: {e}")
        raise
    
    yield
    
    # Shutdown
    emoji_logger.system_info("Encerrando SDR IA Solar Prime...")
    
    try:
        # Kommo Auto Sync removido - usava sistema antigo
        
        
        # Para FollowUp Executor Service
        if settings.enable_follow_up_automation:
            from app.services.followup_executor_service import followup_executor_service
            await followup_executor_service.stop()
            emoji_logger.system_info("FollowUp Executor encerrado")
        
        # Cancela tasks do Message Buffer se existir
        from app.services.message_buffer import message_buffer
        if message_buffer:
            await message_buffer.shutdown()
            emoji_logger.system_info("Message Buffer encerrado")
        
        # Desconecta do Redis (já faz close/aclose internamente)
        await redis_client.disconnect()
        emoji_logger.system_info("Redis desconectado")
        
        emoji_logger.system_info("SDR IA Solar Prime encerrado com sucesso")
        
    except Exception as e:
        emoji_logger.system_error("Shutdown", str(e))

# Cria aplicação FastAPI
app = FastAPI(
    title="SDR IA Solar Prime",
    description="Sistema Inteligente de Vendas para Energia Solar - Powered by AGnO Teams",
    version="0.3.0",  # Pure Stateless Architecture
    lifespan=lifespan
)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(",") if hasattr(settings, 'cors_origins') else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra rotas
app.include_router(health.router)
app.include_router(webhooks.router)
# app.include_router(teams.router)  # Teams router not yet implemented

# Registra webhook do Kommo
from app.api import kommo_webhook
app.include_router(kommo_webhook.router)

# Registra rotas do Google OAuth
from app.api import google_auth
app.include_router(google_auth.router)

# Rotas de teste (apenas em desenvolvimento)
if settings.debug:
    from app.api import test_kommo
    app.include_router(test_kommo.router)

# Exception handler global
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    Tratamento global de exceções
    """
    emoji_logger.system_error("Global Exception Handler", str(exc))
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": str(exc) if settings.debug else "An error occurred",
            "path": str(request.url)
        }
    )

# Rota raiz
@app.get("/")
async def root():
    """
    Endpoint raiz - Informações da API
    """
    return {
        "name": "SDR IA Solar Prime",
        "version": "0.2.0",
        "framework": "AGnO Teams",
        "status": "operational",
        "endpoints": {
            "health": "/health",
            "webhooks": "/webhooks",
            "teams": "/teams"
        },
        "documentation": "/docs",
        "team_mode": "COORDINATE"
    }

# Health check principal
@app.get("/health")
async def health_check():
    """
    Health check geral do sistema
    """
    try:
        # Verifica Redis
        redis_status = await redis_client.ping()
        
        # Verifica Supabase
        supabase_status = await supabase_client.test_connection()
        
        # Status do Team
        team_status = "ready"  # Simplificado para evitar criar múltiplas instâncias
        
        return {
            "status": "healthy",
            "services": {
                "redis": "connected" if redis_status else "disconnected",
                "supabase": "connected" if supabase_status else "disconnected",
                "team": team_status
            }
        }
    except Exception as e:
        emoji_logger.system_error("Health Check", str(e))
        return {
            "status": "unhealthy",
            "error": str(e)
        }

if __name__ == "__main__":
    # Configurações do servidor
    host = settings.api_host if hasattr(settings, 'api_host') else "0.0.0.0"
    port = int(settings.api_port) if hasattr(settings, 'api_port') else 8000
    reload = settings.debug if hasattr(settings, 'debug') else False
    
    emoji_logger.system_start(f"Servidor Uvicorn em {host}:{port}")
    
    # Inicia servidor
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info" if not reload else "debug"
    )