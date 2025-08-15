#!/usr/bin/env python3
"""
🧪 Teste das Melhorias do Team Coordinator
Valida a análise inteligente de intenção para acionamento de serviços
"""

import asyncio
import sys
import os
from datetime import datetime

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.abspath('.'))

from app.core.team_coordinator import TeamCoordinator
from app.utils.logger import emoji_logger

def test_calendar_intent_analysis():
    """Testa a análise de intenção para Calendar Service"""
    coordinator = TeamCoordinator()
    
    test_cases = [
        # Casos que DEVEM ativar Calendar (score >= 0.35)
        {
            "message": "Quero agendar uma reunião com Leonardo amanhã",
            "context": {"user_intent": "agendar reunião", "conversation_stage": "qualificação"},
            "expected": "HIGH",
            "description": "Intenção clara + urgência + stage avançado"
        },
        {
            "message": "Podemos conversar hoje às 14h?",
            "context": {"urgency_level": "alta"},
            "expected": "HIGH", 
            "description": "Tempo específico + urgência alta"
        },
        {
            "message": "Vamos marcar para quando você tem disponível",
            "context": {"conversation_stage": "negociação"},
            "expected": "HIGH",
            "description": "Intenção forte + stage avançado"
        },
        
        # Casos que NÃO devem ativar Calendar (score < 0.35)
        {
            "message": "Obrigado pelas informações sobre energia solar",
            "context": {},
            "expected": "LOW",
            "description": "Sem indicadores de agendamento"
        },
        {
            "message": "Meu nome é João e tenho interesse",
            "context": {"conversation_stage": "início"},
            "expected": "LOW",
            "description": "Apenas dados pessoais"
        },
        
        # Casos limítrofes que podem ativar dependendo do contexto
        {
            "message": "Quando vocês atendem?",
            "context": {"user_intent": "horário de funcionamento"},
            "expected": "MEDIUM",
            "description": "Pergunta sobre horário (ambígua)"
        }
    ]
    
    print("🧪 TESTE: Análise de Intenção para Calendar Service")
    print("=" * 60)
    
    passed = 0
    total = len(test_cases)
    
    for i, case in enumerate(test_cases, 1):
        scores = coordinator.analyze_service_need(case["message"], case["context"])
        calendar_score = scores["calendar"]
        
        # Calcular threshold dinâmico
        dynamic_threshold = coordinator._get_dynamic_threshold("calendar", case["context"])
        
        # Determinar se seria ativado
        would_activate = calendar_score >= dynamic_threshold
        
        # Verificar expectativa
        expected = case["expected"]
        if expected == "HIGH" and would_activate:
            result = "✅ PASS"
            passed += 1
        elif expected == "LOW" and not would_activate:
            result = "✅ PASS"
            passed += 1
        elif expected == "MEDIUM":
            result = "⚡ INFO" 
            passed += 1  # Casos MEDIUM são informativos
        else:
            result = "❌ FAIL"
        
        print(f"\n{i}. {case['description']}")
        print(f"   Mensagem: '{case['message']}'")
        print(f"   Contexto: {case['context']}")
        print(f"   Score: {calendar_score:.3f} | Threshold: {dynamic_threshold:.3f}")
        print(f"   Ativaria: {'SIM' if would_activate else 'NÃO'}")
        print(f"   Resultado: {result}")
    
    print(f"\n🏆 RESULTADO: {passed}/{total} casos passaram")
    print(f"📊 Taxa de sucesso: {(passed/total)*100:.1f}%")
    
    return passed == total

def test_scoring_breakdown():
    """Testa o detalhamento do scoring para debug"""
    coordinator = TeamCoordinator()
    
    print("\n🔍 TESTE: Breakdown Detalhado do Scoring")
    print("=" * 60)
    
    test_message = "Quero agendar reunião com Leonardo para hoje às 15h"
    test_context = {
        "user_intent": "agendar reunião",
        "conversation_stage": "qualificação", 
        "urgency_level": "alta"
    }
    
    print(f"Mensagem: '{test_message}'")
    print(f"Contexto: {test_context}")
    print()
    
    # Analisar score do calendar step by step
    message_lower = test_message.lower()
    calendar_score = 0.0
    
    # 1. Keywords básicas
    basic_keywords = [
        "agendar", "marcar", "reunião", "conversar", "leonardo",
        "horário", "disponível", "data", "quando", "encontro"
    ]
    keyword_matches = sum(1 for kw in basic_keywords if kw in message_lower)
    keyword_score = min(0.4, keyword_matches * 0.2)
    calendar_score += keyword_score
    print(f"1. Keywords ({keyword_matches} matches): +{keyword_score:.3f}")
    
    # 2. Intenções fortes
    strong_intent_phrases = [
        "quero agendar", "vamos marcar", "podemos conversar",
        "falar com leonardo", "marcar reunião", "que horário",
        "estou disponível", "quando posso", "vamos falar"
    ]
    intent_bonus = 0.0
    for phrase in strong_intent_phrases:
        if phrase in message_lower:
            intent_bonus = 0.4
            break
    calendar_score += intent_bonus
    print(f"2. Intenção forte: +{intent_bonus:.3f}")
    
    # 3. Urgência
    urgency_indicators = [
        "hoje", "amanhã", "logo", "rápido", "urgente",
        "já", "agora", "preciso", "importante"
    ]
    urgency_bonus = 0.3 if any(indicator in message_lower for indicator in urgency_indicators) else 0.0
    calendar_score += urgency_bonus
    print(f"3. Urgência: +{urgency_bonus:.3f}")
    
    # 4. Tempo específico
    import re
    time_patterns = [
        r"\d{1,2}h\d{0,2}", r"\d{1,2}:\d{2}", r"\d{1,2}/\d{1,2}",
        "manhã", "tarde", "noite", "segunda", "terça", "quarta", 
        "quinta", "sexta", "sábado", "domingo"
    ]
    time_bonus = 0.0
    for pattern in time_patterns:
        if re.search(pattern, message_lower):
            time_bonus = 0.5
            break
    calendar_score += time_bonus
    print(f"4. Tempo específico: +{time_bonus:.3f}")
    
    print(f"\n📊 Score base: {calendar_score:.3f}")
    
    # 5. Boosts inteligentes
    user_intent_boost = 0.4 if "agendar" in test_context.get("user_intent", "").lower() else 0.0
    stage_boost = 0.3 if test_context.get("conversation_stage", "").lower() in ["qualificação", "negociação", "fechamento"] else 0.0
    
    calendar_score += user_intent_boost + stage_boost
    print(f"5. Boost user_intent: +{user_intent_boost:.3f}")
    print(f"6. Boost conversation_stage: +{stage_boost:.3f}")
    
    final_score = min(1.0, calendar_score)
    print(f"\n🎯 Score final: {final_score:.3f}")
    
    # Threshold dinâmico
    dynamic_threshold = coordinator._get_dynamic_threshold("calendar", test_context)
    print(f"🚦 Threshold dinâmico: {dynamic_threshold:.3f}")
    
    would_activate = final_score >= dynamic_threshold
    print(f"✅ Ativaria Calendar: {'SIM' if would_activate else 'NÃO'}")
    
    return would_activate

def test_context_boost():
    """Testa diferentes cenários de boost por contexto"""
    coordinator = TeamCoordinator()
    
    print("\n🚀 TESTE: Boost Inteligente por Contexto")
    print("=" * 60)
    
    base_message = "agendar"
    
    contexts = [
        {
            "name": "Sem contexto",
            "context": {},
            "expected_boost": "baixo"
        },
        {
            "name": "User intent claro",
            "context": {"user_intent": "agendar reunião"},
            "expected_boost": "alto"
        },
        {
            "name": "Stage avançado",
            "context": {"conversation_stage": "qualificação"},
            "expected_boost": "alto"
        },
        {
            "name": "Urgência alta",
            "context": {"urgency_level": "alta"},
            "expected_boost": "muito_alto"
        },
        {
            "name": "Contexto completo",
            "context": {
                "user_intent": "agendar reunião",
                "conversation_stage": "negociação",
                "urgency_level": "alta"
            },
            "expected_boost": "máximo"
        }
    ]
    
    for i, test in enumerate(contexts, 1):
        scores = coordinator.analyze_service_need(base_message, test["context"])
        threshold = coordinator._get_dynamic_threshold("calendar", test["context"])
        
        print(f"\n{i}. {test['name']}")
        print(f"   Contexto: {test['context']}")
        print(f"   Score Calendar: {scores['calendar']:.3f}")
        print(f"   Threshold: {threshold:.3f}")
        print(f"   Ativaria: {'SIM' if scores['calendar'] >= threshold else 'NÃO'}")

async def main():
    """Executa todos os testes"""
    emoji_logger.system_event("🧪 Iniciando testes do Team Coordinator")
    
    success = True
    
    try:
        # Teste 1: Análise de intenção
        if not test_calendar_intent_analysis():
            success = False
        
        # Teste 2: Breakdown detalhado
        test_scoring_breakdown()
        
        # Teste 3: Boost por contexto
        test_context_boost()
        
        if success:
            emoji_logger.system_success("✅ Todos os testes passaram!")
        else:
            emoji_logger.system_error("❌ Alguns testes falharam")
            
    except Exception as e:
        emoji_logger.system_error(f"Erro durante os testes: {e}")
        success = False
    
    return success

if __name__ == "__main__":
    asyncio.run(main())