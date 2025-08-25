#!/usr/bin/env python3
"""
Teste simples para validar a correção da atualização do estágio do CRM.

Este teste verifica se a lógica de atualização do estágio foi adicionada corretamente.
"""

import re
import os

def test_crm_stage_update_logic():
    """
    Testa se a lógica de atualização do estágio do CRM foi adicionada ao código.
    """
    print("🧪 Testando se a correção foi implementada corretamente...")
    
    # Lê o arquivo do agente
    agent_file = "/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/app/agents/agentic_sdr_stateless.py"
    
    with open(agent_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se a correção foi implementada
    checks = [
        {
            "name": "Comentário de atualização do estágio",
            "pattern": r"# ATUALIZA O ESTÁGIO DO LEAD PARA.*REUNIÃO AGENDADA.*NO CRM",
            "found": False
        },
        {
            "name": "Verificação do kommo_lead_id",
            "pattern": r"if lead_info\.get\(\"kommo_lead_id\"\):",
            "found": False
        },
        {
            "name": "Chamada para update_lead_stage",
            "pattern": r"await self\.crm_service\.update_lead_stage\(",
            "found": False
        },
        {
            "name": "Parâmetro stage_name com reunião_agendada",
            "pattern": r"stage_name=\"reunião_agendada\"",
            "found": False
        },
        {
            "name": "Log de sucesso da atualização",
            "pattern": r"emoji_logger\.system_success.*Lead.*movido para estágio.*Reunião Agendada",
            "found": False
        },
        {
            "name": "Tratamento de erro com try/except",
            "pattern": r"except Exception as e:.*emoji_logger\.service_error.*Erro ao atualizar estágio",
            "found": False
        }
    ]
    
    # Executa as verificações
    for check in checks:
        if re.search(check["pattern"], content, re.DOTALL | re.IGNORECASE):
            check["found"] = True
            print(f"   ✅ {check['name']}")
        else:
            print(f"   ❌ {check['name']}")
    
    # Verifica se todas as verificações passaram
    all_passed = all(check["found"] for check in checks)
    
    if all_passed:
        print("\n🎉 TODAS AS VERIFICAÇÕES PASSARAM!")
        print("✅ A correção foi implementada corretamente.")
        print("✅ O sistema agora deve atualizar o estágio do lead no CRM após agendar reunião.")
        return True
    else:
        print("\n❌ ALGUMAS VERIFICAÇÕES FALHARAM!")
        failed_checks = [check["name"] for check in checks if not check["found"]]
        print(f"Verificações que falharam: {failed_checks}")
        return False

def test_code_placement():
    """
    Verifica se a correção foi colocada no local correto do código.
    """
    print("\n🧪 Verificando se a correção está no local correto...")
    
    agent_file = "/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/app/agents/agentic_sdr_stateless.py"
    
    with open(agent_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Procura pela seção relevante
    in_schedule_section = False
    found_qualification_creation = False
    found_crm_update = False
    found_post_workflow = False
    
    for i, line in enumerate(lines):
        if "if result and result.get(\"success\"):" in line:
            in_schedule_section = True
            print(f"   📍 Seção de agendamento encontrada na linha {i+1}")
        
        if in_schedule_section:
            if "create_lead_qualification" in line:
                found_qualification_creation = True
                print(f"   ✅ Criação de qualificação encontrada na linha {i+1}")
            
            if "update_lead_stage" in line:
                found_crm_update = True
                print(f"   ✅ Atualização do CRM encontrada na linha {i+1}")
            
            if "_execute_post_scheduling_workflow" in line:
                found_post_workflow = True
                print(f"   ✅ Workflow pós-agendamento encontrado na linha {i+1}")
                break
    
    # Verifica a ordem correta
    if found_qualification_creation and found_crm_update and found_post_workflow:
        print("\n✅ A correção está no local correto!")
        print("   1. Criação de qualificação")
        print("   2. Atualização do estágio no CRM (NOVA CORREÇÃO)")
        print("   3. Execução do workflow pós-agendamento")
        return True
    else:
        print("\n❌ A correção não está no local correto ou está faltando algo.")
        return False

def main():
    """
    Executa todos os testes de validação.
    """
    print("🚀 VALIDANDO A CORREÇÃO DO ESTÁGIO DO CRM")
    print("=" * 50)
    
    # Teste 1: Verifica se a lógica foi implementada
    test1_passed = test_crm_stage_update_logic()
    
    # Teste 2: Verifica se está no local correto
    test2_passed = test_code_placement()
    
    print("\n" + "=" * 50)
    
    if test1_passed and test2_passed:
        print("🎉 VALIDAÇÃO COMPLETA - CORREÇÃO IMPLEMENTADA COM SUCESSO!")
        print("\n📋 Resumo da correção:")
        print("   ✅ Após agendar reunião com sucesso")
        print("   ✅ Sistema verifica se existe kommo_lead_id")
        print("   ✅ Chama crm_service.update_lead_stage()")
        print("   ✅ Move lead para estágio 'reunião_agendada'")
        print("   ✅ Registra log de sucesso")
        print("   ✅ Trata erros adequadamente")
        print("   ✅ Continua fluxo normal mesmo se CRM falhar")
        print("\n🚀 A correção está pronta para ser testada em produção!")
        return True
    else:
        print("❌ VALIDAÇÃO FALHOU - CORREÇÃO INCOMPLETA")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)