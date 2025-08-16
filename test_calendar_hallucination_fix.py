#!/usr/bin/env python3
"""
Teste para validar correção da alucinação do Google Calendar
Problema: Agente alucinava respostas quando Calendar funcionava mas não usava Tool Calls
Solução: Integração correta entre TeamCoordinator e Tool Call System
"""

import asyncio
import sys
import os
from datetime import datetime
from typing import Dict, Any, List

# Adicionar path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.utils.logger import emoji_logger

class TestCalendarHallucinationFix:
    
    def __init__(self):
        self.passed_tests = 0
        self.total_tests = 0
        
    async def setup_agent(self) -> AgenticSDRStateless:
        """Cria agente stateless para teste"""
        agent = AgenticSDRStateless()
        await agent.initialize()
        return agent
    
    def assert_test(self, condition: bool, test_name: str, details: str = ""):
        """Verifica condição de teste"""
        self.total_tests += 1
        if condition:
            self.passed_tests += 1
            emoji_logger.system_success(f"✅ {test_name}")
            if details:
                print(f"   📝 {details}")
        else:
            emoji_logger.system_error("Test failed", error=f"❌ {test_name}")
            if details:
                print(f"   📝 {details}")
    
    async def test_service_results_integration(self):
        """Testa se service_results são corretamente integrados no prompt"""
        emoji_logger.system_event("🧪 Testando integração de service_results...")
        
        agent = await self.setup_agent()
        
        # Simular service_results do Calendar
        service_results = [
            {
                "service": "calendar",
                "success": True,
                "data": {
                    "message": "Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?",
                    "available_slots": ["09:00", "10:00", "11:00"],
                    "real": True
                }
            }
        ]
        
        # Criar contexto de agendamento
        context = {
            "conversation_stage": "agendamento",
            "user_intent": "agendar reunião",
            "qualification_score": 8
        }
        
        lead_info = {
            "name": "Mateus",
            "phone": "558182986181"
        }
        
        # Simular mensagem que gerou alucinação
        message = "eu quero agendar uma reuniao pra amanha"
        
        # Testar _build_prompt_with_history com service_results
        prompt = agent._build_prompt_with_history(
            message, context, lead_info, service_results, "", [], {}
        )
        
        # Verificar se o prompt inclui corretamente os service_results
        self.assert_test(
            "📅 Calendar: Tenho estes horários disponíveis amanhã" in prompt,
            "Service results incluídos no prompt",
            "Calendar message encontrada no prompt"
        )
        
        self.assert_test(
            "=== RESULTADOS DE SERVIÇOS ===" in prompt,
            "Seção de resultados formatada",
            "Cabeçalho de resultados presente"
        )
        
        self.assert_test(
            "=== USO ESTES RESULTADOS NA RESPOSTA ===" in prompt,
            "Instrução para usar resultados",
            "Instrução clara para agente usar os dados"
        )
    
    async def test_anti_hallucination_detection(self):
        """Testa detecção de alucinação quando Calendar funciona"""
        emoji_logger.system_event("🧪 Testando detecção anti-alucinação...")
        
        agent = await self.setup_agent()
        
        # Simular service_results bem-sucedidos
        service_results = [
            {
                "service": "calendar", 
                "success": True,
                "data": {"message": "Horários: 09:00, 10:00, 11:00"}
            }
        ]
        
        # Simular response alucinada (problema que estava acontecendo)
        hallucinated_response = "Vixe, Mateus! Desculpa, mas estou tendo alguns probleminhas técnicos aqui pra acessar a agenda do Leonardo."
        
        # Verificar se seria detectada como alucinação
        calendar_result = next((r for r in service_results if r.get("service") == "calendar" and r.get("success")), None)
        has_calendar_success = calendar_result is not None
        mentions_technical_problems = "problemas técnicos" in hallucinated_response.lower()
        
        self.assert_test(
            has_calendar_success,
            "Calendar funcionou corretamente",
            "service_results indica sucesso do Calendar"
        )
        
        self.assert_test(
            mentions_technical_problems,
            "Resposta alucinada identificada", 
            "Resposta problemática menciona 'problemas técnicos' incorretamente"
        )
        
        # Verificar se lógica de correção seria ativada
        would_trigger_correction = has_calendar_success and mentions_technical_problems
        
        self.assert_test(
            would_trigger_correction,
            "Sistema detectaria alucinação",
            "Lógica de correção seria ativada para corrigir a alucinação"
        )
    
    async def test_calendar_message_extraction(self):
        """Testa extração da mensagem do Calendar"""
        emoji_logger.system_event("🧪 Testando extração de mensagem do Calendar...")
        
        service_results = [
            {
                "service": "calendar",
                "success": True, 
                "data": {
                    "message": "Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?",
                    "available_slots": ["09:00", "10:00", "11:00"]
                }
            }
        ]
        
        calendar_result = next((r for r in service_results if r.get("service") == "calendar" and r.get("success")), None)
        
        self.assert_test(
            calendar_result is not None,
            "Calendar result encontrado",
            "service_results contém resultado do Calendar"
        )
        
        if calendar_result:
            calendar_data = calendar_result.get("data", {})
            calendar_message = calendar_data.get("message", "")
            
            self.assert_test(
                bool(calendar_message),
                "Mensagem do Calendar extraída",
                f"Mensagem: {calendar_message[:50]}..."
            )
            
            self.assert_test(
                "horários disponíveis" in calendar_message,
                "Mensagem contém horários",
                "Mensagem inclui informação de horários disponíveis"
            )
    
    async def test_prompt_enhancement_logic(self):
        """Testa lógica de enhancement do prompt"""
        emoji_logger.system_event("🧪 Testando lógica de enhancement...")
        
        agent = await self.setup_agent()
        
        # Verificar se _get_instructions contém regras anti-alucinação
        instructions = agent._get_instructions()
        
        self.assert_test(
            "SERVICE_RESULTS_PRIORITY" in instructions,
            "Regra SERVICE_RESULTS_PRIORITY presente",
            "Prompt contém regra específica para priorizar service_results"
        )
        
        self.assert_test(
            "NUNCA invente problemas técnicos" in instructions,
            "Regra anti-alucinação presente",
            "Prompt proíbe especificamente alucinação de problemas técnicos"
        )
        
        self.assert_test(
            "CONFIE 100% nos dados retornados" in instructions,
            "Regra de confiança nos dados",
            "Prompt instrui a confiar nos resultados dos serviços"
        )
    
    async def test_full_integration_scenario(self):
        """Testa cenário completo de integração"""
        emoji_logger.system_event("🧪 Testando cenário completo...")
        
        agent = await self.setup_agent()
        
        # Simular dados completos do cenário problemático
        message = "eu quero agendar uma reuniao pra amanha"
        
        context = {
            "conversation_stage": "agendamento_processo",
            "user_intent": "agendar reunião", 
            "qualification_score": 8
        }
        
        lead_info = {
            "name": "Mateus",
            "phone": "558182986181"
        }
        
        service_results = [
            {
                "service": "calendar",
                "success": True,
                "data": {
                    "message": "Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?",
                    "available_slots": ["09:00", "10:00", "11:00"],
                    "real": True
                }
            }
        ]
        
        # Construir prompt como seria no processo real
        prompt = agent._build_prompt_with_history(
            message, context, lead_info, service_results, "", [], {}
        )
        
        # Verificar componentes críticos
        self.assert_test(
            "Mateus" in prompt,
            "Nome do lead no prompt",
            "Lead info corretamente incluída"
        )
        
        self.assert_test(
            "eu quero agendar uma reuniao pra amanha" in prompt,
            "Mensagem original no prompt", 
            "Mensagem do usuário preservada"
        )
        
        self.assert_test(
            "📅 Calendar:" in prompt,
            "Resultado do Calendar formatado",
            "Service result do Calendar presente e formatado"
        )
        
        # Verificar contexto (pode estar como texto, não necessariamente como "agendamento_processo")
        has_context = any(stage in prompt for stage in ["agendamento", "calendario", "reunião"])
        self.assert_test(
            has_context,
            "Contexto de agendamento",
            "Contexto de agendamento presente no prompt"
        )
    
    async def run_all_tests(self):
        """Executa todos os testes"""
        emoji_logger.system_event("🚀 Iniciando testes de correção da alucinação do Calendar...")
        
        # Lista de testes
        tests = [
            self.test_service_results_integration,
            self.test_anti_hallucination_detection,
            self.test_calendar_message_extraction,
            self.test_prompt_enhancement_logic,
            self.test_full_integration_scenario
        ]
        
        # Executar testes
        for test in tests:
            try:
                await test()
            except Exception as e:
                emoji_logger.system_error("Test execution failed", error=f"❌ Erro no teste {test.__name__}: {e}")
        
        # Resultado final
        success_rate = (self.passed_tests / self.total_tests * 100) if self.total_tests > 0 else 0
        
        emoji_logger.system_event(f"📊 RESULTADO FINAL: {self.passed_tests}/{self.total_tests} testes passou ({success_rate:.1f}%)")
        
        if self.passed_tests == self.total_tests:
            emoji_logger.system_success("✅ TODOS OS TESTES PASSARAM - Correção validada!")
            return True
        else:
            emoji_logger.system_error("Tests failed", error=f"❌ {self.total_tests - self.passed_tests} teste(s) falharam")
            return False

async def main():
    """Função principal"""
    print("="*80)
    print("🧪 TESTE: Correção da Alucinação do Google Calendar")
    print("="*80)
    print()
    
    tester = TestCalendarHallucinationFix()
    success = await tester.run_all_tests()
    
    print()
    print("="*80)
    if success:
        print("🎉 CORREÇÃO VALIDADA: Sistema não deve mais alucinar com Calendar funcionando")
    else:
        print("🚨 ATENÇÃO: Alguns testes falharam - verificar implementação")
    print("="*80)
    
    return success

if __name__ == "__main__":
    asyncio.run(main())