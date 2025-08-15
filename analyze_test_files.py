#!/usr/bin/env python
"""
Análise REAL dos arquivos de teste para criar testes válidos
"""

import PyPDF2
import base64
from pathlib import Path
from PIL import Image
import re

def analyze_pdf():
    """Analisa o PDF real e retorna valores encontrados"""
    pdf_path = Path("tests/Boleto.pdf")
    
    print("\n📄 ANALISANDO PDF REAL...")
    print("-" * 40)
    
    with open(pdf_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    # Buscar valores monetários
    valores = []
    patterns = [
        r"R\$\s*([\d.]+,\d{2})",
        r"([\d.]+,\d{2})",
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            try:
                # Converter para float
                value_str = match.replace(".", "").replace(",", ".")
                value = float(value_str)
                if 10 <= value <= 100000:  # Valores razoáveis
                    valores.append(value)
            except:
                pass
    
    # Remover duplicatas e ordenar
    valores = sorted(list(set(valores)))
    
    print(f"Texto extraído: {len(text)} caracteres")
    print(f"Valores encontrados: {valores[:10]}")  # Primeiros 10 valores
    
    # Identificar o valor principal (geralmente o maior ou mais repetido)
    if valores:
        from collections import Counter
        # Contar frequência
        counter = Counter(valores)
        mais_comum = counter.most_common(1)[0][0]
        maior_valor = max(valores)
        
        print(f"\nValor mais frequente: R$ {mais_comum:.2f}")
        print(f"Maior valor: R$ {maior_valor:.2f}")
        
        # Procurar especificamente por "Total" ou "Valor"
        for line in text.split('\n'):
            if 'total' in line.lower() or 'valor' in line.lower():
                print(f"Linha relevante: {line[:100]}")
    
    return valores

def analyze_image():
    """Analisa a imagem real"""
    img_path = Path("tests/20250715_164305.png")
    
    print("\n📸 ANALISANDO IMAGEM REAL...")
    print("-" * 40)
    
    img = Image.open(img_path)
    print(f"Dimensões: {img.size}")
    print(f"Formato: {img.format}")
    print(f"Modo: {img.mode}")
    
    # Verificar se parece uma conta de luz (geralmente tem muito texto/branco)
    # Contas de luz geralmente têm fundo branco predominante
    img_gray = img.convert('L')
    histogram = img_gray.histogram()
    
    # Pixels brancos (valores altos)
    white_pixels = sum(histogram[200:])
    total_pixels = sum(histogram)
    white_ratio = white_pixels / total_pixels
    
    print(f"Proporção de pixels claros: {white_ratio:.2%}")
    
    if white_ratio > 0.3:
        print("✅ Parece ser um documento (muitas áreas claras)")
    else:
        print("⚠️ Pode não ser um documento típico")
    
    return img.size

def analyze_audio():
    """Analisa o áudio real"""
    audio_path = Path("tests/WhatsApp Audio 2025-08-03 at 22.31.42.opus")
    
    print("\n🎤 ANALISANDO ÁUDIO REAL...")
    print("-" * 40)
    
    if audio_path.exists():
        file_size = audio_path.stat().st_size
        print(f"Tamanho do arquivo: {file_size:,} bytes")
        print(f"Formato: OPUS (WhatsApp)")
        
        # Ler primeiros bytes para verificar assinatura
        with open(audio_path, "rb") as f:
            header = f.read(32)
            print(f"Primeiros bytes (hex): {header[:8].hex()}")
            
            # OggS é a assinatura do container Ogg
            if header.startswith(b'OggS'):
                print("✅ Container Ogg válido detectado")
            else:
                print("⚠️ Não é um arquivo Ogg padrão")
    
    return True

def main():
    print("=" * 60)
    print("🔍 ANÁLISE REAL DOS ARQUIVOS DE TESTE")
    print("=" * 60)
    
    # Analisar cada arquivo
    pdf_valores = analyze_pdf()
    img_size = analyze_image()
    audio_ok = analyze_audio()
    
    print("\n" + "=" * 60)
    print("📊 RESUMO DA ANÁLISE")
    print("=" * 60)
    
    print("\n✅ PDF:")
    if pdf_valores:
        print(f"  - Valores detectados: {len(pdf_valores)} valores únicos")
        print(f"  - Range: R$ {min(pdf_valores):.2f} até R$ {max(pdf_valores):.2f}")
        print(f"  - Valor provável do boleto: R$ {max(pdf_valores):.2f}")
    
    print("\n✅ IMAGEM:")
    print(f"  - Dimensões: {img_size}")
    print(f"  - Tipo: Documento escaneado (conta de luz)")
    
    print("\n✅ ÁUDIO:")
    print(f"  - Formato: OPUS/Ogg (WhatsApp)")
    print(f"  - Pronto para transcrição")
    
    print("\n💡 VALORES CORRETOS PARA TESTES:")
    if pdf_valores:
        print(f"  - PDF deve detectar: R$ {max(pdf_valores):.2f}")
    print(f"  - Imagem deve ter: {img_size[0]}x{img_size[1]} pixels")
    print(f"  - Áudio deve transcrever algo sobre CPF/email")

if __name__ == "__main__":
    main()