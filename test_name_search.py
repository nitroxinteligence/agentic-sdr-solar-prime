#!/usr/bin/env python3
"""
Teste específico para busca de leads por nome no CONTACTS_UPDATE
"""

import asyncio
import sys
import os
from pathlib import Path

# Adiciona o diretório raiz ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Carrega variáveis de ambiente
from dotenv import load_dotenv
env_path = project_root / '.env'
if env_path.exists():
    load_dotenv(env_path)
    print(f"✅ Arquivo .env encontrado: {env_path}")
else:
    print(f"❌ Arquivo .env não encontrado: {env_path}")
    sys.exit(1)

from app.integrations.supabase_client import supabase_client
from app.api.webhooks import process_contacts_update
import json

async def test_name_search():
    """Testa a busca de leads por nome"""
    print("🔍 TESTANDO BUSCA POR NOME")
    print("=" * 50)
    
    # 1. Criar um lead de teste
    print("\n📝 Criando lead de teste...")
    test_lead_data = {
        "name": "Mateus M",
        "phone_number": "5511999887766",
        "current_stage": "INITIAL_CONTACT",
        "qualification_status": "PENDING"
    }
    
    try:
        created_lead = await supabase_client.create_lead(test_lead_data)
        print(f"✅ Lead criado: ID {created_lead['id']}, Nome: {created_lead['name']}")
        lead_id = created_lead['id']
    except Exception as e:
        print(f"❌ Erro ao criar lead: {e}")
        return
    
    # 2. Testar busca por nome
    print("\n🔍 Testando busca por nome...")
    try:
        found_leads = await supabase_client.search_leads_by_name("Mateus M")
        print(f"✅ Encontrados {len(found_leads)} leads:")
        for lead in found_leads:
            print(f"  - ID: {lead['id']}, Nome: {lead['name']}, Telefone: {lead.get('phone_number', 'N/A')}")
    except Exception as e:
        print(f"❌ Erro na busca por nome: {e}")
    
    # 3. Testar CONTACTS_UPDATE com telefone vazio mas pushName válido
    print("\n📱 Testando CONTACTS_UPDATE com pushName...")
    payload_with_pushname = {
        "event": "contacts.update",
        "instance": "SDR IA SolarPrime",
        "data": [{
            "id": "",  # Telefone vazio
            "pushName": "Mateus M",  # Nome disponível
            "name": "Mateus M",
            "notify": "Mateus M"
        }]
    }
    
    print(f"Payload: {json.dumps(payload_with_pushname, indent=2)}")
    
    try:
        await process_contacts_update(payload_with_pushname)
        print("✅ CONTACTS_UPDATE processado")
    except Exception as e:
        print(f"❌ Erro no CONTACTS_UPDATE: {e}")
    
    # 4. Verificar se o lead foi atualizado
    print("\n🔍 Verificando lead após CONTACTS_UPDATE...")
    try:
        updated_lead = await supabase_client.get_lead_by_id(lead_id)
        if updated_lead:
            print(f"✅ Lead encontrado: {updated_lead['name']} - {updated_lead.get('phone_number', 'N/A')}")
        else:
            print("❌ Lead não encontrado")
    except Exception as e:
        print(f"❌ Erro ao buscar lead: {e}")
    
    # 5. Limpeza - remover lead de teste
    print("\n🧹 Removendo lead de teste...")
    try:
        # Como não temos método delete, vamos apenas marcar como removido
        await supabase_client.update_lead(lead_id, {"qualification_status": "TEST_REMOVED"})
        print("✅ Lead marcado como removido")
    except Exception as e:
        print(f"❌ Erro ao remover lead: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 TESTE CONCLUÍDO")

if __name__ == "__main__":
    asyncio.run(test_name_search())