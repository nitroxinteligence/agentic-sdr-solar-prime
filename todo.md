# TODO - Plano de Ação do Projeto

## Tarefa Atual: Corrigir Inconsistência de Esquema do Banco de Dados

-   [x] **Análise e Diagnóstico:**
    -   [x] Analisar o erro `PGRST204 - Could not find column 'current_stage_id'`.
    -   [x] Identificar a causa como uma migração de banco de dados ausente.
    -   [x] Criar o relatório `DIAGNOSTICO_DB_SCHEMA_ERROR.md`.

-   [x] **Implementação da Correção:**
    -   [x] **Ação:** Criar um novo arquivo de migração SQL.
    -   [x] **Arquivo:** `migrations/20250824_add_stage_id_to_leads.sql`
    -   [x] **Conteúdo:** Adicionar o comando `ALTER TABLE leads ADD COLUMN current_stage_id BIGINT;` ao arquivo.

-   [x] **Verificação e Validação:**
    -   [x] Informar ao usuário sobre a necessidade de aplicar a nova migração no Supabase.

-   [ ] **Finalização:**
    -   [ ] Realizar o commit da migração.

---

## Tarefas Anteriores
-   [x] **Corrigir Pausa de Handoff para ser Baseada em Estado:** Concluído.
-   [x] **Implementar Sincronização Ativa de Handoff:** Concluído.
-   [x] **Correção Webhook Kommo:** Concluído.
-   [x] **Correção Crítica do Protocolo de Silêncio:** Concluído.
-   [x] **Correção Crítica do Sistema de Follow-up:** Concluído.
