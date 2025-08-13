#!/usr/bin/env python
"""
🔍 Teste de Stage Mapping PT/EN
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.crm_service_100_real import CRMServiceReal

async def test_stage_mapping():
    """Testa o mapeamento de stages PT/EN"""
    
    print("\n" + "="*60)
    print("🔍 TESTE DE STAGE MAPPING PT/EN")
    print("="*60)
    
    try:
        crm = CRMServiceReal()
        await crm.initialize()
        
        # Stages que devem estar mapeados
        stages_to_test = {
            "PT": ["qualificado", "proposta enviada", "negociacao", "não interessado"],
            "EN": ["QUALIFIED", "PROPOSAL_SENT", "NEGOTIATION", "NOT_INTERESTED"]
        }
        
        print(f"\n📊 Total de stages mapeados: {len(crm.stage_map)}")
        
        # Verificar cada stage
        missing = []
        found = []
        
        for lang, stages in stages_to_test.items():
            print(f"\n🔍 Testando stages em {lang}:")
            for stage in stages:
                # Procurar variações
                stage_id = None
                variations = [
                    stage,
                    stage.lower(),
                    stage.upper(),
                    stage.replace(" ", "_"),
                    stage.replace(" ", "_").lower()
                ]
                
                for var in variations:
                    if var in crm.stage_map:
                        stage_id = crm.stage_map[var]
                        break
                
                if stage_id:
                    found.append(stage)
                    print(f"   ✅ {stage} → ID: {stage_id}")
                else:
                    missing.append(stage)
                    print(f"   ❌ {stage} → NÃO ENCONTRADO")
        
        # Mostrar alguns stages que existem
        print(f"\n📋 Amostra de stages disponíveis:")
        for i, (name, id) in enumerate(list(crm.stage_map.items())[:10]):
            print(f"   - {name}: {id}")
        
        await crm.close()
        
        # Resultado
        print(f"\n📊 Resultado:")
        print(f"   ✅ Encontrados: {len(found)}/{len(found) + len(missing)}")
        print(f"   ❌ Ausentes: {len(missing)}/{len(found) + len(missing)}")
        
        if missing:
            print(f"\n⚠️ Stages ausentes: {', '.join(missing)}")
        
        return len(missing) == 0
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_stage_mapping())
    sys.exit(0 if success else 1)