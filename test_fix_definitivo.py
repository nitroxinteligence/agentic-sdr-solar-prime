#!/usr/bin/env python3
"""
Script de teste para validar correção DEFINITIVA do loop infinito
"""

import asyncio
import os
from datetime import datetime

# Configurar ambiente
os.environ["DEBUG"] = "true"
os.environ["MESSAGE_BUFFER_TIMEOUT"] = "10.0"

from app.core.context_analyzer import ContextAnalyzer
from app.core.lead_manager import LeadManager
from app.utils.logger import emoji_logger

async def test_deteccao_nome_corrigida():
    """Testa se a detecção de nome funciona com roles corretos"""
    print("\n" + "="*60)
    print("🧪 TESTE: Detecção de Nome com Roles Corretos")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    context_analyzer = ContextAnalyzer()
    context_analyzer.initialize()
    
    # Simular histórico COM ROLES CORRETOS
    messages_corretas = [
        {
            "role": "user",  # ✅ Role correto
            "content": "oi",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "assistant",  # ✅ Role correto
            "content": "Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime. Antes de começarmos, como posso te chamar?",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "user",  # ✅ Role correto
            "content": "Mateus",
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    # Testar extração
    print("\n📋 Testando com roles CORRETOS...")
    lead_info = lead_manager.extract_lead_info(messages_corretas)
    
    if lead_info.get("name"):
        print(f"✅ SUCESSO! Nome detectado: '{lead_info['name']}'")
    else:
        print(f"❌ FALHA! Nome não detectado")
        return False
    
    # Testar determinação de estágio
    stage = context_analyzer._determine_stage(messages_corretas)
    
    if stage == "estágio_1_apresentar_soluções":
        print(f"✅ SUCESSO! Estágio correto: '{stage}'")
    else:
        print(f"❌ FALHA! Estágio incorreto: '{stage}'")
        return False
    
    return True

async def test_problema_antigo():
    """Simula o problema antigo com is_from_lead"""
    print("\n" + "="*60)
    print("🧪 TESTE: Simulação do Bug Antigo (is_from_lead)")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    # Simular histórico INCORRETO (como estava antes)
    messages_bug = [
        {
            "role": "assistant",  # ❌ Tudo vira assistant por causa do bug
            "content": "oi",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "assistant",  # ❌ Tudo vira assistant
            "content": "Bom dia! Como posso te chamar?",
            "timestamp": datetime.now().isoformat()
        },
        {
            "role": "assistant",  # ❌ Tudo vira assistant
            "content": "Mateus",
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    print("\n📋 Testando com bug antigo (tudo assistant)...")
    lead_info = lead_manager.extract_lead_info(messages_bug)
    
    if not lead_info.get("name"):
        print(f"✅ Confirmado: Bug reproduzido (nome não detectado)")
        return True
    else:
        print(f"❌ Estranho: Nome detectado mesmo com bug")
        return False

async def test_variações_nome():
    """Testa diferentes variações de nomes"""
    print("\n" + "="*60)
    print("🧪 TESTE: Variações de Nomes")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    test_cases = [
        ("João", True),
        ("Maria Silva", True),
        ("Pedro de Souza", True),
        ("Ana", True),
        ("oi", False),  # Blacklist
        ("sim", False),  # Blacklist
        ("ok", False),   # Blacklist
    ]
    
    sucesso = True
    for nome_teste, esperado in test_cases:
        messages = [
            {"role": "assistant", "content": "Como posso te chamar?"},
            {"role": "user", "content": nome_teste}
        ]
        
        lead_info = lead_manager.extract_lead_info(messages)
        detectado = lead_info.get("name") is not None
        
        if detectado == esperado:
            print(f"✅ '{nome_teste}': {'Aceito' if detectado else 'Rejeitado'} (correto)")
        else:
            print(f"❌ '{nome_teste}': {'Aceito' if detectado else 'Rejeitado'} (ERRO!)")
            sucesso = False
    
    return sucesso

async def main():
    """Executa todos os testes"""
    print("\n" + "="*80)
    print("🚀 TESTE DEFINITIVO DA CORREÇÃO DO LOOP INFINITO")
    print("="*80)
    
    tests = [
        ("Detecção com Roles Corretos", test_deteccao_nome_corrigida),
        ("Reprodução do Bug Antigo", test_problema_antigo),
        ("Variações de Nomes", test_variações_nome)
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
        print("\n🎉 CORREÇÃO DEFINITIVA VALIDADA!")
        print("\n✅ Mudanças críticas aplicadas:")
        print("   1. Campo 'is_from_lead' → 'role' corrigido")
        print("   2. Logs de debug adicionados")
        print("   3. Detecção de nome mais robusta")
        print("   4. Blacklist expandida")
        print("\n🚀 PRONTO PARA DEPLOY EM PRODUÇÃO!")
    else:
        print("\n⚠️ Alguns testes falharam. Verifique os logs.")
    
    return passed == total

if __name__ == "__main__":
    success = asyncio.run(main())
    exit(0 if success else 1)