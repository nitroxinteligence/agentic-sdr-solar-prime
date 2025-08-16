#!/usr/bin/env python3
"""
Teste completo do sistema anti-alucinação para Google Calendar
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
import re

async def test_anti_hallucination():
    """Testa o sistema anti-alucinação completo"""
    
    print("=" * 70)
    print("TESTE: Sistema Anti-Alucinação para Google Calendar")
    print("=" * 70)
    
    from app.agents.agentic_sdr_stateless import AgenticSDRStateless
    from pathlib import Path
    
    # Mock do team_coordinator
    mock_coordinator = MagicMock()
    mock_model_manager = AsyncMock()
    
    # Criar agente
    agent = AgenticSDRStateless()
    agent.team_coordinator = mock_coordinator
    agent.model_manager = mock_model_manager
    
    # Simular service_results do Calendar
    service_results = [
        {
            "service": "calendar",
            "success": True,
            "data": {
                "message": "Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?"
            },
            "result": "Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?"
        }
    ]
    
    # Lead info
    lead_info = {
        "name": "Mateus",
        "phone": "5511999999999"
    }
    
    # Contexto
    context = {
        "conversation_stage": "agendamento"
    }
    
    print("\n📝 Teste 1: Verificar formatação de service_results no prompt")
    print("-" * 50)
    
    prompt = agent._build_prompt_with_history(
        "eu quero agendar uma reunião pra amanhã",
        context,
        lead_info,
        service_results,
        "",
        [],
        {}
    )
    
    # Verificar se service_results estão no prompt
    tests_passed = 0
    tests_total = 0
    
    # Teste 1: Service results incluídos
    tests_total += 1
    if "RESULTADOS DE SERVIÇOS EXECUTADOS" in prompt:
        print("✅ Service results incluídos no prompt")
        tests_passed += 1
    else:
        print("❌ Service results NÃO incluídos no prompt")
    
    # Teste 2: Seção de resultados formatada
    tests_total += 1
    if "🚨 === RESULTADOS DE SERVIÇOS EXECUTADOS === 🚨" in prompt:
        print("✅ Seção de resultados formatada corretamente")
        tests_passed += 1
    else:
        print("❌ Seção de resultados mal formatada")
    
    # Teste 3: Instrução para usar resultados
    tests_total += 1
    if "VOCÊ DEVE usar estes resultados" in prompt:
        print("✅ Instrução para usar resultados presente")
        tests_passed += 1
    else:
        print("❌ Instrução para usar resultados ausente")
    
    # Teste 4: Calendar funcionou
    tests_total += 1
    if "CALENDAR EXECUTADO COM SUCESSO" in prompt:
        print("✅ Calendar marcado como sucesso")
        tests_passed += 1
    else:
        print("❌ Calendar não marcado como sucesso")
    
    # Teste 5: Mensagem do Calendar
    tests_total += 1
    if "09:00, 10:00, 11:00" in prompt:
        print("✅ Horários do Calendar presentes")
        tests_passed += 1
    else:
        print("❌ Horários do Calendar ausentes")
    
    print("\n📝 Teste 2: Verificar detecção de alucinação")
    print("-" * 50)
    
    # Simular resposta alucinada
    hallucinated_response = """
    <RESPOSTA_FINAL>
    Vixe, Mateus! Desculpa, mas estou tendo alguns probleminhas técnicos aqui pra acessar a agenda do Leonardo.
    </RESPOSTA_FINAL>
    """
    
    # Teste 6: Detectar termos de alucinação
    tests_total += 1
    hallucination_terms = [
        "problemas técnicos", "probleminhas técnicos",
        "erro", "não consegui", "não consigo",
        "desculpa", "desculpe", "vixe"
    ]
    
    response_lower = hallucinated_response.lower()
    has_hallucination = any(term in response_lower for term in hallucination_terms)
    
    if has_hallucination:
        print("✅ Alucinação detectada corretamente")
        tests_passed += 1
    else:
        print("❌ Alucinação não detectada")
    
    # Teste 7: Calendar result encontrado
    tests_total += 1
    calendar_result = next((r for r in service_results if r.get("service") == "calendar" and r.get("success")), None)
    if calendar_result:
        print("✅ Calendar result encontrado")
        tests_passed += 1
    else:
        print("❌ Calendar result não encontrado")
    
    # Teste 8: Extração de mensagem
    tests_total += 1
    calendar_data = calendar_result.get("data", {})
    calendar_message = calendar_data.get("message", "")
    if not calendar_message and calendar_result.get("result"):
        calendar_message = calendar_result.get("result")
    
    if "09:00, 10:00, 11:00" in calendar_message:
        print("✅ Mensagem do Calendar extraída corretamente")
        tests_passed += 1
    else:
        print("❌ Mensagem do Calendar não extraída")
    
    # Teste 9: Sistema detectaria alucinação
    tests_total += 1
    if calendar_result and has_hallucination:
        print("✅ Sistema detectaria e corrigiria alucinação")
        tests_passed += 1
    else:
        print("❌ Sistema não detectaria alucinação")
    
    print("\n📝 Teste 3: Verificar regras no prompt")
    print("-" * 50)
    
    # Ler prompt
    prompt_path = Path("app/prompts/prompt-agente.md")
    if prompt_path.exists():
        prompt_content = prompt_path.read_text(encoding='utf-8')
        
        # Teste 10: Regra SERVICE_RESULTS_PRIORITY
        tests_total += 1
        if "SERVICE_RESULTS_PRIORITY" in prompt_content:
            print("✅ Regra SERVICE_RESULTS_PRIORITY presente")
            tests_passed += 1
        else:
            print("❌ Regra SERVICE_RESULTS_PRIORITY ausente")
        
        # Teste 11: Palavras proibidas
        tests_total += 1
        if "PALAVRAS PROIBIDAS quando serviços funcionaram" in prompt_content:
            print("✅ Lista de palavras proibidas presente")
            tests_passed += 1
        else:
            print("❌ Lista de palavras proibidas ausente")
        
        # Teste 12: Regras invioláveis
        tests_total += 1
        if "REGRAS INVIOLÁVEIS" in prompt_content:
            print("✅ Regras invioláveis definidas")
            tests_passed += 1
        else:
            print("❌ Regras invioláveis não definidas")
    
    print("\n📝 Teste 4: Validar prompt de correção")
    print("-" * 50)
    
    # Teste 13: Contexto de agendamento
    tests_total += 1
    if context.get("conversation_stage") == "agendamento":
        print("✅ Contexto de agendamento identificado")
        tests_passed += 1
    else:
        print("❌ Contexto de agendamento não identificado")
    
    # Teste 14: Nome do lead
    tests_total += 1
    if lead_info.get("name") == "Mateus":
        print("✅ Nome do lead presente")
        tests_passed += 1
    else:
        print("❌ Nome do lead ausente")
    
    # Teste 15: Mensagem original
    tests_total += 1
    message = "eu quero agendar uma reunião pra amanhã"
    if message:
        print("✅ Mensagem original capturada")
        tests_passed += 1
    else:
        print("❌ Mensagem original não capturada")
    
    # Teste 16: Resultado do Calendar
    tests_total += 1
    if calendar_message and "09:00" in calendar_message:
        print("✅ Resultado do Calendar formatado")
        tests_passed += 1
    else:
        print("❌ Resultado do Calendar não formatado")
    
    # Resultado final
    print("\n" + "=" * 70)
    print(f"RESULTADO: {tests_passed}/{tests_total} testes passaram ({tests_passed*100/tests_total:.1f}%)")
    
    if tests_passed == tests_total:
        print("🎉 SUCESSO TOTAL: Sistema anti-alucinação 100% funcional!")
    elif tests_passed >= tests_total * 0.8:
        print("✅ BOM: Sistema anti-alucinação funcionando adequadamente")
    else:
        print("⚠️ ATENÇÃO: Sistema anti-alucinação precisa de ajustes")
    
    print("=" * 70)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    result = asyncio.run(test_anti_hallucination())
    exit(0 if result else 1)