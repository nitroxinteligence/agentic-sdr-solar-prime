#!/usr/bin/env python
"""
📋 Listar todos os stages do Kommo
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.services.crm_service_100_real import CRMServiceReal

async def list_all_stages():
    """Lista todos os stages disponíveis"""
    
    print("\n" + "="*60)
    print("📋 TODOS OS STAGES DO KOMMO CRM")
    print("="*60)
    
    try:
        crm = CRMServiceReal()
        await crm.initialize()
        
        # Agrupar por nome original (sem transformações)
        unique_stages = {}
        for stage_name, stage_id in crm.stage_map.items():
            # Pular variações em maiúsculas e com underscore
            if stage_name.isupper() or "_" in stage_name:
                continue
            if stage_id not in unique_stages.values():
                unique_stages[stage_name] = stage_id
        
        print(f"\n📊 Total de stages únicos: {len(unique_stages)}")
        print("\n📋 Lista de stages:")
        
        for i, (name, id) in enumerate(sorted(unique_stages.items()), 1):
            print(f"   {i:2}. {name:<30} → ID: {id}")
        
        await crm.close()
        
        print("\n✅ Lista completa gerada com sucesso")
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(list_all_stages())