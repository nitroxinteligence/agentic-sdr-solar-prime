#!/usr/bin/env python3
"""
Script de Reorganização da Documentação
SDR IA SolarPrime v0.3
Implementa o plano definido em ANALISE_DOCUMENTACAO.md
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import json

class DocumentationReorganizer:
    """Reorganiza 173 documentos em estrutura clara e navegável"""
    
    def __init__(self):
        self.base_path = Path.cwd()
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.log = []
        self.stats = {
            'critical': [],
            'reference': [],
            'archived': [],
            'errors': []
        }
        
    def log_action(self, action, details):
        """Registra ações realizadas"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'details': details
        }
        self.log.append(entry)
        print(f"{action}: {details}")
        
    def create_directory_structure(self):
        """Cria estrutura de diretórios para reorganização"""
        print("\n📁 Criando estrutura de diretórios...")
        
        directories = [
            'docs/reference',
            'docs/archive',
            'docs/archive/phase1-gemini-errors',
            'docs/archive/phase2-refactoring',
            'docs/archive/phase3-stateless',
            'docs/archive/agno-framework',
            'docs/archive/diagnostics',
            'docs/archive/implementations',
            'docs/archive/validations'
        ]
        
        for dir_path in directories:
            full_path = self.base_path / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
            self.log_action("📁 Diretório criado", str(dir_path))
            
    def identify_critical_files(self):
        """Identifica e preserva arquivos críticos"""
        print("\n🔴 Identificando arquivos CRÍTICOS...")
        
        critical_files = [
            'README.md',
            'docs/docs-3/ANALISE_IMPLEMENTACAO_STATELESS.md',
            'docs/docs-3/RELEASE_NOTES_v03.md', 
            'docs/docs-3/RELATORIO_VALIDACAO_v03.md',
            'docs/docs-2/ARQUITETURA_ATUAL.md'
        ]
        
        for file_path in critical_files:
            full_path = self.base_path / file_path
            if full_path.exists():
                self.stats['critical'].append(str(file_path))
                self.log_action("✅ CRÍTICO preservado", file_path)
            else:
                self.log_action("⚠️ CRÍTICO não encontrado", file_path)
                
    def move_reference_files(self):
        """Move arquivos úteis para pasta de referência"""
        print("\n🟡 Movendo arquivos de REFERÊNCIA...")
        
        reference_files = {
            'docs/AGNO_FRAMEWORK_GUIDE-2.md': 'AGNO_FRAMEWORK_GUIDE.md',
            'docs/docs-3/GOOGLE_CALENDAR_OAUTH_SETUP.md': 'GOOGLE_CALENDAR_OAUTH_SETUP.md',
            'docs/docs-3/CRM_DYNAMIC_SYNC_DOCUMENTATION.md': 'CRM_DYNAMIC_SYNC_DOCUMENTATION.md',
            'docs/docs-uteis/TRANSBORDO_DOCUMENTATION.md': 'TRANSBORDO_DOCUMENTATION.md'
        }
        
        for src, dst_name in reference_files.items():
            src_path = self.base_path / src
            dst_path = self.base_path / 'docs' / 'reference' / dst_name
            
            if src_path.exists():
                try:
                    shutil.copy2(src_path, dst_path)
                    self.stats['reference'].append(dst_name)
                    self.log_action("📚 REFERÊNCIA copiado", f"{src} → docs/reference/{dst_name}")
                except Exception as e:
                    self.stats['errors'].append(f"Erro ao mover {src}: {e}")
                    self.log_action("❌ Erro", str(e))
                    
    def archive_obsolete_files(self):
        """Arquiva documentos obsoletos mantendo histórico"""
        print("\n⚫ Arquivando documentos OBSOLETOS...")
        
        # Mapeamento de padrões para destinos
        archive_mappings = [
            # Fase 1 - Erros do Gemini
            ('*GEMINI*ERROR*.md', 'phase1-gemini-errors'),
            ('*500_ERROR*.md', 'phase1-gemini-errors'),
            ('*RETRY*.md', 'phase1-gemini-errors'),
            
            # Fase 2 - Refatoração
            ('*REFACTOR*.md', 'phase2-refactoring'),
            ('*LIMPEZA*.md', 'phase2-refactoring'),
            ('*REDUNDANCY*.md', 'phase2-refactoring'),
            
            # Fase 3 - Stateless (mas não os críticos)
            ('*STATELESS*.md', 'phase3-stateless'),
            ('*SINGLETON*.md', 'phase3-stateless'),
            
            # Framework AGNO
            ('*AGNO*.md', 'agno-framework'),
            ('*FRAMEWORK*.md', 'agno-framework'),
            
            # Diagnósticos
            ('*DIAGNOSTICO*.md', 'diagnostics'),
            ('*ANALISE*.md', 'diagnostics'),
            ('*ERROR*.md', 'diagnostics'),
            
            # Implementações
            ('*IMPLEMENTATION*.md', 'implementations'),
            ('*SOLUTION*.md', 'implementations'),
            ('*FIX*.md', 'implementations'),
            
            # Validações
            ('*VALIDATION*.md', 'validations'),
            ('*TEST*.md', 'validations'),
            ('*RELATORIO*.md', 'validations')
        ]
        
        # Buscar arquivos em todas as subpastas de docs
        for pattern, dest_folder in archive_mappings:
            for doc_file in Path('docs').rglob(pattern):
                # Pular se for arquivo crítico ou de referência
                if any(critical in str(doc_file) for critical in self.stats['critical']):
                    continue
                if 'reference' in str(doc_file) or 'archive' in str(doc_file):
                    continue
                    
                dest_path = self.base_path / 'docs' / 'archive' / dest_folder / doc_file.name
                
                # Evitar sobrescrever arquivos
                if dest_path.exists():
                    dest_path = dest_path.with_stem(f"{doc_file.stem}_{self.timestamp}")
                
                try:
                    shutil.copy2(doc_file, dest_path)
                    self.stats['archived'].append(doc_file.name)
                    self.log_action("📦 ARQUIVADO", f"{doc_file.name} → archive/{dest_folder}/")
                    
                    # Remover arquivo original após copiar
                    doc_file.unlink()
                    
                except Exception as e:
                    self.stats['errors'].append(f"Erro ao arquivar {doc_file}: {e}")
                    self.log_action("❌ Erro", str(e))
                    
    def create_consolidated_documentation(self):
        """Cria documentação consolidada"""
        print("\n📝 Criando documentação consolidada...")
        
        # Criar SYSTEM_ARCHITECTURE.md
        architecture_content = """# 🏗️ Arquitetura do Sistema - SDR IA SolarPrime v0.3

## Visão Geral

Sistema de SDR (Sales Development Representative) automatizado para energia solar, 
utilizando IA conversacional com arquitetura **100% stateless** para máxima escalabilidade.

## 🎯 Características Principais

- **Arquitetura Stateless**: Cada requisição cria nova instância, sem compartilhamento de estado
- **Multi-usuário**: Suporte ilimitado de conversas simultâneas
- **Rate Limiting**: Proteção contra limites de API (Kommo, Google, etc)
- **Multimodal**: Processamento de texto, imagem, áudio e documentos
- **Integração Completa**: WhatsApp, Kommo CRM, Google Calendar, Supabase

## 🏛️ Arquitetura Stateless

### Por que Stateless?
- ✅ **Escalabilidade Horizontal**: Adicione workers conforme necessário
- ✅ **Thread-Safety**: Sem riscos de contaminação entre conversas
- ✅ **Simplicidade**: Sem gerenciamento complexo de estado
- ✅ **Cloud-Native**: Pronto para Kubernetes, Lambda, etc

### Implementação
```python
# Cada mensagem cria nova instância
agent = await create_stateless_agent()

# Contexto passado explicitamente
execution_context = {
    'phone': phone_number,
    'conversation_history': history,
    'lead_info': lead_data
}

response = await agent.process_message(message, execution_context)
```

## 📦 Componentes Principais

### 1. AgenticSDR Stateless
- Agente conversacional principal
- Personalidade ultra-humanizada (Helen)
- Decision engine para ativação de agentes especializados

### 2. Team Agents
- **CalendarAgent**: Agendamento com Google Calendar
- **CRMAgent**: Gestão de leads no Kommo
- **FollowUpAgent**: Nutrição automática de leads
- **QualificationAgent**: Scoring de leads
- **KnowledgeAgent**: Base de conhecimento
- **BillAnalyzerAgent**: Análise de contas de energia

### 3. Integrações

#### Evolution API v2
- Integração WhatsApp Business
- Processamento de mídia
- Indicadores de digitação

#### Kommo CRM
- Pipeline completo de vendas
- Mapeamento PT/EN de stages
- Update dinâmico de campos
- Rate limiting integrado

#### Supabase
- PostgreSQL + pgvector
- Memória semântica
- Persistência de conversas
- Estado emocional

#### Redis
- Buffer de mensagens
- Cache de stages
- Rate limiting

## 🔄 Fluxo de Mensagens

```
WhatsApp → Evolution API → Webhook → Message Buffer → AgenticSDR → Response
                                              ↓                        ↓
                                         Redis Cache            Kommo CRM/Supabase
```

## ⚡ Performance

- **Inicialização**: <0.5s
- **Tempo de resposta**: ~13s por conversa
- **Conversas simultâneas**: Ilimitado
- **Taxa de sucesso**: 98%

## 🛠️ Tecnologias

- **Framework**: FastAPI + AGnO v1.7.6
- **IA**: Gemini 2.5 Pro + Reasoning
- **Database**: PostgreSQL + pgvector
- **Cache**: Redis
- **WhatsApp**: Evolution API v2
- **CRM**: Kommo
- **Calendar**: Google Calendar OAuth 2.0

## 📊 Configuração

Todas as funcionalidades controladas via environment variables:

```env
USE_STATELESS_MODE=true
ENABLE_MULTIMODAL_ANALYSIS=true
ENABLE_CALENDAR_AGENT=true
ENABLE_CRM_AGENT=true
PRIMARY_AI_MODEL=gemini-2.5-pro
```

## 🚀 Evolução do Sistema

### v0.1 - MVP Singleton
- Arquitetura singleton básica
- Proof of concept funcional
- Problemas de concorrência

### v0.2 - Refatoração Modular
- Separação em módulos
- Melhoria de performance
- Ainda com limitações de escala

### v0.3 - Pure Stateless (Atual)
- Arquitetura 100% stateless
- Rate limiting integrado
- Pronto para produção em escala

## 📚 Documentação Adicional

- [Guias de Referência](./docs/reference/) - Setup e configuração
- [Arquivo Histórico](./docs/archive/) - Documentação histórica do projeto

---

**Última atualização**: 15/08/2025  
**Versão**: 0.3 - Pure Stateless Architecture
"""
        
        arch_path = self.base_path / 'SYSTEM_ARCHITECTURE.md'
        arch_path.write_text(architecture_content, encoding='utf-8')
        self.log_action("📄 Criado", "SYSTEM_ARCHITECTURE.md")
        
    def generate_report(self):
        """Gera relatório da reorganização"""
        print("\n📊 Gerando relatório...")
        
        report = {
            'timestamp': self.timestamp,
            'statistics': {
                'critical_files': len(self.stats['critical']),
                'reference_files': len(self.stats['reference']),
                'archived_files': len(self.stats['archived']),
                'errors': len(self.stats['errors'])
            },
            'details': self.stats,
            'log': self.log
        }
        
        # Salvar relatório JSON
        report_path = self.base_path / f'reorganization_report_{self.timestamp}.json'
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
            
        # Exibir resumo
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO DE REORGANIZAÇÃO")
        print("=" * 60)
        print(f"✅ Arquivos críticos preservados: {len(self.stats['critical'])}")
        print(f"📚 Arquivos de referência organizados: {len(self.stats['reference'])}")
        print(f"📦 Arquivos arquivados: {len(self.stats['archived'])}")
        
        if self.stats['errors']:
            print(f"❌ Erros encontrados: {len(self.stats['errors'])}")
            for error in self.stats['errors']:
                print(f"   - {error}")
        
        print(f"\n💾 Relatório salvo em: {report_path}")
        
        return report
        
    def run(self, dry_run=False):
        """Executa reorganização completa"""
        print("=" * 60)
        print("🚀 REORGANIZAÇÃO DA DOCUMENTAÇÃO - SDR IA v0.3")
        print("=" * 60)
        
        if dry_run:
            print("🔍 MODO DRY RUN - Nenhuma alteração será feita")
            return
        
        # Executar etapas
        self.create_directory_structure()
        self.identify_critical_files()
        self.move_reference_files()
        self.archive_obsolete_files()
        self.create_consolidated_documentation()
        report = self.generate_report()
        
        print("\n✅ Reorganização concluída com sucesso!")
        
        # Sugestão de próximos passos
        print("\n📝 Próximos passos:")
        print("1. Revisar SYSTEM_ARCHITECTURE.md")
        print("2. Atualizar README.md com nova estrutura")
        print("3. Commit das mudanças:")
        print("   git add -A")
        print("   git commit -m 'docs: Reorganização completa da documentação'")
        print("4. Push para o GitHub")
        
        return report

def main():
    """Função principal"""
    import sys
    
    reorganizer = DocumentationReorganizer()
    
    if "--dry-run" in sys.argv:
        reorganizer.run(dry_run=True)
    else:
        print("⚠️ Este script irá reorganizar toda a documentação!")
        print("Um relatório será gerado com todas as ações.")
        
        response = input("\nDeseja continuar? (sim/não): ").lower()
        
        if response in ['sim', 's', 'yes', 'y']:
            reorganizer.run()
        else:
            print("❌ Operação cancelada")

if __name__ == "__main__":
    main()