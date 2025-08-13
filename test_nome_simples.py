#!/usr/bin/env python
"""
🧪 TESTE SIMPLES DE EXTRAÇÃO DE NOME
Valida apenas a extração correta do nome
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.core.lead_manager import LeadManager

async def test_extracao_nome():
    """Testa extração de nome isoladamente"""
    
    print("\n" + "="*60)
    print("🧪 TESTE DE EXTRAÇÃO DE NOME")
    print("="*60)
    
    lead_manager = LeadManager()
    lead_manager.initialize()
    
    # Simular conversa real
    conversa = [
        {"role": "user", "content": "oi quero saber sobre energia solar"},
        {"role": "assistant", "content": "Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime. Antes de começarmos, como posso te chamar?"},
        {"role": "user", "content": "João Teste Silva"}
    ]
    
    # Extrair informações
    lead_info = lead_manager.extract_lead_info(conversa)
    
    print(f"\n📋 Lead Info Extraído:")
    print(f"  Nome: {lead_info.get('name')}")
    print(f"  Score: {lead_info.get('qualification_score')}")
    
    # Verificar se extraiu corretamente
    if lead_info.get('name') == "João Teste Silva":
        print("\n✅ Nome extraído CORRETAMENTE!")
        return True
    else:
        print(f"\n❌ Nome extraído INCORRETAMENTE: '{lead_info.get('name')}'")
        print("\n🔍 Debug - Conversa completa:")
        for i, msg in enumerate(conversa):
            print(f"  {i}. [{msg['role']}]: {msg['content'][:50]}...")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_extracao_nome())
    sys.exit(0 if success else 1)