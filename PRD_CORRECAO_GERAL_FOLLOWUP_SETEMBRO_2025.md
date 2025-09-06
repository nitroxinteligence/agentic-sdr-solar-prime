# PRD: Correção Crítica do Sistema de Follow-up

**Data:** 06 de Setembro de 2025
**Autor:** Gemini
**Status:** Proposto

## 1. Resumo Executivo

Este documento detalha a análise e o plano de ação para corrigir uma série de falhas críticas identificadas no sistema de follow-up do Agente SDR. Os problemas incluem o envio de mensagens fora do horário comercial, a geração de mensagens de fallback incorretas, e a duplicação massiva de tarefas e mensagens de follow-up. A correção proposta visa robustecer o sistema, eliminar a redundância e garantir que o comportamento do agente esteja estritamente alinhado com as regras de negócio.

## 2. Problemas Identificados

Após análise dos logs e do comportamento observado, foram confirmados quatro problemas principais:

1.  **Envio de Follow-ups Fora do Horário Comercial:** O sistema identifica corretamente que está fora do horário de expediente, mas os workers de execução de follow-up enviam as mensagens mesmo assim.
2.  **Falha no Reconhecimento da Tag `<RESPOSTA_FINAL>`:** As mensagens de follow-up geradas pelo LLM não contêm a tag `<RESPOSTA_FINAL>`, fazendo com que o sistema descarte a resposta inteligente e envie uma mensagem de fallback genérica.
3.  **Duplicação de Mensagens de Follow-up:** Os usuários estão recebendo a mesma mensagem de follow-up várias vezes.
4.  **Criação Excessiva de Registros de Follow-up:** O sistema está criando múltiplos registros de follow-up idênticos para o mesmo lead no banco de dados, causando a duplicação de mensagens e poluindo a base de dados.

## 3. Análise da Causa Raiz

A investigação aprofundada do código-fonte revelou as seguintes causas para cada problema:

### 3.1. Envio Fora do Horário Comercial

-   **Causa:** Existe uma separação de responsabilidades falha. O `FollowupManagerService` verifica o horário comercial antes de *agendar* um novo follow-up. No entanto, o `FollowUpWorker`, que é responsável por *executar* as tarefas da fila, não possui uma verificação final. Um follow-up agendado às 17:59 para ser executado em 30 minutos será processado às 18:29, fora do horário, pois o worker não revalida o horário no momento da execução.

### 3.2. Falha na Tag `<RESPOSTA_FINAL>`

-   **Causa:** O prompt dinâmico gerado na função `_generate_intelligent_followup_message` dentro do `FollowUpWorker` não contém a instrução explícita e obrigatória para que o LLM envolva sua resposta na tag `<RESPOSTA_FINAL>`. Como resultado, o LLM gera texto puro, que é subsequentemente rejeitado pela função `extract_final_response` em `app/api/webhooks.py`, acionando a mensagem de fallback.

### 3.3. Duplicação de Mensagens e Registros

-   **Causa:** Uma **condição de corrida** no `ConversationMonitor`. O monitor verifica a inatividade a cada 60 segundos. Se um lead está inativo, ele chama o `FollowupManager` para criar um registro de follow-up no banco de dados. No entanto, o `FollowupManager` **não verifica se já existe um follow-up pendente ou na fila para aquele lead** antes de criar um novo. Se o loop do monitor rodar múltiplas vezes antes do status do lead ser atualizado no Redis, ele criará múltiplos registros idênticos no banco, que serão posteriormente processados pelo worker, resultando em mensagens duplicadas.

## 4. Plano de Ação e Solução Proposta

Para resolver esses problemas de forma definitiva, as seguintes alterações serão implementadas:

### 4.1. Implementar "Guarda do Horário" no Worker

-   **O quê:** Adicionar uma verificação `settings.is_business_hours()` no início da função `_process_task` no `FollowUpWorker`.
-   **Como:**
    -   **Arquivo a ser modificado:** `app/services/followup_worker.py`
    -   **Lógica:** Se a verificação retornar `False`, o worker não deve executar o follow-up. Em vez de marcá-lo como falho, ele deve ser "adiado". A melhor abordagem é simplesmente pular a execução e deixar o `FollowUpSchedulerService` reenfileirar a tarefa na próxima verificação, ou explicitamente reagendá-la para o início do próximo dia útil. A ação imediata será pular a execução e manter o status como `queued`.
-   **Impacto:** Impedirá que qualquer mensagem de follow-up seja enviada fora do horário comercial, independentemente de quando foi agendada.

### 4.2. Reforçar a Regra da Tag no Prompt de Follow-up

-   **O quê:** Modificar o prompt enviado ao LLM para geração de mensagens de follow-up, incluindo a instrução de formatação.
-   **Como:**
    -   **Arquivo a ser modificado:** `app/services/followup_worker.py`
    -   **Lógica:** Na função `_generate_intelligent_followup_message`, adicionar ao final do `prompt_to_llm` a seguinte instrução: `CRÍTICO: Sua resposta final DEVE estar exclusivamente dentro da tag <RESPOSTA_FINAL>.`
-   **Impacto:** Garantirá que as respostas do LLM para follow-ups sigam o protocolo do sistema, eliminando as mensagens de fallback.

### 4.3. Implementar Verificação de Duplicidade Atômica

-   **O quê:** Impedir a criação de follow-ups duplicados, verificando a existência de uma tarefa pendente antes de criar uma nova.
-   **Como:**
    -   **Arquivo a ser modificado:** `app/services/followup_manager.py`
    -   **Lógica:** Na função `_schedule_reengagement_followup`, antes de chamar `self.db.create_follow_up()`, adicionar uma nova chamada ao Supabase: `self.db.check_existing_pending_followup(lead_id, followup_type)`. Esta nova função no `SupabaseClient` verificará se já existe um registro na tabela `follow_ups` para o `lead_id` com status `pending` ou `queued`. Se existir, a criação de um novo follow-up será abortada.
-   **Impacto:** Eliminará a causa raiz da duplicação de registros e mensagens, tornando o processo de agendamento idempotente e seguro contra condições de corrida.

## 5. Critérios de Aceitação

O sucesso da implementação será validado pelos seguintes critérios:

1.  **Horário Comercial:** Um follow-up agendado para ser executado fora do horário comercial não é enviado. O log do worker deve indicar que a execução foi adiada.
2.  **Mensagens Corretas:** As mensagens de follow-up enviadas são personalizadas e inteligentes, sem a presença da mensagem de fallback "Pode repetir, por favor?".
3.  **Não Duplicação:** Para um lead que fica inativo, apenas **um** registro de follow-up de 30 minutos é criado na tabela `follow_ups`. Nenhuma mensagem duplicada é enviada.
4.  **Integridade da Base:** A tabela `follow_ups` não apresenta mais registros duplicados para o mesmo evento de inatividade.