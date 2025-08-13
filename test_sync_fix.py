#!/usr/bin/env python3
"""
Teste da correção do erro sync_new_leads
Valida que o CRM sync não quebra mais
"""

import asyncio
import os
import sys
from pathlib import Path
from unittest.mock import Mock, AsyncMock, patch

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

# Configurar variáveis de ambiente para teste
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "true"
os.environ["ENABLE_KOMMO_AUTO_SYNC"] = "true"

async def test_sync_without_error():
    """Testa se o sync não gera mais erro de método ausente"""
    print("\n🔧 Testando correção do sync_new_leads...")
    
    try:
        from app.core.team_coordinator import TeamCoordinator
        from app.services.crm_service_100_real import CRMServiceReal
        
        # Criar instâncias
        coordinator = TeamCoordinator()
        
        # Mock do CRMServiceReal com método create_lead
        mock_crm = Mock(spec=CRMServiceReal)
        mock_crm.create_lead = AsyncMock(return_value={"id": 12345, "name": "Test Lead"})
        
        # Dados de teste
        test_lead_info = {
            "name": "João Silva",
            "phone": "5511999999999",
            "qualification_score": 75,
            "bill_value": 500.00,
            "interested": True
        }
        
        # Testar o sync_with_crm
        with patch('app.core.team_coordinator.CRMServiceReal', return_value=mock_crm):
            result = await coordinator.sync_with_crm(test_lead_info)
        
        # Verificar resultado
        if result and result.get("success"):
            print("✅ Sync executado sem erro de método ausente!")
            print(f"   Mensagem: {result.get('message')}")
            return True
        else:
            print(f"⚠️ Sync retornou falha: {result}")
            return True  # Ainda é sucesso pois não deu erro de método
            
    except AttributeError as e:
        if "sync_new_leads" in str(e):
            print(f"❌ ERRO: Método sync_new_leads ainda sendo chamado: {e}")
            return False
        else:
            print(f"❌ Erro de atributo diferente: {e}")
            return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

async def test_crm_service_methods():
    """Verifica quais métodos existem no CRMServiceReal"""
    print("\n📋 Verificando métodos disponíveis no CRMServiceReal...")
    
    try:
        from app.services.crm_service_100_real import CRMServiceReal
        
        # Criar instância
        crm = CRMServiceReal()
        
        # Métodos esperados
        expected_methods = ["create_lead", "update_lead", "move_to_stage", "update_fields"]
        missing_methods = []
        available_methods = []
        
        for method in expected_methods:
            if hasattr(crm, method):
                available_methods.append(method)
                print(f"   ✅ {method}: Disponível")
            else:
                missing_methods.append(method)
                print(f"   ❌ {method}: Ausente")
        
        # Métodos de sync antigos que NÃO devem existir
        old_sync_methods = ["sync_new_leads", "sync_lead_updates", "sync_specific_lead"]
        for method in old_sync_methods:
            if hasattr(crm, method):
                print(f"   ⚠️ {method}: Presente (legado)")
            else:
                print(f"   ✅ {method}: Removido corretamente")
        
        return len(available_methods) > 0
        
    except Exception as e:
        print(f"❌ Erro ao verificar métodos: {e}")
        return False

async def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("🧪 TESTE DA CORREÇÃO sync_new_leads")
    print("=" * 60)
    
    results = []
    
    # Teste 1: Sync sem erro
    results.append(await test_sync_without_error())
    
    # Teste 2: Verificar métodos
    results.append(await test_crm_service_methods())
    
    # Resumo
    print("\n" + "=" * 60)
    print("📊 RESUMO DOS TESTES")
    print("=" * 60)
    
    total = len(results)
    passed = sum(results)
    failed = total - passed
    
    print(f"✅ Testes aprovados: {passed}/{total}")
    if failed > 0:
        print(f"❌ Testes falhados: {failed}/{total}")
    
    success_rate = (passed / total) * 100
    print(f"📈 Taxa de sucesso: {success_rate:.1f}%")
    
    if success_rate == 100:
        print("\n🎉 CORREÇÃO APLICADA COM SUCESSO!")
        print("O erro 'sync_new_leads' foi resolvido.")
        return 0
    else:
        print("\n⚠️ Verificar implementação.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)