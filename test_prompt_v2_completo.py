#!/usr/bin/env python3
"""
Teste completo do Prompt V2 Unificado - Validação de todas capacidades
Verifica integração com ContextAnalyzer, LeadManager, KnowledgeService, etc.
"""

import asyncio
import os
from datetime import datetime
from typing import Dict, Any, List

# Configurar ambiente
os.environ["DEBUG"] = "true"

from app.agents.agentic_sdr_refactored import AgenticSDR
from app.utils.logger import emoji_logger

class PromptV2Tester:
    """Classe para testar o novo prompt V2 com todas as capacidades"""
    
    def __init__(self):
        self.agent = None
        self.test_results = []
        
    async def setup(self):
        """Inicializa o agente para testes"""
        print("\n" + "="*100)
        print("🚀 TESTE DO PROMPT V2 UNIFICADO - SISTEMA INTELIGENTE")
        print("="*100)
        
        self.agent = AgenticSDR()
        await self.agent.initialize()
        
        # Verificar que o prompt V2 foi carregado
        prompt_content = self.agent._get_instructions()
        if "v2.0 UNIFIED" in prompt_content:
            print("✅ Prompt V2 carregado com sucesso!")
        else:
            print("⚠️ AVISO: Prompt V2 pode não estar ativo")
    
    async def test_context_adaptation(self):
        """Testa se o agente adapta resposta baseada no contexto emocional"""
        print("\n" + "-"*80)
        print("🧠 TESTE 1: Adaptação Contextual")
        print("-"*80)
        
        # Simular contexto negativo
        self.agent.conversation_history = [
            {"role": "user", "content": "oi", "timestamp": datetime.now().isoformat()},
            {"role": "assistant", "content": "Oi! Como posso te chamar?", "timestamp": datetime.now().isoformat()},
            {"role": "user", "content": "João", "timestamp": datetime.now().isoformat()},
            {"role": "assistant", "content": "Perfeito João! Temos 4 soluções...", "timestamp": datetime.now().isoformat()},
        ]
        
        # Mensagem com tom negativo
        response = await self.agent.process_message(
            "já tenho desconto e não confio em vocês",
            metadata={"phone": "5511999999999"}
        )
        
        # Limpar tags
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"📝 Mensagem negativa: 'já tenho desconto e não confio em vocês'")
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se houve adaptação empática
        empathy_words = ["entendo", "compreendo", "perfeitamente", "preocupação"]
        has_empathy = any(word in response.lower() for word in empathy_words)
        
        result = {
            "test": "Adaptação Contextual",
            "passed": has_empathy,
            "details": "Resposta empática detectada" if has_empathy else "Faltou empatia"
        }
        self.test_results.append(result)
        
        if has_empathy:
            print("✅ Agente demonstrou empatia com sentimento negativo")
        else:
            print("❌ Agente não adaptou tom para sentimento negativo")
            
        return has_empathy
    
    async def test_knowledge_base_consultation(self):
        """Testa se o agente consulta a knowledge base automaticamente"""
        print("\n" + "-"*80)
        print("📚 TESTE 2: Consulta Knowledge Base")
        print("-"*80)
        
        # Resetar histórico
        self.agent.conversation_history = []
        self.agent.current_lead_info = {"name": "Maria"}
        
        # Pergunta técnica que deveria trigger KB
        response = await self.agent.process_message(
            "como funciona o inversor solar?",
            metadata={"phone": "5511888888888"}
        )
        
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"📝 Pergunta técnica: 'como funciona o inversor solar?'")
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se há conteúdo técnico na resposta
        technical_words = ["inversor", "corrente", "energia", "converte", "DC", "AC", "alternada", "contínua"]
        has_technical = any(word in response.lower() for word in technical_words)
        
        result = {
            "test": "Knowledge Base",
            "passed": has_technical,
            "details": "Conteúdo técnico detectado" if has_technical else "Resposta genérica"
        }
        self.test_results.append(result)
        
        if has_technical:
            print("✅ Agente consultou knowledge base para resposta técnica")
        else:
            print("⚠️ Resposta pode não ter consultado knowledge base")
            
        return has_technical
    
    async def test_score_based_strategy(self):
        """Testa se o agente usa o qualification_score para estratégia"""
        print("\n" + "-"*80)
        print("🎯 TESTE 3: Estratégia por Score")
        print("-"*80)
        
        # Simular lead com score alto
        self.agent.current_lead_info = {
            "name": "Pedro",
            "bill_value": 8000.0,
            "qualification_score": 85  # Score alto = URGENTE
        }
        
        response = await self.agent.process_message(
            "quanto vou economizar?",
            metadata={"phone": "5511777777777"}
        )
        
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"📝 Lead com score 85 (URGENTE)")
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se há urgência na resposta
        urgency_words = ["hoje", "agora", "leonardo", "agendar", "reunião", "imediato"]
        has_urgency = any(word in response.lower() for word in urgency_words)
        
        result = {
            "test": "Estratégia por Score",
            "passed": has_urgency,
            "details": "Urgência detectada" if has_urgency else "Sem urgência apropriada"
        }
        self.test_results.append(result)
        
        if has_urgency:
            print("✅ Agente priorizou agendamento para score alto")
        else:
            print("⚠️ Agente não demonstrou urgência para score 85")
            
        return has_urgency
    
    async def test_multimodal_processing(self):
        """Testa processamento de mídia (simulado)"""
        print("\n" + "-"*80)
        print("📸 TESTE 4: Processamento Multimodal")
        print("-"*80)
        
        # Simular recebimento de conta de luz
        self.agent.current_lead_info = {"name": "Ana"}
        
        # Simular mídia processada
        media_metadata = {
            "phone": "5511666666666",
            "media": {
                "type": "image",
                "mimetype": "image/jpeg",
                "data": "base64_simulated_data"
            }
        }
        
        # O multimodal processor detectaria conta de luz
        # Vamos simular o contexto que seria gerado
        print("📷 Simulando envio de imagem de conta de luz...")
        
        # Para este teste, vamos enviar mensagem indicando que enviou conta
        response = await self.agent.process_message(
            "segue minha conta de luz de 750 reais",
            metadata={"phone": "5511666666666"}
        )
        
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se calculou economia
        has_calculation = "150" in response or "600" in response or "20%" in response
        
        result = {
            "test": "Processamento Multimodal",
            "passed": has_calculation,
            "details": "Cálculo detectado" if has_calculation else "Sem cálculo automático"
        }
        self.test_results.append(result)
        
        if has_calculation:
            print("✅ Agente processou valor e calculou economia")
        else:
            print("⚠️ Agente não calculou economia automaticamente")
            
        return has_calculation
    
    async def test_competitor_comparison(self):
        """Testa comparação com concorrentes via KB"""
        print("\n" + "-"*80)
        print("🏢 TESTE 5: Comparação com Concorrentes")
        print("-"*80)
        
        self.agent.current_lead_info = {"name": "Carlos", "bill_value": 5000}
        
        response = await self.agent.process_message(
            "já tenho 25% de desconto com a Origo Energia",
            metadata={"phone": "5511555555555"}
        )
        
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"📝 Menção à Origo Energia")
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se há comparação específica
        comparison_words = ["origo", "diferença", "patrimônio", "usina fica", "duas faturas", "consumo"]
        has_comparison = any(word in response.lower() for word in comparison_words)
        
        result = {
            "test": "Comparação Concorrentes",
            "passed": has_comparison,
            "details": "Comparação detectada" if has_comparison else "Resposta genérica"
        }
        self.test_results.append(result)
        
        if has_comparison:
            print("✅ Agente fez comparação específica com Origo")
        else:
            print("⚠️ Agente não comparou especificamente")
            
        return has_comparison
    
    async def test_flow_adaptation(self):
        """Testa adaptação de fluxo baseada em contexto"""
        print("\n" + "-"*80)
        print("🔄 TESTE 6: Adaptação de Fluxo")
        print("-"*80)
        
        # Simular urgência alta
        self.agent.conversation_history = []
        
        response = await self.agent.process_message(
            "preciso economizar urgente na conta de luz!",
            metadata={"phone": "5511444444444"}
        )
        
        if "<RESPOSTA_FINAL>" in response:
            response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
        
        print(f"📝 Mensagem urgente")
        print(f"🤖 Resposta: {response[:200]}...")
        
        # Verificar se foi mais direto
        direct_words = ["20%", "economia", "desconto", "agora", "hoje"]
        is_direct = any(word in response.lower() for word in direct_words)
        
        result = {
            "test": "Adaptação de Fluxo",
            "passed": is_direct,
            "details": "Abordagem direta" if is_direct else "Seguiu fluxo padrão"
        }
        self.test_results.append(result)
        
        if is_direct:
            print("✅ Agente adaptou fluxo para urgência")
        else:
            print("⚠️ Agente não adaptou para urgência")
            
        return is_direct
    
    async def run_all_tests(self):
        """Executa todos os testes"""
        await self.setup()
        
        tests = [
            self.test_context_adaptation,
            self.test_knowledge_base_consultation,
            self.test_score_based_strategy,
            self.test_multimodal_processing,
            self.test_competitor_comparison,
            self.test_flow_adaptation
        ]
        
        for test_func in tests:
            try:
                await test_func()
                await asyncio.sleep(1)  # Delay entre testes
            except Exception as e:
                print(f"❌ Erro no teste {test_func.__name__}: {e}")
                self.test_results.append({
                    "test": test_func.__name__.replace("test_", ""),
                    "passed": False,
                    "details": f"Erro: {str(e)}"
                })
        
        self.print_summary()
    
    def print_summary(self):
        """Imprime resumo dos testes"""
        print("\n" + "="*100)
        print("📊 RESUMO DOS TESTES - PROMPT V2")
        print("="*100)
        
        total = len(self.test_results)
        passed = sum(1 for r in self.test_results if r["passed"])
        
        for result in self.test_results:
            status = "✅" if result["passed"] else "❌"
            print(f"{status} {result['test']}: {result['details']}")
        
        print(f"\n📈 Taxa de sucesso: {passed}/{total} ({passed*100/total:.1f}%)")
        
        if passed == total:
            print("\n🎉 PROMPT V2 TOTALMENTE FUNCIONAL!")
            print("Todas as capacidades integradas estão operacionais:")
            print("  ✅ Adaptação contextual")
            print("  ✅ Knowledge base")
            print("  ✅ Score automático")
            print("  ✅ Processamento multimodal")
            print("  ✅ Comparação concorrentes")
            print("  ✅ Fluxo adaptativo")
        else:
            print(f"\n⚠️ {total - passed} capacidades precisam de ajustes")
            print("Verifique se:")
            print("  - O prompt V2 está ativo")
            print("  - O _build_prompt está passando contexto")
            print("  - Os serviços estão inicializados")

async def main():
    """Função principal"""
    tester = PromptV2Tester()
    await tester.run_all_tests()

if __name__ == "__main__":
    asyncio.run(main())