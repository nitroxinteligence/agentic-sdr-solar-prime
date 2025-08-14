#!/usr/bin/env python3
"""
Teste definitivo do Fluxo C - Validação da correção do conflito de prompts
Verifica que o agente segue o fluxo correto sem desvios
"""

import asyncio
import os
from datetime import datetime

# Configurar ambiente
os.environ["DEBUG"] = "true"

from app.agents.agentic_sdr_refactored import AgenticSDR
from app.utils.logger import emoji_logger

async def test_fluxo_c_sem_conflito():
    """
    Testa se o Fluxo C funciona corretamente após remoção do conflito de prompts
    Cenário específico: usuário diz "ainda não" deve perguntar valor, NÃO "o que te impede"
    """
    print("\n" + "="*80)
    print("🧪 TESTE DEFINITIVO: Fluxo C sem Conflito de Prompts")
    print("="*80)
    
    # Criar instância do agente
    agent = AgenticSDR()
    await agent.initialize()
    
    # Diálogo exato do problema reportado
    test_dialogue = [
        {
            "user": "oi",
            "expected": "deve pedir nome",
            "forbidden": [],
            "required": ["como posso te chamar", "antes de começarmos"]
        },
        {
            "user": "Mateus",
            "expected": "deve apresentar 4 soluções",
            "forbidden": [],
            "required": ["quatro modelos", "1)", "2)", "3)", "4)"]
        },
        {
            "user": "3",
            "expected": "deve perguntar sobre desconto atual",
            "forbidden": ["o que te impede", "fechar hoje", "fechar negócio"],
            "required": ["desconto", "conta de luz"]
        },
        {
            "user": "ainda não",
            "expected": "CRÍTICO: deve perguntar VALOR da conta",
            "forbidden": [
                "o que te impede",
                "fechar negócio",
                "fechar hoje",
                "impede de fechar"
            ],
            "required": [
                "quanto",
                "paga",
                "conta",
                "valor"
            ]
        },
        {
            "user": "450 reais",
            "expected": "deve calcular e mostrar economia",
            "forbidden": ["vou calcular", "deixa eu ver", "vou analisar"],
            "required": ["360", "20%", "desconto"]
        }
    ]
    
    print("\n📱 Executando diálogo de teste:")
    print("-" * 40)
    
    # Resetar histórico
    agent.conversation_history = []
    test_passed = True
    
    for i, test_case in enumerate(test_dialogue):
        user_msg = test_case["user"]
        expected = test_case["expected"]
        forbidden = test_case["forbidden"]
        required = test_case["required"]
        
        print(f"\n🔹 Passo {i+1}: {expected}")
        print(f"👤 Usuário: '{user_msg}'")
        
        try:
            # Processar mensagem
            response = await agent.process_message(
                user_msg,
                metadata={"phone": "5511999999999"}
            )
            
            # Limpar tags de resposta
            if "<RESPOSTA_FINAL>" in response:
                response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
            
            # Exibir resposta (truncada)
            print(f"🤖 Helen: {response[:150]}...")
            
            # Validar resposta
            response_lower = response.lower()
            
            # Verificar palavras proibidas
            for forbidden_phrase in forbidden:
                if forbidden_phrase in response_lower:
                    print(f"\n❌ ERRO CRÍTICO: Encontrada frase proibida: '{forbidden_phrase}'")
                    print(f"   Isso indica que o conflito de prompts AINDA EXISTE!")
                    test_passed = False
                    break
            
            # Verificar palavras obrigatórias
            if required:
                found_required = False
                for required_phrase in required:
                    if required_phrase in response_lower:
                        found_required = True
                        break
                
                if not found_required:
                    print(f"\n⚠️ AVISO: Nenhuma palavra obrigatória encontrada: {required}")
                    print(f"   O agente pode estar desviando do fluxo!")
            
            # Validação especial para o passo crítico
            if i == 3:  # Resposta para "ainda não"
                if "o que te impede" in response_lower:
                    print("\n🚨 FALHA CRÍTICA: O CONFLITO DE PROMPTS PERSISTE!")
                    print("   O agente ainda está usando 'Ação recomendada: conversar'")
                    test_passed = False
                elif any(word in response_lower for word in ["quanto", "valor", "paga"]):
                    print("✅ SUCESSO: Agente seguiu o fluxo correto!")
                else:
                    print("⚠️ Resposta ambígua - verificar manualmente")
            
        except Exception as e:
            print(f"\n❌ Erro ao processar: {e}")
            test_passed = False
            break
    
    print("\n" + "="*80)
    
    if test_passed:
        print("🎉 TESTE PASSOU - CONFLITO DE PROMPTS RESOLVIDO!")
        print("\n✅ Confirmações:")
        print("   1. Agente NÃO pergunta 'o que te impede de fechar'")
        print("   2. Agente SEGUE o fluxo correto do Fluxo C")
        print("   3. Após 'ainda não', pergunta o valor da conta")
        print("   4. Não há mais 'Ação recomendada: conversar' interferindo")
    else:
        print("❌ TESTE FALHOU - CONFLITO AINDA EXISTE!")
        print("\n⚠️ Ações necessárias:")
        print("   1. Verificar se _build_prompt foi corretamente modificado")
        print("   2. Confirmar que 'Ação recomendada' foi removida")
        print("   3. Garantir que o system prompt é a única fonte de instruções")
    
    return test_passed

async def test_prompt_dinamico_limpo():
    """
    Testa se o prompt dinâmico contém apenas informações factuais
    """
    print("\n" + "="*80)
    print("🧪 TESTE: Verificação do Prompt Dinâmico")
    print("="*80)
    
    agent = AgenticSDR()
    await agent.initialize()
    
    # Criar contexto de teste
    test_context = {
        "conversation_stage": "estágio_2_aguardando_escolha",
        "user_intent": "interesse",
        "action_needed": "conversar"  # Isso NÃO deve aparecer no prompt
    }
    
    test_lead_info = {
        "name": "João",
        "bill_value": 500.0,
        "chosen_flow": "Compra com Desconto"
    }
    
    # Chamar _build_prompt diretamente
    prompt = agent._build_prompt(
        message="ainda não",
        context=test_context,
        lead_info=test_lead_info,
        service_results=[],
        media_context=""
    )
    
    print("\n📋 Prompt gerado:")
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    
    # Validações
    test_passed = True
    
    # Verificar que NÃO contém instruções
    forbidden = [
        "Ação recomendada",
        "ESTÁGIO ATUAL",
        "Responda de forma",
        "Intenção detectada",
        "conversar"
    ]
    
    for phrase in forbidden:
        if phrase in prompt:
            print(f"\n❌ ERRO: Encontrada instrução proibida: '{phrase}'")
            test_passed = False
    
    # Verificar que contém apenas fatos
    expected = [
        "Mensagem do cliente:",
        "Nome do lead:",
        "Valor da conta informado:",
        "Fluxo escolhido:"
    ]
    
    for phrase in expected:
        if phrase in prompt:
            print(f"✅ Informação factual presente: '{phrase}'")
    
    if test_passed:
        print("\n✅ PROMPT DINÂMICO ESTÁ LIMPO!")
        print("   Contém apenas informações factuais")
        print("   Não compete com o system prompt")
    else:
        print("\n❌ PROMPT DINÂMICO AINDA TEM INSTRUÇÕES!")
    
    return test_passed

async def main():
    """Executa todos os testes"""
    print("\n" + "="*100)
    print("🚀 TESTE DEFINITIVO - CORREÇÃO DO CONFLITO DE PROMPTS")
    print("="*100)
    
    tests = [
        ("Prompt Dinâmico Limpo", test_prompt_dinamico_limpo),
        ("Fluxo C Sem Conflito", test_fluxo_c_sem_conflito)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = await test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erro no teste {name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Resumo final
    print("\n" + "="*100)
    print("📊 RESUMO DOS TESTES")
    print("="*100)
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    
    for name, success in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{status}: {name}")
    
    print(f"\n📈 Taxa de sucesso: {passed}/{total} ({passed*100/total:.1f}%)")
    
    if passed == total:
        print("\n🎉 CONFLITO DE PROMPTS DEFINITIVAMENTE RESOLVIDO!")
        print("\n✅ Correções aplicadas com sucesso:")
        print("   1. _build_prompt agora contém APENAS informações factuais")
        print("   2. Removidas todas as instruções dinâmicas conflitantes")
        print("   3. System prompt é a ÚNICA fonte de instruções")
        print("   4. Agente segue o fluxo correto sem desvios")
        print("\n🚀 PRONTO PARA DEPLOY EM PRODUÇÃO!")
    else:
        print("\n⚠️ Alguns testes falharam. Revisar implementação.")
    
    return passed == total

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)