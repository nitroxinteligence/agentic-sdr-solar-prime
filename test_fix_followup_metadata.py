#!/usr/bin/env python3
"""
Teste de Correção - Follow-up Metadata Error
Sistema SDR IA SolarPrime
Data: 16/08/2025

Valida correção do erro:
"AgenticSDRStateless.process_message() got an unexpected keyword argument 'metadata'"
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime

# Adicionar diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

# Cores para output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_test_header(test_name: str):
    """Imprime cabeçalho do teste"""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{test_name}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}")

def print_result(passed: bool, message: str):
    """Imprime resultado do teste"""
    if passed:
        print(f"{GREEN}✅ PASSOU:{RESET} {message}")
    else:
        print(f"{RED}❌ FALHOU:{RESET} {message}")

async def test_agent_signature():
    """Testa assinatura do método process_message"""
    print_test_header("TESTE 1: Assinatura do Método process_message")
    
    try:
        from app.agents.agentic_sdr_stateless import AgenticSDRStateless
        import inspect
        
        # Verificar se método existe
        if not hasattr(AgenticSDRStateless, 'process_message'):
            print_result(False, "Método process_message não encontrado")
            return False
        
        # Obter assinatura do método
        sig = inspect.signature(AgenticSDRStateless.process_message)
        params = list(sig.parameters.keys())
        
        print(f"Parâmetros encontrados: {params}")
        
        # Verificar parâmetros esperados
        if 'self' in params and 'message' in params and 'execution_context' in params:
            print_result(True, "Assinatura correta: (self, message, execution_context)")
            
            # Verificar que 'metadata' NÃO está na assinatura
            if 'metadata' not in params:
                print_result(True, "Parâmetro 'metadata' removido (correto)")
                return True
            else:
                print_result(False, "Parâmetro 'metadata' ainda presente (incorreto)")
                return False
        else:
            print_result(False, f"Assinatura incorreta: {params}")
            return False
            
    except Exception as e:
        print_result(False, f"Erro ao verificar assinatura: {e}")
        return False

async def test_followup_executor_calls():
    """Testa se as chamadas no followup_executor foram corrigidas"""
    print_test_header("TESTE 2: Chamadas no FollowUp Executor")
    
    try:
        import inspect
        from app.services.followup_executor_service import FollowUpExecutorService
        
        # Obter código fonte do método _generate_intelligent_message
        source = inspect.getsource(FollowUpExecutorService._generate_intelligent_message)
        
        # Verificar se usa execution_context em vez de metadata
        if 'execution_context=' in source:
            print_result(True, "Usa 'execution_context' (correto)")
            
            # Verificar que não usa mais metadata
            if 'metadata=' not in source or 'metadata={' not in source:
                print_result(True, "Não usa mais 'metadata' como parâmetro (correto)")
            else:
                # Pode ter metadata em outro contexto, vamos verificar melhor
                if 'process_message(' in source and 'metadata=' in source:
                    print_result(False, "Ainda usa 'metadata' em process_message (incorreto)")
                    return False
                else:
                    print_result(True, "Usa 'metadata' em outro contexto (aceitável)")
            return True
        else:
            print_result(False, "Não usa 'execution_context' (incorreto)")
            return False
            
    except Exception as e:
        print_result(False, f"Erro ao verificar chamadas: {e}")
        return False

async def test_integration():
    """Testa integração completa (simulado)"""
    print_test_header("TESTE 3: Integração AgenticSDR")
    
    try:
        from app.agents.agentic_sdr_stateless import AgenticSDRStateless
        
        # Criar instância
        agent = AgenticSDRStateless()
        
        # Preparar contexto de teste
        test_context = {
            "phone": "5511999999999",
            "lead_info": {"name": "Teste", "phone": "5511999999999"},
            "conversation_id": "test-123",
            "conversation_history": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # Verificar que aceita execution_context
        try:
            # Não vamos executar realmente, apenas verificar a assinatura
            import inspect
            sig = inspect.signature(agent.process_message)
            
            # Tentar bind (verificar se os parâmetros estão corretos)
            bound = sig.bind(
                message="Teste de mensagem",
                execution_context=test_context
            )
            
            print_result(True, "Aceita parâmetros corretos (message, execution_context)")
            
            # Tentar com metadata (deve falhar)
            try:
                bound_wrong = sig.bind(
                    message="Teste",
                    metadata=test_context
                )
                print_result(False, "Aceita 'metadata' (incorreto)")
                return False
            except TypeError:
                print_result(True, "Rejeita 'metadata' (correto)")
                return True
                
        except Exception as e:
            print_result(False, f"Erro ao verificar binding: {e}")
            return False
            
    except Exception as e:
        print_result(False, f"Erro na integração: {e}")
        return False

async def main():
    """Executa todos os testes"""
    print(f"{BOLD}{YELLOW}")
    print("="*60)
    print(" TESTE DE CORREÇÃO - FOLLOW-UP METADATA ERROR")
    print(" Sistema SDR IA SolarPrime")
    print(f" Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)
    print(RESET)
    
    # Executar testes
    results = []
    
    # Teste 1: Assinatura do método
    result = await test_agent_signature()
    results.append(("Assinatura do Método", result))
    
    # Teste 2: Chamadas no FollowUp Executor
    result = await test_followup_executor_calls()
    results.append(("FollowUp Executor", result))
    
    # Teste 3: Integração
    result = await test_integration()
    results.append(("Integração", result))
    
    # Resumo final
    print(f"\n{BOLD}{YELLOW}{'='*60}{RESET}")
    print(f"{BOLD}RESUMO DOS TESTES{RESET}")
    print(f"{YELLOW}{'='*60}{RESET}")
    
    total_tests = len(results)
    passed_tests = sum(1 for _, passed in results if passed)
    
    for test_name, passed in results:
        status = f"{GREEN}✅ PASSOU{RESET}" if passed else f"{RED}❌ FALHOU{RESET}"
        print(f"{test_name}: {status}")
    
    print(f"\n{BOLD}Total: {passed_tests}/{total_tests} testes passaram{RESET}")
    
    if passed_tests == total_tests:
        print(f"\n{GREEN}{BOLD}🎉 CORREÇÃO VALIDADA COM SUCESSO! 🎉{RESET}")
        print(f"{GREEN}O erro de 'metadata' foi corrigido.{RESET}")
    else:
        print(f"\n{RED}{BOLD}⚠️ CORREÇÃO INCOMPLETA ⚠️{RESET}")
        print(f"{RED}Verificar os testes que falharam.{RESET}")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Teste interrompido pelo usuário{RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{RED}Erro fatal: {e}{RESET}")
        sys.exit(1)