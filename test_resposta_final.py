#!/usr/bin/env python
"""
🧪 TESTE DE GERAÇÃO DE RESPOSTA COM TAGS
Verifica se o agente está gerando respostas com tags <RESPOSTA_FINAL>
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.agents.agentic_sdr_refactored import get_agentic_agent
from app.api.webhooks import extract_final_response

async def test_resposta_com_tags():
    """Testa se o agente gera respostas com tags corretas"""
    
    print("\n" + "="*60)
    print("🧪 TESTE DE TAGS <RESPOSTA_FINAL>")
    print("="*60)
    
    try:
        # Inicializar agente
        print("\n📱 1. Inicializando AgenticSDR...")
        agent = await get_agentic_agent()
        
        # Testar primeira mensagem
        print("\n📝 2. Enviando primeira mensagem...")
        response = await agent.process_message(
            "olá, tudo bem?",
            {"phone": "+5511999999999"}
        )
        
        print(f"\n📊 Resposta completa do agente:")
        print("-" * 40)
        print(response[:500] if len(response) > 500 else response)
        print("-" * 40)
        
        # Verificar se tem tags
        has_tags = "<RESPOSTA_FINAL>" in response and "</RESPOSTA_FINAL>" in response
        
        if has_tags:
            print("\n✅ Tags <RESPOSTA_FINAL> encontradas!")
            
            # Testar extração
            extracted = extract_final_response(response)
            print(f"\n📝 Resposta extraída:")
            print(extracted)
            
            # Verificar se é a resposta esperada (Helen se apresentando)
            if "Helen" in extracted and "Solarprime" in extracted:
                print("\n✅ Resposta correta extraída!")
                return True
            else:
                print("\n⚠️ Resposta extraída mas conteúdo inesperado")
                return False
        else:
            print("\n❌ TAGS NÃO ENCONTRADAS NA RESPOSTA!")
            print("\n🔍 Analisando estrutura da resposta...")
            
            # Verificar se tem alguma variação
            if "RESPOSTA_FINAL" in response.upper():
                print("⚠️ Tags presentes mas com formatação diferente")
            else:
                print("❌ Nenhuma variação de RESPOSTA_FINAL encontrada")
            
            # Verificar se a resposta esperada está presente sem tags
            if "Helen" in response and "como posso te chamar" in response.lower():
                print("\n⚠️ Conteúdo correto mas SEM TAGS!")
                print("🔴 PROBLEMA: Agente não está formatando com tags obrigatórias")
            
            return False
            
    except Exception as e:
        print(f"\n❌ Erro no teste: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_resposta_com_tags())
    
    print("\n" + "="*60)
    if success:
        print("✅ TESTE PASSOU - Tags funcionando corretamente")
    else:
        print("❌ TESTE FALHOU - Problema com tags <RESPOSTA_FINAL>")
        print("\n🔧 SOLUÇÃO NECESSÁRIA:")
        print("1. Verificar se o prompt está sendo passado corretamente")
        print("2. Confirmar que o modelo entende a instrução das tags")
        print("3. Adicionar validação para garantir tags na resposta")
    print("="*60)
    
    sys.exit(0 if success else 1)