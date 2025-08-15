#!/usr/bin/env python3
"""
Test: Verificar formatação das 4 opções de soluções energéticas
Garante que as quebras de linha estão funcionando corretamente
"""

import asyncio
import sys
from pathlib import Path

# Adicionar diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

from app.agents.agentic_sdr_stateless import AgenticSDRStateless


async def test_4_options_formatting():
    """
    Testa se o agente formata corretamente as 4 opções com quebras de linha
    """
    print("\n🧪 Testando formatação das 4 opções de soluções energéticas...")
    print("=" * 60)
    
    # Criar instância do agente
    agent = AgenticSDRStateless()
    await agent.initialize()
    
    # Simular contexto após coletar nome
    execution_context = {
        "phone": "+5511999999999",
        "conversation_id": "test-conv-123",
        "conversation_history": [
            {
                "role": "user",
                "content": "Oi",
                "timestamp": "2025-01-15T10:00:00"
            },
            {
                "role": "assistant", 
                "content": "Oi! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?",
                "timestamp": "2025-01-15T10:00:10"
            }
        ],
        "lead_info": {
            "phone_number": "+5511999999999"
        }
    }
    
    # Simular resposta do usuário com seu nome
    message = "Mateus"
    
    print("\n📨 Mensagem do usuário:", message)
    print("\n⏳ Processando resposta do agente...")
    
    # Processar mensagem
    response = await agent.process_message(message, execution_context)
    
    print("\n📤 Resposta do agente:")
    print("-" * 60)
    print(response)
    print("-" * 60)
    
    # Verificar se a resposta contém quebras de linha nas opções
    has_line_breaks = False
    has_numbered_options = False
    
    # Extrair conteúdo da tag RESPOSTA_FINAL se existir
    if "<RESPOSTA_FINAL>" in response:
        start = response.find("<RESPOSTA_FINAL>") + len("<RESPOSTA_FINAL>")
        end = response.find("</RESPOSTA_FINAL>")
        if end > start:
            response_content = response[start:end].strip()
        else:
            response_content = response
    else:
        response_content = response
    
    # Verificar quebras de linha
    if "\n" in response_content:
        has_line_breaks = True
        print("\n✅ Quebras de linha detectadas na resposta")
    else:
        print("\n❌ ERRO: Não foram encontradas quebras de linha na resposta")
    
    # Verificar se as 4 opções estão numeradas
    options_found = []
    for i in range(1, 5):
        if f"{i})" in response_content:
            options_found.append(i)
    
    if len(options_found) == 4:
        has_numbered_options = True
        print("✅ Todas as 4 opções numeradas foram encontradas:", options_found)
    else:
        print(f"❌ ERRO: Apenas {len(options_found)} opções encontradas:", options_found)
    
    # Verificar formatação específica
    expected_patterns = [
        "1) Instalação de usina própria",
        "2) Aluguel de lote",
        "3) Compra de energia com desconto",
        "4) Usina de investimento"
    ]
    
    patterns_found = []
    for pattern in expected_patterns:
        if pattern in response_content or pattern.replace(" de ", " ") in response_content:
            patterns_found.append(pattern)
    
    if len(patterns_found) >= 3:  # Pelo menos 3 das 4 opções
        print(f"✅ Padrões de opções encontrados ({len(patterns_found)}/4):")
        for p in patterns_found:
            print(f"   - {p}")
    else:
        print(f"❌ ERRO: Poucos padrões encontrados ({len(patterns_found)}/4)")
    
    # Análise detalhada das linhas
    print("\n📊 Análise detalhada das linhas:")
    lines = response_content.split("\n")
    for i, line in enumerate(lines, 1):
        if any(opt in line for opt in ["1)", "2)", "3)", "4)"]):
            print(f"   Linha {i}: {line[:80]}{'...' if len(line) > 80 else ''}")
    
    # Resultado final
    print("\n" + "=" * 60)
    if has_line_breaks and has_numbered_options and len(patterns_found) >= 3:
        print("✅ SUCESSO: Formatação das 4 opções está CORRETA!")
        print("   - Quebras de linha: ✅")
        print("   - Opções numeradas: ✅")
        print("   - Padrões corretos: ✅")
        return True
    else:
        print("❌ FALHA: A formatação das 4 opções precisa de ajustes")
        print(f"   - Quebras de linha: {'✅' if has_line_breaks else '❌'}")
        print(f"   - Opções numeradas: {'✅' if has_numbered_options else '❌'}")
        print(f"   - Padrões corretos: {'✅' if len(patterns_found) >= 3 else '❌'}")
        return False


async def main():
    """Executa o teste"""
    print("=" * 60)
    print("🔬 TESTE: Formatação das 4 Opções de Soluções Energéticas")
    print("=" * 60)
    
    try:
        success = await test_4_options_formatting()
        
        if success:
            print("\n🎉 Teste concluído com sucesso!")
            print("As 4 opções estão sendo formatadas corretamente com quebras de linha.")
        else:
            print("\n⚠️ O teste identificou problemas na formatação.")
            print("Verifique o prompt do agente para garantir que as exceções")
            print("de quebra de linha estão sendo aplicadas corretamente.")
        
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())