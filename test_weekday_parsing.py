#!/usr/bin/env python3
"""
Teste de parsing de dias da semana
Valida que o sistema interpreta corretamente nomes de dias da semana
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from datetime import datetime, timedelta

async def test_weekday_parsing():
    """Testa se o sistema processa corretamente dias da semana"""
    
    print("=" * 70)
    print("TESTE: Parsing de Dias da Semana")
    print("=" * 70)
    
    from app.core.team_coordinator import TeamCoordinator
    
    coordinator = TeamCoordinator()
    await coordinator.initialize()
    
    tests_passed = 0
    tests_total = 0
    
    # Teste 1: Segunda-feira
    print("\n📝 Teste 1: Parsing de 'segunda-feira'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("pode ser segunda-feira as 10h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 0:  # 0 = Monday
            print(f"✅ Segunda-feira detectada corretamente: {result['date']}")
            print(f"   Horário: {result['time']}")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para segunda: {result['date']} (weekday={date_obj.weekday()})")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 2: Terça-feira
    print("\n📝 Teste 2: Parsing de 'terça'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("terça às 14h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 1:  # 1 = Tuesday
            print(f"✅ Terça-feira detectada: {result['date']}")
            print(f"   Horário: {result['time']}")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para terça: {result['date']}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 3: Quarta-feira
    print("\n📝 Teste 3: Parsing de 'quarta-feira'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("quarta-feira pode ser?")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 2:  # 2 = Wednesday
            print(f"✅ Quarta-feira detectada: {result['date']}")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para quarta: {result['date']}")
    else:
        print("❌ Falhou ao extrair data")
    
    # Teste 4: Quinta-feira
    print("\n📝 Teste 4: Parsing de 'quinta feira' (sem hífen)")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("quinta feira as 9h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 3:  # 3 = Thursday
            print(f"✅ Quinta-feira detectada: {result['date']}")
            print(f"   Horário: {result['time']}")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para quinta: {result['date']}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 5: Sexta-feira
    print("\n📝 Teste 5: Parsing de 'sexta'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("sexta 16h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 4:  # 4 = Friday
            print(f"✅ Sexta-feira detectada: {result['date']}")
            print(f"   Horário: {result['time']}")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para sexta: {result['date']}")
    else:
        print("❌ Falhou ao extrair data/hora")
    
    # Teste 6: Sábado (fim de semana)
    print("\n📝 Teste 6: Parsing de 'sábado'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("sábado as 10h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 5:  # 5 = Saturday
            print(f"✅ Sábado detectado: {result['date']}")
            print(f"   ⚠️ Nota: Sistema deve bloquear agendamento no sábado")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para sábado: {result['date']}")
    else:
        print("❌ Falhou ao extrair data")
    
    # Teste 7: Domingo (fim de semana)
    print("\n📝 Teste 7: Parsing de 'domingo'")
    print("-" * 50)
    tests_total += 1
    
    result = coordinator._extract_datetime("domingo")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        if date_obj.weekday() == 6:  # 6 = Sunday
            print(f"✅ Domingo detectado: {result['date']}")
            print(f"   ⚠️ Nota: Sistema deve bloquear agendamento no domingo")
            tests_passed += 1
        else:
            print(f"❌ Data incorreta para domingo: {result['date']}")
    else:
        print("❌ Falhou ao extrair data")
    
    # Teste 8: Próxima ocorrência
    print("\n📝 Teste 8: Verificar se pega próxima ocorrência")
    print("-" * 50)
    tests_total += 1
    
    hoje = datetime.now()
    result = coordinator._extract_datetime("segunda-feira as 10h")
    if result:
        date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
        # Deve ser uma data futura
        if date_obj > hoje:
            print(f"✅ Data futura corretamente calculada: {result['date']}")
            print(f"   Hoje: {hoje.strftime('%A, %d/%m/%Y')}")
            print(f"   Agendamento: {date_obj.strftime('%A, %d/%m/%Y')}")
            tests_passed += 1
        else:
            print(f"❌ Data não é futura: {result['date']}")
    else:
        print("❌ Falhou ao extrair data")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Parsing de dias da semana funcionando!")
        print("\n✅ Funcionalidades validadas:")
        print("   • Detecta todos os dias da semana em português")
        print("   • Suporta variações (com/sem hífen)")
        print("   • Calcula próxima ocorrência corretamente")
        print("   • Extrai horário junto com o dia")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_weekday_parsing())
    exit(0 if result else 1)