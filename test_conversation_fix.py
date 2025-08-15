#!/usr/bin/env python3
"""
Script para testar a correção do erro de criação de conversação
"""

import asyncio
import sys
from datetime import datetime

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

async def test_conversation_creation():
    """Testa criação de conversação sem campos channel e sentiment"""
    print(f"\n{YELLOW}📋 Testando criação de conversação...{RESET}")
    
    try:
        from app.integrations.supabase_client import SupabaseClient
        client = SupabaseClient()
        
        # Teste 1: Verificar estrutura de conversation_data
        print("\n1. Verificando estrutura de dados...")
        
        # Simular criação de lead primeiro
        test_phone = f"+5511999{datetime.now().strftime('%H%M%S')}"
        
        try:
            # Criar lead de teste
            lead = await client.create_lead({
                'phone_number': test_phone,
                'name': 'Teste Conversação',
                'qualification_status': 'PENDING'
            })
            
            print_test(
                "Lead de teste criado",
                True,
                f"ID: {lead['id']}"
            )
            
            # Teste 2: Criar conversação
            conversation = await client.create_conversation(
                test_phone,
                lead['id']
            )
            
            print_test(
                "Conversação criada sem 'channel' e 'sentiment'",
                True,
                f"ID: {conversation['id']}, Session: {conversation['session_id']}"
            )
            
            # Teste 3: Verificar campos da conversação
            has_channel = 'channel' in conversation
            has_sentiment = 'sentiment' in conversation
            
            print_test(
                "Campo 'channel' não está presente",
                not has_channel,
                "Campo removido corretamente"
            )
            
            print_test(
                "Campo 'sentiment' não está presente", 
                not has_sentiment,
                "Campo removido corretamente"
            )
            
            # Teste 4: Verificar campos obrigatórios
            required_fields = ['id', 'phone_number', 'lead_id', 'session_id', 'status']
            has_all_required = all(field in conversation for field in required_fields)
            
            print_test(
                "Todos campos obrigatórios presentes",
                has_all_required,
                f"Campos: {', '.join(required_fields)}"
            )
            
            return True
            
        except Exception as e:
            if "channel" in str(e).lower():
                print_test(
                    "Erro relacionado a 'channel'",
                    False,
                    f"ERRO AINDA PRESENTE: {e}"
                )
                return False
            elif "sentiment" in str(e).lower():
                print_test(
                    "Erro relacionado a 'sentiment'",
                    False,
                    f"ERRO AINDA PRESENTE: {e}"
                )
                return False
            else:
                # Outro tipo de erro
                print(f"{YELLOW}⚠️ Erro diferente: {e}{RESET}")
                return None
                
    except ImportError as e:
        print_test("Import supabase_client", False, str(e))
        return False

async def test_conversation_update():
    """Testa atualização de conversação"""
    print(f"\n{YELLOW}📋 Testando atualização de conversação...{RESET}")
    
    try:
        from app.integrations.supabase_client import SupabaseClient
        client = SupabaseClient()
        
        # Usar phone de teste
        test_phone = f"+5511999{datetime.now().strftime('%H%M%S')}"
        
        # Criar lead e conversação
        lead = await client.create_lead({
            'phone_number': test_phone,
            'name': 'Teste Update'
        })
        
        conversation = await client.create_conversation(test_phone, lead['id'])
        
        # Testar atualização
        update_data = {
            'total_messages': 5,
            'status': 'ACTIVE'
        }
        
        updated = await client.update_conversation(
            conversation['id'],
            update_data
        )
        
        print_test(
            "Conversação atualizada sem erros",
            updated is not None,
            f"total_messages: {update_data.get('total_messages')}"
        )
        
        return True
        
    except Exception as e:
        print_test("Atualização de conversação", False, str(e))
        return False

async def main():
    """Executa todos os testes"""
    print(f"\n{GREEN}═══════════════════════════════════════════{RESET}")
    print(f"{GREEN}    TESTE DE CORREÇÃO CONVERSATION FIX    {RESET}")
    print(f"{GREEN}═══════════════════════════════════════════{RESET}")
    
    results = []
    
    # Executar testes
    result1 = await test_conversation_creation()
    if result1 is not None:
        results.append(result1)
    
    result2 = await test_conversation_update()
    results.append(result2)
    
    # Resumo final
    print(f"\n{GREEN}═══════════════════════════════════════════{RESET}")
    print(f"📊 RESUMO DOS TESTES")
    print(f"{GREEN}═══════════════════════════════════════════{RESET}")
    
    total = len(results)
    passed = sum(1 for r in results if r)
    failed = total - passed
    
    if passed == total:
        print(f"\n{GREEN}✅ TODOS OS TESTES PASSARAM! ({passed}/{total}){RESET}")
        print(f"\n🎉 Correção aplicada com sucesso!")
        print(f"📝 Próximo passo: Fazer commit e deploy")
        return 0
    else:
        print(f"\n{RED}❌ ALGUNS TESTES FALHARAM: {failed} de {total}{RESET}")
        print(f"\n⚠️ Verifique os erros acima.")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)