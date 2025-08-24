# TODO - Plano de Ação do Projeto

## Tarefa Atual: Corrigir Erro de JSON no Webhook do Kommo

-   [x] **Análise e Diagnóstico:**
    -   [x] Analisar o erro `Expecting value: line 1 column 1 (char 0)` nos logs.
    -   [x] Identificar a causa raiz como uma regressão no `app/api/kommo_webhook.py` que removeu o tratamento robusto de requisições.
    -   [x] Criar o relatório `DIAGNOSTICO_KOMMO_WEBHOOK_ERROR.md` detalhando a falha.

-   [x] **Implementação da Correção:**
    -   [x] **Ação:** Reintroduzir a lógica de verificação de `Content-Type` e tratamento de corpo vazio na função `kommo_webhook` em `app/api/kommo_webhook.py`.

-   [x] **Verificação e Validação:**
    -   [x] Revisar o código para garantir que ele agora lida corretamente com requisições JSON, de formulário e vazias.

-   [ ] **Finalização:**
    -   [ ] Realizar o commit da correção.

---

## Tarefas Anteriores

-   [x] **Implementar Mecanismo de Pausa de Handoff com Redis:** Concluído.
-   [x] **Correção Crítica do Protocolo de Silêncio:** Concluído.
-   [x] **Correção Crítica do Sistema de Follow-up:** Concluído.
