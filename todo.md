# Plano de Ação para Correção da Criação de Leads e Estabilização do Agente

**Diagnóstico:** O sistema estava falhando em criar novos leads no Supabase, mesmo quando o usuário fornecia seu nome. A causa raiz era uma falha na extração de informações do lead a partir de mensagens combinadas pelo `MessageBuffer`, o que impedia a lógica de criação de ser acionada.

## Fase 1: Correção Imediata e Estabilização

- [x] **Tarefa 1.1: Robustecer a Extração de Nome no `LeadManager`**
    - **Arquivo:** `app/core/lead_manager.py`
    - **Ação:** Modificar o método `extract_lead_info` para garantir que a extração de nome (especialmente com a regex `me chamo...`) seja priorizada e funcione de forma confiável, mesmo com strings multi-linha. Adicionar logging explícito para confirmar se o nome foi ou não extraído em cada passagem.

- [x] **Tarefa 1.2: Simplificar e Tornar a Criação de Leads Atômica**
    - **Arquivo:** `app/agents/agentic_sdr_stateless.py`
    - **Ação:** Refatorar o método `_sync_external_services`. A lógica de *criação* deve ser separada da lógica de *atualização*. O objetivo é garantir que, uma vez que um nome seja detectado, a tentativa de criação no Supabase seja inequívoca.
    - **Ação:** Adicionar logging detalhado em cada etapa dentro deste método: antes de chamar `supabase_client.create_lead`, após a chamada, e no bloco de exceção. Isso é vital para diagnosticar falhas futuras.

- [x] **Tarefa 1.3: Corrigir a Lógica de Sincronização com o CRM**
    - **Arquivo:** `app/agents/agentic_sdr_stateless.py`
    - **Ação:** Garantir que a sincronização de tags e campos customizados (`_sync_crm_data`) seja chamada apenas quando o `kommo_lead_id` existir, prevenindo chamadas desnecessárias à API do Kommo.

## Fase 2: Melhorias de Monitoramento e Prevenção

- [x] **Tarefa 2.1: Aprimorar Logging do `ConversationMonitor`**
    - **Arquivo:** `app/services/conversation_monitor.py`
    - **Ação:** Converter o warning "Lead não encontrado" para um log de nível `DEBUG`. É um estado esperado que uma conversa exista no Redis antes do lead ser criado no Supabase. A mensagem foi tornada mais clara.

- [x] **Tarefa 2.2: Adicionar Transparência ao `MessageBuffer`**
    - **Arquivo:** `app/services/message_buffer.py`
    - **Ação:** Adicionar um log de `DEBUG` no método `_process_messages` que mostra o conteúdo combinado que está sendo enviado ao agente. Ex: `Buffer enviando conteúdo combinado para {phone}: "{conteúdo}"`.

## Fase 3: Validação

- [x] **Tarefa 3.1: Teste de Integração Manual**
    - **Ação:** Realizado teste ponta-a-ponta que confirmou:
        1. O lead é criado corretamente no Supabase após o nome ser fornecido.
        2. O agente avança no fluxo da conversa sem repetir a saudação.
        3. Os logs refletem o fluxo correto de criação e sincronização.

**Conclusão:** Todas as tarefas foram concluídas e o problema foi resolvido. O sistema está estável.