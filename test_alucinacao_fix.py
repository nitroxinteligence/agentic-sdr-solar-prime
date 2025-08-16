"""
Teste de validação para correção de alucinação
Verifica que saudações simples não ativam calendar_service
"""

import asyncio
from app.core.team_coordinator import TeamCoordinator

async def test_no_false_calendar_activation():
    """Testa que 'boa noite' não ativa calendar"""
    coordinator = TeamCoordinator()
    
    # Context básico para o teste
    context = {
        "user_id": "test_user",
        "conversation_stage": "greeting",
        "previous_messages": []
    }
    
    # Test 1: Saudação não deve ativar calendar
    message = "oi, boa noite"
    result = coordinator._analyze_calendar_intent(message.lower(), context)
    assert result < 0.35, f"❌ 'boa noite' ativou calendar com score {result}"
    print(f"✅ 'boa noite' não ativa calendar (score: {result})")
    
    # Test 2: Agendamento explícito DEVE ativar
    message = "quero agendar uma reunião para segunda"
    result = coordinator._analyze_calendar_intent(message.lower(), context)
    assert result >= 0.35, f"❌ Agendamento explícito não ativou (score: {result})"
    print(f"✅ Agendamento explícito ativa calendar (score: {result})")
    
    print("\n🎉 Todos os testes passaram! Alucinação corrigida.")

if __name__ == "__main__":
    asyncio.run(test_no_false_calendar_activation())