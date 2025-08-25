#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste para validar a correção do problema de detecção incorreta de chosen_flow.
Este script testa se as palavras-chave genéricas não causam mais falsos positivos.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.lead_manager import LeadManager

def test_chosen_flow_detection():
    """Testa se a detecção de chosen_flow não gera mais falsos positivos"""
    
    lead_manager = LeadManager()
    
    # Casos que NÃO devem detectar "Usina Investimento"
    negative_cases = [
        "não tenho dinheiro para investimento",
        "não quero fazer investimento agora",
        "investimento é muito caro",
        "recebo não, não tenho investimento",
        "não posso investir",
        "investimento não é para mim",
        "sem condições de investimento"
    ]
    
    # Casos que DEVEM detectar "Usina Investimento"
    positive_cases = [
        "quero a usina de investimento",
        "me interessa a usina investimento",
        "opção 4 por favor",
        "modelo 4 é o que quero",
        "gostaria da usina de investimento"
    ]
    
    print("🧪 Testando casos que NÃO devem detectar 'Usina Investimento':")
    for i, text in enumerate(negative_cases, 1):
        chosen_flow = lead_manager._extract_chosen_flow(text)
        status = "✅ PASSOU" if chosen_flow != "Usina Investimento" else "❌ FALHOU"
        print(f"  {i}. '{text}' -> {chosen_flow} {status}")
    
    print("\n🧪 Testando casos que DEVEM detectar 'Usina Investimento':")
    for i, text in enumerate(positive_cases, 1):
        chosen_flow = lead_manager._extract_chosen_flow(text)
        status = "✅ PASSOU" if chosen_flow == "Usina Investimento" else "❌ FALHOU"
        print(f"  {i}. '{text}' -> {chosen_flow} {status}")
    
    print("\n🧪 Testando outros fluxos:")
    other_cases = [
        ("quero instalação de usina própria", "Instalação Usina Própria"),
        ("prefiro aluguel de lote", "Aluguel de Lote"),
        ("compra de energia com desconto", "Compra com Desconto"),
        ("opção 1 por favor", "Instalação Usina Própria"),
        ("modelo 2 é melhor", "Aluguel de Lote"),
        ("opção 3 para mim", "Compra com Desconto")
    ]
    
    for i, (text, expected) in enumerate(other_cases, 1):
        chosen_flow = lead_manager._extract_chosen_flow(text)
        status = "✅ PASSOU" if chosen_flow == expected else "❌ FALHOU"
        print(f"  {i}. '{text}' -> {chosen_flow} (esperado: {expected}) {status}")

if __name__ == "__main__":
    print("🔧 Teste de Correção: Detecção de Chosen Flow")
    print("=" * 50)
    test_chosen_flow_detection()
    print("\n✅ Teste concluído!")