# TODO - Correção do Agendamento no Google Calendar

Este documento detalha as tarefas para corrigir a falha silenciosa que faz com que os eventos sejam agendados no calendário errado.

## Tarefas

### Fase 1: Tornar a Configuração do Calendário Explícita

-   [x] **Modificar `app/services/calendar_service_100_real.py`:**
    -   Alterar o método `initialize` para remover a lógica de fallback que busca o calendário "principal".
    -   No método `initialize`, verificar se `self.calendar_id` (vindo de `settings.google_calendar_id`) está presente.
    -   Se `self.calendar_id` estiver vazio ou `None`, lançar um `ValueError` com a mensagem: "A variável de ambiente GOOGLE_CALENDAR_ID não está definida. O sistema não pode operar sem saber em qual calendário agendar. Por favor, configure o ID do calendário de destino no seu arquivo .env."
    -   Adicionar um log (`emoji_logger.service_info`) que mostre o `calendar_id` que está sendo utilizado, para clareza na inicialização.

### Fase 2: Documentação para o Usuário

-   [x] **Criar/Atualizar Documentação:**
    -   Criar um novo arquivo `docs/CONFIGURACAO_CALENDARIO.md`.
    -   Neste arquivo, explicar passo a passo como um usuário pode encontrar o `ID do Calendário` no Google Calendar:
        1.  Abra o Google Calendar.
        2.  Na barra lateral esquerda, encontre o calendário desejado (ex: "Agenda do Leonardo").
        3.  Clique nos três pontos (Opções) ao lado do nome do calendário.
        4.  Selecione "Configurações e compartilhamento".
        5.  Na seção "Integrar agenda", copie o valor do campo "ID da agenda".
        6.  Cole este valor na variável `GOOGLE_CALENDAR_ID` no arquivo `.env`.

### Fase 3: Verificação Final

-   [x] **Revisar `app/config.py`:** Garantir que a variável `google_calendar_id` está sendo carregada corretamente do ambiente.
-   [x] **Testar o Fluxo:** Executar o cenário de agendamento novamente, garantindo que:
    -   Se `GOOGLE_CALENDAR_ID` não estiver definido, o sistema falhe na inicialização com o erro esperado.
    -   Se `GOOGLE_CALENDAR_ID` estiver definido, o agendamento apareça no calendário correto.

