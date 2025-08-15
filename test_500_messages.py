#!/usr/bin/env python
"""
Teste do aumento de contexto para 500 mensagens
Valida que o sistema suporta histórico expandido
"""

import asyncio
from datetime import datetime
from app.agents.agentic_sdr_stateless import create_stateless_agent
from app.utils.logger import emoji_logger

async def test_500_messages_context():
    """
    Testa se o sistema processa corretamente 500 mensagens de histórico
    """
    emoji_logger.system_info("🧪 TESTE DE 500 MENSAGENS DE CONTEXTO")
    emoji_logger.system_info("=" * 60)
    
    try:
        # Criar agente stateless
        agent = await create_stateless_agent()
        
        # Criar histórico com 500 mensagens
        emoji_logger.system_info("📝 Criando histórico com 500 mensagens...")
        conversation_history = []
        
        for i in range(500):
            conversation_history.append({
                "role": "user" if i % 2 == 0 else "assistant",
                "content": f"Mensagem teste #{i+1} - Conteúdo da conversa",
                "timestamp": datetime.now().isoformat()
            })
        
        # Criar contexto de execução
        execution_context = {
            "phone": "5511999999999",
            "lead_info": {
                "name": "Cliente Teste",
                "bill_value": 600
            },
            "conversation_history": conversation_history,
            "conversation_id": "test-500",
            "timestamp": datetime.now().isoformat()
        }
        
        # Construir prompt para verificar quantas mensagens são incluídas
        prompt = agent._build_prompt_with_history(
            message="Teste com 500 mensagens",
            context={"conversation_stage": "qualificação"},
            lead_info=execution_context["lead_info"],
            service_results=[],
            media_context="",
            conversation_history=conversation_history,
            execution_context=execution_context
        )
        
        # Contar quantas mensagens foram incluídas no prompt
        messages_in_prompt = 0
        for i in range(500):
            if f"Mensagem teste #{i+1}" in prompt:
                messages_in_prompt += 1
        
        emoji_logger.system_info(f"📊 Mensagens no histórico: {len(conversation_history)}")
        emoji_logger.system_info(f"📨 Mensagens incluídas no prompt: {messages_in_prompt}")
        
        # Verificar se o prompt tem tamanho adequado
        prompt_size = len(prompt)
        emoji_logger.system_info(f"📄 Tamanho do prompt: {prompt_size:,} caracteres")
        
        # Verificar tempo de processamento
        import time
        start_time = time.time()
        
        # Simular processamento de mensagem
        response = await agent.process_message(
            message="Olá, quero saber sobre energia solar",
            execution_context=execution_context
        )
        
        processing_time = time.time() - start_time
        emoji_logger.system_info(f"⏱️ Tempo de processamento: {processing_time:.2f} segundos")
        
        # Validar resultados
        if messages_in_prompt >= 450:  # Pelo menos 450 das 500 mensagens
            emoji_logger.system_success(f"✅ TESTE PASSOU! {messages_in_prompt}/500 mensagens processadas")
            emoji_logger.system_success("✅ Sistema suporta histórico de 500 mensagens")
            emoji_logger.system_success(f"✅ Processamento em {processing_time:.2f}s")
            return True
        else:
            emoji_logger.system_error("Test", f"❌ Apenas {messages_in_prompt}/500 mensagens foram incluídas")
            return False
            
    except Exception as e:
        emoji_logger.system_error("Test", f"Erro no teste: {e}")
        import traceback
        emoji_logger.system_error("Test", f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_500_messages_context())
    exit(0 if success else 1)