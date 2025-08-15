#!/usr/bin/env python3
"""
Script de Limpeza de Código Obsoleto - SDR IA SolarPrime v0.3
Remove código singleton e duplicações após migração para stateless
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple

class CodeCleanup:
    """Gerenciador de limpeza de código obsoleto"""
    
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.backup_dir = self.base_path / f"backup_obsolete_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.changes_log = []
        self.files_to_remove = []
        self.files_to_update = []
        
    def analyze_obsolete_files(self) -> Dict[str, List[Tuple[str, str]]]:
        """Analisa e categoriza arquivos obsoletos"""
        
        obsolete = {
            "high_priority": [
                ("app/agents/agentic_sdr_refactored.py", "Código singleton completamente obsoleto"),
                ("app/services/followup_executor_safe.py", "Duplicação - usar followup_executor_service.py"),
                ("app/integrations/google_oauth_safe.py", "Duplicação - usar google_oauth_handler.py"),
            ],
            "medium_priority": [
                ("app/database/supabase_client.py", "Duplicação - usar app/integrations/supabase_client.py"),
            ],
            "files_to_update": [
                ("app/agents/__init__.py", "Remover exports singleton"),
                ("main.py", "Remover imports singleton"),
                ("app/api/webhooks.py", "Remover lógica singleton"),
            ]
        }
        
        return obsolete
    
    def create_backup(self, file_path: str) -> bool:
        """Cria backup do arquivo antes de remover"""
        try:
            source = self.base_path / file_path
            if not source.exists():
                print(f"⚠️  Arquivo não encontrado: {file_path}")
                return False
                
            # Criar estrutura de diretórios no backup
            dest = self.backup_dir / file_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            
            # Copiar arquivo
            shutil.copy2(source, dest)
            print(f"💾 Backup criado: {file_path}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao criar backup de {file_path}: {e}")
            return False
    
    def remove_file(self, file_path: str, reason: str) -> bool:
        """Remove arquivo obsoleto com segurança"""
        try:
            # Criar backup primeiro
            if not self.create_backup(file_path):
                return False
            
            # Remover arquivo
            full_path = self.base_path / file_path
            if full_path.exists():
                full_path.unlink()
                self.changes_log.append(f"🗑️  REMOVIDO: {file_path} - {reason}")
                print(f"✅ Removido: {file_path}")
                return True
                
        except Exception as e:
            print(f"❌ Erro ao remover {file_path}: {e}")
            return False
    
    def update_agents_init(self):
        """Atualiza app/agents/__init__.py para remover singleton"""
        file_path = self.base_path / "app/agents/__init__.py"
        
        if not file_path.exists():
            return
            
        self.create_backup("app/agents/__init__.py")
        
        new_content = '''"""
Módulo de Agentes - SDR IA SolarPrime v0.3
Arquitetura Stateless
"""

from app.agents.agentic_sdr_stateless import (
    AgenticSDRStateless,
    create_stateless_agent
)

__all__ = [
    'AgenticSDRStateless',
    'create_stateless_agent'
]
'''
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        self.changes_log.append("📝 ATUALIZADO: app/agents/__init__.py - Removidos exports singleton")
        print("✅ Atualizado: app/agents/__init__.py")
    
    def update_main_py(self):
        """Atualiza main.py para remover referências singleton"""
        file_path = self.base_path / "main.py"
        
        if not file_path.exists():
            return
            
        self.create_backup("main.py")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remover imports singleton
        replacements = [
            ("from app.agents import get_agentic_agent, reset_agent", "# Singleton removido - usando stateless"),
            ("get_agentic_agent", "create_stateless_agent"),
            ("reset_agent()", "# Reset não necessário em stateless"),
        ]
        
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
                self.changes_log.append(f"📝 SUBSTITUÍDO: '{old}' por '{new}' em main.py")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Atualizado: main.py")
    
    def update_webhooks(self):
        """Atualiza webhooks.py para usar apenas stateless"""
        file_path = self.base_path / "app/api/webhooks.py"
        
        if not file_path.exists():
            return
            
        self.create_backup("app/api/webhooks.py")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remover condicionais de USE_STATELESS_MODE
        replacements = [
            ("if settings.use_stateless_mode:", "# Sempre usar stateless"),
            ("from app.agents import get_agentic_agent", "# Singleton removido"),
            ("agent = await get_agentic_agent()", "agent = await create_stateless_agent()"),
        ]
        
        for old, new in replacements:
            if old in content:
                content = content.replace(old, new)
                self.changes_log.append(f"📝 SUBSTITUÍDO: '{old}' em webhooks.py")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Atualizado: app/api/webhooks.py")
    
    def generate_report(self):
        """Gera relatório de limpeza"""
        report_path = self.base_path / f"cleanup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        report = f"""# 📊 Relatório de Limpeza de Código Obsoleto

**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Backup**: {self.backup_dir}

## 📋 Resumo das Alterações

### Arquivos Removidos
"""
        
        for log in self.changes_log:
            if "REMOVIDO" in log:
                report += f"- {log}\n"
        
        report += "\n### Arquivos Atualizados\n"
        
        for log in self.changes_log:
            if "ATUALIZADO" in log or "SUBSTITUÍDO" in log:
                report += f"- {log}\n"
        
        report += f"""

## 🔄 Como Reverter

Para reverter as mudanças, restaure os arquivos do diretório de backup:
```bash
cp -r {self.backup_dir}/* .
```

## ✅ Próximos Passos

1. Testar o sistema após limpeza
2. Commit das mudanças após validação
3. Remover diretório de backup após confirmação
4. Atualizar documentação se necessário
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\n📄 Relatório salvo em: {report_path}")
        return report_path
    
    def execute_cleanup(self, dry_run: bool = False):
        """Executa limpeza completa"""
        print("=" * 60)
        print("🧹 LIMPEZA DE CÓDIGO OBSOLETO - SDR IA v0.3")
        print("=" * 60)
        
        if dry_run:
            print("🔍 MODO DRY RUN - Nenhuma alteração será feita\n")
        else:
            print(f"💾 Backup será criado em: {self.backup_dir}\n")
            self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Analisar arquivos obsoletos
        obsolete = self.analyze_obsolete_files()
        
        # Processar alta prioridade (remover)
        print("\n🔴 ALTA PRIORIDADE - Removendo arquivos obsoletos:")
        print("-" * 40)
        
        for file_path, reason in obsolete["high_priority"]:
            if dry_run:
                print(f"[DRY RUN] Removeria: {file_path}")
                print(f"  Motivo: {reason}")
            else:
                self.remove_file(file_path, reason)
        
        # Processar média prioridade (remover duplicações)
        print("\n🟡 MÉDIA PRIORIDADE - Removendo duplicações:")
        print("-" * 40)
        
        for file_path, reason in obsolete["medium_priority"]:
            if dry_run:
                print(f"[DRY RUN] Removeria: {file_path}")
                print(f"  Motivo: {reason}")
            else:
                self.remove_file(file_path, reason)
        
        # Atualizar arquivos
        print("\n📝 ATUALIZANDO ARQUIVOS:")
        print("-" * 40)
        
        if dry_run:
            print("[DRY RUN] Atualizaria: app/agents/__init__.py")
            print("[DRY RUN] Atualizaria: main.py")
            print("[DRY RUN] Atualizaria: app/api/webhooks.py")
        else:
            self.update_agents_init()
            self.update_main_py()
            self.update_webhooks()
        
        # Gerar relatório
        if not dry_run:
            report_path = self.generate_report()
            
            print("\n" + "=" * 60)
            print("✅ LIMPEZA CONCLUÍDA!")
            print("=" * 60)
            print(f"\n📊 Total de mudanças: {len(self.changes_log)}")
            print(f"💾 Backup salvo em: {self.backup_dir}")
            print(f"📄 Relatório: {report_path}")
        else:
            print("\n" + "=" * 60)
            print("🔍 DRY RUN CONCLUÍDO")
            print("=" * 60)
            print("\nPara executar a limpeza real, rode:")
            print("python cleanup_obsolete_code.py --execute")

def main():
    """Função principal"""
    import sys
    
    cleanup = CodeCleanup()
    
    if "--execute" in sys.argv:
        print("⚠️  ATENÇÃO: Esta operação irá remover arquivos obsoletos!")
        print("Um backup será criado automaticamente.")
        
        response = input("\nDeseja continuar? (sim/não): ").lower()
        
        if response in ['sim', 's', 'yes', 'y']:
            cleanup.execute_cleanup(dry_run=False)
        else:
            print("❌ Operação cancelada")
    else:
        cleanup.execute_cleanup(dry_run=True)

if __name__ == "__main__":
    main()