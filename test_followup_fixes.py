#!/usr/bin/env python3
"""
Teste das correções do sistema de follow-up
Valida que os imports e queries estão corretos
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio

async def test_followup_fixes():
    """Testa as correções do sistema de follow-up"""
    
    print("=" * 70)
    print("TESTE: Correções do Sistema de Follow-up")
    print("=" * 70)
    
    tests_passed = 0
    tests_total = 0
    
    print("\n📝 Teste 1: Import do módulo stateless")
    print("-" * 50)
    
    # Teste 1: Verificar import correto
    tests_total += 1
    try:
        from app.agents.agentic_sdr_stateless import create_stateless_agent
        print("✅ Import do módulo stateless funcionando")
        tests_passed += 1
    except ImportError as e:
        print(f"❌ Erro no import: {e}")
    
    # Teste 2: Verificar criação do agent
    tests_total += 1
    try:
        agent = await create_stateless_agent()
        if agent:
            print("✅ Agent stateless criado com sucesso")
            tests_passed += 1
        else:
            print("❌ Agent não foi criado")
    except Exception as e:
        print(f"❌ Erro ao criar agent: {e}")
    
    print("\n📝 Teste 2: Verificação da tabela knowledge_base")
    print("-" * 50)
    
    # Teste 3: Verificar estrutura da tabela
    tests_total += 1
    try:
        from app.integrations.supabase_client import supabase_client
        
        # Tentar query com campo correto
        result = supabase_client.client.table('knowledge_base').select("question").limit(1).execute()
        
        print("✅ Query com campo 'question' funcionando")
        tests_passed += 1
        
        if result.data:
            print(f"   → Encontrado {len(result.data)} registro(s)")
        else:
            print("   → Tabela vazia ou sem registros")
            
    except Exception as e:
        print(f"❌ Erro ao acessar knowledge_base: {e}")
    
    print("\n📝 Teste 3: Verificação do FollowUpExecutorService")
    print("-" * 50)
    
    # Teste 4: Verificar se o serviço pode ser importado
    tests_total += 1
    try:
        from app.services.followup_executor_service import FollowUpExecutorService
        print("✅ FollowUpExecutorService importado com sucesso")
        tests_passed += 1
    except ImportError as e:
        print(f"❌ Erro ao importar FollowUpExecutorService: {e}")
    
    # Teste 5: Verificar inicialização do serviço
    tests_total += 1
    try:
        from app.services.followup_executor_service import FollowUpExecutorService
        executor = FollowUpExecutorService()
        print("✅ FollowUpExecutorService inicializado")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Erro ao inicializar FollowUpExecutorService: {e}")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Sistema de follow-up corrigido!")
        print("\n✅ Correções aplicadas:")
        print("   • Import mudado de agentic_sdr_refactored para agentic_sdr_stateless")
        print("   • Função mudada de get_agentic_agent() para create_stateless_agent()")
        print("   • Campo knowledge_base corrigido de 'title' para 'question'")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema ainda precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_followup_fixes())
    exit(0 if result else 1)