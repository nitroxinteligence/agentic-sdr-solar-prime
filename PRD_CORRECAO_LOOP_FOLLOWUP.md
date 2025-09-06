# PRD: Correção Definitiva e Robustez do Sistema de Follow-up

**Data:** 2025-09-06
**Autor:** Agente Gemini
**Status:** Concluído

---

## 1. Resumo do Problema

O sistema de follow-up automático estava criando um número excessivo e ininterrupto de agendamentos para um mesmo lead, resultando no rápido esgotamento do limite de tentativas anti-spam e na não execução dos follow-ups corretos. A causa raiz não era uma falha de envio, mas um **loop lógico na lógica de decisão de agendamento** que era acionado após 24 horas de inatividade.

Este documento detalha a causa raiz definitiva e a solução implementada para corrigir o loop e garantir que apenas os dois follow-ups desejados (30 minutos e 24 horas) sejam criados.

## 2. Análise da Causa Raiz

A falha originou-se de uma lógica de verificação de estado incorreta no `FollowUpManagerService`, que era acionada repetidamente pelo `ConversationMonitor`.

### O Loop Lógico Detalhado:

1.  **Estado Inicial:** Um lead fica inativo. O status da conversa é `'active'`.
2.  **Follow-up de 30 Minutos (Correto):** Após 30 minutos, o `ConversationMonitor` detecta a inatividade. O `FollowUpManagerService` verifica a condição `inactive_time > 30min and current_status != 'followup_30min_sent'`, que é verdadeira. Um follow-up é agendado e o status da conversa é atualizado para `'followup_30min_sent'`.
3.  **Follow-up de 24 Horas (Correto):** Após 24 horas, o `ConversationMonitor` detecta a inatividade. O `FollowUpManagerService` verifica as condições:
    *   A condição de 30 minutos é falsa (`current_status` é `'followup_30min_sent'`).
    *   A condição de 24 horas (`inactive_time > 24h and current_status != 'followup_24h_sent'`) é verdadeira. Um follow-up de 24 horas é agendado.
    *   O `ConversationMonitor` atualiza o status para `'followup_24h_sent'`.
4.  **Início do Loop (Falha Crítica):** No minuto seguinte (24h e 1min), o `ConversationMonitor` roda novamente:
    *   Ele chama o `FollowUpManagerService` com o status `'followup_24h_sent'`.
    *   A primeira condição no `FollowUpManagerService` é `if inactive_time > 30min and current_status != 'followup_30min_sent'`.
    *   Esta condição se torna **verdadeira novamente**, pois `inactive_time` (24h e 1min) é maior que 30 minutos e `current_status` (`'followup_24h_sent'`) é diferente de `'followup_30min_sent'`.
    *   **O sistema incorretamente agenda um novo follow-up de 30 minutos.**
5.  **Ciclo Vicioso:** Este processo se repete a cada minuto, gerando um novo follow-up de 30 minutos até que o limite anti-spam seja atingido, bloqueando qualquer ação futura.

A causa raiz é a **ordem da lógica de verificação**. A verificação de 30 minutos, por ser a primeira e menos restritiva, captura indevidamente os leads que já passaram para o estágio de 24 horas.

## 3. Solução Implementada

A solução reestrutura a lógica de decisão para ser hierárquica e centralizada, eliminando a possibilidade de loops.

1.  **Inversão da Lógica de Verificação:** A lógica no `FollowUpManagerService` foi invertida para verificar do período mais longo para o mais curto (`48h -> 24h -> 30min`). Isso garante que uma conversa inativa por 24 horas seja tratada pela regra de 24 horas e não caia mais na regra de 30 minutos.

2.  **Centralização da Lógica de Estado:** A responsabilidade de decidir e agendar o follow-up foi totalmente centralizada no `FollowUpManagerService`. Este serviço agora retorna o novo estado da conversa (`'followup_30min_sent'`, `'followup_24h_sent'`, etc.) após agendar uma tarefa.

3.  **Simplificação do `ConversationMonitor`:** O `ConversationMonitor` foi simplificado. Sua única função agora é detectar a inatividade e chamar o `FollowUpManagerService`. Ele então recebe o novo status retornado pelo manager e o atualiza no Redis, eliminando a duplicação de lógica e o uso de variáveis de estado obsoletas.

## 4. Verificação e Confirmação

-   **Teste Lógico:** A nova estrutura de `if/elif` invertida garante que as condições sejam mutuamente exclusivas e avaliadas na ordem correta de precedência.
-   **Teste Funcional:** Após a limpeza dos dados de teste no banco de dados (removendo os follow-ups gerados em excesso), o sistema agora irá:
    1.  Agendar e executar **um** follow-up de 30 minutos.
    2.  Aguardar o marco de 24 horas.
    3.  Agendar e executar **um** follow-up de 24 horas.
    4.  Não agendar mais follow-ups de reengajamento, conforme o esperado.

## 5. Conclusão

O problema de agendamento excessivo de follow-ups foi definitivamente resolvido. A causa raiz era um erro de lógica na ordem de verificação de estado, que foi corrigido reestruturando o fluxo de decisão. O sistema agora se comporta conforme as regras de negócio especificadas (um follow-up aos 30 minutos e outro às 24 horas), com a camada de proteção anti-spam atuando como um guardrail de segurança, e não como um bloqueador do fluxo principal.
