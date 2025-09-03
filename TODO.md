# TODO: Refatoração do Sistema de Análise de Ferramentas

Este documento descreve as tarefas necessárias para corrigir o bug de vazamento de nomenclatura de ferramentas e aumentar a robustez do sistema contra respostas mal formatadas do LLM.

- [ ] **1. Corrigir a Expressão Regular de Análise de Ferramentas**
  - **Arquivo:** `app/agents/agentic_sdr_stateless.py`
  - **Tarefa:** Modificar a regex no método `_parse_and_execute_tools` para tornar a seção de parâmetros (`| params...`) opcional.
  - **Justificativa:** Esta é a causa raiz do bug, pois a regex atual não consegue detectar ferramentas sem parâmetros como `[TOOL: calendar.check_availability]`.

- [ ] **2. Aumentar a Robustez do Parser de Ferramentas**
  - **Arquivo:** `app/agents/agentic_sdr_stateless.py`
  - **Tarefa:** Refatorar `_parse_and_execute_tools` para extrair de forma confiável *todas* as correspondências de ferramentas da resposta do LLM, mesmo que haja texto conversacional misturado.
  - **Justificativa:** Previne que o LLM quebre o fluxo ao adicionar texto extra antes ou depois da chamada da ferramenta.

- [ ] **3. Fortalecer o Guardrail de Resposta Final**
  - **Arquivo:** `app/api/webhooks.py`
  - **Tarefa:** Modificar a função `extract_final_response` para que, se a tag `<RESPOSTA_FINAL>` não for encontrada, a função retorne uma mensagem de fallback segura em vez do texto bruto.
  - **Justificativa:** Atua como uma rede de segurança final para garantir que nenhuma sintaxe de ferramenta ou resposta mal formatada seja enviada ao usuário.

- [ ] **4. Melhorar a Diretiva do Prompt**
  - **Arquivo:** `app/prompts/prompt-agente.md`
  - **Tarefa:** Adicionar uma instrução ainda mais explícita na `master_directive` para enfatizar que a saída para uma chamada de ferramenta deve conter *apenas e exclusivamente* a string da ferramenta.
  - **Justificativa:** Reduz a probabilidade de o LLM gerar saídas mal formatadas em primeiro lugar.
