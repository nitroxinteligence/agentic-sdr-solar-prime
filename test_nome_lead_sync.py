#!/usr/bin/env python
"""
🧪 TESTE DE SINCRONIZAÇÃO DO NOME DO LEAD
Valida o fluxo completo: WhatsApp → Supabase → Kommo CRM
"""

import asyncio
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_refactored import get_agentic_agent
from app.services.crm_service_100_real import CRMServiceReal
from app.integrations.supabase_client import supabase_client
from app.utils.logger import emoji_logger

async def test_nome_sync():
    """Testa o fluxo completo de sincronização do nome"""
    
    print("\n" + "="*60)
    print("🧪 TESTE DE SINCRONIZAÇÃO DE NOME DO LEAD")
    print("="*60)
    
    test_phone = f"+5511999{datetime.now().strftime('%H%M%S')}"  # Número único para teste
    
    results = {
        "pergunta_nome": False,
        "extracao_nome": False,
        "supabase_sync": False,
        "kommo_sync": False,
        "nome_correto": False
    }
    
    try:
        # 1. SIMULAR PRIMEIRO CONTATO
        print("\n📱 1. Simulando primeiro contato no WhatsApp...")
        agent = await get_agentic_agent()
        
        # Primeira mensagem do lead (sem nome)
        response1 = await agent.process_message(
            "oi quero saber sobre energia solar",
            {"phone": test_phone}
        )
        
        # Verificar se o agente perguntou o nome
        if "como posso te chamar" in response1.lower() or "qual seu nome" in response1.lower():
            print("✅ Agente perguntou o nome corretamente")
            results["pergunta_nome"] = True
        else:
            print(f"❌ Agente NÃO perguntou o nome. Resposta: {response1[:100]}...")
        
        # 2. INFORMAR O NOME
        print("\n👤 2. Informando o nome do lead...")
        nome_teste = "João Teste Silva"
        
        response2 = await agent.process_message(
            nome_teste,
            {"phone": test_phone}
        )
        
        # Verificar se o nome foi extraído
        if agent.current_lead_info.get("name") == nome_teste:
            print(f"✅ Nome extraído corretamente: {nome_teste}")
            results["extracao_nome"] = True
        else:
            print(f"❌ Nome não extraído. Lead info: {agent.current_lead_info.get('name')}")
        
        # 3. VERIFICAR SUPABASE
        print("\n💾 3. Verificando sincronização com Supabase...")
        await asyncio.sleep(2)  # Aguardar sincronização
        
        lead_db = await supabase_client.get_lead_by_phone(test_phone)
        if lead_db and lead_db.get("name") == nome_teste:
            print(f"✅ Lead no Supabase com nome correto: {lead_db.get('name')}")
            results["supabase_sync"] = True
        else:
            print(f"❌ Lead no Supabase com problema: {lead_db.get('name') if lead_db else 'Não encontrado'}")
        
        # 4. VERIFICAR KOMMO CRM
        print("\n🎯 4. Verificando sincronização com Kommo CRM...")
        crm = CRMServiceReal()
        await crm.initialize()
        
        # Buscar lead no Kommo pelo telefone
        lead_kommo = await crm._find_lead_by_phone(test_phone)
        
        if lead_kommo:
            nome_kommo = lead_kommo.get("name", "")
            
            print(f"📋 Lead no Kommo: {nome_kommo}")
            
            # Verificar se o nome NÃO é genérico
            if nome_kommo not in ["Lead Solar", "NOVO LEAD", "Lead sem nome", ""]:
                print(f"✅ Nome no Kommo está correto: {nome_kommo}")
                results["kommo_sync"] = True
                
                # Verificar se é exatamente o nome informado
                if nome_kommo == nome_teste:
                    results["nome_correto"] = True
                    print("✅ Nome é exatamente o informado pelo lead")
                else:
                    print(f"⚠️ Nome diferente do informado: '{nome_kommo}' vs '{nome_teste}'")
            else:
                print(f"❌ Nome genérico no Kommo: {nome_kommo}")
        else:
            print("❌ Lead não encontrado no Kommo")
        
        await crm.close()
        
        # 5. RESUMO DOS RESULTADOS
        print("\n" + "="*60)
        print("📊 RESULTADO DOS TESTES")
        print("="*60)
        
        for test_name, passed in results.items():
            status = "✅" if passed else "❌"
            print(f"{status} {test_name.replace('_', ' ').title()}")
        
        total = len(results)
        passed = sum(results.values())
        percentage = (passed / total) * 100
        
        print(f"\n🎯 Taxa de Sucesso: {passed}/{total} ({percentage:.0f}%)")
        
        if percentage == 100:
            print("🎉 SINCRONIZAÇÃO FUNCIONANDO PERFEITAMENTE!")
        elif percentage >= 60:
            print("⚠️ Sincronização parcial - verificar problemas")
        else:
            print("🔴 PROBLEMA CRÍTICO NA SINCRONIZAÇÃO!")
        
        return percentage == 100
        
    except Exception as e:
        print(f"\n❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_nome_sync())
    sys.exit(0 if success else 1)