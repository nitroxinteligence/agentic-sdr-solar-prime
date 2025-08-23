# TODO: Otimização do Funil e Correção do Estágio Pós-Agendamento

**Objetivo:** Simplificar o funil do Kommo CRM, garantindo que leads com reunião agendada sejam movidos diretamente para o estágio "Reunião Agendada" e eliminando o uso do estágio intermediário "Qualificado".

---

### Fase 1: Diagnóstico e Planejamento

-   [x] **Tarefa 1.1: Analisar o Fluxo de Agendamento e CRM**
    -   **Status:** Concluído.
    -   **Análise:** O fluxo de ponta a ponta, desde a qualificação até o agendamento e a atualização do CRM, foi mapeado através da análise dos arquivos em `app/**`.

-   [x] **Tarefa 1.2: Identificar a Causa Raiz**
    -   **Status:** Concluído.
    -   **Análise:** A causa foi identificada como uma instrução explícita, porém indesejada, no prompt do agente (`app/prompts/prompt-agente.md`), que o instruía a mover o lead para o estágio "Qualificado" *antes* de agendar a reunião.

-   [x] **Tarefa 1.3: Documentar o Diagnóstico e a Solução**
    -   **Status:** Concluído.
    -   **Arquivo:** `DIAGNOSTICO_FLUXO_AGENDAMENTO.md`
    -   **Ação:** Um relatório detalhado foi criado para documentar a análise e justificar a solução de refatorar o prompt.

### Fase 2: Implementação da Correção

-   [x] **Tarefa 2.1: Refatorar o Prompt do Agente**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/prompts/prompt-agente.md`
    -   **Ação:**
        -   Localizar a seção `<rule id="flow_enforcement_qualification">`.
        -   Dentro da sub-seção `AÇÃO AUTOMÁTICA PÓS-QUALIFICAÇÃO`, remover a linha: `→ [TOOL: crm.update_stage | stage=qualificado]`.
        -   Garantir que a instrução para mover para `reuniao_agendada` após o sucesso do agendamento permaneça intacta.

### Fase 3: Validação

-   [ ] **Tarefa 3.1: Validação Manual do Novo Fluxo**
    -   **Status:** Pendente.
    -   **Ação:**
        -   Iniciar uma conversa com um novo lead (ou um lead de teste em um estágio inicial).
        -   Conduzir a conversa até o ponto de agendar uma reunião com sucesso.
        -   **Verificar no Kommo CRM:**
            -   O lead **não** deve passar pelo estágio "Qualificado".
            -   O lead deve ser movido **diretamente** para o estágio "Reunião Agendada" após a confirmação do agendamento.

-   [x] **Tarefa 3.2: Atualizar o `todo.md`**
    -   **Status:** Pendente.
    -   **Ação:** Marcar as tarefas de implementação como concluídas neste documento após a validação bem-sucedida.

---