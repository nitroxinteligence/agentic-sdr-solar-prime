#!/usr/bin/env python3
"""
Utilitários para limpeza de dados de teste
Garante estado limpo antes de executar testes
"""

import asyncio
from datetime import datetime
from app.integrations.supabase_client import supabase_client
from app.utils.logger import emoji_logger

async def clean_test_phone(phone: str):
    """
    Remove TODOS os dados de teste para um telefone específico
    
    Args:
        phone: Número de telefone para limpar
    """
    emoji_logger.system_event(f"🧹 Limpando dados de teste para {phone}...")
    
    try:
        # 1. Buscar lead pelo telefone
        lead = await supabase_client.get_lead_by_phone(phone)
        
        if lead:
            lead_id = lead['id']
            emoji_logger.system_event(f"📋 Lead encontrado: {lead_id}")
            
            # 2. Buscar todas as conversas do lead
            conversations_result = supabase_client.client.table('conversations').select("id").eq(
                'lead_id', lead_id
            ).execute()
            
            if conversations_result.data:
                emoji_logger.system_event(f"💬 {len(conversations_result.data)} conversas encontradas")
                
                # 3. Deletar mensagens de cada conversa
                for conv in conversations_result.data:
                    conv_id = conv['id']
                    
                    # Deletar mensagens
                    messages_result = supabase_client.client.table('messages').delete().eq(
                        'conversation_id', conv_id
                    ).execute()
                    
                    emoji_logger.system_event(f"  ✅ Mensagens deletadas da conversa {conv_id}")
                
                # 4. Deletar conversas
                conv_result = supabase_client.client.table('conversations').delete().eq(
                    'lead_id', lead_id
                ).execute()
                
                emoji_logger.system_event(f"✅ {len(conversations_result.data)} conversas deletadas")
            
            # 5. Resetar campos do lead para estado inicial
            update_data = {
                "name": None,
                "email": None,
                "bill_value": None,
                "chosen_flow": None,
                "qualification_score": 0,
                "current_stage": "INITIAL_CONTACT",
                "document": None,
                "property_type": None,
                "address": None,
                "consumption_kwh": None,
                "qualification_status": "PENDING",
                "is_decision_maker": None,
                "has_solar_system": None,
                "wants_new_solar_system": None,
                "has_active_contract": None,
                "contract_end_date": None,
                "solution_interest": None,
                "google_event_id": None,
                "google_event_link": None,
                "meeting_scheduled_at": None,
                "meeting_type": "initial_meeting",
                "meeting_status": "scheduled",
                "kommo_lead_id": None,
                "updated_at": datetime.now().isoformat()
            }
            
            result = supabase_client.client.table('leads').update(update_data).eq(
                'id', lead_id
            ).execute()
            
            if result.data:
                emoji_logger.system_event("✅ Lead resetado para estado inicial")
            
            # 6. Deletar follow-ups se houver
            followup_result = supabase_client.client.table('follow_ups').delete().eq(
                'phone_number', phone
            ).execute()
            
            emoji_logger.system_event("✅ Follow-ups deletados")
            
            # 7. Verificar limpeza
            # Verificar mensagens órfãs
            orphan_messages = supabase_client.client.table('messages').select("count").eq(
                'conversation_id', None
            ).execute()
            
            emoji_logger.system_success(
                f"🎉 Limpeza completa para {phone}",
                details={
                    "lead_resetado": True,
                    "conversas_deletadas": len(conversations_result.data) if conversations_result.data else 0,
                    "estado": "limpo"
                }
            )
            
        else:
            emoji_logger.system_warning(f"⚠️ Nenhum lead encontrado para {phone}")
            
    except Exception as e:
        emoji_logger.system_error("Cleanup", error=f"Erro na limpeza: {e}")
        raise

async def ensure_clean_state(phone: str):
    """
    Garante que o telefone está em estado limpo antes do teste
    
    Args:
        phone: Número de telefone
        
    Returns:
        True se limpeza foi bem sucedida
    """
    try:
        # Limpar dados existentes
        await clean_test_phone(phone)
        
        # Verificar se está limpo
        lead = await supabase_client.get_lead_by_phone(phone)
        
        if lead:
            # Verificar se o lead está no estado inicial
            is_clean = (
                lead.get('name') is None and
                lead.get('bill_value') is None and
                lead.get('chosen_flow') is None and
                lead.get('qualification_score', 0) == 0 and
                lead.get('current_stage') == 'INITIAL_CONTACT'
            )
            
            if is_clean:
                emoji_logger.system_success(f"✅ {phone} está em estado limpo")
                return True
            else:
                emoji_logger.system_warning(f"⚠️ {phone} não está completamente limpo")
                return False
        else:
            # Se não existe lead, está limpo
            emoji_logger.system_success(f"✅ {phone} está limpo (sem lead)")
            return True
            
    except Exception as e:
        emoji_logger.system_error("Cleanup", error=f"Erro ao verificar estado: {e}")
        return False

async def get_test_stats(phone: str):
    """
    Obtém estatísticas de teste para um telefone
    
    Args:
        phone: Número de telefone
        
    Returns:
        Dicionário com estatísticas
    """
    stats = {
        "lead_exists": False,
        "lead_id": None,
        "lead_name": None,
        "chosen_flow": None,
        "conversations_count": 0,
        "messages_count": 0,
        "followups_count": 0
    }
    
    try:
        # Buscar lead
        lead = await supabase_client.get_lead_by_phone(phone)
        
        if lead:
            stats["lead_exists"] = True
            stats["lead_id"] = lead['id']
            stats["lead_name"] = lead.get('name')
            stats["chosen_flow"] = lead.get('chosen_flow')
            
            # Contar conversas
            conv_result = supabase_client.client.table('conversations').select(
                "id", count="exact"
            ).eq('lead_id', lead['id']).execute()
            
            stats["conversations_count"] = conv_result.count if conv_result else 0
            
            # Contar mensagens (se houver conversas)
            if conv_result.data:
                total_messages = 0
                for conv in conv_result.data:
                    msg_result = supabase_client.client.table('messages').select(
                        "id", count="exact"
                    ).eq('conversation_id', conv['id']).execute()
                    
                    if msg_result:
                        total_messages += msg_result.count
                
                stats["messages_count"] = total_messages
            
            # Contar follow-ups
            followup_result = supabase_client.client.table('follow_ups').select(
                "id", count="exact"
            ).eq('phone_number', phone).execute()
            
            stats["followups_count"] = followup_result.count if followup_result else 0
            
    except Exception as e:
        emoji_logger.system_error("Stats", error=f"Erro ao obter stats: {e}")
    
    return stats

def print_test_stats(stats: dict):
    """
    Imprime estatísticas de teste formatadas
    
    Args:
        stats: Dicionário de estatísticas
    """
    print("\n📊 ESTATÍSTICAS DO TESTE:")
    print("-" * 40)
    print(f"  Lead existe: {'✅' if stats['lead_exists'] else '❌'}")
    if stats['lead_exists']:
        print(f"  Lead ID: {stats['lead_id']}")
        print(f"  Nome: {stats['lead_name'] or '(não definido)'}")
        print(f"  Fluxo escolhido: {stats['chosen_flow'] or '(não definido)'}")
    print(f"  Conversas: {stats['conversations_count']}")
    print(f"  Mensagens: {stats['messages_count']}")
    print(f"  Follow-ups: {stats['followups_count']}")
    print("-" * 40)

# Teste standalone
if __name__ == "__main__":
    async def test_cleanup():
        phone = "5511999999999"
        
        print("=" * 80)
        print("🧪 TESTE DE LIMPEZA DE DADOS")
        print("=" * 80)
        
        # Obter estado antes
        print("\n📊 ESTADO ANTES DA LIMPEZA:")
        stats_before = await get_test_stats(phone)
        print_test_stats(stats_before)
        
        # Limpar
        print("\n🧹 EXECUTANDO LIMPEZA...")
        await ensure_clean_state(phone)
        
        # Obter estado depois
        print("\n📊 ESTADO APÓS LIMPEZA:")
        stats_after = await get_test_stats(phone)
        print_test_stats(stats_after)
        
        # Verificar sucesso
        if stats_after["messages_count"] == 0 and stats_after["conversations_count"] == 0:
            print("\n✅ LIMPEZA BEM SUCEDIDA!")
        else:
            print("\n❌ LIMPEZA INCOMPLETA!")
    
    asyncio.run(test_cleanup())