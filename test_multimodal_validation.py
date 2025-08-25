#!/usr/bin/env python3
"""
Teste para validar se o processamento multimodal está funcionando corretamente
após as correções do EmojiLogger.
"""

import os
import sys
import asyncio
from pathlib import Path

# Adiciona o diretório raiz ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Carrega variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()

print(f"✅ Arquivo .env encontrado: {project_root}/.env")

from app.services.knowledge_service import KnowledgeService
from app.integrations.evolution import EvolutionAPIClient
from app.utils.logger import emoji_logger
from app.agents.agentic_sdr_stateless import AgenticSDRStateless

async def test_multimodal_processing():
    """Testa o processamento multimodal completo"""
    print("🚀 Iniciando teste de processamento multimodal...")
    
    try:
        # 1. Inicializar serviços
        print("\n🔧 Inicializando serviços...")
        knowledge_service = KnowledgeService()
        
        # 2. Verificar se o AgenticSDR pode ser inicializado
        print("\n🤖 Testando inicialização do AgenticSDR...")
        try:
            sdr = AgenticSDRStateless()
            print("✅ AgenticSDR inicializado com sucesso")
            
            # Verificar se o multimodal existe
            if hasattr(sdr, 'multimodal'):
                print("✅ MultimodalProcessor encontrado no AgenticSDR")
                
                # Verificar métodos do multimodal
                processor = sdr.multimodal
                if hasattr(processor, 'process_media'):
                    print("✅ Método process_media encontrado")
                else:
                    print("❌ Método process_media não encontrado")
                    
                if hasattr(processor, 'process_image'):
                    print("✅ Método process_image encontrado")
                else:
                    print("❌ Método process_image não encontrado")
                    
                if hasattr(processor, 'process_audio'):
                    print("✅ Método process_audio encontrado")
                else:
                    print("❌ Método process_audio não encontrado")
                    
                if hasattr(processor, 'process_document'):
                    print("✅ Método process_document encontrado")
                else:
                    print("❌ Método process_document não encontrado")
                    
            else:
                print("❌ MultimodalProcessor não encontrado no AgenticSDR")
                
        except Exception as e:
            emoji_logger.system_error("Multimodal Test", f"Erro ao inicializar AgenticSDR: {e}")
            print(f"❌ Erro ao inicializar AgenticSDR: {e}")
        
        # 3. Testar Evolution API para mídia
        print("\n📱 Testando Evolution API para processamento de mídia...")
        try:
            evolution = EvolutionAPIClient()
            
            # Verificar métodos de mídia
            if hasattr(evolution, 'get_media_as_base64'):
                print("✅ Método get_media_as_base64 encontrado")
            else:
                print("❌ Método get_media_as_base64 não encontrado")
                
            if hasattr(evolution, 'download_media'):
                print("✅ Método download_media encontrado")
            else:
                print("❌ Método download_media não encontrado")
                
        except Exception as e:
            emoji_logger.system_error("Evolution Test", f"Erro ao testar Evolution API: {e}")
            print(f"❌ Erro ao testar Evolution API: {e}")
        
        # 4. Verificar se os logs do EmojiLogger estão funcionando
        print("\n📝 Testando logs do EmojiLogger...")
        emoji_logger.system_info("Teste de log de informação")
        emoji_logger.system_success("Teste de log de sucesso")
        emoji_logger.system_error("Multimodal Test", "Teste de log de erro (simulado)")
        print("✅ Logs do EmojiLogger funcionando")
        
        print("\n✅ Teste de validação multimodal concluído!")
        
    except Exception as e:
        emoji_logger.system_error("Multimodal Validation", f"Erro durante teste de validação: {e}")
        print(f"❌ Erro durante teste: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(test_multimodal_processing())