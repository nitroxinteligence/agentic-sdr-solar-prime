# TODO: Correção do Agendamento Sobreposto (Double Booking)

**Objetivo:** Garantir que o sistema nunca agende ou reagende uma reunião em um horário que já esteja ocupado no Google Calendar.

---

### Fase 1: Robustecer o `CalendarService`

-   [x] **Tarefa 1.1: Criar Verificador de Disponibilidade Interno**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/services/calendar_service_100_real.py`
    -   **Ação:** Foi criado o método privado `_is_slot_available` para centralizar a lógica de verificação de conflitos.

-   [x] **Tarefa 1.2: Refatorar `schedule_meeting` para Verificação Proativa**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/services/calendar_service_100_real.py`
    -   **Ação:** A função `schedule_meeting` agora chama `_is_slot_available` antes de qualquer tentativa de agendamento, retornando um erro de conflito se o horário estiver ocupado.

-   [x] **Tarefa 1.3: Refatorar `reschedule_meeting` para Usar o Verificador Central**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/services/calendar_service_100_real.py`
    -   **Ação:** A função `reschedule_meeting` foi atualizada para usar o novo método `_is_slot_available`, garantindo uma verificação consistente e robusta.

### Fase 2: Aprimoramento do Prompt e Testes

-   [x] **Tarefa 2.1: Atualizar o Prompt do Agente**
    -   **Status:** Concluído.
    -   **Arquivo:** `app/prompts/prompt-agente.md`
    -   **Ação:** O prompt foi atualizado para instruir o agente sobre como lidar com erros de conflito de agendamento, tornando a interação com o usuário mais inteligente e resiliente.

-   [ ] **Tarefa 2.2: Criar Testes de Validação**
    -   **Status:** Pendente.
    -   **Ação:** Criar um novo arquivo de teste, `tests/test_calendar_conflict.py`.
    -   **Nota:** A criação de testes foi adiada conforme solicitado.

---