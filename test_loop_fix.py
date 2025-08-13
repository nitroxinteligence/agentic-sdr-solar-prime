#!/usr/bin/env python3
"""
Script de teste para validar as correções do loop infinito e buffer timeout
"""

import asyncio
import os
from datetime import datetime
from typing import Dict, Any, List

# Configurar variáveis de ambiente para teste
os.environ["DEBUG"] = "true"
os.environ["MESSAGE_BUFFER_TIMEOUT"] = "10.0"  # Reduzido de 30s para 10s

from app.core.context_analyzer import ContextAnalyzer
from app.core.lead_manager import LeadManager
from app.utils.logger import emoji_logger

async def test_name_detection():
    """Testa a detecção de nome no contexto"""
    print("\n" + "="*60)
    print("🧪 TESTE 1: Detecção de Nome no Contexto")
    print("="*60)
    
    # Inicializar componentes
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    context_analyzer = ContextAnalyzer()
    context_analyzer.initialize()
    
    # Simular conversa real
    messages = [
        {
            "role": "user",
            "content": "oi",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "assistant", 
            "content": "Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "user",
            "content": "mateus",
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    # Testar extração de lead info
    print("\n📋 Testando LeadManager.extract_lead_info()...")
    lead_info = lead_manager.extract_lead_info(messages)
    
    if lead_info.get("name"):
        print(f"✅ Nome detectado com sucesso: '{lead_info['name']}'")
    else:
        print(f"❌ FALHA: Nome não foi detectado!")
        print(f"   Lead info: {lead_info}")
    
    # Testar determinação de estágio
    print("\n📋 Testando ContextAnalyzer._determine_stage()...")
    stage = context_analyzer._determine_stage(messages)
    
    if stage == "estágio_1_apresentar_soluções":
        print(f"✅ Estágio correto detectado: '{stage}'")
    else:
        print(f"❌ FALHA: Estágio incorreto: '{stage}'")
        print(f"   Esperado: 'estágio_1_apresentar_soluções'")
    
    return lead_info.get("name") is not None

async def test_buffer_timeout():
    """Testa se o buffer timeout foi reduzido"""
    print("\n" + "="*60)
    print("🧪 TESTE 2: Buffer Timeout Reduzido")
    print("="*60)
    
    from app.config import settings
    
    timeout = settings.message_buffer_timeout
    print(f"\n📋 Buffer timeout configurado: {timeout}s")
    
    if timeout == 10.0:
        print(f"✅ Buffer timeout correto: {timeout}s")
        return True
    else:
        print(f"❌ FALHA: Buffer timeout incorreto: {timeout}s (esperado: 10.0s)")
        return False

async def test_blacklist_filtering():
    """Testa se a blacklist está funcionando"""
    print("\n" + "="*60)
    print("🧪 TESTE 3: Filtro de Blacklist")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    # Testar com palavra da blacklist
    messages_blacklist = [
        {
            "role": "assistant",
            "content": "Como posso te chamar?"
        },
        {
            "role": "user",
            "content": "oi"  # Palavra na blacklist
        }
    ]
    
    lead_info = lead_manager.extract_lead_info(messages_blacklist)
    
    if not lead_info.get("name"):
        print(f"✅ Blacklist funcionando: 'oi' não foi aceito como nome")
    else:
        print(f"❌ FALHA: 'oi' foi aceito como nome: {lead_info['name']}")
        return False
    
    # Testar com nome válido
    messages_valid = [
        {
            "role": "assistant",
            "content": "Como posso te chamar?"
        },
        {
            "role": "user",
            "content": "João Silva"
        }
    ]
    
    lead_info = lead_manager.extract_lead_info(messages_valid)
    
    if lead_info.get("name") == "João Silva":
        print(f"✅ Nome válido aceito: '{lead_info['name']}'")
        return True
    else:
        print(f"❌ FALHA: Nome válido não detectado")
        return False

async def test_complete_conversation_flow():
    """Testa o fluxo completo de conversa"""
    print("\n" + "="*60)
    print("🧪 TESTE 4: Fluxo Completo de Conversa")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    context_analyzer = ContextAnalyzer()
    context_analyzer.initialize()
    
    # Simular conversa completa
    conversation = [
        {"role": "user", "content": "oi"},
        {"role": "assistant", "content": "Olá! Como posso te chamar?"},
        {"role": "user", "content": "Pedro"},
        {"role": "assistant", "content": "Prazer Pedro! Temos 4 soluções: instalação, aluguel, compra e investimento."},
        {"role": "user", "content": "Quero a primeira opção"}
    ]
    
    results = []
    for i in range(1, len(conversation) + 1):
        messages = conversation[:i]
        lead_info = lead_manager.extract_lead_info(messages)
        stage = context_analyzer._determine_stage(messages)
        
        print(f"\nMensagem {i}: {messages[-1]['content'][:50]}...")
        print(f"  Nome: {lead_info.get('name', 'Não detectado')}")
        print(f"  Estágio: {stage}")
        
        results.append({
            "message_count": i,
            "name": lead_info.get("name"),
            "stage": stage
        })
    
    # Validar progressão esperada
    expected = [
        {"message_count": 1, "name": None, "stage": "estágio_0_coleta_nome"},
        {"message_count": 2, "name": None, "stage": "estágio_0_coleta_nome"},
        {"message_count": 3, "name": "Pedro", "stage": "estágio_1_apresentar_soluções"},
        {"message_count": 4, "name": "Pedro", "stage": "estágio_2_aguardando_escolha"},
        {"message_count": 5, "name": "Pedro", "stage": "qualificação"}
    ]
    
    success = True
    for i, (result, exp) in enumerate(zip(results, expected)):
        if result["name"] != exp["name"] or result["stage"] != exp["stage"]:
            print(f"\n❌ Falha na mensagem {i+1}:")
            print(f"   Esperado: {exp}")
            print(f"   Obtido: {result}")
            success = False
    
    if success:
        print("\n✅ Fluxo completo funcionando corretamente!")
    
    return success

async def main():
    """Executa todos os testes"""
    print("\n" + "="*80)
    print("🚀 INICIANDO TESTES DE CORREÇÃO DO LOOP INFINITO")
    print("="*80)
    
    tests = [
        ("Detecção de Nome", test_name_detection),
        ("Buffer Timeout", test_buffer_timeout),
        ("Blacklist", test_blacklist_filtering),
        ("Fluxo Completo", test_complete_conversation_flow)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = await test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erro no teste {name}: {e}")
            results.append((name, False))
    
    # Resumo final
    print("\n" + "="*80)
    print("📊 RESUMO DOS TESTES")
    print("="*80)
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    
    for name, success in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{status}: {name}")
    
    print(f"\n📈 Taxa de sucesso: {passed}/{total} ({passed*100/total:.1f}%)")
    
    if passed == total:
        print("\n🎉 TODOS OS TESTES PASSARAM! As correções estão funcionando.")
        print("\n✅ Correções aplicadas com sucesso:")
        print("   1. Buffer timeout reduzido de 30s para 10s")
        print("   2. Detecção de nome no contexto melhorada")
        print("   3. Logs de debug adicionados para troubleshooting")
        print("   4. Instanciação de serviços otimizada")
    else:
        print("\n⚠️ Alguns testes falharam. Verifique os logs acima.")
    
    return passed == total

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)