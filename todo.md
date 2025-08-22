# Plano de Ação para Sincronização do Agente (Prompt vs. Código)

Este plano detalha as tarefas necessárias para alinhar a implementação do código com as funcionalidades descritas no `prompt-agente.md`.

## Tarefas de Prioridade Alta

- [x] **GAP 1: Integrar a Base de Conhecimento (Knowledge Base)**
    - [x] **Código:** Importar e inicializar `KnowledgeService` no `AgenticSDRStateless`.
    - [x] **Código:** Modificar `_execute_single_tool` para incluir um novo `service_name` chamado `knowledge` com o método `search`.
    - [x] **Prompt:** Adicionar a ferramenta `[TOOL: knowledge.search | query=<termo_de_busca>]` à seção `<tool_calling_system>` para que o agente possa acioná-la.

## Tarefas de Prioridade Média

- [ ] **GAP 2: Implementar Gerenciamento de Estado dos Fluxos de Vendas (A, B, C, D)**
    - [ ] **Código:** Expandir `ContextAnalyzer` para detectar e retornar `current_flow` e `flow_step`.
    - [ ] **Código:** Garantir que `lead_info` persista o estado do fluxo entre as mensagens.
    - [ ] **Prompt:** Adicionar placeholders no prompt para receber as novas variáveis de estado do fluxo.

## Tarefas de Prioridade Baixa (Correções Rápidas)

- [x] **INCONSISTÊNCIA 1: Corrigir Horário de Atendimento**
    - [x] **Código:** Alterar `"end_hour": 17` para `"end_hour": 18` em `app/services/calendar_service_100_real.py`.