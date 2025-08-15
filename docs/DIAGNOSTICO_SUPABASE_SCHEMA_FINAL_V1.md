# Diagnóstico e Plano de Ação: Otimização Final do Schema Supabase v2

## 1. Diagnóstico Geral

Após uma análise aprofundada de todos os arquivos SQL e do código-fonte da aplicação, a estrutura de dados atual, embora funcional, pode ser **radicalmente simplificada**. A complexidade e a redundância atuais são um risco para a manutenção futura e para a consistência dos dados.

- **Problema Central - Responsabilidade Diluída:** A informação sobre um lead está espalhada por múltiplas tabelas (`leads`, `profiles`, `leads_qualifications`, `conversations`). A tabela `leads` tenta ser uma "tabela-mãe" que armazena dados de contato, dados de qualificação, estado da conversa e detalhes de eventos, o que a torna sobrecarregada e ineficiente.

- **Problema Crítico - Fluxo de Dados Quebrado:** Como identificado anteriormente, o sistema **não persiste** as informações que o agente coleta (nome, e-mail, valor da conta) de volta no banco de dados. Isso é uma falha crítica que impede o agente de ter uma "memória" funcional.

## 2. Análise Definitiva de Todas as Tabelas

| Tabela | Propósito | Análise de Uso e Redundância | Recomendação Final |
| :--- | :--- | :--- | :--- |
| `leads` | Armazenar informações centrais do contato. | **SOBRECARREGADA E REDUNDANTE**. Contém colunas de qualificação e eventos que pertencem a `leads_qualifications`. | 🟢 **Manter (Simplificar Radicalmente)** |
| `profiles` | Armazenar perfil do usuário. | 🔴 **100% REDUNDANTE**. Todas as suas colunas pertencem à tabela `leads`. | ❌ **ELIMINAR** |
| `conversations` | Registrar sessões de conversa. | **ESSENCIAL**. Funciona como o contêiner para as mensagens. | 🟢 **Manter** |
| `messages` | Armazenar cada mensagem trocada. | **ESSENCIAL**. É o histórico da interação. | 🟢 **Manter** |
| `leads_qualifications` | Registrar o *resultado* de uma qualificação. | **ESSENCIAL, MAS SUBUTILIZADA**. Deve ser o repositório para o *resultado* de uma qualificação, incluindo dados de agendamento. | 🟡 **Aprimorar e Centralizar Eventos** |
| `follow_ups` | Gerenciar contatos futuros. | **ESSENCIAL**. Crucial para a lógica de reengajamento e lembretes. | 🟢 **Manter** |
| `knowledge_base` | Base de conhecimento do agente. | **ESSENCIAL**. | 🟢 **Manter** |
| `analytics` | Registrar eventos para BI. | **ÚTIL**. | 🟢 **Manter** |
| `agent_sessions` | Armazenar estado para agentes stateful. | 🟡 **NÃO UTILIZADA**. A arquitetura é stateless. | ❌ **ELIMINAR** |
| `embeddings` | Armazenar vetores para busca semântica. | 🟡 **NÃO UTILIZADA**. O sistema usa busca por texto (FTS). | ❌ **ELIMINAR** |

## 3. Análise Detalhada de Colunas (Redundância e Não Utilização)

Esta seção detalha, tabela por tabela, quais colunas são desnecessárias com base na análise do código em `@app/**`.

### Tabela: `leads`
| Coluna | Análise de Uso | Recomendação |
| :--- | :--- | :--- |
| `document` | Não há lógica no `LeadManager` ou em qualquer outro local para extrair ou salvar esta informação. | 🔴 **Eliminar** |
| `property_type` | Extraído pelo `LeadManager`, mas nunca salvo no banco. A lógica de qualificação pode ocorrer em tempo real. | 🔴 **Eliminar** |
| `address` | Não há lógica para extrair ou utilizar o endereço. | 🔴 **Eliminar** |
| `consumption_kwh` | Não há lógica para extrair ou utilizar. O `bill_value` é o campo principal. | 🔴 **Eliminar** |
| `google_event_id` | Pertence ao resultado de uma qualificação, não ao lead. | 🟡 **Mover para `leads_qualifications`** |
| `meeting_scheduled_at`| Pertence ao resultado de uma qualificação. | 🟡 **Mover para `leads_qualifications`** |
| `meeting_type` | Não utilizado no código. | 🔴 **Eliminar** |
| `meeting_status` | Não utilizado no código. | 🔴 **Eliminar** |
| `is_decision_maker` | Informação de qualificação, volátil. Pertence ao registro da qualificação. | 🟡 **Mover para `leads_qualifications`** |
| `has_solar_system` | Informação de qualificação. | 🟡 **Mover para `leads_qualifications`** |
| `wants_new_solar_system`| Informação de qualificação. | 🟡 **Mover para `leads_qualifications`** |
| `has_active_contract` | Informação de qualificação. | 🟡 **Mover para `leads_qualifications`** |
| `contract_end_date` | Não utilizado. | 🔴 **Eliminar** |
| `solution_interest` | Redundante com `chosen_flow`. | 🔴 **Eliminar** |
| `is_qualified` | Coluna gerada que duplica `qualification_status`. | 🔴 **Eliminar** |

### Tabela: `conversations`
| Coluna | Análise de Uso | Recomendação |
| :--- | :--- | :--- |
| `ended_at` | O sistema não possui uma lógica para "encerrar" formalmente uma conversa. | 🔴 **Eliminar** |
| `sentiment` | O `ContextAnalyzer` calcula o sentimento, mas ele não é persistido nem utilizado para decisões futuras. | 🔴 **Eliminar** |
| `channel` | O sistema está hardcoded para 'whatsapp'. A coluna não é necessária. | 🔴 **Eliminar** |

### Tabela: `messages`
| Coluna | Análise de Uso | Recomendação |
| :--- | :--- | :--- |
| `whatsapp_message_id`| O `message_id` já é salvo no `media_data`. Redundante. | 🔴 **Eliminar** |
| `media_url` | O `media_data` já contém a URL e o base64. Redundante. | 🔴 **Eliminar** |
| `is_read` | O status de leitura não é utilizado por nenhuma lógica do agente. | 🔴 **Eliminar** |

### Tabela: `analytics`
| Coluna | Análise de Uso | Recomendação |
| :--- | :--- | :--- |
| `user_agent`, `ip_address` | Não são coletados em nenhum ponto do fluxo de webhook. | 🔴 **Eliminar** |

## 4. Plano de Ação: Simplificação Radical

### Fase 1: Otimização do Schema (Execução via SQL)

1.  **Limpeza da Tabela `leads`:**
    *   Executar `ALTER TABLE leads DROP COLUMN ...` para remover todas as colunas marcadas como **Eliminar** e **Mover** na análise acima. O objetivo é deixar a tabela `leads` apenas com os campos essenciais de contato.

2.  **Limpeza das Outras Tabelas:**
    *   Executar `ALTER TABLE ... DROP COLUMN ...` para remover as colunas desnecessárias identificadas em `conversations`, `messages` e `analytics`.

3.  **Fortalecimento de `leads_qualifications`:**
    *   Executar `ALTER TABLE leads_qualifications ADD COLUMN ...` para adicionar os campos movidos da tabela `leads` (ex: `current_stage`, `qualification_score`, `google_event_id`, `meeting_scheduled_at`, etc.).

4.  **Remoção de Tabelas Inteiras:**
    *   Executar `DROP TABLE ...` para eliminar as tabelas `profiles`, `agent_sessions`, e `embeddings`.

### Fase 2: Ajuste do Código e Correção do Fluxo de Dados

1.  **Refatorar `AgenticSDRStateless`:**
    *   Implementar a lógica de detecção de mudanças para comparar as informações extraídas pelo `LeadManager` com as já existentes no `lead_info`.
    *   Após detectar uma nova informação (ex: `name`), chamar `supabase_client.update_lead()` para persistir a mudança na tabela `leads` simplificada.

2.  **Refatorar `TeamCoordinator`:**
    *   Modificar o `_execute_post_scheduling_workflow` para, em vez de atualizar a tabela `leads`, **criar um novo registro** em `leads_qualifications` com todos os dados da qualificação e do agendamento.

## 5. Benefícios da Nova Arquitetura

- **Schema Mínimo e Essencial:** O banco de dados conterá apenas as informações estritamente necessárias para a operação atual, eliminando ruído e complexidade.
- **Clareza Arquitetural:** A responsabilidade de cada tabela se torna cristalina: `leads` para contatos, `conversations`/`messages` para histórico, e `leads_qualifications` para resultados e eventos.
- **Performance e Manutenibilidade:** Um schema mais enxuto é inerentemente mais rápido e muito mais fácil de manter e evoluir.

Este plano representa a implementação mais pura do seu princípio de "o simples funciona". Aguardo sua aprovação para prosseguir.