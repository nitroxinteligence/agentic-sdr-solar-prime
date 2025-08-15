# Diagnóstico e Plano de Ação: Otimização Final do Schema Supabase v2

## 1. Diagnóstico Geral

Após uma análise aprofundada de todos os arquivos SQL e do código-fonte da aplicação, a integração com o Supabase, embora funcional em seu núcleo, apresenta dois problemas arquiteturais críticos que impedem a eficiência, a consistência dos dados e a simplicidade do sistema:

1.  **Redundância de Schemas e Falta de uma Fonte Única da Verdade:** Existem múltiplas tabelas que armazenam informações sobre a mesma entidade (o "lead"). Por exemplo, `leads`, `profiles`, e `conversations` todas contêm `phone_number`. A tabela `leads` possui colunas de status e qualificação que se sobrepõem com a tabela `leads_qualifications`. Essa redundância torna a manutenção complexa, aumenta o risco de dados inconsistentes e dificulta a obtenção de uma visão 360º do lead.

2.  **Fluxo de Atualização de Dados Incompleto:** O agente extrai informações da conversa (nome, email, valor da conta), mas essa informação não é consistentemente persistida de volta no banco de dados. O `LeadManager` extrai os dados, mas o `AgenticSDRStateless` não possui uma lógica clara para chamar o `supabase_client.update_lead()` com as novas informações coletadas. Isso resulta em uma base de dados estagnada, onde os leads nunca são enriquecidos, forçando o agente a trabalhar sem "memória" do que já foi coletado.

## 2. Análise Tabela por Tabela

| Tabela | Propósito | Análise de Uso e Redundância | Recomendação Final |
| :--- | :--- | :--- | :--- |
| `leads` | Armazenar informações centrais do contato. | **SOBRECARREGADA E REDUNDANTE**. Contém colunas de eventos (`meeting_scheduled_at`, `google_event_id`) e status que pertencem a `leads_qualifications`. | 🟢 **Manter (Refatorar Urgente)** |
| `profiles` | Armazenar perfil do usuário. | 🔴 **100% REDUNDANTE**. Todas as suas colunas pertencem à tabela `leads`. | ❌ **ELIMINAR** |
| `conversations` | Registrar cada sessão de conversa. | **ESSENCIAL**. Funciona como o contêiner para as mensagens. | 🟢 **Manter** |
| `messages` | Armazenar cada mensagem trocada. | **ESSENCIAL**. É o histórico da interação. | 🟢 **Manter** |
| `leads_qualifications` | Registrar o *resultado* de uma qualificação. | **CORRETA, MAS SUBUTILIZADA**. É o local ideal para os dados de agendamento. | 🟡 **Aprimorar e Centralizar Eventos** |
| `calendar_events` | Armazenar detalhes de eventos do calendário. | 🔴 **100% REDUNDANTE**. Seu propósito é totalmente coberto pela tabela `leads_qualifications` após a refatoração. | ❌ **ELIMINAR** |
| `follow_ups` | Gerenciar contatos futuros. | **ESSENCIAL**. Crucial para a lógica de reengajamento e lembretes. | 🟢 **Manter** |
| `knowledge_base` | Base de conhecimento para o agente. | **ESSENCIAL**. | 🟢 **Manter** |
| `analytics` | Registrar eventos para BI. | **ÚTIL**. | 🟢 **Manter** |
| `agent_sessions` | Armazenar estado para agentes stateful. | 🟡 **NÃO UTILIZADA**. A arquitetura atual é stateless. | ❌ **ELIMINAR** |
| `embeddings` | Armazenar vetores de texto para busca semântica. | 🟡 **NÃO UTILIZADA**. O sistema usa busca por texto (FTS). | ❌ **ELIMINAR** |

## 3. O Plano de Ação Definitivo: "A Fonte Única da Verdade"

Este plano visa reestruturar o banco de dados para que cada tabela tenha uma responsabilidade única e clara, eliminando toda a complexidade desnecessária.

### Fase 1: Refatoração e Simplificação Radical do Schema SQL

O objetivo é criar uma base de dados enxuta, onde a tabela `leads` é apenas para contatos e as outras tabelas cuidam de seus respectivos domínios.

1.  **Consolidar `profiles` em `leads`:**
    *   **Ação:** Executar um script SQL (`ALTER TABLE leads ADD COLUMN ...`) para adicionar os campos `preferences` (jsonb), `total_messages` (integer), e `interaction_count` (integer) à tabela `leads`.
    *   Migrar os dados existentes de `profiles` para `leads`.

2.  **Esvaziar `leads` de Responsabilidades Extras:**
    *   **Ação:** Executar `ALTER TABLE leads DROP COLUMN ...` para **remover** as seguintes colunas da tabela `leads`:
        *   `current_stage`, `qualification_score`, `qualification_status`, `is_decision_maker`, `has_solar_system`, `chosen_flow`, `solution_interest` (serão movidas para `leads_qualifications`).
        *   `google_event_id`, `meeting_scheduled_at`, `meeting_type`, `meeting_status`, `google_event_link` (serão movidas para `leads_qualifications`).
        *   `document`, `address`, `property_type`, `consumption_kwh`, `wants_new_solar_system`, `has_active_contract`, `contract_end_date` (não utilizadas atualmente).
        *   `is_qualified` (coluna gerada redundante).
    *   **Resultado:** A tabela `leads` se torna uma simples e eficiente tabela de **Contatos**.

3.  **Fortalecer `leads_qualifications` como Tabela de Eventos:**
    *   **Ação:** Executar `ALTER TABLE leads_qualifications ADD COLUMN ...` para garantir que ela contenha todos os campos de qualificação e evento movidos da tabela `leads`.
    *   **Resultado:** Esta tabela passa a registrar a "fotografia" completa de cada tentativa de qualificação e seus resultados (incluindo agendamentos).

4.  **Limpeza Final:**
    *   **Ação:** Executar `DROP TABLE ...` para eliminar definitivamente as tabelas `profiles`, `agent_sessions`, e `embeddings`.

### Fase 2: Implementação do Fluxo de Sincronização de Dados (Inteligência)

O objetivo é fazer o agente "lembrar" e persistir o que aprendeu.

1.  **Atualizar `AgenticSDRStateless`:**
    *   Implementar a lógica de `_detect_and_prepare_changes` para comparar as informações do lead antes e depois da mensagem do usuário.
    *   Se houver dados novos (nome, email), chamar `supabase_client.update_lead()` para atualizar a tabela `leads` simplificada.

2.  **Atualizar `TeamCoordinator`:**
    *   Após um agendamento de reunião bem-sucedido, a lógica não irá mais atualizar a tabela `leads`. Em vez disso, irá **criar um novo registro** na tabela `leads_qualifications`, preenchendo todos os dados da qualificação e do evento (`google_event_id`, `meeting_scheduled_at`, etc.).

## 4. Benefícios da Arquitetura Proposta

- **Simplicidade Absoluta:** O schema se torna intuitivo. `leads` = Contatos. `leads_qualifications` = Eventos/Resultados. `conversations` = Histórico.
- **Consistência de Dados:** Elimina completamente a possibilidade de dados conflitantes ou dessincronizados.
- **Escalabilidade:** O modelo suporta um histórico completo de interações. Um lead pode ter múltiplas tentativas de qualificação ao longo do tempo, cada uma com seu próprio registro e resultado.
- **Performance:** Consultas se tornam mais rápidas e diretas, operando em tabelas menores e mais focadas.

## 5. Próximos Passos

Esta é a solução definitiva para os problemas de base de dados. Recomendo fortemente a execução deste plano.

1.  **Aprovação:** Aguardo seu OK para esta reestruturação.
2.  **Execução:** Uma vez aprovado, posso gerar os scripts SQL de migração e detalhar as alterações de código necessárias para implementar o plano em fases seguras e incrementais.
