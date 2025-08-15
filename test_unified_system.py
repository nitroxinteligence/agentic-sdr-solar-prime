#!/usr/bin/env python3
"""
Teste do sistema unificado - Singleton vs Stateless
"""
import asyncio
import os
from app.agents import get_agentic_agent, create_stateless_agent

async def test_unified_system():
    """Testa ambos os modos do sistema"""
    
    print("=" * 60)
    print("TESTE DO SISTEMA UNIFICADO - SINGLETON VS STATELESS")
    print("=" * 60)
    
    # Teste 1: Modo Singleton (padrão)
    print("\n1. Testando modo SINGLETON...")
    try:
        agent1 = await get_agentic_agent()
        agent2 = await get_agentic_agent()
        
        if agent1 is agent2:
            print("✅ Singleton funcionando - mesma instância retornada")
        else:
            print("❌ Erro: Singleton retornou instâncias diferentes")
    except Exception as e:
        print(f"❌ Erro no modo singleton: {e}")
    
    # Teste 2: Modo Stateless
    print("\n2. Testando modo STATELESS...")
    try:
        agent3 = await create_stateless_agent()
        agent4 = await create_stateless_agent()
        
        if agent3 is not agent4:
            print("✅ Stateless funcionando - instâncias diferentes criadas")
        else:
            print("❌ Erro: Stateless retornou a mesma instância")
    except Exception as e:
        print(f"❌ Erro no modo stateless: {e}")
    
    # Teste 3: Configuração dinâmica
    print("\n3. Testando configuração USE_STATELESS_MODE...")
    os.environ['USE_STATELESS_MODE'] = 'true'
    
    # Recarregar configurações
    from app.config import settings
    print(f"   USE_STATELESS_MODE = {settings.use_stateless_mode}")
    
    # Teste 4: Função create_agent_with_context
    print("\n4. Testando create_agent_with_context...")
    try:
        from app.api.webhooks import create_agent_with_context
        agent, context = await create_agent_with_context(
            phone="+5511999999999"
        )
        print(f"✅ Agent criado com contexto: {type(agent).__name__}")
        print(f"   Contexto inclui: {list(context.keys())}")
    except Exception as e:
        print(f"❌ Erro em create_agent_with_context: {e}")
    
    print("\n" + "=" * 60)
    print("TESTE CONCLUÍDO")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_unified_system())