# Diagnóstico e Plano de Implementação: Sincronizador Contínuo

## 1. Diagnóstico do Sistema de Sincronização Atual

Após uma análise completa do código-fonte (`app/`) e dos schemas do banco de dados (`sqls/`), foi identificado que **existe um mecanismo de sincronização, mas ele é reativo, parcial e acoplado ao fluxo principal de processamento de mensagens.**

### Como Funciona Atualmente:

- **Gatilho**: A sincronização é disparada pelo método `_sync_lead_changes` dentro da classe `AgenticSDR` (`app/agents/agentic_sdr_refactored.py`).
- **Condição**: Ele é acionado **apenas** quando o `LeadManager` detecta uma alteração em um dos campos pré-definidos como importantes (ex: `name`, `bill_value`, `chosen_flow`).
- **Ação**: A chamada é delegada ao `TeamCoordinator`, que utiliza o `CRMService` para atualizar o lead no Kommo.

### Limitações e Pontos Fracos:

1.  **Sincronização Parcial**: O sistema atualiza o Kommo apenas quando um dos campos específicos na lista `sync_triggers` é alterado. Ele não sincroniza o estado completo da conversa, como tags contextuais (ex: "objeção_preço"), notas detalhadas sobre a conversa ou o histórico completo.
2.  **Não é um Worker Dedicado**: A sincronização ocorre no mesmo fluxo da resposta ao usuário. Se a API do Kommo estiver lenta ou falhar, isso pode atrasar ou impedir a resposta do agente ao lead, prejudicando a experiência em tempo real.
3.  **Sem Movimentação de Card no Funil**: Não há uma lógica explícita para analisar o estado da conversa e mover o card do lead no funil do Kommo (ex: de "Em Qualificação" para "Reunião Agendada"). A atualização de estágio só ocorre se o campo `current_stage` for alterado manualmente no código.
4.  **Sem Sincronização de Mídia e Documentos**: O sistema processa imagens e documentos, mas **não salva esses arquivos** em um storage persistente (como o Supabase Storage) nem os anexa ou vincula ao lead no Kommo ou no Supabase.
5.  **Ausência de Reconciliação**: Não existe um processo em background para verificar e corrigir inconsistências entre o Supabase e o Kommo periodicamente.

## 2. Análise das Estruturas de Dados

- **Supabase**: As tabelas existentes (`leads`, `conversations`, `messages`) são uma boa base. A tabela `leads` já possui colunas para `kommo_lead_id` e `google_event_link`, o que é ótimo. No entanto, para armazenar os arquivos de mídia de forma organizada, **falta uma tabela dedicada** (ex: `lead_attachments`).
- **Kommo CRM**: A API do Kommo suporta todas as operações desejadas: atualização de campos customizados, adição de tags e movimentação de leads entre os estágios do funil.

## 3. Plano de Implementação: Worker de Sincronização Contínua

Para atender à demanda por uma sincronização completa e robusta, proponho a criação de um **worker de sincronização em background**. Esta abordagem desacopla a lógica de sincronização do fluxo de resposta do agente, tornando o sistema mais resiliente, performático e completo.

### Arquitetura Proposta

1.  **Fila de Tarefas (Redis)**: Utilizaremos o Redis (que já está integrado) para criar uma fila de tarefas chamada `sync_queue`.
    *   Quando uma conversa com um lead for concluída ou atingir um marco importante (ex: nome coletado, qualificação finalizada), o `AgenticSDR` publicará o `lead_id` (do Supabase) nesta fila.

2.  **Worker de Sincronização (`ConversationSyncWorker`)**: Um novo processo assíncrono, executado em background, que continuamente consome tarefas da `sync_queue`.

### Fluxo de Trabalho do `ConversationSyncWorker`

O worker executará os seguintes passos para cada `lead_id` recebido da fila:

1.  **Coletar Contexto Completo**: Buscar no Supabase todos os dados associados ao `lead_id`:
    *   Dados da tabela `leads` (nome, email, valor da conta, etc.).
    *   O histórico completo da tabela `messages`.
    *   Anexos da nova tabela `lead_attachments`.

2.  **Análise e Extração de Dados para Sincronização**:
    *   Analisar o histórico da conversa para extrair entidades, intenções, objeções e tópicos discutidos.
    *   Determinar o estágio correto do funil com base no status de qualificação e no andamento da conversa.
    *   Gerar uma lista de tags contextuais (ex: `objeção-preço`, `interesse-usina-propria`, `decisor-ausente`).

3.  **Sincronizar com Supabase**:
    *   Garantir que a tabela `leads` está atualizada com as últimas informações extraídas (nome, email, etc.).
    *   Verificar na tabela `messages` se há mensagens com mídia. Se houver, fazer o upload do arquivo para o **Supabase Storage** e criar uma entrada na nova tabela `lead_attachments`, associando o arquivo ao `lead_id`.

4.  **Sincronizar com Kommo CRM**:
    *   **Atualizar Campos**: Usar o `crm_service.update_fields` para preencher campos customizados (Valor da Conta, Solução de Interesse, etc.).
    *   **Adicionar Tags**: Usar `crm_service.add_tags_to_lead` para adicionar as tags contextuais geradas.
    *   **Mover Card no Funil**: Com base no estágio da conversa, usar `crm_service.update_lead_stage` para mover o lead para a coluna correta no pipeline do Kommo.
    *   **Adicionar Notas**: Usar `crm_service.add_note` para adicionar um resumo da conversa ou links para os documentos no Supabase Storage.

### Modificações no Código e Schema

1.  **`agentic_sdr_refactored.py`**:
    *   Modificar o método `_sync_lead_changes`. Em vez de chamar o `TeamCoordinator` diretamente, ele deve publicar o `lead_id` na fila do Redis: `redis_client.enqueue('sync_queue', {'lead_id': self.current_lead_info['id']})`.

2.  **`api/webhooks.py`**:
    *   Na função `process_message_with_agent`, quando uma mensagem com mídia for recebida, o `media_data` (que contém o base64 do arquivo) deve ser salvo na tabela `messages` para que o worker possa processá-lo.

3.  **Novo Arquivo: `app/workers/sync_worker.py`**:
    *   Criar este novo arquivo para abrigar a classe `ConversationSyncWorker` e sua lógica de loop e processamento.

4.  **Atualização do Schema do Supabase (`sqls/`)**:
    *   Criar um novo script SQL para adicionar a tabela de anexos:

    ```sql
    -- Tabela para armazenar anexos dos leads
    CREATE TABLE IF NOT EXISTS public.lead_attachments (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      lead_id UUID NOT NULL REFERENCES public.leads(id) ON DELETE CASCADE,
      message_id UUID REFERENCES public.messages(id) ON DELETE SET NULL,
      file_name TEXT NOT NULL,
      storage_path TEXT NOT NULL, -- Caminho no Supabase Storage
      media_type VARCHAR(50),
      file_size_bytes INTEGER,
      created_at TIMESTAMPTZ DEFAULT NOW(),
      CONSTRAINT fk_lead FOREIGN KEY (lead_id) REFERENCES leads(id)
    );

    CREATE INDEX IF NOT EXISTS idx_lead_attachments_lead_id ON public.lead_attachments(lead_id);
    ```

## 4. Resumo dos Benefícios da Nova Arquitetura

- **Resiliência**: Falhas na API do Kommo não interrompem mais o fluxo de conversa com o lead.
- **Sincronização Completa**: Todos os dados relevantes (campos, tags, estágios, notas, anexos) são sincronizados, fornecendo uma visão 360º do lead para a equipe de vendas.
- **Performance**: O processamento de mensagens se torna mais rápido, pois a sincronização pesada é feita em background.
- **Manutenibilidade**: A lógica de sincronização fica centralizada em um único worker, facilitando futuras manutenções e expansões.
