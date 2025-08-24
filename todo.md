# Plano de Ação para Correção de Alucinação e Falha de Contexto

**Diagnóstico:** O agente estava perdendo o contexto da conversa, resultando em respostas alucinadas e desconexas. A causa raiz era uma falha sistêmica no gerenciamento de estado, onde o `lead_info` não era consistentemente atualizado com informações de mensagens anteriores, especialmente quando o `MessageBuffer` combina várias entradas do usuário.

## Fase 1: Refatoração do Gerenciamento de Estado e Contexto

- [x] **Tarefa 1.1: Modificar `LeadManager` para Processamento Completo do Histórico**
    - **Arquivo:** `app/core/lead_manager.py`
    - **Ação:** Alterado drasticamente o método `extract_lead_info`. Ele agora processa o histórico completo da conversa a cada chamada, garantindo que o estado do lead seja sempre reconstruído com todas as informações disponíveis, eliminando a perda de contexto.

- [x] **Tarefa 1.2: Centralizar e Persistir o Estado no `AgenticSDRStateless`**
    - **Arquivo:** `app/agents/agentic_sdr_stateless.py`
    - **Ação:** Refatorado o método `_update_context` para detectar e persistir imediatamente quaisquer alterações no `lead_info` no Supabase. Isso garante que a fonte da verdade (o banco de dados) esteja sempre sincronizada antes da geração da resposta.

- [x] **Tarefa 1.3: Simplificar a Determinação de Estágio no `ContextAnalyzer`**
    - **Arquivo:** `app/core/context_analyzer.py`
    - **Ação:** Refatorado o método `_determine_stage` para se basear em dados concretos do `lead_info` (nome, valor da conta, etc.) em vez de depender de palavras-chave frágeis, tornando a lógica de fluxo muito mais robusta.

## Fase 2: Aprimoramento do Prompt e Fluxos de Conversa

- [x] **Tarefa 2.1: Revisar e Fortalecer o Prompt do Agente**
    - **Arquivo:** `app/prompts/prompt-agente.md`
    - **Ação:** Adicionada uma nova `ambiguity_guardrail` ao sistema anti-alucinação, instruindo o modelo a fazer perguntas de esclarecimento quando o contexto for vago, em vez de inventar cenários.

- [x] **Tarefa 2.2: Adicionar Fallback para Respostas Vazias**
    - **Arquivo:** `app/api/webhooks.py`
    - **Ação:** Melhorado o fallback na função `extract_final_response`. Agora, em vez de uma saudação genérica, o agente pedirá ao usuário para repetir a mensagem, mantendo a conversação fluida.

## Fase 3: Validação e Testes

- [x] **Tarefa 3.1: Teste de Cenário de Múltiplas Mensagens**
    - **Ação:** Realizado teste de cenário com múltiplas mensagens curtas e vagas.
    - **Verificação:** O agente respondeu de forma coerente, utilizando o contexto acumulado e solicitando esclarecimentos quando necessário, sem apresentar comportamento de alucinação.

- [x] **Tarefa 3.2: Revisão dos Logs**
    - **Ação:** Analisados os logs durante o teste.
    - **Verificação:** Os logs confirmaram que o `LeadManager` processou o histórico completo, as atualizações de estado foram salvas no banco de dados e o `ContextAnalyzer` determinou o estágio correto com base nos dados persistidos.

**Conclusão:** Todas as tarefas foram concluídas e o problema de alucinação foi resolvido. O sistema está estável e com um gerenciamento de estado significativamente mais robusto.