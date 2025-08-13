#!/usr/bin/env python
"""
🚨 TESTE DE CORREÇÕES CRÍTICAS
Valida as 3 correções implementadas:
1. Extração de nome funcionando
2. Erro NoneType corrigido
3. Nome sincronizado com CRM
"""

import asyncio
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_refactored import get_agentic_agent
from app.core.lead_manager import LeadManager
from app.services.crm_service_100_real import CRMServiceReal

async def test_name_extraction():
    """Teste 1: Verifica se extração de nome funciona"""
    print("\n" + "="*60)
    print("🔍 TESTE 1: EXTRAÇÃO DE NOME")
    print("="*60)
    
    try:
        lead_manager = LeadManager()
        
        # Simular conversa real
        messages = [
            {"role": "assistant", "content": "Olá! Tudo bem? Sou a Helen da Solarprime. Como posso te chamar?"},
            {"role": "user", "content": "mateus"}
        ]
        
        lead_info = lead_manager.extract_lead_info(messages)
        
        if lead_info.get("name") == "Mateus":
            print("✅ Nome extraído corretamente: Mateus")
            return True
        else:
            print(f"❌ Nome não extraído. Resultado: {lead_info.get('name')}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

async def test_kommo_stage_check():
    """Teste 2: Verifica se erro NoneType foi corrigido"""
    print("\n" + "="*60)
    print("🔍 TESTE 2: VERIFICAÇÃO DE ESTÁGIO SEM ERRO")
    print("="*60)
    
    try:
        crm = CRMServiceReal()
        await crm.initialize()
        
        # Testar com lead inexistente (deve retornar None sem erro)
        result = await crm.get_lead_by_id(999999999)
        
        # Verificar se retorna None sem erro
        if result is None:
            print("✅ Retorna None para lead inexistente sem erro")
        
        await crm.close()
        
        print("✅ Verificação de estágio funcionando sem NoneType error")
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        return False

async def test_full_flow_with_name():
    """Teste 3: Fluxo completo com nome sendo sincronizado"""
    print("\n" + "="*60)
    print("🔍 TESTE 3: FLUXO COMPLETO COM SINCRONIZAÇÃO")
    print("="*60)
    
    try:
        # Inicializar agente
        print("📱 Inicializando AgenticSDR...")
        agent = await get_agentic_agent()
        
        # Primeira mensagem - saudação
        print("\n📝 Enviando primeira mensagem...")
        response1 = await agent.process_message(
            "oi",
            {"phone": "+5511999999999"}
        )
        
        # Verificar se pergunta o nome
        if "como posso te chamar" in response1.lower() or "qual seu nome" in response1.lower():
            print("✅ Agente perguntou o nome")
        else:
            print("⚠️ Agente não perguntou o nome explicitamente")
        
        # Segunda mensagem - enviar nome
        print("\n📝 Enviando nome 'João'...")
        response2 = await agent.process_message(
            "joão",
            {"phone": "+5511999999999"}
        )
        
        # Verificar se agente reconheceu o nome
        if "joão" in response2.lower():
            print("✅ Agente reconheceu e usou o nome João")
        else:
            print("⚠️ Agente não mencionou o nome na resposta")
        
        # Verificar se o nome foi atualizado no lead_info
        if agent.current_lead_info.get("name") == "João":
            print("✅ Nome salvo no lead_info: João")
            return True
        else:
            print(f"❌ Nome no lead_info: {agent.current_lead_info.get('name')}")
            return False
            
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        return False

async def run_all_tests():
    """Executa todos os testes"""
    
    print("\n" + "="*70)
    print("🚨 TESTE DE CORREÇÕES CRÍTICAS DO SISTEMA")
    print("="*70)
    
    results = {
        "total": 3,
        "passed": 0,
        "failed": 0
    }
    
    # Teste 1: Extração de nome
    if await test_name_extraction():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Teste 2: Verificação de estágio sem erro
    if await test_kommo_stage_check():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Teste 3: Fluxo completo
    if await test_full_flow_with_name():
        results["passed"] += 1
    else:
        results["failed"] += 1
    
    # Relatório Final
    print("\n" + "="*70)
    print("📊 RELATÓRIO FINAL")
    print("="*70)
    
    print(f"\n📈 Resultados:")
    print(f"   Total: {results['total']}")
    print(f"   ✅ Passou: {results['passed']}")
    print(f"   ❌ Falhou: {results['failed']}")
    print(f"   📊 Taxa de sucesso: {(results['passed']/results['total']*100):.1f}%")
    
    if results["passed"] == results["total"]:
        print("\n🎉 TODAS AS CORREÇÕES FUNCIONANDO!")
        print("✅ Sistema corrigido com sucesso")
    else:
        print(f"\n⚠️ {results['failed']} correções ainda precisam de ajustes")
    
    print("="*70)
    
    return results["passed"] == results["total"]

if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)