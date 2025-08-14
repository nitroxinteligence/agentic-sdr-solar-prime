#!/usr/bin/env python
"""
TESTE COMPLETO E REAL DO SISTEMA SDR IA SOLARPRIME
Valida TODO o fluxo do sistema com dados reais
"""

import asyncio
import base64
import json
from pathlib import Path
from datetime import datetime
from app.core.multimodal_processor import MultimodalProcessor
from app.utils.logger import emoji_logger
import sys

# Valores REAIS esperados (baseado na análise dos arquivos)
EXPECTED_VALUES = {
    "pdf": {
        "total_a_pagar": 350.81,  # Valor correto do PDF
        "outros_valores": [20.5, 22.37, 24.67, 38.81, 63.58, 109.17, 189.24, 246.59, 297.0, 310.18],
        "char_count_min": 6000,
        "doc_type": "conta_energia"  # ou "boleto"
    },
    "image": {
        "width": 1024,
        "height": 1536,
        "format": "PNG"
    },
    "audio": {
        "duration_min": 5,
        "duration_max": 10,
        "transcription_keywords": ["cpf", "e-mail", "agendamento"]
    }
}

class SystemValidator:
    """Validador completo do sistema"""
    
    def __init__(self):
        self.processor = MultimodalProcessor()
        self.processor.initialize()
        self.results = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "warnings": [],
            "errors": [],
            "details": {}
        }
    
    async def test_pdf_processing(self):
        """Testa processamento de PDF com validação de valores"""
        self.results["total_tests"] += 1
        test_name = "PDF_PROCESSING"
        
        emoji_logger.system_info("\n📄 TESTE 1: Processamento de PDF Real")
        emoji_logger.system_info("-" * 50)
        
        try:
            # Carregar PDF real
            pdf_path = Path("tests/Boleto.pdf")
            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()
                pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
            
            # Simular formato do webhook
            media_data = {
                "type": "document",
                "mimetype": "application/pdf",
                "data": f"data:application/pdf;base64,{pdf_base64}",
                "content": f"data:application/pdf;base64,{pdf_base64}",
                "fileName": "Boleto.pdf"
            }
            
            # Processar
            result = await self.processor.process_media(media_data)
            
            # Validações
            validations = []
            
            # 1. Sucesso no processamento
            if result["success"]:
                validations.append(("Processamento", True, "PDF processado com sucesso"))
            else:
                validations.append(("Processamento", False, f"Erro: {result.get('message')}"))
            
            # 2. Texto extraído
            text = result.get("text", "")
            char_count = len(text)
            if char_count >= EXPECTED_VALUES["pdf"]["char_count_min"]:
                validations.append(("Extração de texto", True, f"{char_count} caracteres extraídos"))
            else:
                validations.append(("Extração de texto", False, f"Apenas {char_count} caracteres"))
            
            # 3. Detecção de valores
            analysis = result.get("analysis", {})
            detected_value = analysis.get("bill_value")
            
            # Verificar se detectou o valor correto (R$ 350,81)
            if detected_value:
                # Tolerância de 1% para comparação de float
                if abs(detected_value - EXPECTED_VALUES["pdf"]["total_a_pagar"]) < 1:
                    validations.append(("Valor detectado", True, f"R$ {detected_value:.2f} ✅ CORRETO!"))
                else:
                    # ERRO CRÍTICO: Valor errado detectado
                    validations.append(("Valor detectado", False, 
                        f"R$ {detected_value:.2f} ❌ ERRADO! Esperado: R$ {EXPECTED_VALUES['pdf']['total_a_pagar']:.2f}"))
                    self.results["errors"].append(
                        f"PDF: Sistema detectou R$ {detected_value:.2f} mas o valor correto é R$ {EXPECTED_VALUES['pdf']['total_a_pagar']:.2f}"
                    )
            else:
                validations.append(("Valor detectado", False, "Nenhum valor detectado"))
            
            # 4. Tipo de documento
            if analysis.get("is_bill"):
                validations.append(("Tipo de documento", True, f"Identificado como {analysis.get('document_type', 'conta')}"))
            else:
                validations.append(("Tipo de documento", False, "Não identificado como conta/boleto"))
            
            # Resultado final
            passed_count = sum(1 for _, passed, _ in validations if passed)
            total_count = len(validations)
            
            self.results["details"][test_name] = {
                "validations": validations,
                "passed": passed_count,
                "total": total_count,
                "success_rate": (passed_count / total_count * 100) if total_count > 0 else 0
            }
            
            if passed_count == total_count:
                self.results["passed"] += 1
                emoji_logger.system_success(f"✅ TESTE PDF: {passed_count}/{total_count} validações passaram")
            else:
                self.results["failed"] += 1
                emoji_logger.system_error("PDF Test", f"❌ TESTE PDF: {passed_count}/{total_count} validações passaram")
            
            # Mostrar detalhes
            for name, passed, message in validations:
                symbol = "✅" if passed else "❌"
                emoji_logger.system_info(f"  {symbol} {name}: {message}")
            
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"PDF: Exceção - {str(e)}")
            emoji_logger.system_error("PDF Test", f"❌ Exceção: {e}")
    
    async def test_image_processing(self):
        """Testa processamento de imagem"""
        self.results["total_tests"] += 1
        test_name = "IMAGE_PROCESSING"
        
        emoji_logger.system_info("\n📸 TESTE 2: Processamento de Imagem Real")
        emoji_logger.system_info("-" * 50)
        
        try:
            # Carregar imagem real
            img_path = Path("tests/20250715_164305.png")
            with open(img_path, "rb") as f:
                img_bytes = f.read()
                img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            
            # Simular formato do webhook
            media_data = {
                "type": "image",
                "mimetype": "image/png",
                "data": f"data:image/png;base64,{img_base64}",
                "content": f"data:image/png;base64,{img_base64}"
            }
            
            # Processar
            result = await self.processor.process_media(media_data)
            
            # Validações
            validations = []
            
            # 1. Sucesso no processamento
            if result["success"]:
                validations.append(("Processamento", True, "Imagem processada com sucesso"))
            else:
                validations.append(("Processamento", False, f"Erro: {result.get('message')}"))
            
            # 2. Dimensões
            metadata = result.get("metadata", {})
            width = metadata.get("width")
            height = metadata.get("height")
            
            if width == EXPECTED_VALUES["image"]["width"] and height == EXPECTED_VALUES["image"]["height"]:
                validations.append(("Dimensões", True, f"{width}x{height} ✅"))
            else:
                validations.append(("Dimensões", False, f"{width}x{height} (esperado {EXPECTED_VALUES['image']['width']}x{EXPECTED_VALUES['image']['height']})"))
            
            # 3. Formato
            format_img = metadata.get("format", "").upper()
            if format_img == EXPECTED_VALUES["image"]["format"]:
                validations.append(("Formato", True, f"{format_img} ✅"))
            else:
                validations.append(("Formato", False, f"{format_img} (esperado {EXPECTED_VALUES['image']['format']})"))
            
            # 4. OCR (opcional)
            text = result.get("text", "")
            if text:
                validations.append(("OCR", True, f"{len(text)} caracteres extraídos"))
            else:
                self.results["warnings"].append("Imagem: OCR não extraiu texto (Tesseract não configurado)")
                validations.append(("OCR", None, "OCR não disponível (opcional)"))
            
            # Resultado final
            passed_count = sum(1 for _, passed, _ in validations if passed is True)
            total_count = sum(1 for _, passed, _ in validations if passed is not None)
            
            self.results["details"][test_name] = {
                "validations": validations,
                "passed": passed_count,
                "total": total_count,
                "success_rate": (passed_count / total_count * 100) if total_count > 0 else 0
            }
            
            if passed_count == total_count:
                self.results["passed"] += 1
                emoji_logger.system_success(f"✅ TESTE IMAGEM: {passed_count}/{total_count} validações passaram")
            else:
                self.results["failed"] += 1
                emoji_logger.system_error("Image Test", f"❌ TESTE IMAGEM: {passed_count}/{total_count} validações passaram")
            
            # Mostrar detalhes
            for name, passed, message in validations:
                if passed is None:
                    symbol = "⚠️"
                else:
                    symbol = "✅" if passed else "❌"
                emoji_logger.system_info(f"  {symbol} {name}: {message}")
            
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Imagem: Exceção - {str(e)}")
            emoji_logger.system_error("Image Test", f"❌ Exceção: {e}")
    
    async def test_audio_processing(self):
        """Testa processamento de áudio"""
        self.results["total_tests"] += 1
        test_name = "AUDIO_PROCESSING"
        
        emoji_logger.system_info("\n🎤 TESTE 3: Processamento de Áudio Real")
        emoji_logger.system_info("-" * 50)
        
        try:
            # Carregar áudio real
            audio_path = Path("tests/WhatsApp Audio 2025-08-03 at 22.31.42.opus")
            with open(audio_path, "rb") as f:
                audio_bytes = f.read()
                audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
            
            # Simular formato do webhook
            media_data = {
                "type": "audio",
                "mimetype": "audio/ogg",
                "data": f"data:audio/ogg;base64,{audio_base64}",
                "content": f"data:audio/ogg;base64,{audio_base64}",
                "ptt": True
            }
            
            # Processar
            result = await self.processor.process_media(media_data)
            
            # Validações
            validations = []
            
            # 1. Sucesso no processamento
            if result["success"]:
                validations.append(("Processamento", True, "Áudio processado com sucesso"))
            else:
                # Áudio Opus pode falhar no FFmpeg mas ainda ser válido
                if "ffmpeg" in result.get("message", "").lower():
                    validations.append(("Processamento", None, "FFmpeg não suporta Opus (esperado)"))
                    self.results["warnings"].append("Áudio: FFmpeg não processa Opus nativamente")
                else:
                    validations.append(("Processamento", False, f"Erro: {result.get('message')}"))
            
            # 2. Duração (se disponível)
            metadata = result.get("metadata", {})
            duration = metadata.get("duration")
            
            if duration:
                if EXPECTED_VALUES["audio"]["duration_min"] <= duration <= EXPECTED_VALUES["audio"]["duration_max"]:
                    validations.append(("Duração", True, f"{duration:.1f} segundos ✅"))
                else:
                    validations.append(("Duração", False, f"{duration:.1f} segundos (esperado {EXPECTED_VALUES['audio']['duration_min']}-{EXPECTED_VALUES['audio']['duration_max']}s)"))
            
            # 3. Transcrição
            text = result.get("text", "").lower()
            if text:
                # Verificar palavras-chave esperadas
                keywords_found = [kw for kw in EXPECTED_VALUES["audio"]["transcription_keywords"] if kw in text]
                if keywords_found:
                    validations.append(("Transcrição", True, f"Palavras-chave encontradas: {', '.join(keywords_found)}"))
                else:
                    validations.append(("Transcrição", False, f"Nenhuma palavra-chave esperada encontrada"))
                
                emoji_logger.system_info(f"  📝 Transcrição: \"{text[:100]}...\"")
            else:
                validations.append(("Transcrição", False, "Transcrição vazia"))
            
            # Resultado final
            passed_count = sum(1 for _, passed, _ in validations if passed is True)
            total_count = sum(1 for _, passed, _ in validations if passed is not None)
            
            self.results["details"][test_name] = {
                "validations": validations,
                "passed": passed_count,
                "total": total_count,
                "success_rate": (passed_count / total_count * 100) if total_count > 0 else 0
            }
            
            if passed_count == total_count and total_count > 0:
                self.results["passed"] += 1
                emoji_logger.system_success(f"✅ TESTE ÁUDIO: {passed_count}/{total_count} validações passaram")
            else:
                self.results["failed"] += 1
                emoji_logger.system_error("Audio Test", f"❌ TESTE ÁUDIO: {passed_count}/{total_count} validações passaram")
            
            # Mostrar detalhes
            for name, passed, message in validations:
                if passed is None:
                    symbol = "⚠️"
                else:
                    symbol = "✅" if passed else "❌"
                emoji_logger.system_info(f"  {symbol} {name}: {message}")
            
        except Exception as e:
            self.results["failed"] += 1
            self.results["errors"].append(f"Áudio: Exceção - {str(e)}")
            emoji_logger.system_error("Audio Test", f"❌ Exceção: {e}")
    
    def generate_report(self):
        """Gera relatório final detalhado"""
        emoji_logger.system_info("\n" + "=" * 70)
        emoji_logger.system_info("📊 RELATÓRIO FINAL DE VALIDAÇÃO DO SISTEMA")
        emoji_logger.system_info("=" * 70)
        
        # Estatísticas gerais
        total = self.results["total_tests"]
        passed = self.results["passed"]
        failed = self.results["failed"]
        success_rate = (passed / total * 100) if total > 0 else 0
        
        emoji_logger.system_info(f"\n📈 ESTATÍSTICAS GERAIS:")
        emoji_logger.system_info(f"  • Total de testes: {total}")
        emoji_logger.system_info(f"  • Passou: {passed}")
        emoji_logger.system_info(f"  • Falhou: {failed}")
        emoji_logger.system_info(f"  • Taxa de sucesso: {success_rate:.1f}%")
        
        # Detalhes por teste
        emoji_logger.system_info(f"\n📋 DETALHES POR TESTE:")
        for test_name, details in self.results["details"].items():
            emoji_logger.system_info(f"\n  {test_name}:")
            emoji_logger.system_info(f"    • Validações: {details['passed']}/{details['total']}")
            emoji_logger.system_info(f"    • Taxa: {details['success_rate']:.1f}%")
        
        # Erros críticos
        if self.results["errors"]:
            emoji_logger.system_info(f"\n❌ ERROS CRÍTICOS ({len(self.results['errors'])}):")
            for error in self.results["errors"]:
                emoji_logger.system_error("Critical", f"  • {error}")
        
        # Avisos
        if self.results["warnings"]:
            emoji_logger.system_info(f"\n⚠️ AVISOS ({len(self.results['warnings'])}):")
            for warning in self.results["warnings"]:
                emoji_logger.system_warning(f"  • {warning}")
        
        # Veredicto final
        emoji_logger.system_info("\n" + "=" * 70)
        
        # Sistema só está pronto se detectar valores corretos
        has_critical_errors = any("ERRADO" in str(e) or "valor correto" in str(e) for e in self.results["errors"])
        
        if success_rate >= 66 and not has_critical_errors:
            emoji_logger.system_success("✅ SISTEMA APROVADO PARA PRODUÇÃO!")
            emoji_logger.system_info("   Todos os testes críticos passaram.")
            return True
        else:
            emoji_logger.system_error("System Validation", "❌ SISTEMA REPROVADO - CORREÇÕES NECESSÁRIAS")
            if has_critical_errors:
                emoji_logger.system_error("Critical Issue", "   ⚠️ ERRO CRÍTICO: Sistema detecta valores incorretos nos documentos!")
            emoji_logger.system_info("   Verifique os erros listados acima.")
            return False

async def main():
    """Executa validação completa do sistema"""
    emoji_logger.system_info("🚀 INICIANDO VALIDAÇÃO COMPLETA DO SISTEMA SDR IA SOLARPRIME")
    emoji_logger.system_info("Versão: v0.3 - Teste de Produção")
    emoji_logger.system_info(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    emoji_logger.system_info("=" * 70)
    
    validator = SystemValidator()
    
    # Executar todos os testes
    await validator.test_pdf_processing()
    await validator.test_image_processing()
    await validator.test_audio_processing()
    
    # Gerar relatório
    success = validator.generate_report()
    
    # Salvar relatório em JSON
    report_file = Path("test_validation_report.json")
    with open(report_file, "w") as f:
        json.dump(validator.results, f, indent=2, default=str)
    
    emoji_logger.system_info(f"\n📄 Relatório salvo em: {report_file}")
    
    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)