# TODO - Plano de Ação do Projeto

## Tarefa Atual: Corrigir Pausa de Handoff para ser Baseada em Estado

-   [x] **Análise e Diagnóstico:**
    -   [x] Identificar que a pausa de handoff é baseada em tempo (24h) em vez de estado.
    -   [x] Localizar a causa raiz no uso do comando `setex` do Redis em `app/integrations/redis_client.py`.
    -   [x] Criar o relatório `DIAGNOSTICO_HANDOFF_TTL_ERROR.md`.

-   [x] **Implementação da Correção:**
    -   [x] **Ação:** Modificar a função `set_human_handoff_pause` em `app/integrations/redis_client.py`.
    -   [x] **Lógica:**
        -   [x] Remover o parâmetro `hours`.
        -   [x] Substituir `setex` por `set` para criar uma chave persistente.
        -   [x] Atualizar a mensagem de log para remover a menção de tempo.

-   [x] **Verificação e Validação:**
    -   [x] Revisar a alteração para garantir que a chave Redis agora é criada sem TTL.

-   [ ] **Finalização:**
    -   [ ] Realizar o commit da correção definitiva.

---

## Tarefas Anteriores
-   [x] **Implementar Sincronização Ativa de Handoff:** Concluído.
-   [x] **Correção Webhook Kommo:** Concluído.
-   [x] **Correção Crítica do Protocolo de Silêncio:** Concluído.
-   [x] **Correção Crítica do Sistema de Follow-up:** Concluído.
