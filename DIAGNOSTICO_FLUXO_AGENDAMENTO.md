# Relatório de Diagnóstico: Otimização do Funil do CRM e Correção de Estágio Pós-Agendamento

**Data:** 23 de Agosto de 2025
**Autor:** Agente Gemini
**Status:** Análise Concluída

---

## 1. Resumo do Problema e Objetivo

O fluxo atual do agente no Kommo CRM está desalinhado com a estratégia de negócio desejada. Especificamente:
1.  Após agendar uma reunião, o agente move o lead para o estágio "Qualificado", em vez do estágio correto "Reunião Agendada".
2.  O estágio "Qualificado" é considerado redundante, pois um lead com uma reunião agendada é, por definição, qualificado.

O objetivo é corrigir este fluxo para que, após um agendamento bem-sucedido, o lead seja movido **diretamente** para o estágio "Reunião Agendada", eliminando completamente o uso do estágio "Qualificado" neste processo.

## 2. Análise da Causa Raiz

A investigação completa do código-fonte, com foco especial no `app/prompts/prompt-agente.md` e no `app/agents/agentic_sdr_stateless.py`, revelou que o comportamento atual é uma execução correta de instruções incorretas.

### Falha Principal: Lógica de Negócio Desatualizada no Prompt do Agente

1.  **Local da Falha:** A causa do problema reside nas regras de "Ação Automática Pós-Qualificação" dentro do arquivo `app/prompts/prompt-agente.md`.

2.  **Lógica Atual:** O prompt instrui o agente a seguir uma sequência de duas etapas:
    a. **Primeiro,** ao determinar que um lead atende aos critérios de qualificação, a primeira ação é `[TOOL: crm.update_stage | stage=qualificado]`.
    b. **Depois,** somente após a ferramenta `calendar.schedule_meeting` ser executada com sucesso, há uma instrução para mover o lead para `[TOOL: crm.update_stage | stage=reuniao_agendada]`.

3.  **Consequência:** O agente executa a primeira instrução (mover para "Qualificado") e, por alguma razão na cadeia de execução, a segunda instrução (mover para "Reunião Agendada") não está sendo priorizada ou executada de forma consistente, deixando o lead no estágio intermediário indesejado. A própria existência da primeira instrução é a raiz do problema, pois contradiz o fluxo de negócio desejado.

## 3. Solução Estratégica Proposta: Simplificação do Fluxo

A solução mais inteligente e de menor risco é refatorar a lógica de negócio diretamente no prompt do agente, em vez de adicionar complexidade ao código Python. Isso mantém a separação entre a lógica de decisão (prompt) e a execução (código).

### Pilares da Solução:

1.  **Remover a Etapa Redundante:** A correção principal consiste em **remover completamente** a linha `→ [TOOL: crm.update_stage | stage=qualificado]` do prompt em `app/prompts/prompt-agente.md`.

2.  **Consolidar a Ação Correta:** Ao remover a instrução anterior, a única instrução de mudança de estágio que permanece no fluxo de sucesso é a correta: `→ APÓS o agendamento ser confirmado com sucesso pelo tool, sua próxima ação DEVE ser: [TOOL: crm.update_stage | stage=reuniao_agendada]`.

### Novo Fluxo Corrigido e Otimizado:

1.  O agente identifica que o lead atende aos critérios de qualificação.
2.  Ele **não executa nenhuma mudança de estágio** e prossegue diretamente para o processo de agendamento (`check_availability`, `schedule_meeting`).
3.  Assim que a ferramenta `calendar.schedule_meeting` retorna um resultado de sucesso, a única instrução de mudança de estágio que o agente seguirá é mover o lead diretamente para **"Reunião Agendada"**.

Esta abordagem não só corrige o problema, mas também otimiza o fluxo, removendo uma chamada de API desnecessária ao CRM e alinhando perfeitamente o comportamento do agente com a estratégia de negócio definida.