#!/usr/bin/env python
"""
🧪 TESTE DE CONFORMIDADE DO PROMPT
Valida que o AgenticSDR está seguindo 100% as instruções do prompt-agente.md
"""

import asyncio
import os
import sys
from datetime import datetime

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_refactored import get_agentic_agent
from app.utils.logger import emoji_logger

async def test_conformidade():
    """Testa conformidade do agente com o prompt"""
    
    print("\n" + "="*60)
    print("🧪 TESTE DE CONFORMIDADE DO PROMPT v4.0")
    print("="*60)
    
    try:
        # 1. Inicializar agente
        print("\n📦 1. Inicializando AgenticSDR...")
        agent = await get_agentic_agent()
        print("✅ Agente inicializado com sucesso")
        
        # 2. Verificar carregamento do prompt
        print("\n📄 2. Verificando carregamento do prompt externo...")
        instructions = agent._get_instructions()
        
        # Verificar se contém elementos chave do prompt
        checks = {
            "Helen Vieira": "Helen Vieira" in instructions,
            "REGRA ZERO": "REGRA ZERO" in instructions,
            "RESPOSTA_FINAL": "RESPOSTA_FINAL" in instructions,
            "Estágio 0": "ESTÁGIO 0" in instructions,
            "calendar_service": "calendar_service" in instructions,
            "Processo agendamento": "agendamento_processo" in instructions and "step_9" in instructions,
            "Leonardo Ferraz": "Leonardo Ferraz" in instructions,
        }
        
        all_passed = True
        for check, result in checks.items():
            status = "✅" if result else "❌"
            print(f"  {status} {check}: {'Encontrado' if result else 'NÃO encontrado'}")
            if not result:
                all_passed = False
        
        if not all_passed:
            print("\n⚠️ AVISO: Alguns elementos do prompt não foram encontrados!")
            print("  Verifique se o arquivo prompt-agente.md está completo.")
        
        # 3. Testar primeira interação (deve coletar nome)
        print("\n💬 3. Testando primeira interação (REGRA ZERO - coleta de nome)...")
        response1 = await agent.process_message(
            "Oi",
            {"phone": "+5511999999999"}
        )
        
        # Verificar se pede o nome
        nome_checks = [
            "como posso te chamar" in response1.lower(),
            "seu nome" in response1.lower(),
            "qual é o seu nome" in response1.lower(),
            "me diga seu nome" in response1.lower()
        ]
        
        if any(nome_checks):
            print("✅ Agente solicitou o nome (REGRA ZERO cumprida)")
        else:
            print("❌ Agente NÃO solicitou o nome (REGRA ZERO violada)")
            print(f"   Resposta: {response1[:200]}...")
        
        # 4. Testar resposta com nome
        print("\n💬 4. Testando apresentação das 4 soluções...")
        response2 = await agent.process_message(
            "Meu nome é João Silva",
            {"phone": "+5511999999999"}
        )
        
        # Verificar se apresenta soluções (verificar as 4 soluções corretas)
        solucoes_checks = [
            "instalação" in response2.lower() or "usina própria" in response2.lower(),
            "aluguel" in response2.lower() or "lote" in response2.lower(),
            "compra" in response2.lower() or "desconto" in response2.lower(),
            "investimento" in response2.lower() or "renda" in response2.lower()
        ]
        
        solucoes_encontradas = sum(solucoes_checks)
        if solucoes_encontradas >= 3:
            print(f"✅ Agente apresentou {solucoes_encontradas}/4 soluções")
        else:
            print(f"⚠️ Agente apresentou apenas {solucoes_encontradas}/4 soluções")
            print(f"   Resposta: {response2[:200]}...")
        
        # 5. Testar processamento de conta
        print("\n💬 5. Testando REGRA UM - execução instantânea...")
        response3 = await agent.process_message(
            "Minha conta de luz veio R$ 450 esse mês",
            {"phone": "+5511999999999"}
        )
        
        # Verificar se NÃO diz que vai calcular
        proibidos = [
            "vou calcular",
            "deixa eu ver",
            "vou analisar",
            "um momento",
            "já te digo"
        ]
        
        tem_proibido = any(p in response3.lower() for p in proibidos)
        tem_calculo = "R$" in response3 or "economia" in response3.lower()
        
        if not tem_proibido and tem_calculo:
            print("✅ Resposta instantânea com cálculo (REGRA UM cumprida)")
        else:
            if tem_proibido:
                print("❌ Usou expressão proibida (REGRA UM violada)")
            if not tem_calculo:
                print("⚠️ Não apresentou cálculo de economia")
            print(f"   Resposta: {response3[:200]}...")
        
        # 6. Testar agendamento
        print("\n💬 6. Testando fluxo de agendamento...")
        response4 = await agent.process_message(
            "Quero agendar uma reunião com o especialista",
            {"phone": "+5511999999999"}
        )
        
        # Verificar menção ao Leonardo
        if "leonardo" in response4.lower():
            print("✅ Mencionou Leonardo (especialista)")
        else:
            print("⚠️ Não mencionou Leonardo")
        
        # 7. Verificar formato de resposta
        print("\n📝 7. Verificando formato de resposta...")
        # Checar se o webhook vai extrair corretamente
        from app.api.webhooks import extract_final_response
        
        # Simular resposta com tags
        test_response = """
        [Análise interna do agente...]
        
        <RESPOSTA_FINAL>
        Olá! Esta é a resposta final para o cliente.
        </RESPOSTA_FINAL>
        """
        
        extracted = extract_final_response(test_response)
        if extracted and "resposta final" in extracted.lower():
            print("✅ Extração de RESPOSTA_FINAL funcionando")
        else:
            print("❌ Problema na extração de RESPOSTA_FINAL")
        
        # Resumo final
        print("\n" + "="*60)
        print("📊 RESUMO DO TESTE DE CONFORMIDADE")
        print("="*60)
        
        conformance_score = 0
        total_checks = 7
        
        # Calcular pontuação
        if all(checks.values()):
            conformance_score += 2  # Prompt carregado corretamente
        if any(nome_checks):
            conformance_score += 1  # REGRA ZERO
        if solucoes_encontradas >= 3:
            conformance_score += 1  # Apresentação de soluções
        if not tem_proibido and tem_calculo:
            conformance_score += 1  # REGRA UM
        if "leonardo" in response4.lower():
            conformance_score += 1  # Menção ao especialista
        if extracted:
            conformance_score += 1  # Formato de resposta
        
        percentage = (conformance_score / total_checks) * 100
        
        print(f"\n🎯 Conformidade: {conformance_score}/{total_checks} ({percentage:.1f}%)")
        
        if percentage >= 95:
            print("✅ SISTEMA 100% OPERACIONAL E CONFORME!")
        elif percentage >= 80:
            print("⚠️ Sistema funcional mas com pequenos ajustes necessários")
        else:
            print("❌ Sistema precisa de correções importantes")
        
        return percentage >= 95
        
    except Exception as e:
        print(f"\n❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Executar teste
    success = asyncio.run(test_conformidade())
    
    # Retornar código de saída apropriado
    sys.exit(0 if success else 1)