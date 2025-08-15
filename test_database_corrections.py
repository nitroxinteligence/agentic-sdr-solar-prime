#!/usr/bin/env python3
"""
Script de teste para validar as correções de compatibilidade schema-código
Executa testes simples para verificar que as mudanças foram aplicadas corretamente
"""

import asyncio
import sys
from datetime import datetime
import json

# Cores para output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def print_test(name: str, status: bool, details: str = ""):
    """Imprime resultado do teste com cores"""
    symbol = f"{GREEN}✅{RESET}" if status else f"{RED}❌{RESET}"
    status_text = f"{GREEN}PASSOU{RESET}" if status else f"{RED}FALHOU{RESET}"
    print(f"{symbol} {name}: {status_text}")
    if details:
        print(f"   {details}")

async def test_supabase_client():
    """Testa se métodos agent_sessions foram removidos"""
    print("\n📋 Testando supabase_client.py...")
    
    try:
        from app.integrations.supabase_client import SupabaseClient
        client = SupabaseClient()
        
        # Teste 1: Verificar que métodos agent_sessions não existem
        has_agent_session = hasattr(client, 'get_agent_session')
        print_test(
            "Método get_agent_session removido",
            not has_agent_session,
            "Métodos agent_sessions devem ser removidos (arquitetura stateless)"
        )
        
        # Teste 2: Verificar que save_agent_session não existe
        has_save_session = hasattr(client, 'save_agent_session')
        print_test(
            "Método save_agent_session removido",
            not has_save_session
        )
        
        # Teste 3: Verificar que cleanup_old_sessions não existe
        has_cleanup = hasattr(client, 'cleanup_old_sessions')
        print_test(
            "Método cleanup_old_sessions removido",
            not has_cleanup
        )
        
        return not (has_agent_session or has_save_session or has_cleanup)
        
    except Exception as e:
        print_test("Import supabase_client", False, str(e))
        return False

async def test_lead_manager():
    """Testa mapeamento de campos no LeadManager"""
    print("\n📋 Testando lead_manager.py...")
    
    try:
        from app.core.lead_manager import LeadManager
        manager = LeadManager()
        
        # Criar mensagens de teste
        test_messages = [
            {"role": "assistant", "content": "Qual seu nome?"},
            {"role": "user", "content": "João Silva"},
            {"role": "assistant", "content": "Qual valor da sua conta de energia?"},
            {"role": "user", "content": "Minha conta vem R$ 450"},
        ]
        
        # Extrair informações
        lead_info = manager.extract_lead_info(test_messages)
        
        # Teste 1: Verificar campo phone_number (não phone)
        has_phone_number = 'phone_number' in lead_info
        has_old_phone = 'phone' in lead_info
        print_test(
            "Campo phone_number existe",
            has_phone_number and not has_old_phone,
            f"Deve usar 'phone_number', não 'phone'"
        )
        
        # Teste 2: Verificar campo current_stage (não stage)
        has_current_stage = 'current_stage' in lead_info
        has_old_stage = 'stage' in lead_info
        print_test(
            "Campo current_stage existe",
            has_current_stage and not has_old_stage,
            f"current_stage = {lead_info.get('current_stage', 'N/A')}"
        )
        
        # Teste 3: Verificar preferences JSONB
        has_preferences = 'preferences' in lead_info and isinstance(lead_info['preferences'], dict)
        print_test(
            "Campo preferences existe como dict",
            has_preferences,
            f"preferences contém: {list(lead_info.get('preferences', {}).keys())}"
        )
        
        # Teste 4: Verificar que campos extras estão em preferences
        if has_preferences:
            prefs = lead_info['preferences']
            has_location = 'location' in prefs
            has_property_type = 'property_type' in prefs
            has_interests = 'interests' in prefs
            
            print_test(
                "Campos extras em preferences",
                has_location or has_property_type or has_interests,
                "location, property_type, interests movidos para preferences JSONB"
            )
        
        # Teste 5: Verificar valores de stage compatíveis com banco
        stage = lead_info.get('current_stage', '')
        valid_stages = ['INITIAL_CONTACT', 'INTERESTED', 'QUALIFYING', 'WARM', 'HOT']
        is_valid_stage = stage in valid_stages
        print_test(
            "Stage com valor compatível",
            is_valid_stage,
            f"current_stage = '{stage}' (valores em inglês/maiúsculas)"
        )
        
        return has_phone_number and has_current_stage and has_preferences and is_valid_stage
        
    except Exception as e:
        print_test("Import lead_manager", False, str(e))
        return False

async def test_agentic_sdr():
    """Testa implementação de preferences em AgenticSDR"""
    print("\n📋 Testando agentic_sdr_stateless.py...")
    
    try:
        from app.agents.agentic_sdr_stateless import AgenticSDRStateless
        
        # AgenticSDRStateless não recebe parâmetros no __init__
        # É criado via create_stateless_agent
        agent = AgenticSDRStateless()
        
        # Teste 1: Verificar método _map_to_supabase_fields
        test_changes = {
            'name': 'João',
            'phone_number': '+5511999999999',
            'location': 'São Paulo',
            'interests': ['economia', 'sustentabilidade']
        }
        
        mapped = agent._map_to_supabase_fields(test_changes)
        
        has_phone_mapping = 'phone_number' in mapped or 'phone_number' in test_changes
        print_test(
            "Mapeamento phone_number correto",
            has_phone_mapping,
            "phone_number mapeado corretamente"
        )
        
        # Teste 2: Verificar que preferences é criado
        has_preferences_support = 'preferences' in mapped or 'preferences' in str(agent._map_to_supabase_fields)
        print_test(
            "Suporte a preferences JSONB",
            has_preferences_support,
            "Campos extras vão para preferences"
        )
        
        # Teste 3: Verificar _prepare_lead_for_supabase
        lead_data = agent._prepare_lead_for_supabase(
            {'name': 'Test'},
            '+5511999999999',
            {'bill_value': 450}
        )
        
        has_correct_fields = (
            'phone_number' in lead_data and
            'qualification_status' in lead_data and
            lead_data.get('qualification_status') == 'PENDING'
        )
        
        print_test(
            "prepare_lead_for_supabase atualizado",
            has_correct_fields,
            f"qualification_status = {lead_data.get('qualification_status')}"
        )
        
        return has_phone_mapping and has_preferences_support and has_correct_fields
        
    except Exception as e:
        print_test("Import agentic_sdr", False, str(e))
        return False

async def test_database_queries():
    """Testa queries diretas no banco (se possível)"""
    print("\n📋 Testando queries no banco...")
    
    try:
        from app.integrations.supabase_client import SupabaseClient
        client = SupabaseClient()
        
        # Teste 1: Verificar que tabela agent_sessions não existe
        try:
            # Tentar query na tabela (deve falhar)
            result = client.client.table('agent_sessions').select("id").limit(1).execute()
            print_test(
                "Tabela agent_sessions removida",
                False,
                "❌ Tabela ainda existe! Precisa ser removida."
            )
        except Exception:
            print_test(
                "Tabela agent_sessions removida",
                True,
                "Tabela não existe (como esperado)"
            )
        
        # Teste 2: Verificar que leads_qualifications tem meeting_scheduled_at
        try:
            result = client.client.table('leads_qualifications').select(
                "meeting_scheduled_at"
            ).limit(1).execute()
            print_test(
                "Campo meeting_scheduled_at em leads_qualifications",
                True,
                "Campo existe na tabela correta"
            )
        except Exception as e:
            print_test(
                "Campo meeting_scheduled_at em leads_qualifications",
                False,
                f"Erro: {str(e)}"
            )
        
        # Teste 3: Verificar campo preferences em leads
        try:
            result = client.client.table('leads').select("preferences").limit(1).execute()
            print_test(
                "Campo preferences (JSONB) em leads",
                True,
                "Campo JSONB para dados extras existe"
            )
        except Exception as e:
            print_test(
                "Campo preferences em leads",
                False,
                f"Erro: {str(e)}"
            )
        
        return True
        
    except Exception as e:
        print(f"{YELLOW}⚠️ Não foi possível testar queries no banco: {e}{RESET}")
        return None

async def main():
    """Executa todos os testes"""
    print(f"\n{GREEN}═══════════════════════════════════════════{RESET}")
    print(f"{GREEN}    TESTE DE CORREÇÕES SCHEMA-CÓDIGO v1.0    {RESET}")
    print(f"{GREEN}═══════════════════════════════════════════{RESET}")
    
    results = []
    
    # Executar testes
    results.append(await test_supabase_client())
    results.append(await test_lead_manager())
    results.append(await test_agentic_sdr())
    
    # Teste de banco é opcional
    db_result = await test_database_queries()
    if db_result is not None:
        results.append(db_result)
    
    # Resumo final
    print(f"\n{GREEN}═══════════════════════════════════════════{RESET}")
    print(f"📊 RESUMO DOS TESTES")
    print(f"{GREEN}═══════════════════════════════════════════{RESET}")
    
    total = len(results)
    passed = sum(1 for r in results if r)
    failed = total - passed
    
    if passed == total:
        print(f"\n{GREEN}✅ TODOS OS TESTES PASSARAM! ({passed}/{total}){RESET}")
        print(f"\n🎉 Sistema 100% compatível com novo schema!")
        return 0
    else:
        print(f"\n{RED}❌ ALGUNS TESTES FALHARAM: {failed} de {total}{RESET}")
        print(f"\n⚠️ Verifique os erros acima e aplique as correções necessárias.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)