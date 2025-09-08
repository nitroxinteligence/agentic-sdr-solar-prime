#!/usr/bin/env python3
"""
SOLUÇÃO DEFINITIVA: Agente não responde mensagens
Limpa pausas ativas e testa o funcionamento
"""
import asyncio
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.integrations.redis_client import redis_client
from app.api.webhooks import process_new_message

async def fix_agent_not_responding():
    """Corrige o problema do agente não responder mensagens"""
    
    print("🚨 CORREÇÃO: Agente não responde mensagens no WhatsApp")
    print("=" * 60)
    
    # Números específicos do log que você compartilhou
    phones_from_log = [
        "558182556406",  # Do log compartilhado
        # Adicione outros números se necessário
    ]
    
    try:
        # Conectar ao Redis
        if not redis_client.redis_client:
            await redis_client.connect()
        
        if not redis_client.redis_client:
            print("❌ ERRO CRÍTICO: Redis não disponível!")
            print("   Solução: Verificar se Redis está rodando")
            return
        
        print("✅ Redis conectado com sucesso")
        
        # ETAPA 1: Verificar e limpar pausas dos números específicos
        print(f"\n📱 ETAPA 1: Verificando números específicos do log...")
        
        for phone in phones_from_log:
            print(f"\n🔍 Verificando {phone}:")
            
            handoff_active = await redis_client.is_human_handoff_active(phone)
            not_interested_active = await redis_client.is_not_interested_active(phone)
            
            if handoff_active:
                print(f"   🚫 PAUSA HANDOFF ATIVA - REMOVENDO...")
                await redis_client.clear_human_handoff_pause(phone)
                print(f"   ✅ Pausa handoff removida")
            else:
                print(f"   ✅ Sem pausa handoff")
                
            if not_interested_active:
                print(f"   🚫 PAUSA NOT_INTERESTED ATIVA - REMOVENDO...")
                await redis_client.clear_not_interested_pause(phone)
                print(f"   ✅ Pausa not_interested removida")
            else:
                print(f"   ✅ Sem pausa not_interested")
        
        # ETAPA 2: Listar e limpar TODAS as pausas ativas (opcional)
        print(f"\n📋 ETAPA 2: Verificando TODAS as pausas ativas no sistema...")
        
        handoff_keys = await redis_client.redis_client.keys("lead:pause:*")
        not_interested_keys = await redis_client.redis_client.keys("lead:not_interested:*")
        
        total_pauses = len(handoff_keys) + len(not_interested_keys)
        
        print(f"   🤝 Pausas Handoff encontradas: {len(handoff_keys)}")
        print(f"   🚫 Pausas Not Interested encontradas: {len(not_interested_keys)}")
        print(f"   📊 Total de pausas ativas: {total_pauses}")
        
        if total_pauses > 0:
            print(f"\n⚠️ ATENÇÃO: {total_pauses} pausas ativas podem estar bloqueando outros leads")
            
            choice = input("Deseja limpar TODAS as pausas ativas? (y/N): ").strip().lower()
            if choice == 'y':
                # Limpar pausas handoff
                for key in handoff_keys:
                    phone = key.replace("lead:pause:", "")
                    await redis_client.clear_human_handoff_pause(phone)
                    print(f"   ✅ Handoff removido: {phone}")
                
                # Limpar pausas not_interested
                for key in not_interested_keys:
                    phone = key.replace("lead:not_interested:", "")
                    await redis_client.clear_not_interested_pause(phone)
                    print(f"   ✅ Not Interested removido: {phone}")
                
                print(f"🎉 {total_pauses} pausas removidas com sucesso!")
            else:
                print("ℹ️ Pausas gerais mantidas (apenas números específicos foram limpos)")
        
        # ETAPA 3: Teste de processamento de mensagem
        print(f"\n🧪 ETAPA 3: Testando processamento de mensagem simulada...")
        
        test_phone = phones_from_log[0] if phones_from_log else "5581999999999"
        
        # Simular mensagem MESSAGES_UPSERT
        test_message = {
            "key": {
                "remoteJid": f"{test_phone}@s.whatsapp.net",
                "fromMe": False,
                "id": "test_fix_agent_123"
            },
            "message": {
                "conversation": "Teste após correção - quero energia solar"
            },
            "messageTimestamp": "1691234567",
            "pushName": "Teste Correção"
        }
        
        print(f"📱 Simulando mensagem de: {test_phone}")
        print(f"💬 Conteúdo: {test_message['message']['conversation']}")
        
        try:
            await process_new_message(test_message)
            print("✅ Processamento de mensagem simulada executado com sucesso!")
            print("   Verifique os logs do servidor para confirmar o funcionamento")
        except Exception as test_error:
            print(f"❌ Erro no teste: {test_error}")
            import traceback
            traceback.print_exc()
        
        # ETAPA 4: Instruções finais
        print(f"\n🎯 CORREÇÃO CONCLUÍDA!")
        print(f"=" * 40)
        print(f"✅ Pausas removidas para números específicos")
        print(f"✅ Teste de processamento executado")
        print(f"")
        print(f"🔄 PRÓXIMOS PASSOS:")
        print(f"1. Envie uma mensagem real no WhatsApp")
        print(f"2. Verifique se aparecem logs de MESSAGES_UPSERT")
        print(f"3. Confirme se o agente responde normalmente")
        print(f"")
        print(f"📋 LOGS PARA MONITORAR:")
        print(f"- 🔵 'MESSAGES_UPSERT recebido' (webhook funcionando)")
        print(f"- 🔄 'Processamento bloqueado' (se ainda há pausas)")
        print(f"- ✅ Resposta do agente enviada")
        
    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        import traceback
        traceback.print_exc()

async def quick_check():
    """Verificação rápida do status atual"""
    print("⚡ VERIFICAÇÃO RÁPIDA")
    print("-" * 30)
    
    try:
        if not redis_client.redis_client:
            await redis_client.connect()
        
        if not redis_client.redis_client:
            print("❌ Redis não disponível")
            return
        
        # Contar pausas
        handoff_keys = await redis_client.redis_client.keys("lead:pause:*")
        not_interested_keys = await redis_client.redis_client.keys("lead:not_interested:*")
        
        print(f"📊 Status atual:")
        print(f"   🤝 Pausas Handoff: {len(handoff_keys)}")
        print(f"   🚫 Pausas Not Interested: {len(not_interested_keys)}")
        print(f"   📱 Total de leads pausados: {len(handoff_keys) + len(not_interested_keys)}")
        
        if len(handoff_keys) + len(not_interested_keys) > 0:
            print(f"\n⚠️ Leads pausados podem não estar respondendo!")
        else:
            print(f"\n✅ Nenhuma pausa ativa encontrada")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    print("🛠️ CORRETOR DE AGENTE - WHATSAPP")
    print("1 - Correção completa (recomendado)")
    print("2 - Verificação rápida apenas")
    
    choice = input("\nEscolha uma opção (1 ou 2): ").strip()
    
    if choice == "1":
        asyncio.run(fix_agent_not_responding())
    elif choice == "2":
        asyncio.run(quick_check())
    else:
        print("Opção inválida!")