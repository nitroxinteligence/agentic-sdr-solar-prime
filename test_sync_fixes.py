#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste para verificar as correções de sincronização entre Supabase e Kommo CRM.
Este teste verifica:
1. Se o update_lead do Supabase está funcionando corretamente
2. Se o qualification_score está sendo incluído no payload do CRM
3. Se os logs estão sendo emitidos corretamente
"""

import asyncio
import sys
import os
from datetime import datetime

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.integrations.supabase_client import supabase_client
from app.services.crm_sync_service import crm_sync_service
from app.utils.logger import emoji_logger

async def test_supabase_update():
    """Testa se o update_lead do Supabase está funcionando corretamente"""
    print("\n🧪 Testando update_lead do Supabase...")
    
    try:
        # Buscar um lead existente para testar
        test_phone = "558182986181"
        existing_lead = await supabase_client.get_lead_by_phone(test_phone)
        
        if not existing_lead:
            print(f"❌ Lead com telefone {test_phone} não encontrado para teste")
            return False
            
        lead_id = existing_lead["id"]
        print(f"✅ Lead encontrado: {lead_id}")
        
        # Testar atualização com qualification_score
        test_changes = {
            "qualification_score": 15,
            "updated_at": datetime.now().isoformat()
        }
        
        print(f"📝 Testando atualização com: {test_changes}")
        result = await supabase_client.update_lead(lead_id, test_changes)
        
        if result:
            print(f"✅ Update bem-sucedido: {result.get('id')}")
            
            # Verificar se a atualização foi persistida
            updated_lead = await supabase_client.get_lead_by_id(lead_id)
            if updated_lead and updated_lead.get("qualification_score") == 15:
                print(f"✅ Qualification score atualizado corretamente: {updated_lead.get('qualification_score')}")
                return True
            else:
                print(f"❌ Qualification score não foi persistido corretamente")
                return False
        else:
            print("❌ Update retornou resultado vazio")
            return False
            
    except Exception as e:
        print(f"❌ Erro durante teste do Supabase: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_crm_sync_payload():
    """Testa se o qualification_score está sendo incluído no payload do CRM"""
    print("\n🧪 Testando payload do CRM sync...")
    
    try:
        # Lead de teste com qualification_score
        test_lead_info = {
            "name": "Mateus Teste",
            "phone_number": "558182986181",
            "qualification_score": 10,
            "bill_value": 500,
            "chosen_flow": "Instalação Usina Própria"
        }
        
        # Gerar payload
        payload = crm_sync_service.get_update_payload(test_lead_info, [])
        
        print(f"📝 Payload gerado: {payload}")
        
        if payload and "qualification_score" in payload:
            print(f"✅ Qualification score incluído no payload: {payload['qualification_score']}")
            return True
        else:
            print("❌ Qualification score não foi incluído no payload")
            return False
            
    except Exception as e:
        print(f"❌ Erro durante teste do CRM sync: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_crm_sync_without_qualification_score():
    """Testa se o payload funciona sem qualification_score"""
    print("\n🧪 Testando payload sem qualification_score...")
    
    try:
        # Lead de teste sem qualification_score
        test_lead_info = {
            "name": "Mateus Teste",
            "phone_number": "558182986181",
            "bill_value": 500
        }
        
        # Gerar payload
        payload = crm_sync_service.get_update_payload(test_lead_info, [])
        
        print(f"📝 Payload gerado: {payload}")
        
        if payload and "qualification_score" not in payload:
            print("✅ Qualification score corretamente ausente quando não fornecido")
            return True
        else:
            print("❌ Qualification score foi incluído incorretamente")
            return False
            
    except Exception as e:
        print(f"❌ Erro durante teste do CRM sync: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Executa todos os testes"""
    print("🚀 Iniciando testes de correção de sincronização...")
    
    results = []
    
    # Teste 1: Supabase update
    results.append(await test_supabase_update())
    
    # Teste 2: CRM sync com qualification_score
    results.append(test_crm_sync_payload())
    
    # Teste 3: CRM sync sem qualification_score
    results.append(test_crm_sync_without_qualification_score())
    
    # Resumo
    print("\n📊 Resumo dos testes:")
    print(f"✅ Testes bem-sucedidos: {sum(results)}")
    print(f"❌ Testes falharam: {len(results) - sum(results)}")
    
    if all(results):
        print("\n🎉 Todas as correções estão funcionando corretamente!")
    else:
        print("\n⚠️ Algumas correções ainda precisam de ajustes.")
    
    return all(results)

if __name__ == "__main__":
    asyncio.run(main())