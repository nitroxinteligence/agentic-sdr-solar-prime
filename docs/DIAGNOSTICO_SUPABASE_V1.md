# Diagnóstico e Plano de Ação: Sincronização com Supabase v1

## 1. Diagnóstico Geral

Após uma análise aprofundada do schema SQL e do código da aplicação, a integração com o Supabase se mostra funcional, mas sofre de dois problemas principais que limitam sua eficiência e escalabilidade:

1.  **Redundância de Schemas e Falta de uma Fonte Única da Verdade:** Existem múltiplas tabelas que armazenam informações sobre a mesma entidade (o "lead"). Por exemplo, `leads`, `profiles`, e `conversations` todas contêm `phone_number`. A tabela `leads` possui colunas de status e qualificação que se sobrepõem com a tabela `leads_qualifications`. Essa redundância torna a manutenção complexa, aumenta o risco de dados inconsistentes e dificulta a obtenção de uma visão 360º do lead.

2.  **Fluxo de Atualização de Dados Incompleto:** O agente extrai informações da conversa (nome, email, valor da conta), mas essa informação não é consistentemente persistida de volta no banco de dados. O `LeadManager` extrai os dados, mas o `AgenticSDRStateless` não possui uma lógica clara para chamar o `supabase_client.update_lead()` com as novas informações coletadas. Isso resulta em leads que permanecem com dados nulos (`name`, `email`, `bill_value`) no banco, mesmo que o agente já os tenha obtido na conversa.

## 2. Análise Detalhada do Schema e Uso

| Tabela | Análise de Uso e Redundância | Status |
| :--- | :--- | :--- |
| `leads` | **Tabela Central, mas sobrecarregada.** Contém campos que deveriam estar em outras tabelas (ex: `google_event_id`, `meeting_scheduled_at`). | 🟢 **Manter (Refatorar)** |
| `profiles` | **Redundante.** As informações (nome, email, preferências) podem e devem ser consolidadas na tabela `leads`. Não há um uso claro que justifique uma tabela separada. | 🔴 **Eliminar** |
| `conversations` | **Essencial.** Armazena o histórico das interações. O link com `lead_id` é fundamental. | 🟢 **Manter** |
| `messages` | **Essencial.** Coração do histórico de conversas. | 🟢 **Manter** |
| `leads_qualifications` | **Correta, mas subutilizada.** É o local ideal para armazenar o *resultado* de uma qualificação, incluindo dados do agendamento. | 🟡 **Aprimorar e Integrar** |
| `calendar_events` | **Redundante.** As informações de evento (ID, link, data) devem ser colunas na tabela `leads_qualifications`, não uma tabela separada. | 🔴 **Eliminar** |
| `follow_ups` | **Essencial.** Gerencia o agendamento de follow-ups e lembretes. | 🟢 **Manter** |
| `knowledge_base` | **Essencial.** Base de conhecimento do agente. | 🟢 **Manter** |
| `analytics` | **Útil para BI.** Registra eventos importantes para análise de performance. | 🟢 **Manter** |
| `agent_sessions` | **Potencialmente útil para stateful, mas desnecessária na arquitetura stateless atual.** Pode ser arquivada. | 🟡 **Arquivar/Eliminar** |
| `embeddings` | **Não utilizada.** O `KnowledgeService` atual faz busca por texto (FTS), não por similaridade de vetores. | 🔴 **Eliminar** |

## 3. Plano de Ação: Rumo a um Schema Simplificado e Sincronizado

O plano foca em consolidar a tabela `leads` como a **fonte única da verdade** para as informações do contato e garantir que o agente a atualize continuamente.

### Fase 1: Simplificação do Schema (Fundação)

O objetivo é eliminar redundâncias e consolidar a informação.

1.  **Unificar `leads` e `profiles`:**
    *   Migrar quaisquer colunas úteis de `profiles` (como `preferences`) para a tabela `leads` como um campo `jsonb`.
    *   Remover a tabela `profiles`.
    *   Atualizar o código que referencia `profiles` para usar `leads`.

2.  **Unificar `calendar_events` em `leads_qualifications`:**
    *   Adicionar as colunas essenciais de `calendar_events` (`google_event_id`, `meeting_link`, `start_time`, `end_time`, `status`) diretamente na tabela `leads_qualifications`.
    *   Remover a tabela `calendar_events`.
    *   Isso cria a associação correta: uma qualificação bem-sucedida *resulta em* um evento.

3.  **Limpeza de Tabelas Não Utilizadas:**
    *   Remover as tabelas `embeddings` e `agent_sessions`, que não são utilizadas na arquitetura atual.

### Fase 2: Implementação do Fluxo de Sincronização de Dados (A Inteligência)

O objetivo é garantir que as informações coletadas pelo agente sejam salvas no banco de dados em tempo real.

1.  **Refatorar `LeadManager`:**
    *   A função `extract_lead_info` já faz um bom trabalho de extração. Vamos garantir que ela retorne um dicionário limpo apenas com os dados **novos ou alterados**.

2.  **Aprimorar `AgenticSDRStateless` (`process_message`):**
    *   Após a chamada ao `self.lead_manager.extract_lead_info`, teremos um dicionário com as informações atuais (`lead_info`) e um com as novas informações extraídas (`new_lead_info`).
    *   Implementar um passo de **detecção de mudanças**: comparar `lead_info` com `new_lead_info`.
    *   Se houver mudanças (ex: `name` que era `None` agora tem um valor), acionar `supabase_client.update_lead()` com um payload contendo apenas os campos alterados.
    *   **Lógica:**
        ```python
        # Dentro de AgenticSDRStateless.process_message

        # 4. Extrair informações do lead
        new_lead_info = self.lead_manager.extract_lead_info(conversation_history)

        # 5. Detectar e Sincronizar Mudanças (NOVO FLUXO)
        lead_changes = self._detect_lead_changes(lead_info, new_lead_info)
        if lead_changes and lead_info.get('id'):
            await supabase_client.update_lead(lead_info['id'], lead_changes)
            emoji_logger.supabase_update("leads", 1, changes=list(lead_changes.keys()))

        # Atualizar o contexto local com as novas informações
        lead_info.update(new_lead_info)
        ```

### Fase 3: Integração Completa das Tabelas

1.  **`leads_qualifications`:** Garantir que, após um agendamento de reunião bem-sucedido, o `TeamCoordinator` crie um registro nesta tabela, preenchendo `lead_id`, `qualification_status`, `score`, e os novos campos de evento (`google_event_id`, etc.).
2.  **`analytics`:** Revisar o código para garantir que eventos chave (ex: `lead_qualified`, `meeting_scheduled`, `followup_sent`) estão sendo registrados na tabela `analytics` para futuras análises de funil.

## 4. Benefícios Esperados

- **Consistência de Dados:** Com uma fonte única da verdade (`leads`), o risco de dados conflitantes é eliminado.
- **Performance:** Um schema mais enxuto com menos `JOIN`s implícitos resulta em consultas mais rápidas.
- **Inteligência Contextual Real:** O agente sempre terá a informação mais atualizada do lead (nome, email, etc.) para personalizar a conversa, pois o banco será atualizado a cada nova informação coletada.
- **Manutenção Simplificada:** Menos tabelas e um fluxo de dados claro tornam o sistema muito mais fácil de entender, depurar e evoluir.

## 5. Próximos Passos

Sugiro começar pela **Fase 2**, que é uma mudança no código e não no schema, e trará o benefício mais imediato: a atualização em tempo real dos dados do lead. Após validar essa melhoria, podemos prosseguir com a **Fase 1** para a otimização do schema do banco de dados.

Aguardo sua aprovação para começarmos.
