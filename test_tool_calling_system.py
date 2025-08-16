#!/usr/bin/env python3
"""
Teste do Sistema de Tool Calling implementado no prompt da Helen
Versão: v0.3 - Sistema Tool Calling
"""

import re
import sys

def test_tool_calling_prompt():
    """Testa se o sistema de tool calling foi implementado corretamente no prompt"""
    
    # Ler o arquivo do prompt
    try:
        with open('app/prompts/prompt-agente.md', 'r', encoding='utf-8') as f:
            prompt_content = f.read()
    except FileNotFoundError:
        print("❌ Arquivo de prompt não encontrado!")
        return False
    
    # Testes de validação
    tests = [
        {
            "name": "🔧 Seção TOOL CALLING SYSTEM existe",
            "pattern": r"<!-- SEÇÃO 11: TOOL CALLING SYSTEM -->",
            "required": True
        },
        {
            "name": "📝 Sintaxe de tool definida",
            "pattern": r"\[TOOL: service\.method \| param1=value1 \| param2=value2\]",
            "required": True
        },
        {
            "name": "📅 Calendar tools definidos",
            "pattern": r"calendar\.check_availability",
            "required": True
        },
        {
            "name": "📅 Calendar schedule meeting",
            "pattern": r"calendar\.schedule_meeting",
            "required": True
        },
        {
            "name": "🔄 CRM tools definidos",
            "pattern": r"crm\.update_stage",
            "required": True
        },
        {
            "name": "🔄 CRM update field",
            "pattern": r"crm\.update_field",
            "required": True
        },
        {
            "name": "⏰ Followup tools definidos",
            "pattern": r"followup\.schedule",
            "required": True
        },
        {
            "name": "📋 Regras críticas de uso",
            "pattern": r"SEMPRE use tools quando:",
            "required": True
        },
        {
            "name": "⚠️ Tratamento de erros definido",
            "pattern": r"SE TOOL RETORNAR ERRO:",
            "required": True
        },
        {
            "name": "💡 Exemplos práticos incluídos",
            "pattern": r"<practical_examples>",
            "required": True
        },
        {
            "name": "🌟 Integração com personalidade",
            "pattern": r"<integration_with_personality>",
            "required": True
        },
        {
            "name": "🔧 Fluxo A usa tools",
            "pattern": r"\[TOOL: calendar\.check_availability\] para buscar horários",
            "required": True
        },
        {
            "name": "🔧 Fluxo B usa tools",
            "pattern": r"\[TOOL: calendar\.schedule_meeting \| date=YYYY-MM-DD",
            "required": True
        },
        {
            "name": "🔧 Qualified actions usa tools",
            "pattern": r"\[TOOL: crm\.update_stage \| stage=qualificado\]",
            "required": True
        }
    ]
    
    results = []
    
    print("🔍 VALIDANDO IMPLEMENTAÇÃO DO SISTEMA TOOL CALLING")
    print("=" * 60)
    
    for test in tests:
        found = bool(re.search(test["pattern"], prompt_content))
        
        if found:
            status = "✅ PASS"
            results.append(True)
        else:
            status = "❌ FAIL"
            results.append(False)
            
        print(f"{status} - {test['name']}")
        
        if not found and test["required"]:
            print(f"   📍 Pattern não encontrado: {test['pattern']}")
    
    print("\n" + "=" * 60)
    
    # Estatísticas
    passed = sum(results)
    total = len(results)
    percentage = (passed / total) * 100
    
    print(f"📊 RESULTADOS: {passed}/{total} testes passaram ({percentage:.1f}%)")
    
    if percentage >= 90:
        print("🎉 SUCESSO: Sistema de Tool Calling implementado com excelência!")
        return True
    elif percentage >= 75:
        print("⚠️  PARCIAL: Sistema implementado mas precisa de ajustes")
        return False
    else:
        print("❌ FALHA: Sistema precisa ser implementado")
        return False

def test_tool_examples():
    """Testa se os exemplos de tool calling estão corretos"""
    
    print("\n🧪 VALIDANDO EXEMPLOS DE TOOL CALLING")
    print("=" * 50)
    
    examples_to_check = [
        "[TOOL: calendar.check_availability]",
        "[TOOL: calendar.schedule_meeting | date=2024-08-20 | time=14:00 | email=cliente@email.com]",
        "[TOOL: crm.update_stage | stage=qualificado]",
        "[TOOL: crm.update_field | field=energy_value | value=1200.50]",
        "[TOOL: followup.schedule | hours=24 | message=Lembrete de reunião amanhã]"
    ]
    
    try:
        with open('app/prompts/prompt-agente.md', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
        return False
    
    for example in examples_to_check:
        # Escapar caracteres especiais para regex
        escaped = re.escape(example)
        if re.search(escaped, content):
            print(f"✅ Exemplo encontrado: {example}")
        else:
            print(f"❌ Exemplo FALTANDO: {example}")
            return False
    
    print("🎉 Todos os exemplos estão presentes!")
    return True

def main():
    """Função principal do teste"""
    
    print("🚀 TESTE DO SISTEMA TOOL CALLING - Helen v0.3")
    print("=" * 60)
    
    # Executar testes
    test1_passed = test_tool_calling_prompt()
    test2_passed = test_tool_examples()
    
    print("\n" + "=" * 60)
    print("📋 RESUMO FINAL:")
    
    if test1_passed and test2_passed:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✨ Sistema de Tool Calling implementado com SUCESSO!")
        print("🔧 Helen agora pode usar tools de forma robusta!")
        return 0
    else:
        print("❌ ALGUNS TESTES FALHARAM!")
        print("🔧 Verifique a implementação do sistema")
        return 1

if __name__ == "__main__":
    sys.exit(main())