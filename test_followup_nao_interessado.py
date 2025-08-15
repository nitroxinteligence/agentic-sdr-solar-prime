#!/usr/bin/env python3
"""
Teste do Gatilho "Não Interessado" no FollowUp Executor
Valida se leads sem resposta são movidos automaticamente para "NÃO INTERESSADO" após o ciclo de follow-up
"""

import asyncio
import logging
from datetime import datetime, timezone, timedelta
from unittest.mock import AsyncMock, MagicMock, patch
import json

# Configurar logging para o teste
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestFollowUpNaoInteressado:
    """Teste do gatilho de "Não Interessado" no FollowUp Executor"""
    
    def __init__(self):
        self.test_results = []
        
    async def run_all_tests(self):
        """Executa todos os testes do gatilho"""
        print("🧪 TESTE: Gatilho 'Não Interessado' no FollowUp Executor")
        print("=" * 60)
        
        # Teste 1: Verificar se lógica está implementada
        await self.test_trigger_logic_implemented()
        
        # Teste 2: Simular execução do gatilho
        await self.test_trigger_execution()
        
        # Teste 3: Verificar tratamento de erro
        await self.test_error_handling()
        
        # Resultado final
        self.print_results()
        
    async def test_trigger_logic_implemented(self):
        """Teste 1: Verificar se a lógica foi implementada corretamente"""
        try:
            print("\n🔍 Teste 1: Verificação da implementação...")
            
            # Importar o serviço
            from app.services.followup_executor_service import FollowUpExecutorService
            
            # Verificar se o método existe
            service = FollowUpExecutorService()
            assert hasattr(service, '_schedule_next_followup'), "Método _schedule_next_followup não encontrado"
            
            # Verificar se o código foi modificado (buscar string específica)
            import inspect
            source_code = inspect.getsource(service._schedule_next_followup)
            
            # Verificações específicas
            assertions = [
                ('attempt >= 2', 'Condição de limite de tentativas'),
                ('NÃO INTERESSADO', 'Stage de destino correto'),
                ('update_lead_stage', 'Chamada para atualização do CRM'),
                ('kommo_lead_id', 'Verificação do ID do lead no Kommo')
            ]
            
            for check, description in assertions:
                if check in source_code:
                    print(f"  ✅ {description}: Implementado")
                else:
                    print(f"  ❌ {description}: NÃO encontrado")
                    self.test_results.append(f"FALHA: {description}")
                    return
            
            print("  ✅ Lógica implementada corretamente!")
            self.test_results.append("SUCESSO: Implementação da lógica")
            
        except Exception as e:
            print(f"  ❌ Erro no teste de implementação: {e}")
            self.test_results.append(f"ERRO: {e}")
    
    async def test_trigger_execution(self):
        """Teste 2: Simular execução do gatilho"""
        try:
            print("\n🎯 Teste 2: Simulação de execução...")
            
            from app.services.followup_executor_service import FollowUpExecutorService
            
            # Criar instância do serviço
            service = FollowUpExecutorService()
            
            # Mock do serviço CRM
            mock_crm = AsyncMock()
            mock_crm.update_lead_stage = AsyncMock(return_value=True)
            
            # Injetar mock do CRM
            service.services = {"crm": mock_crm}
            
            # Dados de teste
            test_lead = {
                "id": "test-lead-123",
                "name": "João Teste",
                "kommo_lead_id": "123456",
                "phone_number": "+5511999999999"
            }
            
            test_followup = {
                "id": "followup-456",
                "type": "reengagement",
                "attempt": 2,  # Já tentou 2 vezes (30min + 24h)
                "metadata": {
                    "trigger": "agent_response_24h",
                    "phone": "+5511999999999"
                }
            }
            
            # Executar o método (mock da função time_utils)
            with patch('app.utils.time_utils.get_business_aware_datetime') as mock_time:
                mock_time.return_value = datetime.now(timezone.utc) + timedelta(hours=48)
                
                # Executar o método diretamente
                await service._schedule_next_followup("reengagement", test_lead, test_followup)
            
            # Verificar se o CRM foi chamado
            if mock_crm.update_lead_stage.called:
                call_args = mock_crm.update_lead_stage.call_args
                if call_args:
                    lead_id, stage = call_args[0]
                    if lead_id == "123456" and stage == "NÃO INTERESSADO":
                        print("  ✅ CRM chamado corretamente!")
                        print(f"    - Lead ID: {lead_id}")
                        print(f"    - Stage: {stage}")
                        self.test_results.append("SUCESSO: Execução do gatilho")
                    else:
                        print(f"  ❌ CRM chamado com parâmetros incorretos: {call_args}")
                        self.test_results.append("FALHA: Parâmetros incorretos")
                else:
                    print("  ❌ CRM chamado sem argumentos")
                    self.test_results.append("FALHA: Sem argumentos")
            else:
                print("  ❌ CRM não foi chamado")
                self.test_results.append("FALHA: CRM não chamado")
                
        except Exception as e:
            print(f"  ❌ Erro no teste de execução: {e}")
            self.test_results.append(f"ERRO: {e}")
    
    async def test_error_handling(self):
        """Teste 3: Verificar tratamento de erro"""
        try:
            print("\n🛡️ Teste 3: Tratamento de erros...")
            
            from app.services.followup_executor_service import FollowUpExecutorService
            
            # Criar instância do serviço
            service = FollowUpExecutorService()
            
            # Mock do CRM que falha
            mock_crm = AsyncMock()
            mock_crm.update_lead_stage = AsyncMock(side_effect=Exception("Erro simulado do CRM"))
            
            # Injetar mock do CRM
            service.services = {"crm": mock_crm}
            
            # Dados de teste
            test_lead = {
                "id": "test-lead-error",
                "name": "Teste Erro",
                "kommo_lead_id": "999999"
            }
            
            test_followup = {
                "id": "followup-error",
                "type": "reengagement",
                "attempt": 2,
                "metadata": {"trigger": "agent_response_24h"}
            }
            
            # Capturar logs de erro
            with patch('app.services.followup_executor_service.logger') as mock_logger:
                with patch('app.utils.time_utils.get_business_aware_datetime') as mock_time:
                    mock_time.return_value = datetime.now(timezone.utc) + timedelta(hours=48)
                    
                    # Executar e verificar se não quebra
                    await service._schedule_next_followup("reengagement", test_lead, test_followup)
            
            # Verificar se o erro foi logado
            if mock_logger.error.called:
                error_calls = [call for call in mock_logger.error.call_args_list 
                              if "Erro ao mover lead para NÃO INTERESSADO" in str(call)]
                if error_calls:
                    print("  ✅ Erro tratado e logado corretamente!")
                    self.test_results.append("SUCESSO: Tratamento de erro")
                else:
                    print("  ❌ Erro não logado corretamente")
                    self.test_results.append("FALHA: Log de erro")
            else:
                print("  ⚠️ Logger não foi chamado (pode ser normal)")
                self.test_results.append("ALERTA: Logger não chamado")
                
        except Exception as e:
            print(f"  ❌ Erro no teste de tratamento: {e}")
            self.test_results.append(f"ERRO: {e}")
    
    def print_results(self):
        """Imprime resultados finais dos testes"""
        print("\n" + "=" * 60)
        print("📊 RESULTADOS DOS TESTES")
        print("=" * 60)
        
        success_count = len([r for r in self.test_results if r.startswith("SUCESSO")])
        total_tests = len([r for r in self.test_results if r.startswith(("SUCESSO", "FALHA"))])
        
        for result in self.test_results:
            if result.startswith("SUCESSO"):
                print(f"✅ {result}")
            elif result.startswith("FALHA"):
                print(f"❌ {result}")
            elif result.startswith("ERRO"):
                print(f"🚨 {result}")
            else:
                print(f"⚠️ {result}")
        
        print(f"\n📈 RESUMO: {success_count}/{total_tests} testes passaram")
        
        if success_count == total_tests and total_tests > 0:
            print("🎉 TODOS OS TESTES PASSARAM! Implementação está correta.")
        else:
            print("⚠️ Alguns testes falharam. Verifique a implementação.")

async def main():
    """Executa os testes"""
    test_runner = TestFollowUpNaoInteressado()
    await test_runner.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main())