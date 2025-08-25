#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste simples para verificar se a sincronização do nome do lead está funcionando.
"""

import asyncio
from app.services.crm_sync_service import crm_sync_service

def test_name_sync_payload():
    """Testa se o nome é incluído no payload de sincronização."""
    
    # Simular lead_info com nome
    lead_info = {
        "name": "João Silva",
        "phone_number": "5511999999999",
        "bill_value": 150.0,
        "chosen_flow": "Instalação Usina Própria"
    }
    
    # Simular histórico de conversa vazio
    conversation_history = []
    
    # Gerar payload de atualização
    payload = crm_sync_service.get_update_payload(lead_info, conversation_history)
    
    print("=== TESTE DE SINCRONIZAÇÃO DO NOME ===")
    print(f"Lead Info: {lead_info}")
    print(f"Payload gerado: {payload}")
    
    # Verificações
    assert payload is not None, "Payload não deveria ser None"
    assert "name" in payload, "Nome deveria estar no payload"
    assert payload["name"] == "João Silva", f"Nome esperado: 'João Silva', recebido: '{payload['name']}'"
    assert "chosen_flow" in payload, "Chosen flow deveria estar no payload"
    assert "bill_value" in payload, "Bill value deveria estar no payload"
    assert "phone" in payload, "Phone deveria estar no payload"
    assert "tags" in payload, "Tags deveriam estar no payload"
    
    print("✅ Todos os testes passaram!")
    print(f"✅ Nome '{payload['name']}' será sincronizado com o Kommo CRM")
    
    return payload

def test_name_sync_without_name():
    """Testa comportamento quando não há nome."""
    
    # Simular lead_info sem nome
    lead_info = {
        "phone_number": "5511999999999",
        "bill_value": 150.0,
        "chosen_flow": "Aluguel de Lote"
    }
    
    conversation_history = []
    payload = crm_sync_service.get_update_payload(lead_info, conversation_history)
    
    print("\n=== TESTE SEM NOME ===")
    print(f"Lead Info: {lead_info}")
    print(f"Payload gerado: {payload}")
    
    # Verificações
    assert payload is not None, "Payload não deveria ser None mesmo sem nome"
    assert "name" not in payload, "Nome não deveria estar no payload quando ausente"
    assert "chosen_flow" in payload, "Chosen flow deveria estar no payload"
    assert "bill_value" in payload, "Bill value deveria estar no payload"
    
    print("✅ Teste sem nome passou!")
    
    return payload

if __name__ == "__main__":
    print("Iniciando testes de sincronização do nome...\n")
    
    try:
        # Teste 1: Com nome
        payload_with_name = test_name_sync_payload()
        
        # Teste 2: Sem nome
        payload_without_name = test_name_sync_without_name()
        
        print("\n" + "="*50)
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("🔧 A sincronização do nome está funcionando corretamente.")
        print("📋 Resumo:")
        print(f"   - Com nome: {len(payload_with_name)} campos sincronizados")
        print(f"   - Sem nome: {len(payload_without_name)} campos sincronizados")
        print("="*50)
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        raise