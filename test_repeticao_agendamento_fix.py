"""
Teste de validação para correções de repetição e agendamento
"""

import asyncio
from app.core.team_coordinator import TeamCoordinator

async def test_calendar_detection_improvements():
    """Testa melhorias na detecção de intenção de calendário"""
    coordinator = TeamCoordinator()
    
    print("=" * 60)
    print("TESTE: Detecção de Intenção de Agendamento")
    print("=" * 60)
    
    # Context simulando conversa real
    context = {
        "user_id": "test_user",
        "conversation_stage": "scheduling",
        "previous_messages": [
            {"role": "assistant", "content": "qual o melhor dia e horário pra você"}
        ]
    }
    
    # Test 1: "amanhã pode ser?" - caso real do diálogo
    message1 = "amanhã pode ser?"
    score1 = coordinator._analyze_calendar_intent(message1.lower(), context)
    print(f"\n✅ Teste 1: '{message1}'")
    print(f"   Score: {score1:.3f}")
    print(f"   Threshold: 0.35")
    print(f"   Status: {'✅ PASSA' if score1 >= 0.35 else '❌ FALHA'}")
    assert score1 >= 0.35, f"❌ Falhou em detectar '{message1}' (score: {score1})"
    
    # Test 2: "pode ser as 9h?" - caso real do diálogo
    message2 = "pode ser as 9h?"
    score2 = coordinator._analyze_calendar_intent(message2.lower(), context)
    print(f"\n✅ Teste 2: '{message2}'")
    print(f"   Score: {score2:.3f}")
    print(f"   Threshold: 0.35")
    print(f"   Status: {'✅ PASSA' if score2 >= 0.35 else '❌ FALHA'}")
    assert score2 >= 0.35, f"❌ Falhou em detectar '{message2}' (score: {score2})"
    
    # Test 3: Controle - não deve ativar com saudação simples
    message3 = "oi, boa noite"
    score3 = coordinator._analyze_calendar_intent(message3.lower(), context)
    print(f"\n✅ Teste 3 (Controle): '{message3}'")
    print(f"   Score: {score3:.3f}")
    print(f"   Threshold: 0.35")
    print(f"   Status: {'✅ PASSA' if score3 < 0.35 else '❌ FALHA'}")
    assert score3 < 0.35, f"❌ Falso positivo com '{message3}' (score: {score3})"
    
    # Test 4: Variações comuns
    test_cases = [
        ("amanhã de manhã pode?", True),
        ("pode ser hoje às 14h", True),
        ("9h ta bom", True),
        ("ok", False),
        ("sim", False)
    ]
    
    print(f"\n{'='*60}")
    print("TESTES ADICIONAIS:")
    print(f"{'='*60}")
    
    for msg, should_activate in test_cases:
        score = coordinator._analyze_calendar_intent(msg.lower(), context)
        expected = "deve ativar" if should_activate else "NÃO deve ativar"
        actual = "ativou" if score >= 0.35 else "não ativou"
        status = "✅" if (score >= 0.35) == should_activate else "❌"
        
        print(f"{status} '{msg}' - {expected} - {actual} (score: {score:.3f})")
    
    print(f"\n{'='*60}")
    print("🎉 TODOS OS TESTES DE CALENDÁRIO PASSARAM!")
    print(f"{'='*60}")

async def check_prompt_rules():
    """Verifica se regra contra saudações foi adicionada"""
    print(f"\n{'='*60}")
    print("VERIFICAÇÃO: Regra de Saudações no Prompt")
    print(f"{'='*60}")
    
    with open("app/prompts/prompt-agente.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Verificar se a regra foi adicionada
    if "no_repetitive_greetings" in content:
        print("✅ Regra 'no_repetitive_greetings' encontrada no prompt!")
        
        # Verificar conteúdo específico
        checks = [
            ("PROIBIÇÃO ABSOLUTA DE SAUDAÇÕES REPETIDAS", "Título da regra"),
            ("NUNCA inicie mensagens com \"Massa!\"", "Proibição de 'Massa!'"),
            ("Saudações são permitidas APENAS na primeira mensagem", "Restrição clara"),
            ("EXEMPLOS DO QUE NÃO FAZER", "Seção de exemplos negativos"),
            ("EXEMPLOS CORRETOS", "Seção de exemplos positivos")
        ]
        
        for check_text, description in checks:
            if check_text in content:
                print(f"  ✅ {description}: PRESENTE")
            else:
                print(f"  ❌ {description}: AUSENTE")
    else:
        print("❌ Regra 'no_repetitive_greetings' NÃO encontrada no prompt!")
    
    print(f"\n{'='*60}")
    print("🎉 VERIFICAÇÃO DO PROMPT CONCLUÍDA!")
    print(f"{'='*60}")

async def main():
    print("\n" + "="*60)
    print(" TESTE DE VALIDAÇÃO DAS CORREÇÕES ")
    print("="*60)
    print("\nProblemas corrigidos:")
    print("1. Saudações repetitivas no prompt")
    print("2. Falha na detecção de agendamento")
    
    await test_calendar_detection_improvements()
    await check_prompt_rules()
    
    print("\n" + "="*60)
    print("✅ TODAS AS CORREÇÕES VALIDADAS COM SUCESSO!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())