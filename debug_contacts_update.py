#!/usr/bin/env python3
"""
Script para debugar o webhook CONTACTS_UPDATE e identificar por que o telefone está vazio
"""

import asyncio
import json
from app.api.webhooks import process_contacts_update
from app.utils.logger import emoji_logger

# Payload real baseado no log - simulando o que está chegando
real_payload_empty_phone = {
    "event": "contacts.update",
    "instance": "SDR IA SolarPrime", 
    "data": [{
        "id": "",  # Telefone vazio como no log
        "pushName": "Mateus M",
        "name": "Mateus M",
        "notify": "Mateus M"
    }]
}

# Payload com telefone correto para comparação
correct_payload = {
    "event": "contacts.update",
    "instance": "SDR IA SolarPrime",
    "data": [{
        "id": "5511999887766@c.us",
        "pushName": "Mateus M",
        "name": "Mateus M", 
        "notify": "Mateus M"
    }]
}

# Payload com estrutura aninhada
nested_payload = {
    "event": "contacts.update",
    "instance": "SDR IA SolarPrime",
    "data": {
        "contactInfo": {
            "id": "5511999887766@c.us",
            "pushName": "Mateus M",
            "profile": {
                "name": "Mateus M",
                "displayName": "Mateus M"
            }
        }
    }
}

async def debug_contacts_update():
    """Testa diferentes cenários de CONTACTS_UPDATE"""
    
    print("🔍 DEBUGANDO CONTACTS_UPDATE")
    print("=" * 50)
    
    # Teste 1: Payload com telefone vazio (problema atual)
    print("\n📱 Teste 1: Payload com telefone vazio (problema atual)")
    print(f"Payload: {json.dumps(real_payload_empty_phone, indent=2)}")
    try:
        await process_contacts_update(real_payload_empty_phone)
        print("✅ Processado sem erro")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # Teste 2: Payload com telefone correto
    print("\n📱 Teste 2: Payload com telefone correto")
    print(f"Payload: {json.dumps(correct_payload, indent=2)}")
    try:
        await process_contacts_update(correct_payload)
        print("✅ Processado sem erro")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    # Teste 3: Payload com estrutura aninhada
    print("\n📱 Teste 3: Payload com estrutura aninhada")
    print(f"Payload: {json.dumps(nested_payload, indent=2)}")
    try:
        await process_contacts_update(nested_payload)
        print("✅ Processado sem erro")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 ANÁLISE CONCLUÍDA")

if __name__ == "__main__":
    asyncio.run(debug_contacts_update())