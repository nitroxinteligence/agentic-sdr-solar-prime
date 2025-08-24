# TODO - Plano de Ação do Projeto

## Tarefa Atual: Implementar Mecanismo de Pausa de Handoff com Redis

-   [x] **Análise e Diagnóstico:**
    -   [x] Analisar logs que mostram o agente respondendo a leads em atendimento humano.
    -   [x] Identificar a causa raiz como uma falha arquitetural (fonte da verdade incorreta, dependência de dados locais do Supabase em vez do status em tempo real do Kommo).
    -   [x] Criar o relatório `DIAGNOSTICO_HANDOFF_REDIS.md` detalhando a falha e propondo a solução robusta baseada em Redis.

-   [x] **Implementação da Correção:**
    -   [x] **Passo 1 (Guard Rail no Webhook):** Modificar `app/api/webhooks.py`. No início da função `process_new_message`, adicionar uma verificação `await redis_client.is_human_handoff_active(phone)`. Se for `True`, interromper a execução imediatamente.
    -   [x] **Passo 2 (Ativação da Pausa via Agente):** Modificar `app/services/crm_service_100_real.py`. Na função `update_lead_stage`, verificar se o `stage_name` corresponde ao estágio de handoff humano. Se corresponder, chamar `await redis_client.set_human_handoff_pause(phone)`.
    -   [x] **Passo 3 (Ativação/Desativação da Pausa via Webhook Kommo):** Aprimorar `app/api/kommo_webhook.py`. Implementar a lógica para processar eventos de mudança de estágio. Se o novo estágio for de handoff, chamar `set_human_handoff_pause`. Se o lead sair do estágio de handoff, chamar `clear_human_handoff_pause`.

-   [x] **Verificação e Validação:**
    -   [x] Revisar todas as alterações para garantir a correta implementação da lógica de pausa.
    -   [x] (Sugerido) Testar o fluxo completo: mover um lead para handoff (manual ou via agente) e verificar se o agente para de responder. Em seguida, mover o lead para fora do handoff e verificar se o agente volta a responder.

-   [ ] **Finalização:**
    -   [ ] Realizar o commit das alterações com uma mensagem clara sobre a nova arquitetura de handoff.

---

## Tarefas Anteriores

-   [x] **Correção Crítica do Protocolo de Silêncio:** Concluído.
-   [x] **Correção Crítica do Sistema de Follow-up:** Concluído.
