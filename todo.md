# TODO - Refatoração do Fluxo de Reagendamento

Este documento detalha as tarefas necessárias para refatorar o sistema de agendamento, eliminando o "bypass de intenção" e centralizando a lógica no fluxo principal do LLM.

## Tarefas

### Fase 1: Refatoração do `AgenticSDRStateless`

-   [ ] **Remover `_handle_intent_bypass`:** Excluir completamente o método `_handle_intent_bypass` de `app/agents/agentic_sdr_stateless.py`.
-   [ ] **Simplificar `process_message`:** Modificar o método `process_message` para que todas as mensagens, sem exceção, sejam direcionadas para `_generate_llm_response`. A verificação de intenção (`user_intent`) deve ser removida.
-   [ ] **Remover `_extract_schedule_details`:** Excluir o método `_extract_schedule_details` de `app/agents/agentic_sdr_stateless.py`, pois a extração de data/hora será responsabilidade do LLM.

### Fase 2: Fortalecimento do `CalendarService`

-   [ ] **Mover Lógica de Fallback para `reschedule_meeting`:** Transferir a lógica que busca a última reunião agendada do Supabase do método `_execute_single_tool` (em `agentic_sdr_stateless.py`) para dentro do método `reschedule_meeting` em `app/services/calendar_service_100_real.py`.
-   [ ] **Tornar `reschedule_meeting` mais inteligente:** O método deve ser capaz de lidar com parâmetros parciais (apenas data ou apenas hora), buscando os dados faltantes da reunião original. Se nenhuma reunião ativa for encontrada, deve retornar um erro claro.

### Fase 3: Aprimoramento do Prompt

-   [ ] **Atualizar `prompt-agente.md`:** Adicionar instruções explícitas para o LLM sobre como lidar com pedidos de agendamento, reagendamento e cancelamento. O prompt deve instruir o agente a:
    1.  Sempre coletar **todas** as informações necessárias (data, hora, e-mail) antes de chamar a ferramenta `calendar.schedule_meeting`.
    2.  Fazer perguntas de esclarecimento se a solicitação do usuário for ambígua (ex: "às 10h" -> "Claro, para qual dia?").
    3.  Priorizar a chamada da ferramenta `calendar.reschedule_meeting` ou `calendar.cancel_meeting` quando a intenção for clara.

### Fase 4: Limpeza e Verificação

-   [ ] **Revisar `_execute_single_tool`:** Após mover a lógica de fallback, simplificar o `case` de `reschedule_meeting` dentro de `_execute_single_tool` para apenas passar os parâmetros recebidos para o `calendar_service`.
-   [ ] **Testar o Novo Fluxo:** Realizar testes manuais para garantir que os cenários de agendamento, reagendamento (com informações completas e parciais) e cancelamento estão funcionando de forma robusta e natural.
-   [ ] **Revisar Logs:** Acompanhar os logs (`logs-console.md`) durante os testes para garantir que o fluxo de execução está correto e sem erros.