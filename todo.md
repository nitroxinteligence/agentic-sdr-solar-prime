# Relatório de Diagnóstico e Plano de Ação

## 1. Relatório do Problema

**Data:** 22 de Agosto de 2025

**Problema:** O agente de IA falha consistentemente em executar a ferramenta `calendar.check_availability` quando recebe uma instrução direta para agendar uma reunião (ex: "Agende para mim..."). Em vez de chamar a ferramenta, o agente responde com perguntas de qualificação, ignorando as regras do prompt e a intenção explícita do usuário.

**Histórico de Tentativas:**
1.  **Modificações no Prompt:** Múltiplas tentativas de reforçar as regras de execução de ferramentas no `prompt-agente.md` falharam.
2.  **Implementação do Code Guardian:** Uma barreira de código foi adicionada para capturar as respostas inválidas do modelo. Os logs confirmam que o guardião **funcionou** ao detectar a saída incorreta, mas isso apenas tratou o sintoma, não a causa, e introduziu um bug de tipo de dado.

A persistência do problema, mesmo com um prompt extremamente explícito, indicou que a causa raiz não estava nas instruções, mas sim nos **dados e contexto que o código estava injetando no prompt**.

---

## 2. Diagnóstico da Causa Raiz

Após uma análise completa de todos os arquivos em `app/`, a causa raiz foi identificada:

**Causa Raiz:** O módulo `ContextAnalyzer` (`app/core/context_analyzer.py`) está analisando o histórico da conversa e **forçando um estágio de "qualificação" incorreto**, que sobrescreve a intenção imediata do usuário.

### Mecanismo Detalhado da Falha:

1.  **Análise de Contexto Incorreta:** A função `_determine_stage` no `ContextAnalyzer` usa uma lógica rígida baseada no histórico (se o nome foi coletado, se as soluções foram apresentadas, etc.). Com base nisso, ele conclui que o estágio da conversa é `qualificação`.
2.  **Injeção de Contexto Conflitante:** O `agentic_sdr_stateless.py` pega essa análise (`'conversation_stage': 'qualificação'`) e a injeta no topo do prompt do sistema dentro de um bloco `<dynamic_context>`.
3.  **Conflito de Instruções:** O modelo de linguagem (LLM) recebe duas instruções conflitantes:
    *   **Do Usuário:** "Agende uma reunião para mim agora." (Intenção: `agendamento`)
    *   **Do Código (via Contexto Injetado):** "O estágio atual desta conversa é `qualificação`."
4.  **Decisão Equivocada do Modelo:** O modelo prioriza o contexto injetado pelo código, pois ele parece ser uma diretiva de sistema mais forte. Ele então conclui: "O usuário quer agendar, mas o sistema me diz que a tarefa atual é qualificar. Portanto, preciso fazer mais uma pergunta de qualificação antes de poder agendar."
5.  **Resultado:** O modelo gera uma pergunta de qualificação (ex: "Você é o tomador de decisão?"), a qual não contém um `[TOOL:...]`, fazendo com que o fluxo falhe.

**Conclusão do Diagnóstico:** O problema não é que o modelo ignora o prompt. O problema é que o **código o está confundindo**, fornecendo um contexto que contradiz a intenção imediata do usuário. A solução é parar de injetar essa análise de estágio falha e deixar o modelo decidir a próxima ação com base apenas no histórico da conversa e nas regras do prompt.

---

## 3. Plano de Ação e Checklist de Tarefas

O objetivo é eliminar a injeção de contexto conflitante e simplificar o fluxo de decisão do agente, seguindo o princípio de que "O SIMPLES FUNCIONA".

- [x] **Tarefa 1: Remover o Code Guardian (Concluído)**
  - `git restore app/agents/agentic_sdr_stateless.py` foi executado para reverter a lógica de validação que estava apenas mascarando o problema.

- [ ] **Tarefa 2: Desativar a Análise de Contexto Conflitante**
  - **Arquivo a ser modificado:** `app/agents/agentic_sdr_stateless.py`
  - **Ação:** Localizar a linha `context = self.context_analyzer.analyze_context(...)` e substituí-la por `context = {}`. Isso irá neutralizar completamente o `ContextAnalyzer`, impedindo que ele injete o estágio incorreto no prompt.

- [ ] **Tarefa 3: Simplificar a Geração de Resposta**
  - **Arquivo a ser modificado:** `app/agents/agentic_sdr_stateless.py`
  - **Ação:** Na função `_generate_response`, remover a lógica que formata e injeta o `context_injection` no `system_prompt`. Como o `context` agora estará sempre vazio, essa lógica se tornou desnecessária. O `system_prompt` será usado em sua forma pura, diretamente do arquivo `.md`.

- [ ] **Tarefa 4: Publicar a Correção Definitiva**
  - **Ação:** Adicionar as alterações ao git, commitar com uma mensagem clara explicando a remoção da análise de contexto como a solução definitiva, e fazer o push para o repositório.