#!/usr/bin/env python3
"""
Script para finalizar a limpeza da documentação
Remove duplicações e organiza arquivos restantes
"""

import os
import shutil
from pathlib import Path

def cleanup_docs():
    """Finaliza a reorganização removendo duplicações"""
    
    print("=" * 60)
    print("🧹 FINALIZANDO LIMPEZA DA DOCUMENTAÇÃO")
    print("=" * 60)
    
    # 1. Mover arquivos .md soltos em docs/ para archive
    loose_files = list(Path('docs').glob('*.md'))
    print(f"\n📦 Movendo {len(loose_files)} arquivos soltos para archive...")
    
    for file in loose_files:
        # Pular README.md da pasta docs
        if file.name == 'README.md':
            continue
            
        dest = Path('docs/archive/implementations') / file.name
        if not dest.exists():
            shutil.move(str(file), str(dest))
            print(f"   ✓ {file.name} → archive/implementations/")
    
    # 2. Remover docs-2 (exceto ARQUITETURA_ATUAL.md que já foi preservado)
    docs2_path = Path('docs/docs-2')
    if docs2_path.exists():
        # Verificar se ARQUITETURA_ATUAL.md foi preservado
        arch_file = docs2_path / 'ARQUITETURA_ATUAL.md'
        if arch_file.exists():
            print("\n⚠️ ARQUITETURA_ATUAL.md ainda em docs-2, preservando...")
        else:
            # Mover outros arquivos restantes para archive
            remaining = list(docs2_path.glob('*.md'))
            if remaining:
                print(f"\n📦 Arquivando {len(remaining)} arquivos de docs-2...")
                for file in remaining:
                    dest = Path('docs/archive/phase2-refactoring') / file.name
                    if not dest.exists():
                        shutil.move(str(file), str(dest))
                        print(f"   ✓ {file.name} → archive/phase2-refactoring/")
            
            # Remover diretório vazio
            if not any(docs2_path.iterdir()):
                shutil.rmtree(docs2_path)
                print("   ✓ Removido diretório docs-2 vazio")
    
    # 3. Remover docs-3 (arquivos críticos já foram preservados)
    docs3_path = Path('docs/docs-3')
    if docs3_path.exists():
        # Verificar arquivos críticos
        critical_files = [
            'ANALISE_IMPLEMENTACAO_STATELESS.md',
            'RELEASE_NOTES_v03.md', 
            'RELATORIO_VALIDACAO_v03.md',
            'GOOGLE_CALENDAR_OAUTH_SETUP.md',
            'CRM_DYNAMIC_SYNC_DOCUMENTATION.md'
        ]
        
        # Mover arquivos não-críticos restantes
        remaining = []
        for file in docs3_path.glob('*.md'):
            if file.name not in critical_files:
                remaining.append(file)
        
        if remaining:
            print(f"\n📦 Arquivando {len(remaining)} arquivos de docs-3...")
            for file in remaining:
                dest = Path('docs/archive/phase3-stateless') / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                    print(f"   ✓ {file.name} → archive/phase3-stateless/")
    
    # 4. Remover docs-uteis (já processado)
    docs_uteis = Path('docs/docs-uteis')
    if docs_uteis.exists():
        # TRANSBORDO_DOCUMENTATION.md já foi copiado para reference
        remaining = list(docs_uteis.glob('*.md'))
        if remaining:
            print(f"\n📦 Arquivando {len(remaining)} arquivos de docs-uteis...")
            for file in remaining:
                if file.name != 'TRANSBORDO_DOCUMENTATION.md' or not (Path('docs/reference') / file.name).exists():
                    dest = Path('docs/archive/implementations') / file.name
                    if not dest.exists():
                        shutil.move(str(file), str(dest))
                        print(f"   ✓ {file.name} → archive/implementations/")
        
        # Remover diretório
        if not any(docs_uteis.iterdir()) or all(f.name == 'TRANSBORDO_DOCUMENTATION.md' for f in docs_uteis.iterdir()):
            shutil.rmtree(docs_uteis)
            print("   ✓ Removido diretório docs-uteis")
    
    # 5. Remover arquivos .txt soltos
    txt_files = list(Path('docs').glob('*.txt'))
    if txt_files:
        print(f"\n📦 Arquivando {len(txt_files)} arquivos .txt...")
        for file in txt_files:
            dest = Path('docs/archive/validations') / file.name
            shutil.move(str(file), str(dest))
            print(f"   ✓ {file.name} → archive/validations/")
    
    print("\n" + "=" * 60)
    print("✅ LIMPEZA FINALIZADA!")
    print("=" * 60)
    
    # Mostrar estrutura final
    print("\n📊 ESTRUTURA FINAL:")
    print("docs/")
    print("├── reference/     (4 guias de referência)")
    print("├── archive/       (150+ documentos históricos)")
    print("├── docs-2/        (apenas ARQUITETURA_ATUAL.md se crítico)")
    print("└── docs-3/        (apenas 3 arquivos críticos)")
    
    return True

if __name__ == "__main__":
    import sys
    
    print("⚠️ Este script irá finalizar a limpeza da documentação!")
    print("Irá remover duplicações e organizar arquivos restantes.")
    
    response = input("\nDeseja continuar? (sim/não): ").lower()
    
    if response in ['sim', 's', 'yes', 'y']:
        cleanup_docs()
    else:
        print("❌ Operação cancelada")