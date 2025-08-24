# TODO - Plano de Ação do Projeto

## Tarefa Atual: Implementar Sincronização Ativa de Handoff

-   [x] **Análise e Diagnóstico:**
    -   [x] Analisar logs e identificar que o agente responde a leads em handoff devido a dados desatualizados do Supabase.
    -   [x] Identificar a falha arquitetural: o sistema não consulta a fonte da verdade (Kommo CRM) em tempo real.
    -   [x] Criar o relatório `DIAGNOSTICO_HANDOFF_SYNC_ERROR.md` detalhando a nova arquitetura de sincronização ativa.

-   [x] **Implementação da Correção:**
    -   [x] **Passo 1 (Criar Exceção Customizada):** Em `app/exceptions/__init__.py`, criar uma nova exceção `class HandoffActiveException(BaseSDRException): pass`.
    -   [x] **Passo 2 (Modificar `crm_service`):** Adicionar uma nova função `get_lead_by_id(lead_id: str)` em `app/services/crm_service_100_real.py` para buscar um lead diretamente pelo seu ID do Kommo.
    -   [x] **Passo 3 (Centralizar Lógica em `webhooks.py`):**
        -   [x] Modificar a função `create_agent_with_context` em `app/api/webhooks.py`.
        -   [x] Após buscar o lead do Supabase, se ele tiver um `kommo_lead_id`, chamar o novo `crm_service.get_lead_by_id()`.
        -   [x] Comparar o `status_id` do Kommo com o `settings.kommo_human_handoff_stage_id`.
        -   [x] Se for o estágio de handoff, chamar `redis_client.set_human_handoff_pause(phone)` e `raise HandoffActiveException()`.
        -   [x] Se não for, chamar `redis_client.clear_human_handoff_pause(phone)`.
        -   [x] Atualizar o estágio no Supabase se houver divergência.
    -   [x] **Passo 4 (Tratar Exceção):** Na função `process_message_with_agent` em `app/api/webhooks.py`, no bloco `try...except` que chama `create_agent_with_context`, adicionar um `except HandoffActiveException:` para capturar a exceção e encerrar o processamento silenciosamente.
    -   [x] **Passo 5 (Remover Lógica Antiga):** Remover a verificação `is_human_handoff_active` do início de `process_new_message`, pois a nova lógica a torna redundante.

-   [x] **Verificação e Validação:**
    -   [x] Revisar o fluxo para garantir que a chamada à API do Kommo, a comparação de estágios e o acionamento da exceção estão corretos.

-   [ ] **Finalização:**
    -   [ ] Realizar o commit da nova arquitetura de handoff.

---

## Tarefas Anteriores
-   [x] **Correção Webhook Kommo:** Concluído.
-   [x] **Implementar Mecanismo de Pausa de Handoff com Redis (Abordagem Anterior):** Substituído pela tarefa atual.
-   [x] **Correção Crítica do Protocolo de Silêncio:** Concluído.
-   [x] **Correção Crítica do Sistema de Follow-up:** Concluído.