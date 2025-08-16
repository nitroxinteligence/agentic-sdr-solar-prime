#!/usr/bin/env python3
"""
Teste de integração para validar que o sistema completo funciona após as correções
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import asyncio
import re
from unittest.mock import AsyncMock, MagicMock, patch

async def test_full_integration():
    """Testa o fluxo completo com as correções aplicadas"""
    
    print("=" * 60)
    print("TESTE DE INTEGRAÇÃO: Sistema de Tool Calling Corrigido")
    print("=" * 60)
    
    # Importar após adicionar ao path
    from app.agents.agentic_sdr_stateless import AgenticSDRStateless
    
    # Mock do team_coordinator com todos os serviços
    mock_coordinator = MagicMock()
    mock_calendar = AsyncMock()
    mock_crm = AsyncMock()
    mock_followup = AsyncMock()
    
    # Configurar retornos esperados
    mock_calendar.check_availability.return_value = {
        "available_times": ["Segunda 14h", "Terça 10h", "Quarta 16h"],
        "success": True
    }
    
    mock_calendar.schedule_meeting.return_value = {
        "success": True,
        "meet_link": "https://meet.google.com/abc-def-ghi",
        "event_id": "event123"
    }
    
    mock_crm.update_lead_stage.return_value = {
        "success": True,
        "new_stage": "qualificado"
    }
    
    mock_followup.schedule_followup.return_value = {
        "success": True,
        "scheduled_for": "24 hours from now"
    }
    
    mock_coordinator.services = {
        "calendar": mock_calendar,
        "crm": mock_crm,
        "followup": mock_followup
    }
    
    # Criar agente
    agent = AgenticSDRStateless()
    agent.team_coordinator = mock_coordinator
    
    # Simular uma resposta do agente com tool calls
    test_response = """
    Olá João! Deixa eu verificar a agenda do Leonardo para você.
    
    [TOOL: calendar.check_availability]
    
    Perfeito! O Leonardo tem esses horários disponíveis. Vou agendar a reunião.
    
    [TOOL: calendar.schedule_meeting | date=2025-08-17 | time=14:00 | email=joao@empresa.com]
    
    Também vou atualizar seu status no sistema.
    
    [TOOL: crm.update_stage | stage=qualificado]
    
    E configurar um lembrete para você.
    
    [TOOL: followup.schedule | hours=24 | message=Lembrete da reunião com Leonardo amanhã]
    """
    
    # Executar parser e tools
    lead_info = {
        "phone": "5511999999999",
        "name": "João",
        "kommo_lead_id": "12345",
        "email": "joao@empresa.com"
    }
    
    context = {
        "message": "Quero agendar uma reunião"
    }
    
    print("\n📝 Testando extração e execução de tools...")
    
    try:
        # Executar o método de parsing e execução
        tool_results = await agent._parse_and_execute_tools(
            test_response, 
            lead_info, 
            context
        )
        
        print("\n✅ Tools executados com sucesso!")
        print("\n📊 Resultados obtidos:")
        
        # Verificar cada tool
        expected_tools = [
            "calendar.check_availability",
            "calendar.schedule_meeting",
            "crm.update_stage",
            "followup.schedule"
        ]
        
        for tool in expected_tools:
            if tool in tool_results:
                print(f"  ✅ {tool}: {tool_results[tool]}")
            else:
                print(f"  ❌ {tool}: NÃO EXECUTADO")
        
        # Verificar chamadas aos mocks
        print("\n🔍 Verificando chamadas aos serviços:")
        
        if mock_calendar.check_availability.called:
            print("  ✅ Calendar: check_availability foi chamado")
        else:
            print("  ❌ Calendar: check_availability NÃO foi chamado")
            
        if mock_calendar.schedule_meeting.called:
            print("  ✅ Calendar: schedule_meeting foi chamado")
            args = mock_calendar.schedule_meeting.call_args
            print(f"     Parâmetros: {args}")
        else:
            print("  ❌ Calendar: schedule_meeting NÃO foi chamado")
            
        if mock_crm.update_lead_stage.called:
            print("  ✅ CRM: update_lead_stage foi chamado")
            args = mock_crm.update_lead_stage.call_args
            print(f"     Parâmetros: {args}")
        else:
            print("  ❌ CRM: update_lead_stage NÃO foi chamado")
            
        if mock_followup.schedule_followup.called:
            print("  ✅ Follow-up: schedule_followup foi chamado")
            args = mock_followup.schedule_followup.call_args
            print(f"     Parâmetros: {args}")
        else:
            print("  ❌ Follow-up: schedule_followup NÃO foi chamado")
        
        # Resultado final
        all_called = all([
            mock_calendar.check_availability.called,
            mock_calendar.schedule_meeting.called,
            mock_crm.update_lead_stage.called,
            mock_followup.schedule_followup.called
        ])
        
        print("\n" + "=" * 60)
        if all_called and len(tool_results) == 4:
            print("🎉 SUCESSO TOTAL: Sistema de Tool Calling 100% funcional!")
            return True
        else:
            print("⚠️ PARCIAL: Alguns tools não foram executados corretamente")
            return False
            
    except Exception as e:
        print(f"\n❌ ERRO na execução: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    result = asyncio.run(test_full_integration())
    print("=" * 60)
    exit(0 if result else 1)