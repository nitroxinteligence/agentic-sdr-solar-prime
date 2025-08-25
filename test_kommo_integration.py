#!/usr/bin/env python3
"""
Teste de integração com KommoCRM
Verifica se o telefone está sendo enviado corretamente para o campo WhatsApp
"""

import asyncio
import json
from app.services.crm_service_100_real import CRMServiceReal
from app.utils.logger import emoji_logger

async def test_kommo_integration():
    """Testa a criação de lead no KommoCRM com telefone no campo WhatsApp"""
    print("🔧 Iniciando teste de integração com KommoCRM...")
    print("=" * 60)
    
    # Inicializar o serviço CRM
    crm_service = CRMServiceReal()
    await crm_service.initialize()
    
    if not crm_service.is_initialized:
        print("❌ Falha ao inicializar o serviço CRM")
        return
    
    print("✅ Serviço CRM inicializado com sucesso")
    
    # Dados de teste para criação do lead
    test_lead_data = {
        "name": "Teste KommoCRM Integration",
        "phone": "5511999888777",
        "email": "teste@kommocrm.com",
        "bill_value": 250.0,
        "chosen_flow": "Instalação Usina Própria"
    }
    
    print(f"📋 Dados do lead de teste: {json.dumps(test_lead_data, indent=2)}")
    
    try:
        # Criar lead no KommoCRM
        print("\n🚀 Criando lead no KommoCRM...")
        result = await crm_service.create_lead(test_lead_data)
        
        if result.get("success"):
            lead_id = result.get("lead_id")
            print(f"✅ Lead criado com sucesso! ID: {lead_id}")
            
            # Verificar se o lead foi criado corretamente
            print("\n🔍 Verificando lead criado...")
            created_lead = await crm_service.get_lead_by_phone(test_lead_data["phone"])
            
            if created_lead:
                print(f"✅ Lead encontrado: {created_lead.get('name')}")
                print(f"📞 ID do lead: {created_lead.get('id')}")
                
                # Verificar campos customizados
                custom_fields = created_lead.get('custom_fields_values', [])
                print(f"\n📋 Campos customizados encontrados: {len(custom_fields)}")
                
                for field in custom_fields:
                    field_name = field.get('field_name', 'N/A')
                    field_values = field.get('values', [])
                    if field_values:
                        field_value = field_values[0].get('value', 'N/A')
                        print(f"  📝 {field_name}: {field_value}")
                        
                        # Verificar especificamente o campo WhatsApp
                        if 'whatsapp' in field_name.lower() or 'phone' in field_name.lower():
                            if field_value == test_lead_data["phone"]:
                                print(f"  ✅ Campo {field_name} configurado corretamente!")
                            else:
                                print(f"  ⚠️ Campo {field_name} com valor inesperado: {field_value}")
                
                print("\n🧪 Testando atualização do lead...")
                update_data = {
                    "name": "Teste KommoCRM Updated",
                    "phone": "5511999888777",  # Mesmo telefone
                    "bill_value": 350.0
                }
                
                update_result = await crm_service.update_lead(str(lead_id), update_data)
                
                if update_result.get("success"):
                    print("✅ Lead atualizado com sucesso!")
                else:
                    print(f"❌ Falha ao atualizar lead: {update_result}")
                    
            else:
                print("❌ Lead não encontrado após criação")
                
        else:
            print(f"❌ Falha ao criar lead: {result}")
            
    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)
    print("🏁 Teste de integração concluído")

if __name__ == "__main__":
    asyncio.run(test_kommo_integration())