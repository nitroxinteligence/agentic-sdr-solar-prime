# TODO v2 - Correção e Resiliência do Agendamento no Google Calendar

Este documento detalha as tarefas para corrigir a falha de configuração do Google Calendar, restaurando a funcionalidade de fallback e adicionando validações para tornar o sistema mais resiliente.

## Tarefas

### Fase 1: Refatoração do `CalendarService` para Resiliência

-   [ ] **Modificar `app/services/calendar_service_100_real.py`:**
    -   **Reintroduzir a Lógica de Fallback:** No método `initialize`, restaurar a lógica que busca o calendário principal (`'primary': true`) da conta Google autenticada.
    -   **Implementar Validação de `GOOGLE_CALENDAR_ID`:**
        -   Antes de usar o `settings.google_calendar_id`, verificar se o valor **não é** uma URL (não deve começar com `http` ou `https`).
        -   Se o ID fornecido for inválido (é uma URL), registrar um `emoji_logger.system_warning` informando: "O GOOGLE_CALENDAR_ID fornecido é uma URL inválida. Ignorando o valor e utilizando o calendário principal da conta."
        -   Se o ID for válido, usá-lo. Se for inválido ou não for fornecido, prosseguir com a lógica de fallback para o calendário principal.
    -   **Garantir Logging Explícito:** Independentemente do método usado (ID explícito ou fallback), o log final da inicialização deve informar claramente qual calendário foi selecionado, mostrando seu `summary` (nome) e `id`. Ex: `emoji_logger.service_ready("Google Calendar conectado ao calendário: '{summary}'", calendar_id=self.calendar_id)`.
    -   **Remover o `ValueError`:** A verificação que lança um `ValueError` se o ID não estiver presente deve ser removida para permitir o funcionamento do fallback.

### Fase 2: Aprimoramento da Documentação

-   [ ] **Atualizar `docs/CONFIGURACAO_CALENDARIO.md`:**
    -   Adicionar uma seção de "Exemplos de IDs Válidos e Inválidos".
    -   **Válido:** `seunome@gmail.com`
    -   **Válido:** `c_1234567890abcdefg12345678@group.calendar.google.com`
    -   **INVÁLIDO:** `https://calendar.google.com/calendar/embed?src=...`
    -   Adicionar uma nota explicando que, se o ID não for fornecido ou for inválido, o sistema usará o calendário principal da conta Google conectada.

### Fase 3: Teste e Verificação

-   [ ] **Testar Cenário 1 (ID Inválido):**
    -   Manter a URL inválida no `.env` para `GOOGLE_CALENDAR_ID`.
    -   Reiniciar a aplicação e verificar nos logs se o aviso de ID inválido aparece.
    -   Verificar se o serviço continua e seleciona o calendário principal.
    -   Realizar um agendamento e confirmar se ele aparece no calendário principal da conta.
-   [ ] **Testar Cenário 2 (Sem ID):**
    -   Comentar ou remover a linha `GOOGLE_CALENDAR_ID` do `.env`.
    -   Reiniciar a aplicação e verificar se o serviço inicializa usando o calendário principal.
    -   Realizar um agendamento e confirmar o resultado.
-   [ ] **Testar Cenário 3 (ID Válido):**
    -   Configurar um `GOOGLE_CALENDAR_ID` **válido** no `.env`.
    -   Reiniciar a aplicação e verificar nos logs se o calendário correto foi selecionado.
    -   Realizar um agendamento e confirmar que o evento foi criado no calendário especificado.