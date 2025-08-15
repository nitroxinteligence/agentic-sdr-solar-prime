#!/usr/bin/env python3
"""
Teste rápido para verificar correção do import
"""

import asyncio
from app.api.webhooks import create_stateless_agent

async def test():
    print("🔍 Testando import de create_stateless_agent...")
    
    try:
        # Tenta criar agente
        agent = await create_stateless_agent()
        print("✅ Import funcionando corretamente!")
        print(f"✅ Agente criado: {type(agent).__name__}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test())
    
    if success:
        print("\n🎉 CORREÇÃO APLICADA COM SUCESSO!")
        print("O sistema agora pode processar mensagens normalmente.")
    else:
        print("\n⚠️ Ainda há problemas a resolver")