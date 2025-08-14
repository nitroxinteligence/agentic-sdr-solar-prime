#!/usr/bin/env python
"""
Diagnóstico da estrutura da tabela follow_ups
Verifica campos e constraints reais no banco
"""

from app.database.supabase_client import SupabaseClient
from app.utils.logger import emoji_logger
import json

def diagnose_table():
    """
    Diagnostica a estrutura real da tabela follow_ups
    """
    emoji_logger.system_info("🔍 DIAGNÓSTICO DA TABELA FOLLOW_UPS")
    emoji_logger.system_info("=" * 60)
    
    db = SupabaseClient()
    
    # 1. Tentar inserir um registro de teste para ver os campos reais
    emoji_logger.system_info("\n1️⃣ Testando inserção com diferentes formatos...")
    
    # Primeiro, criar um lead de teste
    test_phone = "5511888888888"
    lead_data = {
        'phone_number': test_phone,
        'name': 'Teste Diagnóstico',
        'current_stage': 'INITIAL_CONTACT'
    }
    
    lead_result = db.client.table('leads').select("*").eq('phone_number', test_phone).execute()
    
    if not lead_result.data:
        create_result = db.client.table('leads').insert(lead_data).execute()
        lead_id = create_result.data[0]['id'] if create_result.data else None
    else:
        lead_id = lead_result.data[0]['id']
    
    if not lead_id:
        emoji_logger.system_error("Test", "Não foi possível criar lead de teste")
        return
    
    emoji_logger.system_info(f"Lead de teste: {lead_id}")
    
    # Testar diferentes formatos
    test_configs = [
        {
            'name': 'Formato 1: type (minúsculo)',
            'data': {
                'lead_id': lead_id,
                'type': 'reengagement',
                'scheduled_at': '2025-08-14T20:00:00',
                'status': 'pending',
                'phone_number': test_phone
            }
        },
        {
            'name': 'Formato 2: type (maiúsculo)',
            'data': {
                'lead_id': lead_id,
                'type': 'IMMEDIATE_REENGAGEMENT',
                'scheduled_at': '2025-08-14T20:00:00',
                'status': 'pending',
                'phone_number': test_phone
            }
        },
        {
            'name': 'Formato 3: follow_up_type',
            'data': {
                'lead_id': lead_id,
                'follow_up_type': 'IMMEDIATE_REENGAGEMENT',
                'scheduled_at': '2025-08-14T20:00:00',
                'status': 'pending',
                'phone_number': test_phone
            }
        },
        {
            'name': 'Formato 4: Ambos os campos',
            'data': {
                'lead_id': lead_id,
                'type': 'CUSTOM',
                'follow_up_type': 'IMMEDIATE_REENGAGEMENT',
                'scheduled_at': '2025-08-14T20:00:00',
                'status': 'pending',
                'phone_number': test_phone
            }
        }
    ]
    
    for config in test_configs:
        emoji_logger.system_info(f"\n🧪 Testando: {config['name']}")
        
        try:
            result = db.client.table('follow_ups').insert(config['data']).execute()
            
            if result.data:
                emoji_logger.system_success(f"✅ SUCESSO! Formato aceito")
                emoji_logger.system_info("Campos retornados:")
                
                # Mostrar estrutura
                for key in result.data[0].keys():
                    value = result.data[0][key]
                    if key in ['type', 'follow_up_type']:
                        emoji_logger.system_info(f"  🔑 {key}: {value}")
                
                # Limpar registro de teste
                db.client.table('follow_ups').delete().eq('id', result.data[0]['id']).execute()
                
                # Se funcionou, sair do loop
                break
                
        except Exception as e:
            error_msg = str(e)
            if 'violates check constraint' in error_msg:
                emoji_logger.system_warning(f"❌ Constraint violation: {error_msg[:100]}...")
            elif 'null value' in error_msg:
                emoji_logger.system_warning(f"❌ Campo null não permitido: {error_msg[:100]}...")
            else:
                emoji_logger.system_warning(f"❌ Erro: {error_msg[:100]}...")
    
    # 2. Buscar um follow-up existente para ver a estrutura
    emoji_logger.system_info("\n2️⃣ Buscando follow-ups existentes para análise...")
    
    existing = db.client.table('follow_ups').select("*").limit(1).execute()
    
    if existing.data:
        emoji_logger.system_info("📋 Estrutura de follow-up existente:")
        
        sample = existing.data[0]
        for key in ['id', 'lead_id', 'type', 'follow_up_type', 'status', 'phone_number']:
            if key in sample:
                emoji_logger.system_info(f"  • {key}: {sample[key]}")
    else:
        emoji_logger.system_info("Nenhum follow-up existente encontrado")
    
    # Limpar lead de teste
    db.client.table('leads').delete().eq('id', lead_id).execute()
    
    emoji_logger.system_info("\n" + "=" * 60)
    emoji_logger.system_info("📊 CONCLUSÃO DO DIAGNÓSTICO")
    emoji_logger.system_info("Verifique os resultados acima para determinar o formato correto")

if __name__ == "__main__":
    diagnose_table()