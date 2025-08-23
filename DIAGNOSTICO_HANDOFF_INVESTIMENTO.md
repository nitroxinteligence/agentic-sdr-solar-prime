# Relatório de Diagnóstico: Implementação do Fluxo de Transbordo (Handoff)

**Data:** 23 de Agosto de 2025
**Autor:** Agente Gemini
**Status:** Análise Concluída

---

## 1. Resumo do Problema e Objetivo

A funcionalidade de transbordo (handoff) para um atendente humano quando um lead expressa interesse em "Usina de Investimento" não está implementada. O objetivo é garantir que, ao identificar essa intenção, o agente execute as seguintes ações de forma autônoma e imediata:
1.  Adicione a tag "Usina Investimento" ao lead no Kommo CRM.
2.  Mova o card do lead para o estágio "Atendimento Humano" no pipeline do Kommo CRM.
3.  Envie uma mensagem final de transbordo ao lead.
4.  Cesse completamente a comunicação com o lead.

## 2. Análise da Causa Raiz e do Estado Atual

A investigação completa do código na pasta `app/` revelou que a infraestrutura para esta funcionalidade já existe parcialmente, mas a lógica de orquestração está ausente.

### Componentes Analisados:

1.  **Detecção de Intenção (`app/core/lead_manager.py`):**
    *   **Status:** ✅ **Funcional.**
    *   **Detalhes:** O método `_extract_chosen_flow` no `LeadManager` já identifica corretamente quando um usuário seleciona "Usina de Investimento" e atualiza o `lead_info` com `chosen_flow = "Usina Investimento"`.

2.  **Adição de Tag no CRM (`app/services/crm_sync_service.py`):**
    *   **Status:** ✅ **Funcional.**
    *   **Detalhes:** O `CRMDataSync` service utiliza o `solution_to_tag_map` para mapear o `chosen_flow` para a tag correta ("Usina Investimento"). Esta tag será incluída no payload de atualização do CRM.

3.  **Lógica de Transbordo no Agente (`app/prompts/prompt-agente.md`):**
    *   **Status:** ❌ **Ausente.**
    *   **Detalhes:** Esta é a falha central. A seção `<flow id="D" name="usina_investimento">` no prompt do agente, que deveria ditar o comportamento para este cenário, contém apenas uma descrição do produto. Faltam as instruções cruciais para:
        *   Chamar a ferramenta `crm.update_stage` para mover o lead para "Atendimento Humano".
        *   Formular e enviar uma mensagem de encerramento e handoff.

4.  **Mecanismo de Parada de Interação (`app/prompts/prompt-agente.md`):**
    *   **Status:** ✅ **Existente, mas inativo.**
    *   **Detalhes:** O prompt possui uma diretiva mestra (`<core_directive>`) que proíbe o agente de interagir com leads no estágio "ATENDIMENTO HUMANO". Este mecanismo é o ideal para garantir que o agente pare a comunicação, mas ele nunca é ativado porque o agente não é instruído a mover o lead para esse estágio.

## 3. Solução Estratégica Proposta

A solução mais eficiente e alinhada com a arquitetura do agente é modificar o "cérebro" do agente (o prompt) para incluir a lógica de negócio ausente, aproveitando as ferramentas e mecanismos já existentes.

### Pilares da Solução:

1.  **Refatorar o Fluxo "D" no Prompt:** A seção `<flow id="D" name="usina_investimento">` no arquivo `app/prompts/prompt-agente.md` será completamente reescrita. Em vez de uma simples introdução, ela conterá um fluxo de ações claras e obrigatórias.

2.  **Orquestração de Ferramentas e Resposta:** O novo fluxo instruirá o agente a gerar uma resposta que combine duas ações em uma única etapa:
    *   **Ação 1 (Ferramenta):** Chamar `[TOOL: crm.update_stage | stage=atendimento_humano]`.
    *   **Ação 2 (Sincronização):** O `crm_sync_service` será acionado no mesmo ciclo para adicionar a tag "Usina Investimento" com base no `chosen_flow`.
    *   **Ação 3 (Resposta Final):** Após a execução bem-sucedida das ferramentas, o agente será instruído a enviar uma mensagem de transbordo padronizada e encerrar a interação.

3.  **Ativação do Mecanismo de Parada:** Ao mover o lead para o estágio "Atendimento Humano", a diretiva mestra existente será automaticamente ativada para quaisquer futuras mensagens, garantindo que o agente não interaja mais com o lead.

Esta abordagem é a mais inteligente porque centraliza a lógica de negócio no prompt, que é o local correto para as decisões do agente, e reutiliza as ferramentas e mecanismos de segurança já implementados, garantindo uma solução robusta e de baixo risco.