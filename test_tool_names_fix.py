#!/usr/bin/env python3
"""
Teste para validar a correção dos nomes de tools
"""

import re
import asyncio
from pathlib import Path

async def test_tool_names():
    """Testa se os nomes dos tools estão corretos no prompt e no executor"""
    
    print("=" * 50)
    print("TESTE: Correção dos nomes de tools")
    print("=" * 50)
    
    # Ler o prompt
    prompt_path = Path("app/prompts/prompt-agente.md")
    prompt_content = prompt_path.read_text(encoding='utf-8')
    
    # Ler o executor
    executor_path = Path("app/agents/agentic_sdr_stateless.py")
    executor_content = executor_path.read_text(encoding='utf-8')
    
    # Padrões errados que não devem existir
    wrong_patterns = [
        r'calendar_service\.check_availability\(\)',
        r'calendar_service\.create_event\(\)',
        r'calendar_service\.schedule_meeting',
        r'followup_service\.schedule',
        r'crm_service\.'
    ]
    
    # Verificar se existem padrões errados no prompt
    errors_found = []
    for pattern in wrong_patterns:
        matches = re.findall(pattern, prompt_content)
        if matches:
            errors_found.append(f"❌ Padrão errado encontrado no prompt: {pattern}")
            for match in matches[:3]:  # Mostrar até 3 exemplos
                print(f"   - {match}")
    
    # Padrões corretos que devem existir
    correct_patterns = [
        r'\[TOOL:\s*calendar\.check_availability\]',
        r'\[TOOL:\s*calendar\.schedule_meeting[^\]]*\]',
        r'\[TOOL:\s*followup\.schedule[^\]]*\]',
        r'\[TOOL:\s*crm\.update_stage[^\]]*\]'
    ]
    
    # Verificar se os padrões corretos existem
    correct_found = []
    for pattern in correct_patterns:
        matches = re.findall(pattern, prompt_content)
        if matches:
            correct_found.append(f"✅ Padrão correto encontrado: {matches[0]}")
    
    # Verificar o executor
    executor_services = {
        'calendar': ['check_availability', 'schedule_meeting', 'suggest_times'],
        'crm': ['update_stage', 'update_field'],
        'followup': ['schedule']
    }
    
    print("\n📝 Verificando prompt:")
    if errors_found:
        for error in errors_found:
            print(error)
    else:
        print("✅ Nenhum padrão errado encontrado no prompt!")
    
    print("\n✅ Padrões corretos encontrados:")
    for found in correct_found[:5]:  # Mostrar até 5 exemplos
        print(f"   {found}")
    
    print("\n🔧 Verificando executor:")
    for service, methods in executor_services.items():
        if f'service_name == "{service}"' in executor_content:
            print(f"✅ Serviço '{service}' mapeado corretamente")
            for method in methods:
                if f'method_name == "{method}"' in executor_content:
                    print(f"   ✅ Método '{method}' implementado")
        else:
            print(f"❌ Serviço '{service}' não encontrado no executor")
    
    # Resultado final
    print("\n" + "=" * 50)
    if not errors_found:
        print("🎉 SUCESSO: Todos os nomes de tools estão corretos!")
    else:
        print("⚠️ ATENÇÃO: Ainda existem referências antigas que precisam ser corrigidas")
    print("=" * 50)
    
    return len(errors_found) == 0

if __name__ == "__main__":
    result = asyncio.run(test_tool_names())
    exit(0 if result else 1)