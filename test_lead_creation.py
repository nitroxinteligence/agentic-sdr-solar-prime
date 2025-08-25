#!/usr/bin/env python3
"""
Teste para validar a correção de criação de leads sem nome.
Este script simula o cenário onde uma mensagem "oi?" deve criar um lead básico.
"""

import asyncio
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.integrations.supabase_client import supabase_client

async def test_lead_creation_without_name():
    """
    Testa se um lead é criado quando não há nome extraído da mensagem.
    """
    print("🧪 Iniciando teste de criação de lead sem nome...")
    
    # Dados de teste
    test_phone = "558182986181"
    test_message = "oi?"
    
    # Limpar lead existente se houver (para teste limpo)
    try:
        existing_lead = await supabase_client.get_lead_by_phone(test_phone)
        if existing_lead:
            print(f"⚠️  Lead existente encontrado: {existing_lead.get('id')}")
            print("   Para teste limpo, considere usar outro número ou limpar manualmente")
    except Exception as e:
        print(f"❌ Erro ao verificar lead existente: {e}")
        return False
    
    # Simular execution_context como seria no webhook
    execution_context = {
        "phone": test_phone,
        "lead_info": {},  # Lead vazio, como seria para nova conversa
        "conversation_id": "test-conversation-id",
        "conversation_history": [],
        "media": None,
        "timestamp": "2025-01-27T14:32:47.987Z"
    }
    
    try:
        # Inicializar agente
        agent = AgenticSDRStateless()
        await agent.initialize()
        
        print(f"📱 Processando mensagem: '{test_message}' do número: {test_phone}")
        
        # Processar mensagem
        response, updated_lead_info = await agent.process_message(
            message=test_message,
            execution_context=execution_context
        )
        
        # O process_message retorna (response, lead_info) diretamente
        
        if updated_lead_info.get("id"):
            print(f"✅ SUCESSO! Lead criado com ID: {updated_lead_info.get('id')}")
            print(f"   Nome: {updated_lead_info.get('name', 'Não definido')}")
            print(f"   Telefone: {updated_lead_info.get('phone_number')}")
            print(f"   Kommo ID: {updated_lead_info.get('kommo_lead_id', 'Não sincronizado')}")
            
            # Verificar no banco
            db_lead = await supabase_client.get_lead_by_phone(test_phone)
            if db_lead:
                print(f"✅ Lead confirmado no Supabase: {db_lead.get('id')}")
                return True
            else:
                print("❌ Lead não encontrado no Supabase")
                return False
        else:
            print("❌ FALHA! Lead não foi criado")
            print(f"   Lead info retornado: {updated_lead_info}")
            return False
            
    except Exception as e:
        print(f"❌ Erro durante teste: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """
    Função principal do teste.
    """
    print("🚀 Teste de Criação de Leads - Correção Implementada")
    print("=" * 60)
    
    success = await test_lead_creation_without_name()
    
    print("=" * 60)
    if success:
        print("🎉 TESTE PASSOU! A correção está funcionando corretamente.")
        print("   Leads agora são criados mesmo sem nome extraído da mensagem.")
    else:
        print("💥 TESTE FALHOU! Verifique a implementação.")
        print("   A correção pode não ter sido aplicada corretamente.")
    
    return success

if __name__ == "__main__":
    result = asyncio.run(main())
    sys.exit(0 if result else 1)