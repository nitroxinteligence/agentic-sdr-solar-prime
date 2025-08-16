#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Teste para validar a correção do filtro de frases proibidas
Data: 16/08/2025
Objetivo: Verificar que "deixa eu" não é mais bloqueada incorretamente
"""

import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.response_formatter import ResponseFormatter

def test_filtro_frases():
    """Testa o filtro de frases proibidas após correção"""
    
    print("🧪 TESTE: Validação do Filtro de Frases Proibidas")
    print("=" * 60)
    
    # Casos que DEVEM PASSAR (não devem ser bloqueados)
    casos_validos = [
        "Ôxe, deixa eu ver sua conta aqui",
        "deixa eu explicar melhor",
        "Beleza! deixa eu analisar isso",
        "Eita, deixa eu conferir os dados",
        "deixa eu te falar uma coisa",
        "Perfeito! deixa eu calcular",
        "Helen aqui! deixa eu verificar",
        "Oi! deixa eu entender melhor",
        "deixa eu te ajudar com isso",
        "Claro! deixa eu ver"
    ]
    
    # Casos que DEVEM SER BLOQUEADOS
    casos_proibidos = [
        "Vou analisar seu caso",
        "Estou processando as informações",
        "Aguarde um momento enquanto processo",
        "Analisando os dados fornecidos",
        "Processando sua solicitação",
        "Verificando as informações",
        "Analisando sua conta de energia",
        "Processando os dados da sua conta",
        "Aguarde enquanto analiso",
        "Estou verificando os dados"
    ]
    
    print("📋 TESTE 1: Frases que DEVEM PASSAR")
    print("-" * 40)
    
    passou_casos_validos = 0
    for i, frase in enumerate(casos_validos, 1):
        # Criar resposta formatada para teste
        resposta_formatada = f"<RESPOSTA_FINAL>{frase}</RESPOSTA_FINAL>"
        resultado = ResponseFormatter.validate_response_content(resposta_formatada)
        status = "✅ PASSOU" if resultado else "❌ BLOQUEOU"
        print(f"{i:2d}. {status} - '{frase}'")
        if resultado:
            passou_casos_validos += 1
    
    print(f"\nResultado: {passou_casos_validos}/{len(casos_validos)} casos válidos passaram")
    
    print("\n📋 TESTE 2: Frases que DEVEM SER BLOQUEADAS")
    print("-" * 40)
    
    bloqueou_casos_proibidos = 0
    for i, frase in enumerate(casos_proibidos, 1):
        # Criar resposta formatada para teste
        resposta_formatada = f"<RESPOSTA_FINAL>{frase}</RESPOSTA_FINAL>"
        resultado = ResponseFormatter.validate_response_content(resposta_formatada)
        status = "✅ BLOQUEOU" if not resultado else "❌ PASSOU"
        print(f"{i:2d}. {status} - '{frase}'")
        if not resultado:
            bloqueou_casos_proibidos += 1
    
    print(f"\nResultado: {bloqueou_casos_proibidos}/{len(casos_proibidos)} casos proibidos foram bloqueados")
    
    print("\n📊 RESUMO FINAL")
    print("=" * 60)
    
    # Calcular score geral
    total_casos = len(casos_validos) + len(casos_proibidos)
    casos_corretos = passou_casos_validos + bloqueou_casos_proibidos
    porcentagem = (casos_corretos / total_casos) * 100
    
    print(f"Total de casos testados: {total_casos}")
    print(f"Casos corretos: {casos_corretos}")
    print(f"Porcentagem de acerto: {porcentagem:.1f}%")
    
    # Validação específica da correção
    print(f"\n🎯 VALIDAÇÃO DA CORREÇÃO:")
    print(f"- Casos 'deixa eu' que passaram: {passou_casos_validos}/{len(casos_validos)}")
    print(f"- Frases proibidas ainda bloqueadas: {bloqueou_casos_proibidos}/{len(casos_proibidos)}")
    
    if passou_casos_validos == len(casos_validos) and bloqueou_casos_proibidos == len(casos_proibidos):
        print(f"\n🎉 SUCESSO! O filtro está funcionando corretamente!")
        print(f"✅ 'deixa eu' não é mais bloqueada incorretamente")
        print(f"✅ Frases realmente proibidas ainda são bloqueadas")
        return True
    else:
        print(f"\n⚠️  ATENÇÃO! Alguns casos falharam:")
        if passou_casos_validos < len(casos_validos):
            print(f"❌ {len(casos_validos) - passou_casos_validos} casos 'deixa eu' foram bloqueados incorretamente")
        if bloqueou_casos_proibidos < len(casos_proibidos):
            print(f"❌ {len(casos_proibidos) - bloqueou_casos_proibidos} frases proibidas não foram bloqueadas")
            
            # Mostrar quais frases específicas falharam
            print(f"\n🔍 ANÁLISE DAS FALHAS:")
            for i, frase in enumerate(casos_proibidos, 1):
                resposta_formatada = f"<RESPOSTA_FINAL>{frase}</RESPOSTA_FINAL>"
                resultado = ResponseFormatter.validate_response_content(resposta_formatada)
                if resultado:  # Se passou quando deveria bloquear
                    print(f"❌ Frase {i} não foi bloqueada: '{frase}'")
            
            print(f"\n💡 SUGESTÕES DE MELHORIA:")
            print(f"- Adicionar 'analisando' à lista de frases proibidas")
            print(f"- O filtro atual só tem 'vou analisar' mas não 'analisando'")
            print(f"- Considerar palavras-raiz para capturar variações")
        
        return False

if __name__ == "__main__":
    try:
        sucesso = test_filtro_frases()
        exit_code = 0 if sucesso else 1
        print(f"\n🏁 Teste finalizado com código: {exit_code}")
        sys.exit(exit_code)
        
    except Exception as e:
        print(f"\n💥 ERRO durante o teste: {str(e)}")
        print(f"Tipo: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        sys.exit(1)