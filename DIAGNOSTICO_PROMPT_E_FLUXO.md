# Relatório de Diagnóstico: Desvio de Fluxo do Agente

## 1. Resumo do Diagnóstico

O agente falha em seguir o fluxo de conversação definido no prompt (`prompt-agente.md`) porque a arquitetura atual cria um **conflito de instruções**. O código gera um "mini-prompt" dinâmico que compete com o prompt principal (system prompt), fazendo com que o modelo de linguagem (LLM) ignore as regras do fluxo específico e recorra a um comportamento genérico e inadequado.

## 2. Análise da Inconsistência (Diálogo vs. Prompt)

O desvio é evidente no diálogo fornecido:

1.  **Escolha do Fluxo**: O usuário escolhe a opção 3, "Compra de energia com desconto", ativando o **FLUXO C**.
2.  **Primeira Pergunta (Correta)**: O agente segue o script e pergunta: `Hoje você já recebe algum tipo de desconto na conta de luz?`
3.  **Resposta do Usuário**: O usuário responde `ainda nao`.
4.  **Ponto de Falha (Incorreto)**: Neste momento, o script do **FLUXO C** para a condição `SE NÃO TEM DESCONTO` é claro e direto:
    > 2. "Entendi! Quanto você paga na conta de luz?"
    > 3. [Calcular] "Com nosso desconto de 20%..."

    O agente **ignora completamente** esta instrução. Em vez disso, ele faz uma pergunta genérica e proibida pelas regras: `Entendi... O que te impede de fechar negócio com a Solarprime hoje?`.
5.  **Perda Total de Contexto**: A partir daí, o agente abandona o fluxo, começando a falar sobre a história da empresa e fazendo perguntas genéricas, como se a conversa estivesse recomeçando.

## 3. Causa Raiz: Por que o Agente se Desvia?

A investigação do código revela três causas interligadas:

### Causa 1: Conflito de Prompts (Código vs. Arquivo `prompt-agente.md`)

Este é o problema central. O método `_build_prompt` em `app/agents/agentic_sdr_refactored.py` constrói um prompt de contexto dinâmico a cada turno da conversa. Este "mini-prompt" inclui informações como `Ação recomendada: conversar`.

Quando o LLM recebe as instruções, ele vê:
1.  **Prompt Principal (Longo)**: O conteúdo completo de `prompt-agente.md` com as regras detalhadas dos fluxos.
2.  **Mini-Prompt de Contexto (Curto e Imediato)**: Uma instrução curta e direta gerada pelo código, como `Ação recomendada: conversar`.

O modelo, especialmente quando a resposta do usuário é simples como "ainda nao", dá mais peso ao "mini-prompt" imediato e ignora as regras complexas do prompt principal. A instrução genérica `Ação recomendada: conversar` o leva a improvisar em vez de seguir o script.

### Causa 2: Complexidade e Redundância Excessiva do Prompt

O arquivo `prompt-agente.md` é muito longo e detalhado. Ele contém múltiplas seções, regras repetidas e uma estrutura que, embora clara para um humano, é difícil para um LLM seguir perfeitamente em todos os turnos da conversa, especialmente quando recebe instruções conflitantes do código.

### Causa 3: Análise de Contexto Genérica

O `ContextAnalyzer` classifica a resposta "ainda nao" com uma intenção e ação genéricas (ex: `conversa`). Essa classificação alimenta o "mini-prompt" problemático, reforçando o desvio do fluxo correto.

## 4. Plano de Ação Corretivo (Foco na Simplificação)

Seguindo o princípio de que "o simples funciona sempre", a solução é eliminar a fonte do conflito e simplificar as instruções para o LLM.

### Ação I: Centralizar e Simplificar o Prompt (A Solução Principal)

O objetivo é ter uma **única fonte da verdade** para as instruções do agente.

1.  **Remover a Geração Dinâmica de Prompt**: O método `_build_prompt` em `agentic_sdr_refactored.py` deve ser eliminado ou drasticamente simplificado. Ele não deve mais gerar instruções como "Ação recomendada". O único prompt enviado ao LLM deve ser o histórico da conversa.

2.  **Refatorar e Simplificar `prompt-agente.md`**: O prompt deve ser reescrito para ser mais direto e menos verboso. A lógica de qual fluxo seguir deve ser clara e concisa, confiando que o LLM é capaz de seguir um fluxo a partir do histórico da conversa.

    **Exemplo de Prompt Refatorado (Conceito):**

    ```markdown
    # HELEN VIEIRA - CONSULTORA SOLARPRIME 

    ## 🎯 IDENTIDADE
    Você é Helen Vieira, consultora de energia solar da SolarPrime. Seu objetivo é qualificar leads e agendar reuniões com o especialista, Leonardo. Seja profissional, empática e amigável. Use o nome do lead com moderação. NUNCA use emojis.

    ## ⚡ REGRA DE OURO: FLUXO CONVERSACIONAL
    Siga o fluxo de forma estrita. NÃO pule etapas. NÃO improvise.

    --- 

    ### ESTÁGIO 0: Início
    - Se for o primeiro contato, se apresente e pergunte o nome: "Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime. Antes de começarmos, como posso te chamar?"
    - **Transição**: Após obter o nome, vá para o ESTÁGIO 1.

    --- 

    ### ESTÁGIO 1: Apresentação
    - Apresente as 4 soluções numeradas e pergunte qual interessa ao lead.
    - **Transição**: Com base na resposta, siga o FLUXO específico (A, B, C ou D).

    --- 

    ### ESTÁGIO 2: Qualificação (Fluxos)

    **SE FLUXO C (Compra com Desconto):**
    1.  Pergunte: "Você já recebe algum desconto na conta de luz?"
    2.  **Se a resposta for NÃO**: Pergunte o valor da conta. Ex: "Entendi! E qual o valor médio da sua conta de luz?"
    3.  **Se a resposta for SIM**: Pergunte os detalhes do desconto. Ex: "Legal! E qual o valor sem o desconto e a porcentagem que você recebe?"
    4.  Continue o fluxo até o agendamento.

    **(Definir os outros fluxos A, B, D de forma similar e concisa)**

    --- 

    ### ⚠️ REGRAS GERAIS
    - **NUNCA** anuncie ações ("vou calcular"). Responda com o resultado.
    - **NUNCA** pergunte "O que te impede de fechar?".
    - **SEMPRE** termine suas respostas com a próxima pergunta do fluxo.
    ```

### Ação II: Refinar a Lógica do Agente

1.  **Modificar `AgenticSDR.process_message`**: A chamada para `_build_prompt` deve ser removida. O prompt enviado ao `ModelManager` deve ser apenas o histórico da conversa. O `system_prompt` será a versão simplificada e refatorada do `prompt-agente.md`.
2.  **Ajustar `ContextAnalyzer`**: A análise de contexto ainda é útil para métricas e logging, mas seu resultado **não deve mais ser injetado no prompt** enviado ao LLM.

## 5. Benefícios Esperados

- **Confiabilidade**: Ao remover o "mini-prompt" conflitante, o LLM terá uma única fonte de instruções, aumentando drasticamente a probabilidade de seguir o fluxo corretamente.
- **Simplicidade**: Um prompt mais curto e direto é mais fácil para o LLM processar e para os humanos manterem.
- **Performance**: Menos lógica de código para construir prompts resulta em um processamento ligeiramente mais rápido a cada turno.