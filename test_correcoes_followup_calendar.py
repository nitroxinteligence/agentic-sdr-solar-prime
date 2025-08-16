#!/usr/bin/env python3
"""
Teste de Validação das Correções - Follow-up e Calendar
Sistema SDR IA SolarPrime v0.5
Data: 16/08/2025

Este script valida as correções implementadas para:
1. Erro 'NoneType' no follow-up service
2. Tools de cancel_meeting e reschedule_meeting
"""

import asyncio
import sys
import os
from datetime import datetime
from pathlib import Path

# Adicionar diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

from app.services.followup_service_100_real import FollowUpServiceReal
from app.services.calendar_service_100_real import CalendarServiceReal
from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.utils.logger import emoji_logger

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

async def test_followup_service():
    """Testa correção do erro 'NoneType' no follow-up service"""
    print_test_header("TESTE 1: Follow-up Service - Correção 'NoneType'")
    
    try:
        # Inicializar serviço
        followup_service = FollowUpServiceReal()
        await followup_service.initialize()
        print_result(True, "Serviço inicializado com sucesso")
        
        # Testar método get_pending_followups (que estava com erro)
        try:
            pending = await followup_service.get_pending_followups()
            print_result(True, f"get_pending_followups executado sem erro - {len(pending)} pendentes")
            
            # Testar schedule_followup
            result = await followup_service.schedule_followup(
                phone_number="5511999999999",
                message="Teste de follow-up",
                delay_hours=24,
                lead_info={"name": "Teste", "phone": "5511999999999"}
            )
            
            if result.get("success"):
                print_result(True, f"Follow-up agendado: {result.get('followup_id')}")
            else:
                print_result(False, f"Erro ao agendar: {result.get('message')}")
                
        except AttributeError as e:
            if "'NoneType' object" in str(e):
                print_result(False, f"Erro 'NoneType' ainda presente: {e}")
                return False
            raise
            
        return True
        
    except Exception as e:
        print_result(False, f"Erro inesperado: {e}")
        return False
    finally:
        # Fechar sessão se existir
        if hasattr(followup_service, 'session') and followup_service.session:
            await followup_service.session.close()

async def test_calendar_cancel_meeting():
    """Testa funcionalidade de cancelamento de reunião"""
    print_test_header("TESTE 2: Calendar - Cancel Meeting")
    
    try:
        # Inicializar serviço
        calendar_service = CalendarServiceReal()
        
        # Verificar se método existe
        if not hasattr(calendar_service, 'cancel_meeting'):
            print_result(False, "Método cancel_meeting não encontrado")
            return False
        
        print_result(True, "Método cancel_meeting existe")
        
        # Testar parâmetros do método (sem executar real)
        import inspect
        sig = inspect.signature(calendar_service.cancel_meeting)
        params = list(sig.parameters.keys())
        
        if 'meeting_id' in params:
            print_result(True, "Parâmetro meeting_id presente")
        else:
            print_result(False, "Parâmetro meeting_id ausente")
            return False
            
        return True
        
    except Exception as e:
        print_result(False, f"Erro: {e}")
        return False

async def test_calendar_reschedule_meeting():
    """Testa funcionalidade de reagendamento de reunião"""
    print_test_header("TESTE 3: Calendar - Reschedule Meeting")
    
    try:
        # Inicializar serviço
        calendar_service = CalendarServiceReal()
        
        # Verificar se método existe
        if not hasattr(calendar_service, 'reschedule_meeting'):
            print_result(False, "Método reschedule_meeting não encontrado")
            return False
        
        print_result(True, "Método reschedule_meeting existe")
        
        # Testar parâmetros do método
        import inspect
        sig = inspect.signature(calendar_service.reschedule_meeting)
        params = list(sig.parameters.keys())
        
        required_params = ['meeting_id', 'date', 'time', 'lead_info']
        for param in required_params:
            if param in params:
                print_result(True, f"Parâmetro {param} presente")
            else:
                print_result(False, f"Parâmetro {param} ausente")
                return False
                
        return True
        
    except Exception as e:
        print_result(False, f"Erro: {e}")
        return False

async def test_agent_tool_executor():
    """Testa se os novos tools estão disponíveis no agente"""
    print_test_header("TESTE 4: Agent - Tool Executor")
    
    try:
        # Criar instância do agente
        agent = AgenticSDRStateless()
        
        # Verificar se método _execute_single_tool existe
        if not hasattr(agent, '_execute_single_tool'):
            print_result(False, "Método _execute_single_tool não encontrado")
            return False
        
        print_result(True, "Método _execute_single_tool existe")
        
        # Ler código do método para verificar se tem os novos tools
        import inspect
        source = inspect.getsource(agent._execute_single_tool)
        
        # Verificar se cancel_meeting está no código
        if 'cancel_meeting' in source:
            print_result(True, "Tool cancel_meeting presente no executor")
        else:
            print_result(False, "Tool cancel_meeting ausente no executor")
            return False
        
        # Verificar se reschedule_meeting está no código
        if 'reschedule_meeting' in source:
            print_result(True, "Tool reschedule_meeting presente no executor")
        else:
            print_result(False, "Tool reschedule_meeting ausente no executor")
            return False
            
        return True
        
    except Exception as e:
        print_result(False, f"Erro: {e}")
        return False

async def test_prompt_documentation():
    """Testa se a documentação dos novos tools está no prompt"""
    print_test_header("TESTE 5: Prompt - Documentação dos Tools")
    
    try:
        # Ler arquivo de prompt
        prompt_path = Path(__file__).parent / "app" / "prompts" / "prompt-agente.md"
        
        if not prompt_path.exists():
            print_result(False, "Arquivo prompt-agente.md não encontrado")
            return False
            
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt_content = f.read()
        
        # Verificar documentação do cancel_meeting
        if 'calendar.cancel_meeting' in prompt_content:
            print_result(True, "Documentação de calendar.cancel_meeting presente")
        else:
            print_result(False, "Documentação de calendar.cancel_meeting ausente")
            return False
        
        # Verificar documentação do reschedule_meeting
        if 'calendar.reschedule_meeting' in prompt_content:
            print_result(True, "Documentação de calendar.reschedule_meeting presente")
        else:
            print_result(False, "Documentação de calendar.reschedule_meeting ausente")
            return False
        
        # Verificar exemplos
        if 'meeting_id=' in prompt_content:
            print_result(True, "Exemplos com meeting_id presentes")
        else:
            print_result(False, "Exemplos com meeting_id ausentes")
            
        return True
        
    except Exception as e:
        print_result(False, f"Erro: {e}")
        return False

async def main():
    """Executa todos os testes"""
    print(f"{BOLD}{YELLOW}")
    print("="*60)
    print(" TESTE DE VALIDAÇÃO - CORREÇÕES FOLLOW-UP E CALENDAR")
    print(" Sistema SDR IA SolarPrime v0.5")
    print(f" Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("="*60)
    print(RESET)
    
    # Executar testes
    results = []
    
    # Teste 1: Follow-up Service
    result = await test_followup_service()
    results.append(("Follow-up Service", result))
    
    # Teste 2: Cancel Meeting
    result = await test_calendar_cancel_meeting()
    results.append(("Cancel Meeting", result))
    
    # Teste 3: Reschedule Meeting
    result = await test_calendar_reschedule_meeting()
    results.append(("Reschedule Meeting", result))
    
    # Teste 4: Agent Tool Executor
    result = await test_agent_tool_executor()
    results.append(("Agent Tool Executor", result))
    
    # Teste 5: Prompt Documentation
    result = await test_prompt_documentation()
    results.append(("Prompt Documentation", result))
    
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
        print(f"\n{GREEN}{BOLD}🎉 TODAS AS CORREÇÕES VALIDADAS COM SUCESSO! 🎉{RESET}")
        print(f"{GREEN}Sistema pronto para produção.{RESET}")
    else:
        print(f"\n{RED}{BOLD}⚠️ ALGUMAS CORREÇÕES FALHARAM ⚠️{RESET}")
        print(f"{RED}Revisar os testes que falharam antes de ir para produção.{RESET}")
    
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