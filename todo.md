# TODO: Implementação do Protocolo de Silêncio Pós-Handoff

**Objetivo:** Corrigir a falha de resposta do Gemini que ocorre quando um usuário, já em atendimento humano, envia uma nova mensagem. A solução é criar um protocolo explícito para que o agente permaneça em silêncio sem causar erros no sistema.

---

### Fase 1: Diagnóstico e Planejamento

-   [x] **Tarefa 1.1: Analisar Logs de Erro**
    -   **Status:** Concluído.
    -   **Análise:** Os logs `Gemini response has no valid part` e `finish_reason: 1` foram identificados como o sintoma principal.

-   [x] **Tarefa 1.2: Identificar a Causa Raiz**
    -   **Status:** Concluído.
    -   **Análise:** A causa foi identificada como um conflito lógico. A regra no prompt que proíbe o agente de responder a leads em "Atendimento Humano" faz com que o modelo Gemini retorne uma resposta vazia, o que não é tratado pelo código Python e causa uma exceção.

-   [x] **Tarefa 1.3: Documentar o Diagnóstico e a Solução**
    -   **Status:** Concluído.
    -   **Arquivo:** `DIAGNOSTICO_SILENCE_TAG.md`
    -   **Ação:** Um relatório detalhado foi criado para documentar a análise e a solução proposta.

### Fase 2: Implementação da Correção

-   [x] **Tarefa 2.1: Refatorar o Prompt do Agente com a Tag `<SILENCE>`**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/prompts/prompt-agente.md`
    -   **Ação:**
        -   Localizar a regra `id="human_takeover_guardrail"`.
        -   Substituir a instrução `você está ESTRITAMENTE PROIBIDA de enviar qualquer mensagem` por `sua ÚNICA E EXCLUSIVA resposta DEVE ser a tag <SILENCE>. Nenhuma outra palavra ou caractere é permitido.`.

-   [x] **Tarefa 2.2: Implementar a Interceptação da Tag `<SILENCE>` no Código**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/api/webhooks.py`
    -   **Função:** `process_message_with_agent`
    -   **Ação:**
        -   Após a linha `final_response = extract_final_response(response_text)`.
        -   Adicionar uma condição para verificar se `final_response` contém a string `<SILENCE>`.
        -   Se a condição for verdadeira, registrar um log informando que o silêncio foi intencional e **interromper a execução da função** (usando `return`), para que nenhuma mensagem seja enviada ao usuário.

### Fase 3: Validação

-   [ ] **Tarefa 3.1: Validação Manual do Novo Fluxo**
    -   **Status:** Pendente.
    -   **Ação:**
        -   Iniciar uma conversa e prosseguir até o ponto de handoff (ex: escolher "Usina de Investimento").
        -   Verificar se o lead é movido para "Atendimento Humano" no Kommo.
        -   **Enviar uma nova mensagem para o agente** (ex: "Obrigado").
        -   **Verificar os logs:**
            -   O erro do Gemini (`Gemini response has no valid part`) **não** deve mais aparecer.
            -   Deve haver um log indicando que a tag `<SILENCE>` foi recebida e o envio da mensagem foi intencionalmente ignorado.
        -   **Verificar o WhatsApp:** O usuário **não** deve receber nenhuma resposta do agente.

-   [ ] **Tarefa 3.2: Atualizar o `todo.md`**
    -   **Status:** Pendente.
    -   **Ação:** Marcar as tarefas de implementação como concluídas neste documento após a validação bem-sucedida.

---