#!/usr/bin/env python3
"""
Teste do prompt simplificado - Validação do Fluxo C (Compra com Desconto)
"""

import asyncio
import os
from datetime import datetime

# Configurar ambiente
os.environ["DEBUG"] = "true"

from app.agents.agentic_sdr_refactored import AgenticSDR
from app.utils.logger import emoji_logger

async def test_fluxo_c_completo():
    """Testa o Fluxo C completo - Compra com Desconto"""
    print("\n" + "="*80)
    print("🧪 TESTE: Fluxo C - Compra com Desconto")
    print("="*80)
    
    # Criar instância do agente
    agent = AgenticSDR()
    await agent.initialize()
    
    # Simular conversa seguindo o fluxo
    test_messages = [
        ("oi", "Primeira mensagem - deve pedir nome"),
        ("Mateus", "Nome fornecido - deve apresentar 4 soluções"),
        ("3", "Escolheu opção 3 - deve seguir Fluxo C"),
        ("ainda não", "Não tem desconto - deve perguntar valor"),
        ("450 reais", "Valor fornecido - deve calcular desconto"),
        ("quero conhecer mais", "Interesse - deve oferecer agendamento")
    ]
    
    print("\n📱 Simulando conversa:")
    print("-" * 40)
    
    # Resetar histórico do agente
    agent.conversation_history = []
    
    for user_msg, expected_behavior in test_messages:
        print(f"\n👤 USUÁRIO: {user_msg}")
        print(f"   (Esperado: {expected_behavior})")
        
        # Processar mensagem
        try:
            response = await agent.process_message(
                user_msg,
                metadata={"phone": "5511999999999"}
            )
            
            # Limpar tags de resposta para exibição
            if "<RESPOSTA_FINAL>" in response:
                response = response.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
            
            print(f"\n🤖 HELEN: {response[:200]}...")
            
            # Validações específicas
            if user_msg == "3":
                # Verificar se NÃO está sendo agressiva
                if "o que te impede" in response.lower():
                    print("\n❌ ERRO: Agente está sendo agressivo!")
                    return False
                
                # Verificar se está seguindo o Fluxo C
                if "desconto" in response.lower() and "empresários" in response.lower():
                    print("✅ Seguindo Fluxo C corretamente")
                else:
                    print("❌ ERRO: Não está seguindo o Fluxo C!")
                    return False
            
            if user_msg == "450 reais":
                # Verificar se calculou o desconto
                if "360" in response or "20%" in response:
                    print("✅ Desconto calculado corretamente")
                else:
                    print("⚠️ Desconto não mencionado claramente")
            
        except Exception as e:
            print(f"\n❌ Erro ao processar: {e}")
            return False
    
    print("\n" + "-" * 40)
    print("✅ Fluxo C testado com sucesso!")
    return True

async def test_resposta_instantanea():
    """Testa se o agente responde com dados já calculados"""
    print("\n" + "="*80)
    print("🧪 TESTE: Resposta Instantânea (sem 'vou calcular')")
    print("="*80)
    
    agent = AgenticSDR()
    await agent.initialize()
    
    # Preparar contexto
    agent.conversation_history = [
        {"role": "user", "content": "oi"},
        {"role": "assistant", "content": "Bom dia! Como posso te chamar?"},
        {"role": "user", "content": "João"},
        {"role": "assistant", "content": "Perfeito, João! Hoje na Solarprime..."},
        {"role": "user", "content": "3"}
    ]
    
    # Enviar valor para cálculo
    response = await agent.process_message(
        "Pago 500 reais",
        metadata={"phone": "5511999999999"}
    )
    
    # Verificar se NÃO tem frases proibidas
    forbidden_phrases = [
        "vou calcular",
        "deixa eu ver",
        "vou analisar",
        "só um minutinho",
        "vou somar",
        "estou verificando"
    ]
    
    response_lower = response.lower()
    for phrase in forbidden_phrases:
        if phrase in response_lower:
            print(f"❌ ERRO: Encontrada frase proibida: '{phrase}'")
            return False
    
    # Verificar se tem o valor calculado
    if "400" in response or "20%" in response:
        print("✅ Resposta instantânea com cálculo pronto!")
        return True
    else:
        print("⚠️ Cálculo não encontrado na resposta")
        return False

async def test_nome_moderado():
    """Testa se o agente usa o nome com moderação"""
    print("\n" + "="*80)
    print("🧪 TESTE: Uso Moderado do Nome")
    print("="*80)
    
    agent = AgenticSDR()
    await agent.initialize()
    
    # Simular conversa
    messages = [
        "oi",
        "Pedro",
        "opção 1",
        "500 reais",
        "só minha casa",
        "Rua das Flores 123"
    ]
    
    agent.conversation_history = []
    nome_count = 0
    total_responses = 0
    
    for msg in messages:
        response = await agent.process_message(
            msg,
            metadata={"phone": "5511999999999"}
        )
        
        if "Pedro" in response:
            nome_count += 1
        total_responses += 1
    
    uso_percentual = (nome_count / total_responses) * 100
    
    print(f"\n📊 Nome usado em {nome_count}/{total_responses} mensagens ({uso_percentual:.1f}%)")
    
    if uso_percentual <= 30:  # Máximo 30% aceitável
        print("✅ Nome usado com moderação!")
        return True
    else:
        print("❌ Nome usado excessivamente!")
        return False

async def main():
    """Executa todos os testes"""
    print("\n" + "="*100)
    print("🚀 TESTE DO PROMPT SIMPLIFICADO")
    print("="*100)
    
    tests = [
        ("Fluxo C Completo", test_fluxo_c_completo),
        ("Resposta Instantânea", test_resposta_instantanea),
        ("Nome Moderado", test_nome_moderado)
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
    
    # Resumo
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
        print("\n🎉 PROMPT SIMPLIFICADO FUNCIONANDO!")
        print("\n✅ Melhorias implementadas:")
        print("   1. Prompt reduzido de 1376 para 132 linhas (90% menor)")
        print("   2. Fluxos claros e diretos")
        print("   3. Sem perguntas agressivas")
        print("   4. Respostas instantâneas")
        print("   5. Nome usado com moderação")
        print("\n🚀 PRONTO PARA DEPLOY!")
    else:
        print("\n⚠️ Alguns testes falharam. Verifique os logs.")
    
    return passed == total

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)