#!/usr/bin/env python3
"""
Teste das correções de erros identificados nos logs
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils.logger import EmojiLogger
from app.api.webhooks import process_contacts_update

def test_emoji_logger_methods():
    """Testa se todos os métodos do EmojiLogger estão funcionando"""
    print("\n=== TESTE EMOJI LOGGER ===")
    
    # Testa método que estava causando erro
    try:
        EmojiLogger.conversation_event("Teste de conversação")
        print("✅ conversation_event funcionando")
    except AttributeError as e:
        print(f"❌ Erro em conversation_event: {e}")
        return False
    
    # Testa outros métodos importantes
    try:
        EmojiLogger.system_warning("Teste de warning")
        EmojiLogger.system_debug("Teste de debug")
        EmojiLogger.system_success("Teste de sucesso")
        print("✅ Métodos básicos funcionando")
    except Exception as e:
        print(f"❌ Erro nos métodos básicos: {e}")
        return False
    
    return True

async def test_contacts_update_processing():
    """Testa o processamento de CONTACTS_UPDATE com diferentes cenários"""
    print("\n=== TESTE CONTACTS_UPDATE ===")
    
    # Cenário 1: Dados válidos
    valid_data = {
        'data': {
            'id': '558182986181@c.us',
            'pushName': 'Mateus M'
        }
    }
    
    # Cenário 2: Telefone vazio (deve gerar warning específico)
    empty_phone_data = {
        'data': {
            'id': '',
            'pushName': 'Mateus M'
        }
    }
    
    # Cenário 3: pushName vazio (deve gerar warning específico)
    empty_pushname_data = {
        'data': {
            'id': '558182986181@c.us',
            'pushName': ''
        }
    }
    
    # Cenário 4: Ambos vazios
    both_empty_data = {
        'data': {
            'id': '',
            'pushName': ''
        }
    }
    
    test_cases = [
        ("Dados válidos", valid_data),
        ("Telefone vazio", empty_phone_data),
        ("PushName vazio", empty_pushname_data),
        ("Ambos vazios", both_empty_data)
    ]
    
    for test_name, test_data in test_cases:
        print(f"\n--- Testando: {test_name} ---")
        try:
            await process_contacts_update(test_data)
            print(f"✅ {test_name} processado sem erro")
        except Exception as e:
            print(f"❌ Erro em {test_name}: {e}")
            return False
    
    return True

async def main():
    """Executa todos os testes"""
    print("🧪 INICIANDO TESTES DE CORREÇÃO DE ERROS")
    
    # Teste 1: EmojiLogger
    emoji_test = test_emoji_logger_methods()
    
    # Teste 2: CONTACTS_UPDATE
    contacts_test = await test_contacts_update_processing()
    
    # Resultado final
    print("\n" + "="*50)
    if emoji_test and contacts_test:
        print("🎉 TODOS OS TESTES PASSARAM!")
        print("✅ Correção do EmojiLogger: OK")
        print("✅ Melhoria do CONTACTS_UPDATE: OK")
        return True
    else:
        print("❌ ALGUNS TESTES FALHARAM")
        if not emoji_test:
            print("❌ Problema no EmojiLogger")
        if not contacts_test:
            print("❌ Problema no CONTACTS_UPDATE")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)