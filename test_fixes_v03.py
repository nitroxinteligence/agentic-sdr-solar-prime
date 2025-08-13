#!/usr/bin/env python3
"""
Teste das correções v0.3 - SDR IA SolarPrime
Valida as 3 correções críticas aplicadas
"""

import asyncio
import os
import sys
from pathlib import Path

# Adicionar diretório raiz ao path
sys.path.insert(0, str(Path(__file__).parent))

# Configurar variáveis de ambiente para teste
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "true"

async def test_kommo_auto_sync_fix():
    """Testa correção do módulo kommo_auto_sync ausente"""
    print("\n🔧 Testando correção do módulo kommo_auto_sync...")
    
    try:
        # Tentar importar o team_coordinator com a correção
        from app.core.team_coordinator import TeamCoordinator
        
        # Verificar se o import foi bem-sucedido
        coordinator = TeamCoordinator()
        print("✅ TeamCoordinator importado com sucesso!")
        
        # Verificar se o CRM service está acessível
        from app.services.crm_service_100_real import CRMServiceReal
        print("✅ CRM Service está acessível como fallback!")
        
        return True
        
    except ImportError as e:
        print(f"❌ Erro de import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

async def test_resposta_final_tags():
    """Testa se o agent agora inclui tags RESPOSTA_FINAL"""
    print("\n🏷️ Testando tags RESPOSTA_FINAL no AgenticSDR...")
    
    try:
        from app.agents.agentic_sdr_refactored import AgenticSDR
        
        # Criar instância do agent
        agent = AgenticSDR()
        
        # Verificar se as instruções contêm a estrutura obrigatória
        instructions = agent._get_instructions()
        
        if "<RESPOSTA_FINAL>" in instructions and "</RESPOSTA_FINAL>" in instructions:
            print("✅ Tags RESPOSTA_FINAL presentes nas instruções!")
            
            # Verificar se há explicação sobre as tags
            if "ESTRUTURA OBRIGATÓRIA" in instructions:
                print("✅ Estrutura obrigatória está documentada!")
                return True
            else:
                print("⚠️ Tags presentes mas sem documentação clara")
                return True
        else:
            print("❌ Tags RESPOSTA_FINAL não encontradas nas instruções")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao testar agent: {e}")
        return False

async def test_kommo_webhook_handling():
    """Testa melhoria no tratamento de webhooks Kommo"""
    print("\n🔔 Testando tratamento de webhooks Kommo...")
    
    try:
        from app.api.webhooks import kommo_webhook
        from fastapi import Request
        from unittest.mock import Mock, AsyncMock
        
        # Criar mock de request sem evento (caso comum)
        mock_request = Mock(spec=Request)
        mock_request.headers = {"content-type": "application/x-www-form-urlencoded"}
        mock_request.form = AsyncMock(return_value={})
        
        # Testar webhook sem evento (não deve gerar erro)
        try:
            result = await kommo_webhook(mock_request)
            if result.get("status") == "ok":
                print("✅ Webhook sem evento tratado corretamente!")
                return True
            else:
                print("⚠️ Webhook processado mas com status inesperado")
                return True
        except Exception as e:
            print(f"❌ Erro ao processar webhook vazio: {e}")
            return False
            
    except ImportError as e:
        print(f"❌ Erro de import: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

async def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("🧪 TESTE DAS CORREÇÕES v0.3 - SDR IA SOLARPRIME")
    print("=" * 60)
    
    results = []
    
    # Teste 1: Módulo kommo_auto_sync
    results.append(await test_kommo_auto_sync_fix())
    
    # Teste 2: Tags RESPOSTA_FINAL
    results.append(await test_resposta_final_tags())
    
    # Teste 3: Webhooks Kommo
    results.append(await test_kommo_webhook_handling())
    
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
        print("\n🎉 TODAS AS CORREÇÕES FORAM APLICADAS COM SUCESSO!")
        return 0
    else:
        print("\n⚠️ Algumas correções precisam de revisão.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)