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
from app.services.message_buffer import message_buffer
from app.services.message_splitter import message_splitter
from app.services.followup_manager import followup_manager_service
from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.conversation_monitor import get_conversation_monitor
from app.agents.agentic_sdr_stateless import AgenticSDRStateless

# Importações dos routers
from app.api.health import router as health_router
from app.api.webhooks import router as webhooks_router
from app.api.kommo_webhook import router as kommo_router
from app.api.google_auth import router as google_auth_router

# Variáveis globais para serviços
agentic_sdr = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação"""
    global agentic_sdr
    
    # Startup
    start_time = time.time()
    emoji_logger.system_start("SDR IA Solar Prime v0.3")
    
    try:
        # Inicializar Redis
        await redis_client.connect()
        emoji_logger.system_ready("Redis")
        
        # Inicializar Supabase
        await supabase_client.initialize()
        emoji_logger.system_ready("Supabase")
        
        # Inicializar Message Buffer
        await message_buffer.initialize()
        emoji_logger.system_ready("Message Buffer", data={"timeout": f"{message_buffer.timeout}s"})
        
        # Inicializar Message Splitter
        await message_splitter.initialize()
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
        
        # Inicializar AgenticSDR Stateless
        agentic_sdr = AgenticSDRStateless()
        await agentic_sdr.initialize()
        emoji_logger.system_ready("AgenticSDR (Stateless)", data={"status": "sistema pronto"})
        
        # FollowUp Services prontos
        emoji_logger.system_ready("FollowUp Services")
        
        # Pré-aquecer o sistema
        emoji_logger.info("🔥 Pré-aquecendo AgenticSDR (Stateless)...")
        warmup_agent = AgenticSDRStateless()
        await warmup_agent.initialize()
        
        # Sistema pronto
        startup_time = time.time() - start_time
        emoji_logger.system_ready("SDR IA Solar Prime", startup_time=startup_time)
        
        yield
        
    except Exception as e:
        emoji_logger.error(f"Erro durante startup: {e}")
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