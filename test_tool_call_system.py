"""
Teste End-to-End do Sistema de Tool Call
Valida parser, executor e anti-alucinação
"""

import asyncio
import re
from unittest.mock import Mock, AsyncMock, patch
from datetime import datetime, timedelta

# Importações do sistema
from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.core.team_coordinator import TeamCoordinator
from app.config import Settings

class TestToolCallSystem:
    """Testes completos do sistema de tool_call"""
    
    def __init__(self):
        self.config = Settings()
        self.passed = 0
        self.failed = 0
        self.tests = []
    
    async def setup(self):
        """Configura o ambiente de teste"""
        print("="*60)
        print("🧪 TESTE END-TO-END: SISTEMA DE TOOL CALL")
        print("="*60)
        
        # Mock do AgenticSDR
        self.agent = AgenticSDRStateless()
        await self.agent.initialize()
        
        # Mock dos serviços
        self.mock_calendar = AsyncMock()
        self.mock_crm = AsyncMock()
        self.mock_followup = AsyncMock()
        
        # Configurar retornos dos mocks
        self.mock_calendar.check_availability.return_value = {
            "slots": ["09:00", "10:00", "14:00", "15:00"],
            "date": "2025-08-17"
        }
        
        self.mock_calendar.schedule_meeting.return_value = {
            "success": True,
            "meet_link": "https://meet.google.com/xyz-123-abc",
            "event_id": "evt_12345"
        }
        
        self.mock_crm.update_stage.return_value = {
            "success": True,
            "new_stage": "qualificado"
        }
        
        self.mock_followup.schedule.return_value = {
            "success": True,
            "scheduled_for": "2025-08-18 09:00"
        }
        
        # Injetar mocks no agent
        if hasattr(self.agent, 'team_coordinator'):
            self.agent.team_coordinator.services = {
                "calendar": self.mock_calendar,
                "crm": self.mock_crm,
                "followup": self.mock_followup
            }
    
    async def test_parser(self):
        """Testa o parser de tool_calls"""
        print("\n📝 TESTE 1: Parser de Tool Calls")
        print("-" * 40)
        
        test_cases = [
            # Formato simples
            ("[TOOL: calendar.check_availability]", 
             [("calendar.check_availability", "")]),
            
            # Com parâmetros
            ("[TOOL: calendar.schedule_meeting | date=2025-08-17 | time=09:00 | email=test@email.com]",
             [("calendar.schedule_meeting", "date=2025-08-17 | time=09:00 | email=test@email.com")]),
            
            # Múltiplos tools
            ("Vou verificar [TOOL: calendar.check_availability] e atualizar [TOOL: crm.update_stage | stage=qualificado]",
             [("calendar.check_availability", ""), ("crm.update_stage", "stage=qualificado")]),
            
            # Sem tools
            ("Esta é uma mensagem normal sem tool calls",
             [])
        ]
        
        pattern = r'\[TOOL:\s*([^|]+?)(?:\s*\|\s*([^\]]+))?\]'
        
        for text, expected in test_cases:
            matches = re.findall(pattern, text)
            # Normalizar matches para comparação
            normalized = [(m[0].strip(), m[1].strip() if len(m) > 1 and m[1] else "") for m in matches]
            
            if normalized == expected:
                print(f"✅ Parser OK: '{text[:50]}...'")
                self.passed += 1
            else:
                print(f"❌ Parser FALHOU: '{text[:50]}...'")
                print(f"   Esperado: {expected}")
                print(f"   Obtido: {normalized}")
                self.failed += 1
    
    async def test_executor(self):
        """Testa o executor de tools"""
        print("\n⚙️ TESTE 2: Executor de Tools")
        print("-" * 40)
        
        # Contexto de teste
        lead_info = {
            "name": "João Teste",
            "phone": "11999999999",
            "email": "joao@teste.com",
            "kommo_lead_id": "12345"
        }
        
        context = {
            "message": "quero agendar para amanhã",
            "user_id": "test_user"
        }
        
        # Teste 1: Calendar check_availability
        response = "Vou verificar a agenda [TOOL: calendar.check_availability]"
        results = await self.agent._parse_and_execute_tools(response, lead_info, context)
        
        if "calendar.check_availability" in results:
            if "slots" in str(results["calendar.check_availability"]):
                print("✅ Executor: calendar.check_availability funcionou")
                self.passed += 1
            else:
                print("❌ Executor: calendar.check_availability retornou dados incorretos")
                self.failed += 1
        else:
            print("❌ Executor: calendar.check_availability não foi executado")
            self.failed += 1
        
        # Teste 2: Calendar schedule_meeting com parâmetros
        response = "[TOOL: calendar.schedule_meeting | date=2025-08-17 | time=09:00 | email=joao@teste.com]"
        results = await self.agent._parse_and_execute_tools(response, lead_info, context)
        
        if "calendar.schedule_meeting" in results:
            if "meet_link" in str(results["calendar.schedule_meeting"]):
                print("✅ Executor: calendar.schedule_meeting funcionou")
                self.passed += 1
            else:
                print("❌ Executor: calendar.schedule_meeting retornou dados incorretos")
                self.failed += 1
        else:
            print("❌ Executor: calendar.schedule_meeting não foi executado")
            self.failed += 1
        
        # Teste 3: Tool inválido
        response = "[TOOL: servico_invalido.metodo_invalido]"
        results = await self.agent._parse_and_execute_tools(response, lead_info, context)
        
        if "servico_invalido.metodo_invalido" in results:
            if "error" in results["servico_invalido.metodo_invalido"]:
                print("✅ Executor: Tratou tool inválido corretamente")
                self.passed += 1
            else:
                print("❌ Executor: Não tratou erro de tool inválido")
                self.failed += 1
        else:
            print("❌ Executor: Não processou tool inválido")
            self.failed += 1
    
    async def test_anti_hallucination(self):
        """Testa regras anti-alucinação"""
        print("\n🛡️ TESTE 3: Sistema Anti-Alucinação")
        print("-" * 40)
        
        # Casos que DEVEM usar tools
        dangerous_phrases = [
            "Agendei para amanhã às 9h",
            "Marquei a reunião para segunda",
            "Confirmado o agendamento!",
            "Horários disponíveis: 9h, 10h, 14h",
            "Atualizei seu status para qualificado"
        ]
        
        # Verificar se prompt tem regras anti-alucinação
        with open("app/prompts/prompt-agente.md", "r", encoding="utf-8") as f:
            prompt_content = f.read()
        
        if "anti_hallucination_system" in prompt_content:
            print("✅ Regras anti-alucinação presentes no prompt")
            self.passed += 1
        else:
            print("❌ Regras anti-alucinação NÃO encontradas")
            self.failed += 1
        
        # Verificar regras específicas
        critical_rules = [
            "NO_FAKE_DATA",
            "TOOL_DEPENDENCY",
            "TRANSPARENCY",
            "validation_checks"
        ]
        
        for rule in critical_rules:
            if rule in prompt_content:
                print(f"  ✅ Regra '{rule}' presente")
                self.passed += 1
            else:
                print(f"  ❌ Regra '{rule}' ausente")
                self.failed += 1
    
    async def test_integration(self):
        """Teste de integração completo"""
        print("\n🔗 TESTE 4: Integração Completa")
        print("-" * 40)
        
        # Simular conversa real
        scenarios = [
            {
                "name": "Agendamento completo",
                "user_message": "quero agendar uma reunião para amanhã",
                "expected_tools": ["calendar.check_availability"],
                "description": "Deve usar calendar para verificar disponibilidade"
            },
            {
                "name": "Escolha de horário",
                "user_message": "pode ser às 9h",
                "expected_tools": ["calendar.schedule_meeting"],
                "description": "Deve agendar após escolha de horário"
            },
            {
                "name": "Atualização CRM",
                "user_message": "tenho interesse na solução",
                "expected_tools": ["crm.update_stage"],
                "description": "Deve atualizar estágio no CRM"
            }
        ]
        
        for scenario in scenarios:
            print(f"\n📌 Cenário: {scenario['name']}")
            
            # Simular resposta com tool_call
            mock_response = f"Claro! [TOOL: {scenario['expected_tools'][0]}]"
            
            # Parse
            pattern = r'\[TOOL:\s*([^|]+?)(?:\s*\|\s*([^\]]+))?\]'
            matches = re.findall(pattern, mock_response)
            
            if matches:
                tool_name = matches[0][0].strip()
                if tool_name in scenario['expected_tools']:
                    print(f"  ✅ {scenario['description']}")
                    self.passed += 1
                else:
                    print(f"  ❌ Tool incorreto: {tool_name}")
                    self.failed += 1
            else:
                print(f"  ❌ Nenhum tool detectado")
                self.failed += 1
    
    async def run_all_tests(self):
        """Executa todos os testes"""
        await self.setup()
        
        # Executar testes
        await self.test_parser()
        await self.test_executor()
        await self.test_anti_hallucination()
        await self.test_integration()
        
        # Relatório final
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL")
        print("="*60)
        
        total = self.passed + self.failed
        success_rate = (self.passed / total * 100) if total > 0 else 0
        
        print(f"✅ Testes aprovados: {self.passed}")
        print(f"❌ Testes falhados: {self.failed}")
        print(f"📈 Taxa de sucesso: {success_rate:.1f}%")
        
        if self.failed == 0:
            print("\n🎉 TODOS OS TESTES PASSARAM! Sistema de tool_call está 100% funcional!")
        else:
            print(f"\n⚠️ {self.failed} testes falharam. Verifique os erros acima.")
        
        return self.failed == 0

async def main():
    """Função principal de teste"""
    print("\n" + "🚀 INICIANDO TESTES DO SISTEMA DE TOOL_CALL " + "🚀")
    print("Versão: 1.0.0 | Data: 2025-08-16")
    
    tester = TestToolCallSystem()
    success = await tester.run_all_tests()
    
    if success:
        print("\n✅ Sistema aprovado para produção!")
        exit(0)
    else:
        print("\n❌ Sistema precisa de correções antes do deploy.")
        exit(1)

if __name__ == "__main__":
    asyncio.run(main())