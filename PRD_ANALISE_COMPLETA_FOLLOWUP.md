# PRD: Análise de Robustez e Correção do Sistema de Follow-up

**Data:** 2025-09-05
**Autor:** Agente Gemini
**Status:** Concluído

---

## 1. Visão Geral

Este documento detalha uma análise completa do sistema de follow-up automático, realizada para garantir sua robustez e confiabilidade. A investigação inicial foi motivada por uma falha crítica onde as mensagens de follow-up não estavam sendo enviadas aos usuários, apesar de serem agendadas corretamente no backend.

A análise confirmou a causa raiz inicial e identificou pontos de fragilidade adicionais na arquitetura. Este PRD consolida todas as descobertas, a correção já implementada e as recomendações para fortalecer o sistema contra falhas futuras.

## 2. Arquitetura do Sistema de Follow-up

O fluxo de dados e execução do sistema de follow-up ocorre nas seguintes etapas:

1.  **Detecção de Inatividade (`ConversationMonitor`):** O serviço monitora as conversas no Redis. Quando uma conversa fica inativa por um período pré-definido (ex: 30 minutos, 24 horas), ele é acionado.
2.  **Lógica de Agendamento (`FollowUpManagerService`):** Com base no tempo de inatividade e no status atual da conversa, este serviço decide se um follow-up deve ser criado, respeitando os limites de tentativas por lead.
3.  **Persistência (`SupabaseClient`):** Se um follow-up é necessário, o `FollowUpManagerService` cria um novo registro na tabela `follow_ups` do Supabase com o status `pending`.
4.  **Enfileiramento (`FollowUpSchedulerService`):** Um serviço em background (`followup_executor_service.py`) verifica periodicamente a tabela `follow_ups` em busca de registros com status `pending` e cuja `scheduled_at` já passou. Ele então os enfileira na fila `followup_tasks` do Redis e atualiza seu status para `queued`.
5.  **Execução (`FollowUpWorker`):** O worker (`followup_worker.py`) é o consumidor da fila `followup_tasks`. Ele pega uma tarefa, gera uma mensagem de follow-up inteligente usando o `AgenticSDRStateless` (LLM), e a envia para o usuário via `EvolutionAPIClient`.
6.  **Envio (`EvolutionAPIClient`):** O cliente da Evolution API é a ponte final, responsável por entregar a mensagem ao WhatsApp do usuário.

## 3. Análise de Pontos de Falha

### 3.1. Ponto de Falha Primário (CORRIGIDO)

-   **Problema:** As mensagens não eram enviadas.
-   **Causa Raiz:** O método `send_text_message` em `app/integrations/evolution.py`, utilizado pelo `FollowUpWorker`, não anexava o sufixo `@s.whatsapp.net` ao número de telefone do destinatário. A API da Evolution descartava silenciosamente essas requisições malformadas.
-   **Status:** **Corrigido.** A linha de construção do payload foi alterada para incluir o sufixo, resolvendo o bloqueador principal.

### 3.2. Ponto de Falha Secundário: Ausência de Validação Pré-Envio

-   **Problema:** O `FollowUpWorker` não realiza uma verificação final do status do lead antes de enviar a mensagem.
-   **Cenário de Risco:**
    1.  Um follow-up é agendado para um lead.
    2.  Antes do envio, um atendente humano move manualmente o lead para o estágio "Atendimento Humano" no CRM.
    3.  O `FollowUpWorker` processa a tarefa e envia a mensagem automática, interferindo no atendimento humano.
-   **Causa Raiz:** Falta de uma verificação de status (ex: `redis_client.is_human_handoff_active`) como um "guardrail" final no `_process_task` do `FollowUpWorker`.

### 3.3. Ponto de Falha Terciário: Resiliência do Modo de Polling

-   **Problema:** O modo de fallback do `FollowUpWorker` (quando o Redis está indisponível) é suscetível à perda de tarefas.
-   **Cenário de Risco:**
    1.  O worker, em modo de polling, busca um follow-up `pending` no Supabase.
    2.  Ele atualiza o status para `queued` no banco de dados.
    3.  O processo do worker falha (ex: crash, reinicialização do servidor) antes de conseguir enviar a mensagem.
    4.  A tarefa fica permanentemente no estado `queued` e nunca mais é selecionada pelo polling, resultando em um follow-up perdido.
-   **Causa Raiz:** A atualização de estado ocorre antes da conclusão da ação crítica (envio da mensagem), sem um mecanismo de recuperação em caso de falha.

### 3.4. Ponto de Falha Quaternário: Lógica de Execução Duplicada

-   **Problema:** O arquivo `app/services/followup_service_100_real.py` contém um método `execute_pending_followups` que replica a funcionalidade principal do `FollowUpWorker`.
-   **Cenário de Risco:** Manutenção futura pode atualizar a lógica em um local e não no outro, criando comportamento inconsistente e dificultando o debug.
-   **Causa Raiz:** Código legado ou refatoração incompleta que deixou uma funcionalidade redundante no sistema.

## 4. Recomendações e Plano de Ação

Para garantir a robustez e a manutenibilidade do sistema de follow-up, as seguintes ações são recomendadas:

1.  **Adicionar Validação Pré-Envio no `FollowUpWorker` (Alta Prioridade):**
    -   **Ação:** Modificar o método `_process_task` em `app/services/followup_worker.py`.
    -   **Implementação:** Antes de gerar a mensagem e enviá-la, adicionar verificações para `is_human_handoff_active` e `is_not_interested_active`. Se qualquer uma for verdadeira, o follow-up deve ser cancelado (status atualizado para `cancelled` ou `skipped`) e a mensagem não deve ser enviada.

2.  **Melhorar a Resiliência do Modo de Polling (Média Prioridade):**
    -   **Ação:** Refatorar o `_database_polling_loop` em `app/services/followup_worker.py`.
    -   **Implementação:** Em vez de mudar o status para `queued`, o worker deve tentar processar a tarefa `pending` diretamente. O status só deve ser atualizado para `executed` ou `failed` após a tentativa de envio. Para evitar que múltiplos workers peguem a mesma tarefa, pode-se adicionar um campo `locked_at` ou `processing_by` na tabela `follow_ups`.

3.  **Refatorar Lógica Duplicada (Baixa Prioridade / Limpeza Técnica):**
    -   **Ação:** Remover o método `execute_pending_followups` de `app/services/followup_service_100_real.py`.
    -   **Implementação:** Garantir que nenhuma parte do código esteja chamando este método e removê-lo para consolidar a lógica de execução exclusivamente no `FollowUpWorker`.

## 5. Conclusão

A falha crítica no envio de follow-ups foi resolvida com a correção na formatação do número de telefone. No entanto, a análise aprofundada revelou fragilidades arquitetônicas que comprometem a robustez do sistema. A implementação das recomendações acima, especialmente a adição de validações pré-envio, é crucial para garantir que o sistema de follow-up opere de forma confiável, inteligente e sem interferir em outros processos de negócio.
