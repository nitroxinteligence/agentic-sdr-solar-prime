# TODO: Correção da Duplicação de Leads

**Objetivo:** Eliminar a criação de leads duplicados e com dados incorretos no Supabase e no Kommo CRM, centralizando a lógica de criação no agente e condicionando-a à extração de um nome válido.

---

### Fase 1: Diagnóstico e Planejamento

-   [x] **Tarefa 1.1: Analisar o Fluxo de Criação de Leads**
    -   **Status:** Concluído.
    -   **Análise:** O fluxo de ponta a ponta, desde o recebimento da mensagem no webhook até a persistência nos bancos de dados, foi mapeado.

-   [x] **Tarefa 1.2: Identificar a Causa Raiz**
    -   **Status:** Concluído.
    -   **Análise:** A causa foi identificada como a **criação prematura de leads** no arquivo `app/api/webhooks.py`, que ocorria antes da extração de informações essenciais (como o nome) e sem proteção contra condições de corrida.

-   [x] **Tarefa 1.3: Documentar o Diagnóstico e a Solução**
    -   **Status:** Concluído.
    -   **Arquivo:** `DIAGNOSTICO_DUPLICATE_LEADS.md`
    -   **Ação:** Um relatório detalhado foi criado para documentar a análise e a solução proposta.

### Fase 2: Implementação da Correção

-   [x] **Tarefa 2.1: Remover a Criação de Leads do Webhook**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/api/webhooks.py`
    -   **Função:** `process_message_with_agent`
    -   **Ação:**
        -   Localizar o bloco de código: `if not lead: ...`
        -   **Remover completamente** este bloco, que é responsável pela criação prematura do lead no Supabase.
        -   Garantir que a função continue a buscar o lead, mas passe um dicionário vazio (`{}`) para o agente caso o lead não seja encontrado.

-   [x] **Tarefa 2.2: Centralizar a Lógica de Criação no Agente**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/agents/agentic_sdr_stateless.py`
    -   **Função:** `_sync_external_services`
    -   **Ação:**
        -   Modificar a assinatura da função para aceitar o `phone` como parâmetro: `async def _sync_external_services(self, lead_info: dict, phone: str) -> dict:`.
        -   Implementar a nova lógica:
            -   Verificar se `lead_info` já possui um `id`. Se sim, o lead já existe, e a função deve apenas prosseguir para a criação do lead no Kommo (se necessário).
            -   Se `lead_info` não tem `id` **mas tem um `name`**, este é o gatilho para criar um novo lead.
            -   **Passo 1:** Criar o lead no **Supabase** com os dados disponíveis (`phone`, `name`, etc.).
            -   **Passo 2:** Atualizar o `lead_info` local com os dados retornados pelo Supabase (incluindo o novo `id`).
            -   **Passo 3:** Criar o lead no **Kommo CRM**.
            -   **Passo 4:** Atualizar o registro do Supabase com o `kommo_lead_id` retornado.
        -   Atualizar a chamada para esta função em `process_message` para passar o `phone`.

### Fase 3: Validação

-   [ ] **Tarefa 3.1: Validação Manual do Novo Fluxo**
    -   **Status:** Pendente.
    -   **Ação:**
        -   Enviar uma série de mensagens rápidas de um **número de telefone completamente novo**.
        -   **Verificar no Supabase:** Apenas **um** novo lead deve ser criado, e o campo `name` deve estar preenchido corretamente.
        -   **Verificar no Kommo CRM:** Apenas **um** novo lead correspondente deve ser criado.
        -   Verificar se a conversa com um lead existente continua funcionando normalmente, sem criar duplicatas.

-   [ ] **Tarefa 3.2: Atualizar o `todo.md`**
    -   **Status:** Pendente.
    -   **Ação:** Marcar as tarefas de implementação como concluídas neste documento após a validação bem-sucedida.

---