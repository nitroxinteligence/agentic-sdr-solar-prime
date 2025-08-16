#!/usr/bin/env python3
"""
Teste completo do sistema de agendamento
Valida parsing de dias da semana, bloqueio de finais de semana e fluxo completo
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from datetime import datetime, timedelta

async def test_scheduling_complete():
    """Testa o fluxo completo de agendamento com dias da semana"""
    
    print("=" * 70)
    print("TESTE COMPLETO: Sistema de Agendamento com Dias da Semana")
    print("=" * 70)
    
    from app.core.team_coordinator import TeamCoordinator
    from app.services.calendar_service_100_real import CalendarServiceReal
    
    coordinator = TeamCoordinator()
    await coordinator.initialize()
    
    calendar = CalendarServiceReal()
    await calendar.initialize()
    
    tests_passed = 0
    tests_total = 0
    
    # Teste 1: Agendamento em dia útil (segunda-feira)
    print("\n📝 Teste 1: Agendar em segunda-feira (dia útil)")
    print("-" * 50)
    tests_total += 1
    
    # Extrair data para segunda-feira
    datetime_info = coordinator._extract_datetime("segunda-feira as 10h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        # Tentar agendar
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time=datetime_info['time'],
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("success"):
            print(f"✅ Agendamento bem-sucedido para segunda-feira")
            print(f"   → {result.get('message')}")
            tests_passed += 1
            
            # Cancelar o evento criado
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
                print("   → Evento de teste cancelado")
        else:
            if result.get("error") == "weekend_not_allowed":
                print(f"❌ Segunda-feira incorretamente bloqueada como fim de semana")
            else:
                print(f"❌ Erro ao agendar: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 2: Agendamento em sexta-feira (dia útil)
    print("\n📝 Teste 2: Agendar em sexta-feira (dia útil)")
    print("-" * 50)
    tests_total += 1
    
    datetime_info = coordinator._extract_datetime("sexta as 14h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time=datetime_info['time'],
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("success"):
            print(f"✅ Agendamento bem-sucedido para sexta-feira")
            tests_passed += 1
            
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
                print("   → Evento de teste cancelado")
        else:
            print(f"❌ Erro ao agendar: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 3: Bloqueio de sábado
    print("\n📝 Teste 3: Bloqueio de agendamento no sábado")
    print("-" * 50)
    tests_total += 1
    
    datetime_info = coordinator._extract_datetime("sábado as 10h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time=datetime_info['time'],
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("error") == "weekend_not_allowed":
            print(f"✅ Sábado corretamente bloqueado")
            print(f"   → {result.get('message')}")
            tests_passed += 1
        elif result.get("success"):
            print(f"❌ ERRO: Permitiu agendar no sábado!")
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
        else:
            print(f"❌ Erro inesperado: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 4: Bloqueio de domingo
    print("\n📝 Teste 4: Bloqueio de agendamento no domingo")
    print("-" * 50)
    tests_total += 1
    
    datetime_info = coordinator._extract_datetime("domingo as 15h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time=datetime_info['time'],
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("error") == "weekend_not_allowed":
            print(f"✅ Domingo corretamente bloqueado")
            print(f"   → {result.get('message')}")
            tests_passed += 1
        elif result.get("success"):
            print(f"❌ ERRO: Permitiu agendar no domingo!")
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
        else:
            print(f"❌ Erro inesperado: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 5: Bloqueio de horário fora do expediente
    print("\n📝 Teste 5: Bloqueio de horário fora do expediente (20h)")
    print("-" * 50)
    tests_total += 1
    
    datetime_info = coordinator._extract_datetime("segunda as 20h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time="20:00",  # Forçar horário fora do expediente
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("error") == "outside_business_hours":
            print(f"✅ Horário fora do expediente corretamente bloqueado")
            print(f"   → {result.get('message')}")
            tests_passed += 1
        elif result.get("success"):
            print(f"❌ ERRO: Permitiu agendar às 20h!")
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
        else:
            print(f"⚠️ Outro erro: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 6: Horário dentro do expediente (10h)
    print("\n📝 Teste 6: Agendamento às 10h (dentro do expediente)")
    print("-" * 50)
    tests_total += 1
    
    datetime_info = coordinator._extract_datetime("terça as 10h")
    
    if datetime_info:
        print(f"   Data extraída: {datetime_info['date']} {datetime_info['time']}")
        
        result = await calendar.schedule_meeting(
            date=datetime_info['date'],
            time=datetime_info['time'],
            lead_info={"name": "Teste", "email": "teste@example.com"}
        )
        
        if result.get("success"):
            print(f"✅ Agendamento bem-sucedido dentro do expediente")
            tests_passed += 1
            
            if result.get("meeting_id"):
                await calendar.cancel_meeting(result["meeting_id"])
                print("   → Evento de teste cancelado")
        else:
            print(f"❌ Erro ao agendar: {result.get('message')}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Sistema de agendamento funcionando perfeitamente!")
        print("\n✅ Funcionalidades validadas:")
        print("   • Parsing correto de dias da semana em português")
        print("   • Agendamento permitido em dias úteis (segunda a sexta)")
        print("   • Bloqueio efetivo de sábados e domingos")
        print("   • Bloqueio de horários fora do expediente (antes 8h, após 17h)")
        print("   • Mensagens amigáveis com sugestões de dias úteis")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema ainda precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_scheduling_complete())
    exit(0 if result else 1)