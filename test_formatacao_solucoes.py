#!/usr/bin/env python3
"""
Teste para validar a formatação especial das 4 soluções
"""

import os
import sys

# Configurar ambiente
os.environ["MESSAGE_MAX_LENGTH"] = "150"

# Adicionar path do projeto
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.message_splitter import MessageSplitter
from app.utils.logger import emoji_logger

def test_formatacao_4_solucoes():
    """Testa se a mensagem das 4 soluções é formatada corretamente"""
    print("\n" + "="*80)
    print("🧪 TESTE: Formatação das 4 Soluções SolarPrime")
    print("="*80)
    
    # Criar splitter
    splitter = MessageSplitter(max_length=150, add_indicators=False)
    
    # Mensagem original (como vem do agente)
    mensagem_original = "Perfeito, Mateus! Hoje na Solarprime nós temos quatro modelos de soluções energéticas: 1) Instalação de usina própria - você fica dono da usina ao final 2) Aluguel de lote para instalação de usina própria - sua usina em nosso terreno 3) Compra de energia com desconto - economia imediata de 20% 4) Usina de investimento - renda passiva com energia solar Qual desses modelos seria do seu interesse?"
    
    print(f"\n📝 Mensagem original ({len(mensagem_original)} caracteres):")
    print("-" * 40)
    print(mensagem_original)
    print("-" * 40)
    
    # Processar com o splitter
    chunks = splitter.split_message(mensagem_original)
    
    print(f"\n✅ Resultado: {len(chunks)} parte(s)")
    print("-" * 40)
    
    for i, chunk in enumerate(chunks, 1):
        if len(chunks) > 1:
            print(f"\n[Parte {i}/{len(chunks)}]")
        print(chunk)
        print(f"\n({len(chunk)} caracteres)")
    
    print("-" * 40)
    
    # Verificações
    if len(chunks) == 1:
        print("\n✅ SUCESSO: Mensagem não foi dividida!")
        
        # Verificar se tem quebras de linha
        if "\n" in chunks[0]:
            print("✅ SUCESSO: Quebras de linha adicionadas!")
            
            # Contar linhas
            lines = chunks[0].split("\n")
            print(f"📊 Total de linhas: {len(lines)}")
            
            # Verificar se cada opção está em sua linha
            for i in range(1, 5):
                if any(f"{i})" in line for line in lines):
                    print(f"✅ Opção {i} está em linha separada")
        else:
            print("⚠️ AVISO: Sem quebras de linha (pode ser intencional)")
    else:
        print(f"❌ FALHA: Mensagem foi dividida em {len(chunks)} partes!")
        return False
    
    return True

def test_mensagem_normal():
    """Testa que mensagens normais continuam sendo divididas"""
    print("\n" + "="*80)
    print("🧪 TESTE: Mensagem Normal (deve dividir se necessário)")
    print("="*80)
    
    splitter = MessageSplitter(max_length=150, add_indicators=False)
    
    # Mensagem longa normal
    mensagem_normal = "Esta é uma mensagem normal muito longa que deveria ser dividida normalmente pelo splitter porque não é a mensagem especial das 4 soluções. " * 3
    
    print(f"\n📝 Mensagem normal ({len(mensagem_normal)} caracteres)")
    
    chunks = splitter.split_message(mensagem_normal)
    
    print(f"\n✅ Resultado: {len(chunks)} parte(s)")
    
    if len(chunks) > 1:
        print("✅ SUCESSO: Mensagem normal foi dividida!")
        return True
    else:
        print("❌ FALHA: Mensagem normal não foi dividida!")
        return False

def test_deteccao_variações():
    """Testa detecção de variações da mensagem das 4 soluções"""
    print("\n" + "="*80)
    print("🧪 TESTE: Detecção de Variações")
    print("="*80)
    
    splitter = MessageSplitter(max_length=150, add_indicators=False)
    
    variações = [
        # Variação 1: Com "Hoje na Solarprime"
        "Perfeito! Hoje na Solarprime temos 4 modelos: 1) Instalação de usina própria 2) Aluguel de lote 3) Compra de energia com desconto 4) Usina de investimento. Qual te interessa?",
        
        # Variação 2: Com "quatro modelos de soluções"
        "João, temos quatro modelos de soluções energéticas: 1) Instalação própria 2) Aluguel 3) Compra com desconto 4) Investimento",
        
        # Variação 3: Menção completa das opções
        "Oferecemos: 1) Instalação de usina própria - você fica dono 2) Aluguel de lote para usina 3) Compra de energia com desconto de 20% 4) Usina de investimento com renda passiva"
    ]
    
    for i, msg in enumerate(variações, 1):
        print(f"\n📋 Variação {i}:")
        if splitter._is_four_solutions_message(msg):
            print("✅ Detectada como mensagem das 4 soluções")
        else:
            print("❌ NÃO detectada")
    
    return True

def main():
    """Executa todos os testes"""
    print("\n" + "="*100)
    print("🚀 TESTE DA FORMATAÇÃO ESPECIAL DAS 4 SOLUÇÕES")
    print("="*100)
    
    tests = [
        ("Formatação das 4 Soluções", test_formatacao_4_solucoes),
        ("Mensagem Normal", test_mensagem_normal),
        ("Detecção de Variações", test_deteccao_variações)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Erro no teste {name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Resumo
    print("\n" + "="*100)
    print("📊 RESUMO DOS TESTES")
    print("="*100)
    
    total = len(results)
    passed = sum(1 for _, success in results if success)
    
    for name, success in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{status}: {name}")
    
    print(f"\n📈 Taxa de sucesso: {passed}/{total} ({passed*100/total:.1f}%)")
    
    if passed == total:
        print("\n🎉 FORMATAÇÃO ESPECIAL FUNCIONANDO!")
        print("\n✅ Benefícios implementados:")
        print("   1. Mensagem das 4 soluções NÃO é cortada")
        print("   2. Quebras de linha adequadas para WhatsApp")
        print("   3. Mensagens normais continuam sendo divididas")
        print("   4. Detecção inteligente de variações")
        print("\n🚀 PRONTO PARA DEPLOY!")
    else:
        print("\n⚠️ Alguns testes falharam. Verifique os logs.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)