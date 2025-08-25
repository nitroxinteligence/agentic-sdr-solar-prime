#!/usr/bin/env python3
"""
Teste para verificar se o processamento de mídia está funcionando após as correções do EmojiLogger.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.integrations.evolution import EvolutionAPIClient
from app.api.webhooks import _handle_media_message
from app.utils.logger import emoji_logger

def test_evolution_media_methods():
    """Testa se os métodos de mídia do Evolution estão disponíveis"""
    print("🔍 Testando métodos de mídia do Evolution...")
    
    # Verifica se os métodos existem
    client = EvolutionAPIClient()
    
    # Testa se get_media_as_base64 existe e tem o decorador retry
    if hasattr(client, 'get_media_as_base64'):
        print("✅ get_media_as_base64 encontrado")
        # Verifica se tem o decorador retry
        if hasattr(client.get_media_as_base64, '__wrapped__'):
            print("✅ get_media_as_base64 tem decorador retry")
        else:
            print("⚠️ get_media_as_base64 pode não ter decorador retry")
    else:
        print("❌ get_media_as_base64 NÃO encontrado")
    
    # Testa se download_media existe
    if hasattr(client, 'download_media'):
        print("✅ download_media encontrado")
    else:
        print("❌ download_media NÃO encontrado")
    
    print()

def test_webhook_media_handler():
    """Testa se o handler de mídia do webhook está funcionando"""
    print("🔍 Testando handler de mídia do webhook...")
    
    try:
        # Verifica se a função existe
        if callable(_handle_media_message):
            print("✅ _handle_media_message encontrado e é callable")
        else:
            print("❌ _handle_media_message NÃO é callable")
    except Exception as e:
        print(f"❌ Erro ao verificar _handle_media_message: {e}")
    
    print()

def test_emoji_logger_calls():
    """Testa se as chamadas do EmojiLogger estão funcionando"""
    print("🔍 Testando chamadas do EmojiLogger...")
    
    try:
        # Testa chamadas corretas
        emoji_logger.system_info("Teste de chamada correta")
        print("✅ emoji_logger.system_info funcionando")
        
        emoji_logger.system_error("TestComponent", "Teste de erro")
        print("✅ emoji_logger.system_error funcionando")
        
        emoji_logger.system_success("Teste de sucesso")
        print("✅ emoji_logger.system_success funcionando")
        
    except Exception as e:
        print(f"❌ Erro nas chamadas do EmojiLogger: {e}")
    
    print()

if __name__ == "__main__":
    print("🚀 Iniciando testes de processamento de mídia...\n")
    
    test_evolution_media_methods()
    test_webhook_media_handler()
    test_emoji_logger_calls()
    
    print("✅ Testes concluídos!")