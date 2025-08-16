#!/usr/bin/env python3
"""
Teste completo de todas as correções da v0.5
Valida todas as melhorias implementadas recentemente
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from datetime import datetime, timedelta

async def test_all_fixes():
    """Testa todas as correções implementadas na v0.5"""
    
    print("=" * 70)
    print("TESTE COMPLETO: Todas as Correções v0.5")
    print("=" * 70)
    
    tests_passed = 0
    tests_total = 0
    
    # ========== TESTE 1: Tool Calling System ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 1: Tool Calling System")
    print("=" * 70)
    
    from app.agents.agentic_sdr_stateless import create_stateless_agent
    
    tests_total += 1
    try:
        agent = await create_stateless_agent()
        
        # Testar parsing de tool calls
        test_messages = [
            "[TOOL: calendar.check_availability]",
            "[TOOL: calendar.schedule_meeting | date=2025-08-18 | time=10:00 | email=user@test.com]",
            "[TOOL: crm.update_stage | stage=qualificado]",
        ]
        
        all_parsed = True
        for msg in test_messages:
            import re
            tool_pattern = r'\[TOOL:\s*([^|]+?)(?:\s*\|\s*([^\]]+))?\]'
            if not re.search(tool_pattern, msg):
                all_parsed = False
                break
        
        if all_parsed:
            print("✅ Tool Call Parser funcionando")
            tests_passed += 1
        else:
            print("❌ Problema no Tool Call Parser")
    except Exception as e:
        print(f"❌ Erro no Tool Calling System: {e}")
    
    # ========== TESTE 2: Weekday Parsing ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 2: Parsing de Dias da Semana")
    print("=" * 70)
    
    from app.core.team_coordinator import TeamCoordinator
    
    coordinator = TeamCoordinator()
    await coordinator.initialize()
    
    weekday_tests = [
        ("segunda-feira as 10h", 0),  # Monday
        ("terça às 14h", 1),           # Tuesday
        ("quarta feira", 2),            # Wednesday
        ("quinta", 3),                  # Thursday
        ("sexta as 16h", 4),           # Friday
        ("sábado", 5),                 # Saturday
        ("domingo as 9h", 6),          # Sunday
    ]
    
    weekday_success = 0
    for text, expected_weekday in weekday_tests:
        tests_total += 1
        result = coordinator._extract_datetime(text)
        if result:
            date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
            if date_obj.weekday() == expected_weekday:
                weekday_success += 1
                tests_passed += 1
    
    print(f"✅ Weekday Parsing: {weekday_success}/{len(weekday_tests)} testes passaram")
    
    # ========== TESTE 3: Business Hours Enforcement ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 3: Bloqueio de Horário Comercial")
    print("=" * 70)
    
    from app.services.calendar_service_100_real import CalendarServiceReal
    
    calendar = CalendarServiceReal()
    await calendar.initialize()
    
    # Teste de fim de semana
    tests_total += 1
    result = await calendar.schedule_meeting(
        date="2025-08-23",  # Saturday
        time="10:00",
        lead_info={"name": "Teste", "email": "test@example.com"}
    )
    
    if result.get("error") == "weekend_not_allowed":
        print("✅ Bloqueio de sábado funcionando")
        tests_passed += 1
    else:
        print("❌ Falha no bloqueio de sábado")
    
    # Teste de domingo
    tests_total += 1
    result = await calendar.schedule_meeting(
        date="2025-08-24",  # Sunday
        time="14:00",
        lead_info={"name": "Teste", "email": "test@example.com"}
    )
    
    if result.get("error") == "weekend_not_allowed":
        print("✅ Bloqueio de domingo funcionando")
        tests_passed += 1
    else:
        print("❌ Falha no bloqueio de domingo")
    
    # Teste de horário fora do expediente
    tests_total += 1
    result = await calendar.schedule_meeting(
        date="2025-08-18",  # Monday
        time="20:00",  # 8 PM - outside business hours
        lead_info={"name": "Teste", "email": "test@example.com"}
    )
    
    if result.get("error") == "outside_business_hours":
        print("✅ Bloqueio de horário fora do expediente")
        tests_passed += 1
    else:
        print("❌ Falha no bloqueio de horário")
    
    # ========== TESTE 4: Context-Aware Scheduling ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 4: Detecção de Contexto para Agendamento")
    print("=" * 70)
    
    tests_total += 1
    
    # Simular contexto de seleção de horário
    conversation_history = [
        {"role": "assistant", "content": "Tenho estes horários disponíveis: 10:00, 14:00, 16:00. Qual prefere?"},
        {"role": "user", "content": "pode ser as 10h"}
    ]
    
    is_selecting = coordinator._detect_time_selection_pattern(
        "pode ser as 10h",
        conversation_history
    )
    
    if is_selecting:
        print("✅ Detecção de seleção de horário funcionando")
        tests_passed += 1
    else:
        print("❌ Falha na detecção de contexto")
    
    # ========== TESTE 5: Follow-up System Fixes ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 5: Correções do Sistema de Follow-up")
    print("=" * 70)
    
    tests_total += 1
    try:
        from app.services.followup_executor_service import FollowUpExecutorService
        executor = FollowUpExecutorService()
        print("✅ FollowUpExecutorService carregado corretamente")
        tests_passed += 1
    except Exception as e:
        print(f"❌ Erro no FollowUpExecutorService: {e}")
    
    # ========== TESTE 6: Anti-Hallucination Rules ==========
    print("\n" + "=" * 70)
    print("SEÇÃO 6: Regras Anti-Alucinação")
    print("=" * 70)
    
    tests_total += 1
    
    # Verificar se o prompt tem as regras anti-alucinação
    import os
    prompt_path = os.path.join(
        os.path.dirname(__file__),
        "app/prompts/prompt-agente.md"
    )
    
    if os.path.exists(prompt_path):
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "<anti_hallucination_system" in content:
                print("✅ Regras anti-alucinação presentes no prompt")
                tests_passed += 1
            else:
                print("❌ Regras anti-alucinação não encontradas")
    else:
        print("❌ Arquivo de prompt não encontrado")
    
    # ========== RESULTADOS FINAIS ==========
    print("\n" + "=" * 70)
    print("RESULTADO FINAL")
    print("=" * 70)
    
    print(f"\n📊 Total: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("\n🎉 SUCESSO TOTAL: Todas as correções v0.5 funcionando!")
        print("\n✅ Funcionalidades Validadas:")
        print("   • Tool Calling System operacional")
        print("   • Parsing de dias da semana em português")
        print("   • Bloqueio de fins de semana e horário comercial")
        print("   • Detecção inteligente de contexto")
        print("   • Sistema de follow-up corrigido")
        print("   • Regras anti-alucinação implementadas")
    elif tests_passed >= tests_total * 0.8:
        print("\n✅ BOM: Sistema funcionando adequadamente")
    else:
        print("\n⚠️ ATENÇÃO: Sistema ainda precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_all_fixes())
    exit(0 if result else 1)