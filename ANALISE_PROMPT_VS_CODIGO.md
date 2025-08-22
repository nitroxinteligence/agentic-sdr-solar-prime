# Relatório de Análise e Sincronia: Prompt vs. Código

**Data da Análise:** 21 de Agosto de 2025
**Versão do Sistema:** 0.3 (Arquitetura Stateless)
**Prompt Analisado:** `app/prompts/prompt-agente.md`

## 1. Sumário Executivo

Esta análise aprofundada do diretório `app/` e sua comparação com o novo `prompt-agente.md` revela que o prompt é um excelente documento de design para o **estado futuro desejado** do agente, mas **não reflete com precisão as capacidades atuais do código implementado**.

A arquitetura do agente é stateless, modular e robusta, com uma clara separação de responsabilidades. No entanto, existem Gaps críticos entre as funcionalidades detalhadas no prompt e o que o código pode, de fato, executar. O principal risco é o comportamento imprevisível do agente, que pode tentar seguir regras e usar informações (como a base de conhecimento) que não estão programaticamente acessíveis a ele.

Este relatório detalha os pontos de alinhamento, os Gaps críticos e as inconsistências encontradas, finalizando com um plano de ação recomendado para sincronizar o código com a visão do prompt.

---

## 2. Pontos de Sincronia (O que está 100% alinhado)

As seguintes funcionalidades estão bem definidas no prompt e corretamente implementadas no código:

*   **✅ Chamada de Ferramentas (Tool Calling):** A sintaxe `[TOOL: service.method | ...]` e a lista de ferramentas disponíveis na seção `<tool_calling_system>` do prompt correspondem **exatamente** aos métodos implementados na função `_execute_single_tool` em `app/agents/agentic_sdr_stateless.py`.
    *   `calendar.check_availability`
    *   `calendar.schedule_meeting`
    *   `calendar.suggest_times`
    *   `calendar.cancel_meeting`
    *   `calendar.reschedule_meeting`
    *   `crm.update_stage`
    *   `crm.update_field`
    *   `followup.schedule`

*   **✅ Processamento Multimodal Básico:** A regra no prompt para o agente reagir à `ANÁLISE DE MÍDIA RECEBIDA` está alinhada com o fluxo do código, que de fato processa a mídia via `MultimodalProcessor` e injeta esse contexto no prompt para o LLM.

*   **✅ Arquitetura de Serviços:** O prompt reconhece corretamente a existência e o propósito dos serviços principais que são inicializados e utilizados pelo agente: `CalendarServiceReal`, `CRMServiceReal`, e `FollowUpServiceReal`.

---

## 3. Gaps Críticos (Funcionalidades no Prompt que Faltam no Código)

Esta é a seção mais importante. O agente **não pode executar** o que está descrito aqui, pois a lógica correspondente não existe no código.

*   **❌ GAP 1: Integração com a Base de Conhecimento (Knowledge Base) é Inexistente.**
    *   **O que o Prompt diz:** A seção `<knowledge_base>` instrui o agente a lidar com objeções específicas (`ja_tenho_usina`, `ja_tenho_desconto_maior_20`) e a comparar-se com concorrentes (`Origo Energia`, `Setta Energia`) usando informações pré-definidas.
    *   **O que o Código faz:** **O agente (`AgenticSDRStateless`) nunca chama o `KnowledgeService`.** O arquivo `app/services/knowledge_service.py` existe, mas está isolado e sua funcionalidade de busca nunca é utilizada no fluxo de conversação.
    *   **Impacto:** **Crítico.** O agente não tem como responder a objeções complexas ou perguntas sobre concorrentes com a informação validada do banco de dados. Ele dependerá exclusivamente do conhecimento pré-treinado do LLM, que pode ser genérico, desatualizado ou incorreto, falhando em aplicar os diferenciais competitivos da empresa.

*   **❌ GAP 2: Os Fluxos de Vendas (A, B, C, D) não são Refletidos na Lógica do Agente.**
    *   **O que o Prompt diz:** A seção `<conversation_flows>` detalha quatro fluxos de qualificação distintos e sequenciais (A: Instalação, B: Aluguel, C: Desconto, D: Investimento), cada um com suas próprias perguntas e lógica.
    *   **O que o Código faz:** Não há nenhuma lógica no `AgenticSDRStateless` ou no `ContextAnalyzer` para rastrear em qual fluxo (`A`, `B`, `C`, ou `D`) a conversa está. A detecção de estágio em `_determine_stage` é muito mais simples e genérica (ex: `estágio_0_coleta_nome`, `qualificação`).
    *   **Impacto:** **Alto.** O agente não tem um "estado" que o informe que ele está no "Passo 2 do Fluxo A". Ele depende 100% da capacidade do LLM de ler todo o histórico e o prompt a cada turno para se manter no caminho certo. Isso é propenso a erros, desvios e repetição de perguntas, especialmente em conversas mais longas.

---

## 4. Inconsistências e Pontos de Melhoria

*   **⚠️ Inconsistência 2: Falta de Chamada ao `knowledge_base` no Prompt.**
    *   **Prompt:** Embora o prompt liste o *conteúdo* da base de conhecimento, ele não instrui explicitamente o agente a usar uma *ferramenta* como `[TOOL: knowledge.search | query=...]`.
    *   **Código:** Sem essa instrução de ferramenta, mesmo que o `KnowledgeService` fosse integrado ao agente, o LLM não teria um mecanismo claro para acioná-lo.
    *   **Impacto:** Médio. A falta de uma ferramenta explícita torna a consulta à base de conhecimento menos confiável.

---

## 5. Relatório Final e Recomendações

Seu novo prompt é um excelente guia para a evolução do agente. Para que ele se torne 100% funcional e alinhado com o código, as seguintes ações são recomendadas:

1.  **Implementar a Integração com a Base de Conhecimento (Prioridade Alta):**
    *   **No Código:** Adicionar o `KnowledgeService` ao `AgenticSDRStateless`. Modificar o fluxo `_generate_response` para, antes de chamar o LLM, fazer uma busca na `knowledge_base` se o `ContextAnalyzer` detectar uma intenção de "objeção" ou "informação técnica". Adicionar os resultados da busca como um novo contexto no prompt.
    *   **No Prompt:** Adicionar a ferramenta `[TOOL: knowledge.search | query=<termo_de_busca>]` à lista de `available_tools` para que o agente possa usá-la explicitamente.

2.  **Aprimorar o Gerenciamento de Estado dos Fluxos (Prioridade Média):**
    *   **No Código:** Expandir o `ContextAnalyzer` para detectar e retornar o fluxo atual (`A`, `B`, `C`, `D`) e a etapa dentro desse fluxo. Armazenar `current_flow` e `flow_step` no `lead_info` para persistir o estado entre as mensagens.
    *   **No Prompt:** Utilizar essas novas variáveis de estado para dar instruções mais precisas ao agente (ex: "O lead está no Fluxo C, Passo 2. A próxima pergunta é sobre o valor da conta.").

3.  **Corrigir a Inconsistência do Horário (Prioridade Baixa/Rápida):**
    *   **No Código:** Alterar `"end_hour": 17` para `"end_hour": 18` em `app/services/calendar_service_100_real.py` para alinhar com o prompt.
