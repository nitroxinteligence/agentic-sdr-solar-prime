#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste CRÍTICO para validar que tools não são envolvidas com tags RESPOSTA_FINAL
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.response_formatter import ResponseFormatter

def test_tool_formatting():
    """Testa se tools não são envolvidas com tags RESPOSTA_FINAL"""
    
    formatter = ResponseFormatter()
    
    # Casos que NÃO devem ser envolvidos com tags (contêm tools)
    tool_cases = [
        "[TOOL: calendar.check_availability]",
        "[TOOL: calendar.schedule_meeting]",
        "[CRM: update_lead]",
        "[CALENDAR: check_slots]",
        "Vou verificar sua agenda [TOOL: calendar.check_availability]",
        "[TOOL: crm.create_lead] para o cliente"
    ]
    
    # Casos que DEVEM ser envolvidos com tags (respostas normais)
    normal_cases = [
        "Oi! Como posso ajudar?",
        "Vou verificar sua agenda e te retorno",
        "Perfeito! Vamos agendar sua reunião",
        "Entendi, você quer saber sobre energia solar"
    ]
    
    print("🧪 Testando casos que NÃO devem ser envolvidos com tags (tools):")
    for i, response in enumerate(tool_cases, 1):
        formatted = formatter.ensure_response_tags(response)
        has_tags = "<RESPOSTA_FINAL>" in formatted
        status = "❌ FALHOU" if has_tags else "✅ PASSOU"
        print(f"  {i}. '{response}' -> {status}")
        if has_tags:
            print(f"     ERRO: Tool foi envolvida com tags: {formatted}")
    
    print("\n🧪 Testando casos que DEVEM ser envolvidos com tags (respostas normais):")
    for i, response in enumerate(normal_cases, 1):
        formatted = formatter.ensure_response_tags(response)
        has_tags = "<RESPOSTA_FINAL>" in formatted
        status = "✅ PASSOU" if has_tags else "❌ FALHOU"
        print(f"  {i}. '{response}' -> {status}")
        if not has_tags:
            print(f"     ERRO: Resposta normal não foi envolvida com tags: {formatted}")

if __name__ == "__main__":
    print("🚨 TESTE CRÍTICO: Formatação de Tools")
    print("=" * 50)
    test_tool_formatting()
    print("\n✅ Teste concluído!")