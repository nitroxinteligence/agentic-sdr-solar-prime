#!/usr/bin/env python
"""
Teste SIMPLES do OCR para PDFs no MultimodalProcessor
Verifica se a solução implementada funciona corretamente
"""

import asyncio
import base64
from pathlib import Path
from app.core.multimodal_processor import MultimodalProcessor
from app.utils.logger import emoji_logger

async def test_multimodal_ocr():
    """
    Testa o OCR com diferentes tipos de PDFs
    """
    emoji_logger.system_info("🧪 Iniciando teste do MultimodalProcessor com OCR")
    
    # Inicializar processor
    processor = MultimodalProcessor()
    processor.initialize()
    
    # 1. Teste com texto simulado (base64 de um PDF simples)
    # Este é um PDF de teste muito simples apenas para verificar se o código funciona
    test_pdf_base64 = "JVBERi0xLjQKJeLjz9MKNCAwIG9iago8PC9MZW5ndGggNzg+PgpzdHJlYW0KeGDMSc/LSgvSACA="
    
    emoji_logger.system_info("📄 Testando com PDF de exemplo...")
    
    result = await processor.process_document(test_pdf_base64)
    
    if result["success"]:
        emoji_logger.system_success("✅ PDF processado com sucesso!")
        emoji_logger.system_info(f"📝 Tipo: {result['metadata'].get('doc_type', 'unknown')}")
        emoji_logger.system_info(f"🔤 Caracteres extraídos: {result['metadata'].get('char_count', 0)}")
        emoji_logger.system_info(f"📸 OCR usado: {result['metadata'].get('ocr_used', False)}")
        
        if result.get("analysis", {}).get("bill_value"):
            emoji_logger.system_success(
                f"💰 Valor detectado: R$ {result['analysis']['bill_value']:.2f}"
            )
        
        # Mostrar primeiros 200 caracteres do texto extraído
        text_preview = result.get("text", "")[:200]
        if text_preview:
            emoji_logger.system_info(f"📖 Preview do texto: {text_preview}...")
    else:
        emoji_logger.system_error(f"❌ Falha ao processar PDF: {result.get('message', 'Erro desconhecido')}")
    
    emoji_logger.system_info("=" * 60)
    
    # 2. Teste com validação de detecção de valor
    emoji_logger.system_info("💰 Testando detecção de valores em texto...")
    
    # Simular texto extraído de uma conta de luz
    sample_text = """
    CONTA DE ENERGIA ELÉTRICA
    
    Valor a Pagar: R$ 359,10
    Vencimento: 15/01/2025
    Consumo: 450 kWh
    """
    
    # Usar método interno para análise
    analysis = processor._analyze_document_content(sample_text)
    
    emoji_logger.system_info(f"📊 Análise do documento:")
    emoji_logger.system_info(f"  - É conta? {analysis['is_bill']}")
    emoji_logger.system_info(f"  - Tipo: {analysis['document_type']}")
    if analysis['bill_value']:
        emoji_logger.system_success(f"  - Valor detectado: R$ {analysis['bill_value']:.2f}")
    
    emoji_logger.system_info("=" * 60)
    emoji_logger.system_success("🎉 Teste concluído!")

if __name__ == "__main__":
    asyncio.run(test_multimodal_ocr())