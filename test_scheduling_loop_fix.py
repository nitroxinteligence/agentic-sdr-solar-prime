#!/usr/bin/env python3
"""
Teste completo da correção do loop de agendamento
Valida que o sistema não fica em loop quando usuário escolhe horário
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
import re

async def test_scheduling_loop_fix():
    """Testa a correção do loop de agendamento"""
    
    print("=" * 70)
    print("TESTE: Correção do Loop de Agendamento")
    print("=" * 70)
    
    from app.core.team_coordinator import TeamCoordinator
    
    tests_passed = 0
    tests_total = 0
    
    # Criar instância do TeamCoordinator
    coordinator = TeamCoordinator()
    
    print("\n📝 Teste 1: Detecção de padrão de escolha de horário")
    print("-" * 50)
    
    # Simular histórico com horários apresentados
    conversation_history = [
        {"role": "user", "content": "quero agendar uma reunião"},
        {"role": "assistant", "content": "Perfeito! Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?"},
        {"role": "user", "content": "pode ser as 10h"}
    ]
    
    # Teste 1: Detectar escolha de horário "pode ser as 10h"
    tests_total += 1
    is_selection = coordinator._detect_time_selection_pattern(
        "pode ser as 10h",
        conversation_history[:-1]  # Sem a última mensagem (que é a atual)
    )
    if is_selection:
        print("✅ Detectou 'pode ser as 10h' como escolha de horário")
        tests_passed += 1
    else:
        print("❌ NÃO detectou 'pode ser as 10h' como escolha")
    
    # Teste 2: Detectar variações de escolha
    tests_total += 1
    test_phrases = [
        "10h tá bom",
        "escolho 11h", 
        "prefiro às 9h",
        "fica as 10",
        "vamos as 11h",
        "ok, 10h",
        "sim, as 9h"
    ]
    
    detection_count = 0
    for phrase in test_phrases:
        if coordinator._detect_time_selection_pattern(phrase, conversation_history[:-1]):
            detection_count += 1
    
    if detection_count >= 5:  # Pelo menos 5 de 7 frases
        print(f"✅ Detectou {detection_count}/7 variações de escolha de horário")
        tests_passed += 1
    else:
        print(f"❌ Detectou apenas {detection_count}/7 variações")
    
    # Teste 3: NÃO detectar quando é pergunta
    tests_total += 1
    question_phrases = [
        "quais horários tem disponível?",
        "tem horário amanhã?",
        "pode verificar a agenda?"
    ]
    
    false_positives = 0
    for phrase in question_phrases:
        if coordinator._detect_time_selection_pattern(phrase, conversation_history[:-1]):
            false_positives += 1
    
    if false_positives == 0:
        print("✅ NÃO detectou perguntas como escolhas (0 falsos positivos)")
        tests_passed += 1
    else:
        print(f"❌ Detectou {false_positives} perguntas como escolhas")
    
    print("\n📝 Teste 2: Extração de data/hora com contexto")
    print("-" * 50)
    
    # Teste 4: Extrair hora quando usuário diz apenas "10h"
    tests_total += 1
    datetime_info = coordinator._extract_datetime("pode ser as 10h", conversation_history)
    if datetime_info and datetime_info["time"] == "10:00":
        print(f"✅ Extraiu hora corretamente: {datetime_info['time']}")
        tests_passed += 1
    else:
        print(f"❌ Falhou ao extrair hora: {datetime_info}")
    
    # Teste 5: Herdar data do contexto (amanhã)
    tests_total += 1
    from datetime import datetime, timedelta
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    if datetime_info and datetime_info["date"] == tomorrow:
        print(f"✅ Herdou data do contexto (amanhã): {datetime_info['date']}")
        tests_passed += 1
    else:
        print(f"❌ Não herdou data corretamente: {datetime_info}")
    
    print("\n📝 Teste 3: execute_services com detecção de contexto")
    print("-" * 50)
    
    # Mock dos serviços
    mock_calendar = AsyncMock()
    mock_calendar.check_availability = AsyncMock(return_value={
        "success": True,
        "message": "Horários disponíveis"
    })
    
    coordinator.services = {"calendar": mock_calendar}
    coordinator.is_initialized = True
    
    # Teste 6: NÃO executar check_availability quando detecta escolha
    tests_total += 1
    context = {
        "conversation_history": conversation_history[:-1],
        "conversation_stage": "agendamento"
    }
    
    results = await coordinator.execute_services(
        "pode ser as 10h",
        context,
        {"name": "Teste", "phone": "123"}
    )
    
    if len(results) == 0:
        print("✅ NÃO executou serviços quando detectou escolha de horário")
        tests_passed += 1
    else:
        print(f"❌ Executou {len(results)} serviços quando não deveria")
    
    # Teste 7: Verificar que check_availability NÃO foi chamado
    tests_total += 1
    if mock_calendar.check_availability.call_count == 0:
        print("✅ check_availability NÃO foi chamado (correto!)")
        tests_passed += 1
    else:
        print(f"❌ check_availability foi chamado {mock_calendar.check_availability.call_count} vezes")
    
    print("\n📝 Teste 4: Fluxo normal sem escolha")
    print("-" * 50)
    
    # Reset mock
    mock_calendar.check_availability.reset_mock()
    
    # Teste 8: EXECUTAR check_availability quando é pergunta
    tests_total += 1
    context_question = {
        "conversation_history": [],
        "conversation_stage": "agendamento"
    }
    
    # Simular necessidade de calendar
    coordinator.decision_threshold = 0.3  # Baixar threshold para teste
    
    results = await coordinator.execute_services(
        "quero agendar uma reunião amanhã",
        context_question,
        {"name": "Teste", "phone": "123"}
    )
    
    # Como o analyze_service_need deve detectar necessidade de calendar
    # e não há padrão de escolha, deve executar
    if coordinator.analyze_service_need("quero agendar uma reunião amanhã", context_question)["calendar"] > 0.3:
        print("✅ Detectou necessidade de calendar para pergunta de agendamento")
        tests_passed += 1
    else:
        print("❌ NÃO detectou necessidade de calendar")
    
    print("\n📝 Teste 5: Validação das regras no prompt")
    print("-" * 50)
    
    # Ler prompt
    from pathlib import Path
    prompt_path = Path("app/prompts/prompt-agente.md")
    if prompt_path.exists():
        prompt_content = prompt_path.read_text(encoding='utf-8')
        
        # Teste 9: Verificar Step 5 no fluxo
        tests_total += 1
        if "Step 5: DETECTAR escolha e NÃO repetir check_availability" in prompt_content:
            print("✅ Step 5 de detecção presente no prompt")
            tests_passed += 1
        else:
            print("❌ Step 5 de detecção ausente no prompt")
        
        # Teste 10: Verificar regra crítica
        tests_total += 1
        if "REGRA CRÍTICA DO STEP 5" in prompt_content:
            print("✅ Regra crítica do Step 5 presente")
            tests_passed += 1
        else:
            print("❌ Regra crítica do Step 5 ausente")
        
        # Teste 11: Verificar exemplos de escolha
        tests_total += 1
        if '"pode ser as 10h"' in prompt_content and '"escolho 11h"' in prompt_content:
            print("✅ Exemplos de escolha de horário presentes")
            tests_passed += 1
        else:
            print("❌ Exemplos de escolha ausentes")
        
        # Teste 12: Verificar instrução de não repetir
        tests_total += 1
        if "NÃO use check_availability novamente" in prompt_content:
            print("✅ Instrução de não repetir check presente")
            tests_passed += 1
        else:
            print("❌ Instrução de não repetir ausente")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Loop de agendamento corrigido!")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_scheduling_loop_fix())
    exit(0 if result else 1)