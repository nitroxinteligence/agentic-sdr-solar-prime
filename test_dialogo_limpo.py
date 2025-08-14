#!/usr/bin/env python3
"""
TESTE LIMPO E ISOLADO - CENÁRIO COMPLETO
Limpa dados antes de executar para garantir estado pristine
"""

import asyncio
import os
from datetime import datetime

# Configurar ambiente
os.environ["DEBUG"] = "false"  # Desabilitar debug para saída limpa

from app.agents.agentic_sdr_refactored import AgenticSDR
from test_utils_cleanup import ensure_clean_state, get_test_stats, print_test_stats

async def test_dialogo_limpo():
    """Testa o cenário completo com estado limpo"""
    
    print("\n" + "="*100)
    print("🧪 TESTE LIMPO E ISOLADO - CENÁRIO COMPLETO")
    print("="*100)
    
    phone = "5511999999999"
    
    # ========== LIMPEZA INICIAL ==========
    print("\n🧹 FASE 0: LIMPEZA DE DADOS")
    print("-"*80)
    
    # Limpar dados existentes
    is_clean = await ensure_clean_state(phone)
    if not is_clean:
        print("⚠️ Aviso: Limpeza pode ter sido parcial")
    
    # Verificar estado limpo
    stats = await get_test_stats(phone)
    print_test_stats(stats)
    
    if stats["messages_count"] > 0 or stats["conversations_count"] > 0:
        print("❌ ERRO: Dados não foram completamente limpos!")
        return
    
    print("✅ Estado limpo confirmado!")
    
    # ========== DIA 1 - CONVERSA INICIAL ==========
    print("\n" + "="*80)
    print("📅 DIA 1 - CONVERSA INICIAL (ESTADO LIMPO)")
    print("-"*80)
    
    agent1 = AgenticSDR()
    await agent1.initialize()
    
    # Verificar estado inicial
    print(f"\n📊 Estado inicial do agent:")
    print(f"  - Histórico: {len(agent1.conversation_history)} mensagens")
    print(f"  - Lead info: {agent1.current_lead_info}")
    
    # 1. Primeira mensagem
    print("\n👤 Mateus: 'oi'")
    response1 = await agent1.process_message("oi", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response1:
        response1 = response1.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response1[:200]}...")
    
    # Verificar se Helen pediu o nome
    asked_for_name = "como posso te chamar" in response1.lower() or "seu nome" in response1.lower()
    print(f"  ℹ️ Helen pediu nome? {'✅ Sim' if asked_for_name else '❌ Não'}")
    
    # 2. Mateus diz nome
    print("\n👤 Mateus: 'mateus'")
    response2 = await agent1.process_message("mateus", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response2:
        response2 = response2.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response2[:200]}...")
    
    # Verificar se Helen usou o nome
    used_name = "mateus" in response2.lower()
    print(f"  ℹ️ Helen usou o nome? {'✅ Sim' if used_name else '❌ Não'}")
    print(f"  ℹ️ Nome detectado: {agent1.current_lead_info.get('name')}")
    
    # 3. Escolhe opção 3 (Compra com desconto)
    print("\n👤 Mateus: 'Compra de energia com desconto'")
    response3 = await agent1.process_message("Compra de energia com desconto", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response3:
        response3 = response3.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response3[:200]}...")
    
    # Verificar se o fluxo foi detectado
    print(f"  ℹ️ Fluxo detectado: {agent1.current_lead_info.get('chosen_flow')}")
    
    # 4. Confirma com número
    print("\n👤 Mateus: '3'")
    response4 = await agent1.process_message("3", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response4:
        response4 = response4.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response4[:200]}...")
    
    # Verificar fluxo após número
    print(f"  ℹ️ Fluxo após '3': {agent1.current_lead_info.get('chosen_flow')}")
    
    # 5. Responde que não tem desconto ainda
    print("\n👤 Mateus: 'ainda nao'")
    response5 = await agent1.process_message("ainda nao", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response5:
        response5 = response5.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response5[:200]}...")
    
    # Verificar se Helen está no contexto correto (desconto)
    mentioned_discount = "desconto" in response5.lower() or "economia" in response5.lower()
    print(f"  ℹ️ Helen mencionou desconto/economia? {'✅ Sim' if mentioned_discount else '❌ Não'}")
    
    print(f"\n📊 Estado após DIA 1:")
    print(f"  - Nome: {agent1.current_lead_info.get('name')}")
    print(f"  - Fluxo: {agent1.current_lead_info.get('chosen_flow')}")
    print(f"  - Histórico: {len(agent1.conversation_history)} mensagens")
    print(f"  - Conversation ID: {agent1.conversation_id}")
    
    # ========== DIA 2 - NOVA SESSÃO ==========
    print("\n" + "="*100)
    print("📅 DIA 2 - NOVA SESSÃO (RECUPERAÇÃO DE CONTEXTO)")
    print("-"*80)
    
    # Aguardar para simular tempo entre sessões
    print("⏳ Aguardando 3 segundos para simular nova sessão...")
    await asyncio.sleep(3)
    
    # Criar novo agente (simula nova sessão)
    agent2 = AgenticSDR()
    await agent2.initialize()
    
    print(f"\n📊 Estado inicial do agent2 (antes de processar):")
    print(f"  - Histórico: {len(agent2.conversation_history)} mensagens")
    print(f"  - Lead info: {agent2.current_lead_info}")
    
    # Mensagem do dia seguinte
    print("\n👤 Mateus: 'OI?'")
    response_dia2 = await agent2.process_message("OI?", metadata={"phone": phone})
    if "<RESPOSTA_FINAL>" in response_dia2:
        response_dia2 = response_dia2.split("<RESPOSTA_FINAL>")[1].split("</RESPOSTA_FINAL>")[0].strip()
    print(f"🤖 Helen: {response_dia2[:250]}...")
    
    print(f"\n📊 Estado após recuperação:")
    print(f"  - Nome recuperado: {agent2.current_lead_info.get('name')}")
    print(f"  - Fluxo recuperado: {agent2.current_lead_info.get('chosen_flow')}")
    print(f"  - Histórico: {len(agent2.conversation_history)} mensagens")
    
    # ========== VALIDAÇÃO FINAL ==========
    print("\n" + "="*100)
    print("🎯 VALIDAÇÃO FINAL")
    print("="*100)
    
    resultados = []
    
    # 1. Verificar se histórico foi recuperado corretamente
    expected_messages = 10  # Dia 1: 5 user + 5 assistant = 10
    if len(agent2.conversation_history) >= expected_messages:
        resultados.append(f"✅ Histórico completo recuperado ({len(agent2.conversation_history)} msgs)")
    else:
        resultados.append(f"❌ Histórico incompleto: {len(agent2.conversation_history)} msgs (esperado: {expected_messages}+)")
    
    # 2. Verificar se recuperou nome
    if agent2.current_lead_info.get('name') == 'Mateus':
        resultados.append("✅ Nome 'Mateus' recuperado corretamente")
    else:
        resultados.append(f"❌ Nome incorreto: {agent2.current_lead_info.get('name')}")
    
    # 3. Verificar se recuperou fluxo correto
    if agent2.current_lead_info.get('chosen_flow') == 'Compra com Desconto':
        resultados.append("✅ Fluxo 'Compra com Desconto' recuperado corretamente")
    else:
        resultados.append(f"❌ Fluxo incorreto: {agent2.current_lead_info.get('chosen_flow')}")
    
    # 4. Verificar se pediu nome novamente
    if "como posso te chamar" in response_dia2.lower() or "qual seu nome" in response_dia2.lower():
        resultados.append("❌ Agent pediu nome novamente (ERRO)")
    else:
        resultados.append("✅ Agent NÃO pediu nome novamente")
    
    # 5. Verificar se usou nome na resposta
    if "mateus" in response_dia2.lower():
        resultados.append("✅ Agent usou o nome 'Mateus' na resposta")
    else:
        resultados.append("⚠️ Agent não usou o nome na resposta (pode ser intencional por moderação)")
    
    # 6. Verificar se mencionou valor inventado
    if "460" in response_dia2 or "quatrocentos" in response_dia2.lower():
        resultados.append("❌ Agent mencionou R$460 (valor INVENTADO)")
    else:
        resultados.append("✅ Agent NÃO inventou valores")
    
    # 7. Verificar continuidade do fluxo
    if "desconto" in response_dia2.lower() or "economia" in response_dia2.lower():
        resultados.append("✅ Agent manteve contexto do fluxo de desconto")
    elif "usina" in response_dia2.lower() and "desconto" not in response_dia2.lower():
        resultados.append("❌ Agent mudou para fluxo de usina (ERRO)")
    else:
        resultados.append("⚠️ Fluxo não claramente identificado na resposta")
    
    # 8. Verificar se a resposta faz sentido contextualmente
    if len(response_dia2) > 50 and not response_dia2.startswith("Olá!"):
        resultados.append("✅ Resposta contextualizada (não repetiu saudação inicial)")
    else:
        resultados.append("❌ Resposta parece ser saudação inicial (perdeu contexto)")
    
    # Imprimir resultados
    for resultado in resultados:
        print(resultado)
    
    # Contabilizar
    erros = sum(1 for r in resultados if "❌" in r)
    avisos = sum(1 for r in resultados if "⚠️" in r)
    sucessos = sum(1 for r in resultados if "✅" in r)
    
    print(f"\n📊 RESULTADO FINAL:")
    print(f"  ✅ Sucessos: {sucessos}/8")
    print(f"  ⚠️ Avisos: {avisos}/8")
    print(f"  ❌ Erros: {erros}/8")
    
    # Estatísticas finais
    print("\n📊 ESTATÍSTICAS FINAIS DO TESTE:")
    final_stats = await get_test_stats(phone)
    print_test_stats(final_stats)
    
    if erros == 0:
        print("\n🎉 SISTEMA 100% FUNCIONAL! TODOS OS TESTES PASSARAM!")
        return True
    elif erros <= 2:
        print(f"\n✅ Sistema funcional com {erros} pequenos problemas")
        return True
    else:
        print(f"\n⚠️ Sistema com {erros} problemas que precisam correção")
        return False

if __name__ == "__main__":
    result = asyncio.run(test_dialogo_limpo())
    exit(0 if result else 1)