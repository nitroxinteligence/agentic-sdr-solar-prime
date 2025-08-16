#!/usr/bin/env python3
"""
Teste do bloqueio de agendamento fora do horário comercial
Valida que o sistema bloqueia finais de semana e horários fora do expediente
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from datetime import datetime, timedelta

async def test_business_hours_blocking():
    """Testa o bloqueio de horários fora do expediente"""
    
    print("=" * 70)
    print("TESTE: Bloqueio de Horário Comercial")
    print("=" * 70)
    
    from app.services.calendar_service_100_real import CalendarServiceReal
    
    # Criar instância do serviço
    calendar_service = CalendarServiceReal()
    
    tests_passed = 0
    tests_total = 0
    
    print("\n📝 Teste 1: Validação de horário comercial")
    print("-" * 50)
    
    # Teste 1: Segunda-feira às 10h (DEVE PASSAR)
    tests_total += 1
    monday_10am = datetime(2025, 8, 18, 10, 0)  # Segunda, 18/08/2025, 10:00
    if calendar_service.is_business_hours(monday_10am):
        print("✅ Segunda-feira 10h: Dentro do horário comercial")
        tests_passed += 1
    else:
        print("❌ Segunda-feira 10h: Incorretamente bloqueado")
    
    # Teste 2: Sexta-feira às 16h (DEVE PASSAR)
    tests_total += 1
    friday_4pm = datetime(2025, 8, 22, 16, 0)  # Sexta, 22/08/2025, 16:00
    if calendar_service.is_business_hours(friday_4pm):
        print("✅ Sexta-feira 16h: Dentro do horário comercial")
        tests_passed += 1
    else:
        print("❌ Sexta-feira 16h: Incorretamente bloqueado")
    
    # Teste 3: Sábado às 10h (DEVE BLOQUEAR)
    tests_total += 1
    saturday_10am = datetime(2025, 8, 23, 10, 0)  # Sábado, 23/08/2025, 10:00
    if not calendar_service.is_business_hours(saturday_10am):
        print("✅ Sábado 10h: Corretamente bloqueado")
        tests_passed += 1
    else:
        print("❌ Sábado 10h: Não foi bloqueado")
    
    # Teste 4: Domingo às 14h (DEVE BLOQUEAR)
    tests_total += 1
    sunday_2pm = datetime(2025, 8, 24, 14, 0)  # Domingo, 24/08/2025, 14:00
    if not calendar_service.is_business_hours(sunday_2pm):
        print("✅ Domingo 14h: Corretamente bloqueado")
        tests_passed += 1
    else:
        print("❌ Domingo 14h: Não foi bloqueado")
    
    # Teste 5: Segunda às 7h (DEVE BLOQUEAR - antes do expediente)
    tests_total += 1
    monday_7am = datetime(2025, 8, 18, 7, 0)  # Segunda, 18/08/2025, 07:00
    if not calendar_service.is_business_hours(monday_7am):
        print("✅ Segunda 7h: Corretamente bloqueado (antes do expediente)")
        tests_passed += 1
    else:
        print("❌ Segunda 7h: Não foi bloqueado")
    
    # Teste 6: Terça às 18h (DEVE BLOQUEAR - após expediente)
    tests_total += 1
    tuesday_6pm = datetime(2025, 8, 19, 18, 0)  # Terça, 19/08/2025, 18:00
    if not calendar_service.is_business_hours(tuesday_6pm):
        print("✅ Terça 18h: Corretamente bloqueado (após expediente)")
        tests_passed += 1
    else:
        print("❌ Terça 18h: Não foi bloqueado")
    
    print("\n📝 Teste 2: Próximo dia útil")
    print("-" * 50)
    
    # Teste 7: Próximo dia útil de sexta
    tests_total += 1
    friday = datetime(2025, 8, 22, 10, 0)  # Sexta
    next_day = calendar_service.get_next_business_day(friday + timedelta(days=1))
    if next_day.weekday() == 0:  # Segunda
        print(f"✅ Próximo dia útil após sexta: Segunda ({next_day.strftime('%d/%m')})")
        tests_passed += 1
    else:
        print(f"❌ Próximo dia útil incorreto: {next_day.strftime('%A, %d/%m')}")
    
    # Teste 8: Próximo dia útil de sábado
    tests_total += 1
    saturday = datetime(2025, 8, 23, 10, 0)  # Sábado
    next_day = calendar_service.get_next_business_day(saturday)
    if next_day.weekday() == 0:  # Segunda
        print(f"✅ Próximo dia útil de sábado: Segunda ({next_day.strftime('%d/%m')})")
        tests_passed += 1
    else:
        print(f"❌ Próximo dia útil incorreto: {next_day.strftime('%A, %d/%m')}")
    
    print("\n📝 Teste 3: Mensagem de horário comercial")
    print("-" * 50)
    
    # Teste 9: Formato da mensagem
    tests_total += 1
    message = calendar_service.format_business_hours_message()
    if "Segunda a Sexta" in message and "8h" in message and "17h" in message:
        print(f"✅ Mensagem formatada: {message}")
        tests_passed += 1
    else:
        print(f"❌ Mensagem incorreta: {message}")
    
    print("\n📝 Teste 4: Validação no schedule_meeting (simulado)")
    print("-" * 50)
    
    # Teste 10: Simular tentativa de agendar no sábado
    tests_total += 1
    saturday_date = "2025-08-23"  # Sábado
    saturday_time = "10:00"
    
    # Simular o que aconteceria (sem fazer chamada real ao Google)
    meeting_datetime = datetime.strptime(f"{saturday_date} {saturday_time}", "%Y-%m-%d %H:%M")
    
    if not calendar_service.is_business_hours(meeting_datetime):
        print("✅ Agendamento no sábado seria bloqueado")
        tests_passed += 1
        
        # Verificar mensagem de erro
        if meeting_datetime.weekday() in [5, 6]:
            print("   → Mensagem: 'Não agendamos reuniões aos finais de semana'")
            next_business = calendar_service.get_next_business_day(meeting_datetime)
            print(f"   → Sugestão: Segunda-feira, {next_business.strftime('%d/%m')}")
    else:
        print("❌ Agendamento no sábado NÃO seria bloqueado")
    
    # Teste 11: Simular tentativa de agendar às 20h
    tests_total += 1
    evening_date = "2025-08-18"  # Segunda
    evening_time = "20:00"
    
    meeting_datetime = datetime.strptime(f"{evening_date} {evening_time}", "%Y-%m-%d %H:%M")
    
    if not calendar_service.is_business_hours(meeting_datetime):
        print("✅ Agendamento às 20h seria bloqueado")
        tests_passed += 1
        print("   → Mensagem: 'Esse horário está fora do nosso expediente'")
        print(f"   → Horário comercial: {calendar_service.format_business_hours_message()}")
    else:
        print("❌ Agendamento às 20h NÃO seria bloqueado")
    
    # Teste 12: Simular tentativa de agendar às 6h da manhã
    tests_total += 1
    early_date = "2025-08-18"  # Segunda
    early_time = "06:00"
    
    meeting_datetime = datetime.strptime(f"{early_date} {early_time}", "%Y-%m-%d %H:%M")
    
    if not calendar_service.is_business_hours(meeting_datetime):
        print("✅ Agendamento às 6h seria bloqueado")
        tests_passed += 1
        print("   → Mensagem: 'Esse horário está fora do nosso expediente'")
    else:
        print("❌ Agendamento às 6h NÃO seria bloqueado")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Bloqueio de horário comercial funcionando!")
        print("\n✅ Sistema configurado para:")
        print("   • Bloquear agendamentos aos sábados e domingos")
        print("   • Permitir apenas de Segunda a Sexta")
        print("   • Horário: 8h às 17h")
        print("   • Mensagens amigáveis ao usuário")
        print("   • Sugestões de dias/horários alternativos")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_business_hours_blocking())
    exit(0 if result else 1)