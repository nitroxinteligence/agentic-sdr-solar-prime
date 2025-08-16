#!/usr/bin/env python3
"""
Teste para validar que o executor de tools agora reconhece os nomes corretos
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from app.agents.agentic_sdr_stateless import AgenticSDRStateless

async def test_tool_executor():
    """Testa se o executor reconhece os nomes corretos dos tools"""
    
    print("=" * 50)
    print("TESTE: Executor de Tools com nomes corretos")
    print("=" * 50)
    
    # Mock do team_coordinator
    mock_coordinator = MagicMock()
    mock_calendar = AsyncMock()
    mock_crm = AsyncMock()
    mock_followup = AsyncMock()
    
    # Configurar retornos simulados
    mock_calendar.check_availability.return_value = {
        "horarios": ["Segunda 14h", "Terça 10h"]
    }
    mock_calendar.schedule_meeting.return_value = {
        "success": True,
        "meet_link": "https://meet.google.com/test"
    }
    mock_crm.update_lead_stage.return_value = {
        "success": True
    }
    mock_followup.schedule_followup.return_value = {
        "success": True
    }
    
    mock_coordinator.services = {
        "calendar": mock_calendar,
        "crm": mock_crm,
        "followup": mock_followup
    }
    
    # Criar instância do agente
    agent = AgenticSDRStateless()
    agent.team_coordinator = mock_coordinator
    
    # Testar tools com nomes corretos
    test_cases = [
        {
            "name": "calendar.check_availability",
            "params": {},
            "lead_info": {"phone": "123456"},
            "context": {"message": "teste"}
        },
        {
            "name": "calendar.schedule_meeting",
            "params": {"date": "2025-08-17", "time": "14:00", "email": "test@test.com"},
            "lead_info": {"phone": "123456"},
            "context": {}
        },
        {
            "name": "crm.update_stage",
            "params": {"stage": "qualificado"},
            "lead_info": {"kommo_lead_id": "123"},
            "context": {}
        },
        {
            "name": "followup.schedule",
            "params": {"hours": "24", "message": "Lembrete"},
            "lead_info": {"phone": "123456"},
            "context": {}
        }
    ]
    
    results = []
    for test in test_cases:
        try:
            result = await agent._execute_single_tool(
                test["name"],
                test["params"],
                test["lead_info"],
                test["context"]
            )
            results.append({
                "tool": test["name"],
                "status": "✅ SUCESSO",
                "result": result
            })
            print(f"✅ Tool '{test['name']}' executado com sucesso!")
        except Exception as e:
            results.append({
                "tool": test["name"],
                "status": "❌ ERRO",
                "error": str(e)
            })
            print(f"❌ Tool '{test['name']}' falhou: {e}")
    
    # Teste com nomes antigos (devem falhar)
    old_names = [
        "calendar_service.check_availability",
        "calendar_service.schedule_meeting",
        "followup_service.schedule"
    ]
    
    print("\n📝 Testando nomes antigos (devem falhar):")
    for old_name in old_names:
        try:
            result = await agent._execute_single_tool(
                old_name,
                {},
                {"phone": "123456"},
                {}
            )
            print(f"❌ PROBLEMA: Tool '{old_name}' não deveria funcionar!")
        except Exception as e:
            if "Tool não reconhecido" in str(e):
                print(f"✅ Correto: Tool '{old_name}' rejeitado como esperado")
            else:
                print(f"⚠️ Erro inesperado para '{old_name}': {e}")
    
    # Resultado final
    print("\n" + "=" * 50)
    success_count = sum(1 for r in results if r["status"] == "✅ SUCESSO")
    if success_count == len(test_cases):
        print(f"🎉 SUCESSO TOTAL: {success_count}/{len(test_cases)} tools funcionando!")
    else:
        print(f"⚠️ PARCIAL: {success_count}/{len(test_cases)} tools funcionando")
    print("=" * 50)
    
    return success_count == len(test_cases)

if __name__ == "__main__":
    result = asyncio.run(test_tool_executor())
    exit(0 if result else 1)