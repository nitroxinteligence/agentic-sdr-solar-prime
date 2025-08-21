# TODO - Plano de Ação v2.1 (Concluído)

## Prioridade Máxima: Estabilidade e Consistência

- [x] **Corrigir Inconsistências de `tool_calling`:**
    - [x] Em `agentic_sdr_stateless.py`, no método `_execute_single_tool`, criar aliases para os nomes de `tools` do prompt. Ex: `if method_name == "update_stage": return await self.crm_service.update_lead_stage(...)`.
    - [x] Remover a instrução para agendar lembretes (`[TOOL: followup.schedule]`) da seção de agendamento do `prompt-agente.md` para eliminar a redundância com o `_execute_post_scheduling_workflow`.

- [x] **Implementar Locks de Concorrência (Redis):**
    - [x] No `CalendarServiceReal`, implementar `redis_client.acquire_lock` no início dos métodos `check_availability` e `schedule_meeting`, e `release_lock` no final (em um bloco `finally`). A chave do lock para agendamento deve ser baseada no horário (ex: `lock:schedule:2025-08-20:10:00`).
    - [x] No `CRMServiceReal`, implementar um lock similar no `create_or_update_lead` para evitar a criação de leads duplicados.

- [x] **Garantir Persistência do `ConversationMonitor`:**
    - [x] Refatorar o `ConversationMonitor` para usar o Redis em vez de um dicionário em memória (`self.active_conversations`). Cada vez que uma mensagem for registrada, usar `redis_client.set` com um TTL (ex: 7 dias) para a chave `monitor:conversation:{phone}`. O loop de monitoramento deve então escanear essas chaves no Redis.

## Prioridade Alta: Robustez dos Processos

- [x] **Implementar Mecanismos de Compensação (Rollback):**
    - [x] No `CalendarServiceReal`, refatorar `reschedule_meeting`. Antes de cancelar o evento antigo, buscar e armazenar seus dados. Se a criação do novo evento falhar, recriar o evento original com os dados armazenados.
    - [x] No `AgenticSDRStateless`, envolver cada chamada dentro do `_execute_post_scheduling_workflow` em seu próprio bloco `try...except` para que a falha de uma etapa não impeça a execução das outras.

- [x] **Corrigir Arquitetura do `FollowUpExecutorService`:**
    - [x] Modificar o `FollowUpExecutorService` para que ele não envie mensagens diretamente, mas sim enfileire uma "tarefa de follow-up" em uma fila do Redis. (Renomeado para `FollowUpSchedulerService`).
    - [x] Criar um novo arquivo `followup_worker.py` com a lógica para consumir da fila, instanciar um `AgenticSDRStateless` completo e usar o método `process_message` para gerar e enviar a mensagem de follow-up, garantindo o uso de todo o contexto e personalidade do agente.

## Prioridade Média: Melhorias de Lógica e UX

- [x] **Implementar Prevenção de Spam de Follow-up:**
    - [x] No `FollowUpSchedulerService`, antes de enfileirar um follow-up, consultar a tabela `follow_ups` no Supabase para contar quantos follow-ups foram enviados para o `lead_id` na última semana. Se o limite for atingido, marcar o follow-up atual como `cancelled`.
    - [x] Adicionado o método `get_recent_followup_count` ao `SupabaseClient` para suportar esta funcionalidade.

- [x] **Robustecer Extração de Nome:**
    - [x] Refatorar a lógica de extração de nome em `LeadManager` para ser mais conservadora, focando em padrões explícitos de apresentação e adicionando uma função de validação `_is_valid_name` para evitar a captura de palavras comuns como nomes.
