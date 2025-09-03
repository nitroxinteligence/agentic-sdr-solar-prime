#!/usr/bin/env python3
"""
SDR IA Solar Prime - Aplicação Principal
Ponto de entrada da aplicação FastAPI
"""

import asyncio
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importações dos módulos da aplicação
from app.config import settings
from app.utils.logger import emoji_logger
from app.integrations.redis_client import redis_client
from app.integrations.supabase_client import supabase_client
from app.services.message_buffer import get_message_buffer
from app.services.message_splitter import get_message_splitter
from app.services.followup_manager import followup_manager_service
from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.followup_executor_service import FollowUpSchedulerService
from app.services.followup_worker import FollowUpWorker
from app.services.conversation_monitor import get_conversation_monitor
from app.agents.agentic_sdr_stateless import AgenticSDRStateless

# Importações dos routers
from app.api.health import router as health_router
from app.api.webhooks import router as webhooks_router
from app.api.kommo_webhook import router as kommo_router
from app.api.google_auth import router as google_auth_router
from app.api.webhook_routes import router as webhook_routes_router

# Variáveis globais para serviços
agentic_sdr = None
followup_scheduler = None
followup_worker = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação"""
    global agentic_sdr, followup_scheduler, followup_worker
    
    # Startup
    start_time = time.time()
    emoji_logger.system_start("SDR IA Solar Prime v0.3")
    
    try:
        # Conectar ao Redis (opcional em desenvolvimento)
        try:
            await redis_client.connect()
            if redis_client.redis_client:
                emoji_logger.system_ready("Redis", data={"url": redis_client.redis_url.split('@')[-1]})
            else:
                emoji_logger.system_warning("Redis não disponível - continuando sem cache")
        except Exception as e:
            emoji_logger.system_warning(f"Redis não disponível: {e} - continuando sem cache")
        
        # Testar conexão Supabase
        if await supabase_client.test_connection():
            emoji_logger.system_ready("Supabase")
        else:
            emoji_logger.system_error("Supabase", "Falha na conexão")
        
        # Inicializar Message Buffer com configurações corretas
        from app.services.message_buffer import set_message_buffer, MessageBuffer
        message_buffer = MessageBuffer(
            timeout=settings.message_buffer_timeout,
            max_size=10
        )
        set_message_buffer(message_buffer)
        emoji_logger.system_ready("Message Buffer", data={"timeout": f"{message_buffer.timeout}s"})
        
        # Inicializar Message Splitter
        message_splitter = get_message_splitter()
        emoji_logger.system_ready("Message Splitter", data={"max_length": message_splitter.max_length})
        
        # Inicializar Conversation Monitor
        conversation_monitor = get_conversation_monitor()
        await conversation_monitor.initialize()
        emoji_logger.system_ready("Conversation Monitor")
        
        # Sistema refatorado pronto
        emoji_logger.system_ready("Sistema Refatorado", data={"modules": "Core + Services"})
        
        # Inicializar FollowUp Service
        followup_service = FollowUpServiceReal()
        emoji_logger.system_ready("FollowUp Service")
        
        # Inicializar Workers Redis (APENAS SE REDIS DISPONÍVEL)
        followup_scheduler = None
        followup_worker = None
        
        if redis_client.redis_client:
            try:
                # Inicializar FollowUp Scheduler
                followup_scheduler = FollowUpSchedulerService()
                await followup_scheduler.start()
                emoji_logger.system_ready("FollowUp Scheduler", data={"interval": f"{followup_scheduler.check_interval}s"})
            except Exception as e:
                emoji_logger.system_error(f"Erro ao inicializar FollowUp Scheduler: {e}")
                followup_scheduler = None
            
            try:
                # Inicializar FollowUp Worker  
                followup_worker = FollowUpWorker()
                await followup_worker.start()
                emoji_logger.system_ready("FollowUp Worker", data={"queue": "followup_tasks"})
            except Exception as e:
                emoji_logger.system_error(f"Erro ao inicializar FollowUp Worker: {e}")
                followup_worker = None
        else:
            emoji_logger.system_warning("Workers Redis desabilitados - Redis não disponível")
        
        # Inicializar AgenticSDR Stateless
        agentic_sdr = AgenticSDRStateless()
        await agentic_sdr.initialize()
        emoji_logger.system_ready("AgenticSDR (Stateless)", data={"status": "sistema pronto"})
        
        # FollowUp Services prontos
        redis_status = "✅ Com Redis Workers" if followup_scheduler else "⚠️ Sem Redis Workers"
        emoji_logger.system_ready("FollowUp Services", data={"redis_workers": redis_status})
        
        # Sistema pronto
        startup_time = time.time() - start_time
        emoji_logger.system_ready("SDR IA Solar Prime", startup_time=startup_time)
        
        yield
        
    except Exception as e:
        emoji_logger.system_error("Startup", f"Erro durante startup: {e}")
        raise
    
    # Shutdown
    try:
        emoji_logger.info("🔄 Iniciando shutdown...")
        
        # Parar serviços
        if message_buffer:
            await message_buffer.shutdown()
        
        conversation_monitor = get_conversation_monitor()
        if conversation_monitor:
            await conversation_monitor.shutdown()
            
        # Parar Workers Redis
        if followup_scheduler:
            await followup_scheduler.stop()
            emoji_logger.system_info("FollowUp Scheduler parado")
            
        if followup_worker:
            await followup_worker.stop()
            emoji_logger.system_info("FollowUp Worker parado")
            
        # FollowUp Manager não precisa de shutdown
            
        if redis_client:
            await redis_client.disconnect()
            
        emoji_logger.info("✅ Shutdown concluído")
        
    except Exception as e:
        emoji_logger.error(f"Erro durante shutdown: {e}")

# Criar aplicação FastAPI
app = FastAPI(
    title="SDR IA Solar Prime",
    description="Sistema de IA para automação de vendas via WhatsApp",
    version="0.3.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(health_router, tags=["health"])
app.include_router(webhooks_router, tags=["webhooks"])
app.include_router(kommo_router, tags=["kommo"])
app.include_router(google_auth_router, tags=["auth"])
app.include_router(webhook_routes_router, tags=["calendar-webhooks"])

# Endpoint raiz
@app.get("/")
async def root():
    """Endpoint raiz da aplicação"""
    return {
        "message": "SDR IA Solar Prime",
        "version": "0.3.0",
        "status": "running",
        "agent": "Helen Vieira"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        workers=1
    )