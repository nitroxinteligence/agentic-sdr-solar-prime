# Plano de Ação Estratégico: Resolução de Erros de Parsing do LLM e Estabilização do Agente

*Objetivo: Eliminar erros de `re.error: unbalanced parenthesis` e garantir a robustez do agente contra saídas malformadas do LLM, além de estabilizar o sistema de follow-up.*

---

### Fase 1: Diagnóstico Aprofundado do Erro de Parsing do LLM

-   [ ] **1.1. Capturar Resposta Bruta do LLM:**
    -   **Ação:** Adicionar um log de nível `DEBUG` em `app/agents/agentic_sdr_stateless.py`, no método `_parse_and_execute_tools`, para registrar a `response` completa (string bruta) *antes* de `re.findall` ser chamado.
    -   **Justificativa:** Precisamos ver o conteúdo exato que está causando o `re.error` para identificar o padrão problemático.

-   [ ] **1.2. Implementar Tratamento Defensivo de `re.error`:**
    -   **Ação:** Envolver a chamada `re.findall(tool_pattern, response)` em um bloco `try-except re.error`.
    -   **Comportamento em Erro:** Se `re.error` for capturado, logar o erro completo e a `response` que o causou, e retornar um dicionário vazio (`{}`) para `tool_results`.
    -   **Justificativa:** Prevenir o crash do agente e fornecer informações cruciais para depuração sem interromper o fluxo.

---

### Fase 2: Refatoração e Prevenção de Erros do LLM

-   [ ] **2.1. Reforçar Prompting para Saída Estruturada:**
    -   **Ação:** Revisar `app/prompts/prompt-agente.md`. Adicionar instruções explícitas e exemplos para o LLM sobre como *não* gerar caracteres especiais de regex (`[`, `]`, `(`, `)`) em seu texto de resposta final, a menos que sejam parte de uma `[TOOL: ...]` bem formada.
    -   **Justificativa:** Reduzir a probabilidade de o LLM gerar saídas que quebrem o parser.

-   [ ] **2.2. Aprimorar a Regex de Parsing de Tools (se necessário):**
    -   **Ação:** Com base na análise da `response` bruta (após a Fase 1.1), ajustar a `tool_pattern` em `_parse_and_execute_tools` para ser mais resiliente a variações ou malformações *esperadas* do LLM, se houver.
    -   **Justificativa:** Tornar o parser mais tolerante a pequenas inconsistências na saída do LLM.

---

### Fase 3: Retomada e Estabilização do Sistema de Follow-up

-   [ ] **3.1. Validar Correção da Contagem de Follow-ups:**
    -   **Ação:** Confirmar que a correção em `app/integrations/supabase_client.py` (`get_recent_followup_count`) resolveu o problema de "limite de follow-ups atingido".
    -   **Justificativa:** Garantir que o agendamento de follow-ups de reengajamento não seja mais bloqueado.

-   [ ] **3.2. Centralizar e Simplificar a Lógica de Agendamento de Follow-ups:**
    -   **Ação:** Criar `app/services/followup_manager.py` para centralizar a lógica de decisão sobre quando e qual follow-up agendar.
    -   **Justificativa:** Reduzir a complexidade e a duplicação de código, tornando o sistema mais manutenível.

-   [ ] **3.3. Refatorar o `FollowUpWorker` para Inteligência Contextual:**
    -   **Ação:** Aprimorar `_generate_intelligent_followup_message` em `followup_worker.py` para gerar mensagens de follow-up mais relevantes e personalizadas.
    -   **Justificativa:** Melhorar a qualidade das interações de reengajamento.

-   [ ] **3.4. Validar Lembretes de Reunião:**
    -   **Ação:** Revisar o fluxo de agendamento de lembretes de reunião para garantir que sejam criados e enviados corretamente.
    -   **Justificativa:** Assegurar que os leads recebam os lembretes importantes.

---

### Fase 4: Testes e Validação Final

-   [ ] **4.1. Testes Automatizados:**
    -   [ ] Escrever testes unitários para as novas lógicas implementadas.
-   [ ] **4.2. Validação Manual:**
    -   [ ] Executar cenários de ponta a ponta para confirmar que todos os fluxos (conversação normal, fallback, follow-ups de reengajamento e lembretes) funcionam sem erros e conforme o esperado.
