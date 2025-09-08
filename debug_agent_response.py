#!/usr/bin/env python3
"""
Debug para verificar por que o agente não está respondendo
"""
import asyncio
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.integrations.redis_client import redis_client

async def debug_agent_response():
    """Debug completo do problema de resposta do agente"""
    
    print("🔍 DIAGNÓSTICO: Por que o agente não responde?")
    print("=" * 50)
    
    # Telefone do log
    phone_number = "558182556406"
    
    try:
        # Conectar ao Redis
        if not redis_client.redis_client:
            await redis_client.connect()
        
        if not redis_client.redis_client:
            print("❌ REDIS NÃO DISPONÍVEL - Esta pode ser a causa!")
            return
        
        print("✅ Redis conectado")
        
        # Verificar pausas ativas
        print(f"\n📱 Verificando pausas para {phone_number}:")
        
        handoff_active = await redis_client.is_human_handoff_active(phone_number)
        not_interested_active = await redis_client.is_not_interested_active(phone_number)
        
        print(f"   🤝 Pausa Handoff: {'🔴 ATIVA' if handoff_active else '🟢 Inativa'}")
        print(f"   🚫 Pausa Not Interested: {'🔴 ATIVA' if not_interested_active else '🟢 Inativa'}")
        
        if handoff_active or not_interested_active:
            print("\n🚨 PROBLEMA IDENTIFICADO: PAUSAS ATIVAS BLOQUEANDO AGENTE!")
            
            choice = input("\nDeseja limpar as pausas? (y/N): ").strip().lower()
            if choice == 'y':
                if handoff_active:
                    await redis_client.clear_human_handoff_pause(phone_number)
                    print("✅ Pausa handoff removida")
                
                if not_interested_active:
                    await redis_client.clear_not_interested_pause(phone_number)
                    print("✅ Pausa not_interested removida")
                
                print("🎉 Pausas removidas! Teste enviar uma mensagem agora.")
            else:
                print("ℹ️ Pausas não foram removidas.")
        else:
            print("✅ Nenhuma pausa ativa encontrada")
        
        # Verificar outras possíveis causas
        print(f"\n🔍 OUTRAS VERIFICAÇÕES:")
        
        # Verificar cache de conversa
        conversation = await redis_client.get_conversation(phone_number)
        print(f"   💬 Cache de conversa: {'📦 Existe' if conversation else '📭 Vazio'}")
        
        # Verificar informações do lead
        lead_info = await redis_client.get_lead_info(phone_number)
        print(f"   👤 Informações do lead: {'📦 Existe' if lead_info else '📭 Vazio'}")
        
        # Listar todas as pausas ativas no sistema
        print(f"\n📋 PAUSAS ATIVAS NO SISTEMA:")
        
        handoff_keys = await redis_client.redis_client.keys("lead:pause:*")
        not_interested_keys = await redis_client.redis_client.keys("lead:not_interested:*")
        
        print(f"   🤝 Handoff pausas: {len(handoff_keys)}")
        for key in handoff_keys[:5]:  # Mostrar só as primeiras 5
            phone = key.replace("lead:pause:", "")
            print(f"      📱 {phone}")
        
        if len(handoff_keys) > 5:
            print(f"      ... e mais {len(handoff_keys) - 5}")
        
        print(f"   🚫 Not Interested pausas: {len(not_interested_keys)}")
        for key in not_interested_keys[:5]:  # Mostrar só as primeiras 5
            phone = key.replace("lead:not_interested:", "")
            print(f"      📱 {phone}")
        
        if len(not_interested_keys) > 5:
            print(f"      ... e mais {len(not_interested_keys) - 5}")
        
        # Dicas de solução
        print(f"\n💡 POSSÍVEIS CAUSAS E SOLUÇÕES:")
        print(f"1. 🔴 Pausas ativas → Limpar com esta ferramenta")
        print(f"2. 📱 Evolution API não envia MESSAGES_UPSERT → Verificar configuração")
        print(f"3. 🔧 Servidor não processa mensagens → Verificar logs do webhook")
        print(f"4. ⚡ Redis não disponível → Verificar conexão")
        print(f"5. 🚫 Rate limiting → Verificar limites de API")
        
    except Exception as e:
        print(f"❌ Erro no diagnóstico: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(debug_agent_response())