#!/usr/bin/env python3
"""
Test: Verificar conversão de qualification_score para INTEGER
Garante que valores float são convertidos corretamente para int
"""

import asyncio
import sys
from pathlib import Path

# Adicionar diretório do projeto ao path
sys.path.insert(0, str(Path(__file__).parent))

from app.agents.agentic_sdr_stateless import AgenticSDRStateless
from app.utils.safe_conversions import safe_int_conversion


def test_safe_int_conversion():
    """Testa a função de conversão segura"""
    print("\n🧪 Testando safe_int_conversion...")
    
    test_cases = [
        (10.0, 10, "Float 10.0"),
        (10.5, 10, "Float 10.5"),
        (15.9, 15, "Float 15.9"),
        (0.0, 0, "Float 0.0"),
        (100.0, 100, "Float 100.0"),
        ("10.0", 10, "String '10.0'"),
        (10, 10, "Integer 10"),
        (None, 0, "None value"),
    ]
    
    for value, expected, description in test_cases:
        result = safe_int_conversion(value, 0)
        status = "✅" if result == expected else "❌"
        print(f"  {status} {description}: {value} → {result} (esperado: {expected})")
        assert result == expected, f"Falha: {description}"
    
    print("  ✅ Todos os testes de conversão passaram!")


async def test_map_to_supabase_fields():
    """Testa o mapeamento de campos para Supabase"""
    print("\n🧪 Testando _map_to_supabase_fields...")
    
    agent = AgenticSDRStateless()
    
    # Teste 1: qualification_score como float
    changes = {
        'name': 'João Silva',
        'qualification_score': 10.0,  # Float que causaria erro
        'bill_value': 450.50,
        'current_stage': 'QUALIFIED'
    }
    
    result = agent._map_to_supabase_fields(changes)
    
    # Verificar que qualification_score foi convertido para int
    assert isinstance(result['qualification_score'], int), "qualification_score deve ser int"
    assert result['qualification_score'] == 10, f"Esperado 10, recebido {result['qualification_score']}"
    
    print(f"  ✅ Float 10.0 convertido para int: {result['qualification_score']}")
    
    # Teste 2: qualification_score como float com decimal
    changes['qualification_score'] = 15.7
    result = agent._map_to_supabase_fields(changes)
    
    assert isinstance(result['qualification_score'], int), "qualification_score deve ser int"
    assert result['qualification_score'] == 15, f"Esperado 15, recebido {result['qualification_score']}"
    
    print(f"  ✅ Float 15.7 convertido para int: {result['qualification_score']}")
    
    # Teste 3: qualification_score já como int
    changes['qualification_score'] = 20
    result = agent._map_to_supabase_fields(changes)
    
    assert isinstance(result['qualification_score'], int), "qualification_score deve ser int"
    assert result['qualification_score'] == 20, f"Esperado 20, recebido {result['qualification_score']}"
    
    print(f"  ✅ Int 20 mantido como int: {result['qualification_score']}")
    
    print("  ✅ Todos os testes de mapeamento passaram!")


async def test_prepare_lead_for_supabase():
    """Testa a preparação de dados do lead para Supabase"""
    print("\n🧪 Testando _prepare_lead_for_supabase...")
    
    agent = AgenticSDRStateless()
    
    lead_info = {
        'name': 'Maria Santos',
        'email': 'maria@example.com',
        'qualification_score': 8.5,  # Float que causaria erro
        'bill_value': 650.00
    }
    
    changes = {
        'qualification_score': 12.3  # Mudança também como float
    }
    
    result = agent._prepare_lead_for_supabase(lead_info, '+5511999999999', changes)
    
    # Verificar que qualification_score foi convertido para int
    assert isinstance(result['qualification_score'], int), "qualification_score deve ser int"
    assert result['qualification_score'] == 12, f"Esperado 12, recebido {result['qualification_score']}"
    
    print(f"  ✅ Float 12.3 convertido para int: {result['qualification_score']}")
    
    # Verificar outros campos
    assert result['phone_number'] == '+5511999999999', "phone_number incorreto"
    assert result['name'] == 'Maria Santos', "name incorreto"
    assert result['email'] == 'maria@example.com', "email incorreto"
    assert result['bill_value'] == 650.00, "bill_value incorreto"
    
    print("  ✅ Todos os campos preparados corretamente!")
    print("  ✅ Todos os testes de preparação passaram!")


async def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("🔬 TESTE: Conversão de qualification_score para INTEGER")
    print("=" * 60)
    
    try:
        # Teste 1: Função de conversão
        test_safe_int_conversion()
        
        # Teste 2: Mapeamento de campos
        await test_map_to_supabase_fields()
        
        # Teste 3: Preparação de lead
        await test_prepare_lead_for_supabase()
        
        print("\n" + "=" * 60)
        print("✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("=" * 60)
        print("\n📋 Resumo:")
        print("  - safe_int_conversion funciona corretamente")
        print("  - _map_to_supabase_fields converte float para int")
        print("  - _prepare_lead_for_supabase converte float para int")
        print("  - Erro 'invalid input syntax for type integer' resolvido!")
        
    except AssertionError as e:
        print(f"\n❌ ERRO NOS TESTES: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())