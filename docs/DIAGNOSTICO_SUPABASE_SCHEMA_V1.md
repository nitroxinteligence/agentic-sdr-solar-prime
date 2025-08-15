# Diagnóstico e Plano de Ação: Otimização do Schema Supabase v1

## 1. Diagnóstico Geral

Após uma análise aprofundada de todos os arquivos SQL e do código-fonte da aplicação, a integração com o Supabase, embora funcional em seu núcleo, apresenta dois problemas arquiteturais críticos que impedem a eficiência, a consistência dos dados e a simplicidade do sistema:

1.  **Schema Redundante e Desnormalizado:** A estrutura atual do banco de dados viola o princípio da "fonte única da verdade". Informações sobre a mesma entidade (o lead) estão espalhadas e duplicadas em várias tabelas (`leads`, `profiles`). Além disso, a tabela `leads` está sobrecarregada com colunas que não descrevem o lead em si, mas sim *eventos* relacionados a ele (como agendamentos), que pertencem a outras tabelas.

2.  **Fluxo de Sincronização Quebrado:** Este é o problema mais impactante para a inteligência do agente. O `LeadManager` extrai com sucesso informações da conversa (nome, e-mail, valor da conta), mas **o sistema não salva essas informações de volta no Supabase**. O `AgenticSDRStateless` não possui a lógica para invocar `supabase_client.update_lead()` após a coleta de novos dados. Isso resulta em uma base de dados estagnada, onde os leads nunca são enriquecidos, forçando o agente a trabalhar sem "memória" do que já foi coletado.

## 2. Análise Tabela por Tabela

| Tabela | Propósito | Análise de Uso e Redundância | Recomendação |
| :--- | :--- | :--- | :--- |
| `leads` | Armazenar informações centrais do contato. | **SOBRECARREGADA**. Contém colunas de eventos (`meeting_scheduled_at`, `google_event_id`) e status que pertencem a `leads_qualifications`. | 🟢 **Manter (Refatorar Urgente)** |
| `profiles` | Armazenar informações adicionais do lead. | 🔴 **100% REDUNDANTE**. Todos os seus campos (`preferences`, `total_messages`, etc.) podem e devem ser colunas na tabela `leads`. | ❌ **ELIMINAR** |
| `conversations` | Registrar cada sessão de conversa. | **ESSENCIAL**. Funciona como um contêiner para as mensagens. | 🟢 **Manter** |
| `messages` | Armazenar cada mensagem trocada. | **ESSENCIAL**. É o histórico bruto da interação. | 🟢 **Manter** |
| `leads_qualifications` | Registrar o *resultado* de uma qualificação. | **CORRETA, MAS SUBUTILIZADA**. É o local perfeito para os dados de agendamento. | 🟡 **Aprimorar e Centralizar Eventos** |
| `calendar_events` | Armazenar detalhes de eventos do calendário. | 🔴 **100% REDUNDANTE**. Seu propósito é totalmente coberto pela tabela `leads_qualifications` após a refatoração. | ❌ **ELIMINAR** |
| `follow_ups` | Gerenciar o agendamento de contatos futuros. | **ESSENCIAL**. Crucial para a lógica de reengajamento. | 🟢 **Manter** |
| `knowledge_base` | Base de conhecimento para o agente. | **ESSENCIAL**. | 🟢 **Manter** |
| `analytics` | Registrar eventos para análise de BI. | **ÚTIL**. | 🟢 **Manter** |
| `agent_sessions` | Armazenar estado para agentes stateful. | 🟡 **NÃO UTILIZADA**. A arquitetura atual é stateless. Pode ser removida para simplificar. | ❌ **ELIMINAR** |
| `embeddings` | Armazenar vetores de texto para busca semântica. | 🟡 **NÃO UTILIZADA**. O `KnowledgeService` atual usa busca por texto (FTS), não vetorial. | ❌ **ELIMINAR** |

## 3. Análise Detalhada de Colunas da Tabela `leads`

Uma análise aprofundada na tabela `leads` revela quais colunas devem ser mantidas, movidas ou eliminadas para alcançar um design limpo e eficiente.

| Coluna | Análise | Recomendação |
| :--- | :--- | :--- |
| `id`, `phone_number`, `name`, `email` | Dados de identificação fundamentais do lead. | 🟢 **Manter (Essencial)** |
| `bill_value`, `consumption_kwh` | Informações de consumo, chave para qualificação. | 🟢 **Manter (Essencial)** |
| `current_stage`, `qualification_score`, `qualification_status` | Descrevem o estado atual do lead no funil. | 🟢 **Manter (Essencial)** |
| `chosen_flow`, `solution_interest` | Guarda a opção de solução que o lead escolheu. | 🟢 **Manter (Essencial)** |
| `is_decision_maker`, `has_solar_system`, etc. | Campos de qualificação booleana. | 🟢 **Manter (Essencial)** |
| `kommo_lead_id` | Chave de sincronização com o CRM. | 🟢 **Manter (Essencial)** |
| `created_at`, `updated_at`, `last_interaction` | Timestamps para controle e auditoria. | 🟢 **Manter (Essencial)** |
| `google_event_id`, `meeting_scheduled_at`, `meeting_type`, `meeting_status`, `google_event_link` | **Lógica de Evento, não de Lead.** Descrevem um evento de agendamento, que é um *resultado* da qualificação. | 🟡 **MOVER** para `leads_qualifications` |
| `document`, `address`, `property_type` | Atualmente não são extraídos ou utilizados pelo agente. | 🟡 **ARQUIVAR/REMOVER**. Podem ser removidos para simplificar e adicionados no futuro se necessário. |
| `is_qualified` | Coluna gerada que duplica a informação de `qualification_status`. | 🔴 **REMOVER**. Redundante. |

## 4. Plano de Ação Proposto

### Fase 1: Otimização Radical do Schema (Simplificação)

O objetivo é criar uma base de dados enxuta e com fontes únicas de verdade.

1.  **Consolidar `profiles` em `leads`:**
    *   Executar um script SQL (`ALTER TABLE leads ADD COLUMN ...`) para adicionar os campos `preferences` (jsonb), `total_messages` (integer), e `interaction_count` (integer) à tabela `leads`.
    *   Migrar os dados existentes de `profiles` para `leads`.

2.  **Centralizar Dados de Eventos em `leads_qualifications`:**
    *   Remover as colunas relacionadas a eventos da tabela `leads` (`google_event_id`, `meeting_scheduled_at`, etc.).
    *   Garantir que estas colunas já existem e estão sendo usadas em `leads_qualifications`.

3.  **Executar Limpeza Final:**
    *   Executar um script SQL (`DROP TABLE ...`) para remover as tabelas agora redundantes e não utilizadas: `profiles`, `calendar_events`, `embeddings`, `agent_sessions`.

### Fase 2: Implementação do Fluxo de Sincronização (Inteligência)

O objetivo é fazer o agente "lembrar" e persistir o que aprendeu.

1.  **Criar Função de Detecção de Mudanças:**
    *   No `AgenticSDRStateless`, criar um método privado `_detect_and_prepare_changes(old_info, new_info)` que compara os dois dicionários e retorna um payload apenas com os campos que mudaram e têm valor (não são `None`).

2.  **Ativar a Sincronização no `process_message`:**
    *   No fluxo principal do `process_message`, logo após a extração de `new_lead_info` pelo `LeadManager`, chamar a nova função de detecção.
    *   Se houverem mudanças, chamar imediatamente `supabase_client.update_lead(lead_id, changes)`.
    *   **Resultado:** A cada mensagem do usuário, o agente verifica se aprendeu algo novo (nome, e-mail, etc.) e, se sim, atualiza o banco de dados instantaneamente.

## 5. Benefícios Esperados

- **Fim da Amnésia do Agente:** O agente passará a ter um conhecimento evolutivo do lead, tornando a conversa mais natural e inteligente.
- **Consistência Absoluta:** Elimina o risco de dados dessincronizados entre tabelas.
- **Performance Otimizada:** Queries se tornarão mais simples e rápidas, sem a necessidade de `JOINs` complexos para montar o perfil de um lead.
- **Manutenção Drasticamente Simplificada:** Um schema limpo é mais fácil de entender, manter e escalar no futuro.

## 6. Próximos Passos

Recomendo fortemente iniciar pela **Fase 2**, pois não requer alterações no schema e resolve o problema mais crítico: a falta de sincronização. Após validarmos que o agente está salvando os dados corretamente, podemos proceder com a **Fase 1** para a otimização estrutural do banco de dados.

Aguardo sua aprovação para detalhar e iniciar a implementação da Fase 2.
