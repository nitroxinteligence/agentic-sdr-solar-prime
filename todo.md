# Plano de Ação: Refatoração do Sistema de Follow-up

*Objetivo: Corrigir a lógica de contagem de follow-ups, garantir que o reengajamento funcione e validar o fluxo de lembretes de reunião, tornando o sistema confiável e fácil de manter.*

---

### Fase 1: Diagnóstico e Análise de Código

- [ ] **1.1. Analisar o Fluxo de Dados:**
  - [x] Mapear o ciclo de vida de um follow-up: `followup_service` (cria no DB) -> `followup_executor_service` (lê do DB e enfileira no Redis) -> `followup_worker` (consome do Redis e executa).
- [ ] **1.2. Isolar a Lógica de Contagem:**
  - [x] Revisar o método `enqueue_pending_followups` em `followup_executor_service.py`.
  - [x] Revisar o método `get_recent_followup_count` em `supabase_client.py` para entender como a contagem é feita. A hipótese é que a consulta SQL está incorreta.

---

### Fase 2: Correção e Refatoração

- [ ] **2.1. Corrigir a Contagem de Follow-ups:**
  - **Ação:** Modificar a consulta em `get_recent_followup_count` para que ela **não** inclua follow-ups com status `pending` ou `queued` na contagem de "tentativas". Apenas follow-ups `executed` ou `failed` devem contar como uma tentativa real. Isso resolverá o problema do "limite atingido" imediatamente.

- [ ] **2.2. Centralizar e Simplificar a Lógica de Agendamento:**
  - **Problema:** A lógica de quando agendar um follow-up está espalhada (o `ConversationMonitor` agenda, o `AgenticSDRStateless` também pode).
  - **Ação:** Criar um novo serviço `FollowUpManagerService` (`app/services/followup_manager.py`).
  - **Responsabilidade:** Este novo serviço terá um único método, como `handle_conversation_inactivity(lead_id, phone_number)`, que será chamado pelo `ConversationMonitor`. Ele conterá a lógica de verificar o limite e agendar o follow-up, centralizando a regra de negócio.

- [ ] **2.3. Refatorar o `FollowUpWorker` para Inteligência Contextual:**
  - **Problema:** O worker atual gera uma mensagem de follow-up baseada em um prompt genérico.
  - **Ação:** Melhorar o método `_generate_intelligent_followup_message` no `followup_worker.py`.
  - **Melhoria:** O prompt enviado ao LLM será mais rico, contendo um resumo claro do último ponto da conversa e uma instrução explícita para "reengajar o lead a partir deste ponto", garantindo que o follow-up seja relevante e não uma mensagem genérica de "ainda tem interesse?".

- [ ] **2.4. Validar Lembretes de Reunião:**
  - **Ação:** Revisar o método `_execute_post_scheduling_workflow` em `agentic_sdr_stateless.py` para garantir que, após um agendamento, os follow-ups de lembrete (24h e 2h antes) sejam criados corretamente no banco de dados pelo `followup_service`.

---

### Fase 3: Testes e Validação

- [ ] **3.1. Criar Testes para a Nova Lógica:**
  - [ ] Escrever um teste unitário para o novo `FollowUpManagerService` para validar a lógica de contagem e agendamento.
  - [ ] Escrever um teste para o `FollowUpWorker` que simula uma tarefa da fila e verifica se o prompt gerado para o LLM é contextualmente rico.
- [ ] **3.2. Validação Manual:**
  - [ ] Após a implementação, solicitar a execução de um cenário de teste onde um lead para de responder, para observarmos nos logs se o follow-up de reengajamento é agendado e executado corretamente.
