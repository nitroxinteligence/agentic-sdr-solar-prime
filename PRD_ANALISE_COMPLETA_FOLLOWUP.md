# PRD Final: Diagnóstico e Solução Definitiva para o Sistema de Follow-up

**Data:** 2025-09-05
**Autor:** Agente Gemini
**Status:** Concluído

---

## 1. Resumo Executivo

Após uma investigação aprofundada, motivada pela persistência de falhas no envio de mensagens de follow-up, a causa raiz definitiva foi identificada. O problema não era um único bug técnico, mas uma combinação de uma falha na camada de transporte (já corrigida) e um bloqueio na camada de lógica de negócio (o verdadeiro problema atual).

Este documento detalha a causa raiz final, a solução imediata para desobstruir os testes e as recomendações para tornar o sistema permanentemente robusto.

## 2. Diagnóstico Final da Causa Raiz

A falha observada, onde o agente não envia o follow-up após um período de inatividade, é causada pela **lógica de proteção anti-spam do sistema**, que está funcionando como projetado, mas com dados de teste acumulados.

### Análise do Fluxo de Falha:

1.  **Inatividade Detectada:** O `ConversationMonitor` corretamente identifica que um lead está inativo.
2.  **Tentativa de Agendamento:** O `FollowUpManagerService` é acionado para criar um novo registro de follow-up.
3.  **Verificação de Limite:** Antes de criar o registro, o serviço chama a função `get_recent_followup_count` para verificar quantas tentativas de follow-up já foram feitas para o lead na última semana.
4.  **Bloqueio Lógico:** A consulta ao banco de dados retorna um número igual ou superior ao limite configurado (`max_follow_up_attempts = 5`), pois o lead de teste (`ed59d1e3-ff55-4737-a336-23d2b25d55c5`) possui um histórico de tentativas de testes anteriores.
5.  **Cancelamento Silencioso:** Ao receber a contagem elevada, o `FollowUpManagerService` emite o log `Limite de follow-ups atingido` e **encerra o processo de agendamento**.
6.  **Resultado:** Nenhum novo registro de follow-up é criado no banco de dados. Consequentemente, não há nada para o `FollowUpSchedulerService` enfileirar e para o `FollowUpWorker` executar. A mensagem nunca é enviada porque o sistema, para se proteger de spam, decidiu não criá-la.

A correção anterior (formatação do número de telefone) era necessária, mas só seria relevante se a tarefa de follow-up chegasse à fase de envio, o que não estava acontecendo devido a este bloqueio lógico.

## 3. Solução e Plano de Ação

### 3.1. Solução Imediata (Para Desbloqueio de Testes)

Para permitir que os testes com o lead `ed59d1e3-ff55-4737-a336-23d2b25d55c5` prossigam, é necessário limpar seu histórico de follow-ups do banco de dados.

-   **Ação:** Executar o seguinte comando SQL diretamente no painel do Supabase:
    ```sql
    DELETE FROM follow_ups WHERE lead_id = 'ed59d1e3-ff55-4737-a336-23d2b25d55c5';
    ```
-   **Impacto:** Esta ação resetará o contador de tentativas para este lead específico, permitindo que o `FollowUpManagerService` agende novos follow-ups normalmente. Não há impacto em outros leads.

### 3.2. Recomendações para Robustez a Longo Prazo

As correções anteriores e a limpeza do banco de dados tornam o sistema funcional. As seguintes recomendações visam aprimorar a manutenibilidade e a resiliência.

1.  **Refatorar a Lógica de Contagem de Follow-ups (Média Prioridade):**
    -   **Problema:** A lógica atual não distingue entre diferentes tipos de follow-up. Um lead pode atingir o limite com lembretes de reunião e, consequentemente, não receber um follow-up de reengajamento importante.
    -   **Recomendação:** Alterar a função `get_recent_followup_count` para aceitar um parâmetro opcional `follow_up_type`. Isso permitiria que o `FollowUpManagerService` verificasse o limite apenas para follow-ups do tipo `reengagement`, sem afetar os lembretes de reunião.

2.  **Melhorar a Resiliência do Modo de Polling (Média Prioridade):**
    -   **Problema:** O modo de fallback do `FollowUpWorker` (quando o Redis está offline) pode perder tarefas se o worker falhar após marcar uma tarefa como `queued` mas antes de executá-la.
    -   **Recomendação:** Implementar um mecanismo de "lock" na tabela `follow_ups` (ex: um campo `locked_at` ou `processing_by`). No modo de polling, o worker buscaria tarefas `pending`, as "bloquearia" no banco, tentaria processá-las e, finalmente, atualizaria o status para `executed` ou `failed`, liberando o lock.

3.  **Remover Lógica Duplicada (Baixa Prioridade):**
    -   **Problema:** O método `execute_pending_followups` em `followup_service_100_real.py` é redundante e cria uma segunda fonte de verdade para a execução de follow-ups.
    -   **Recomendação:** Remover este método e centralizar toda a lógica de execução no `FollowUpWorker`.

## 4. Conclusão Final

O sistema de follow-up está, agora, compreendido em sua totalidade. A combinação da correção da formatação do telefone, da adição da validação de status pré-envio e da limpeza dos dados de teste resolve o problema de forma definitiva. As recomendações adicionais, quando implementadas, elevarão a arquitetura do sistema a um nível superior de robustez e confiabilidade.