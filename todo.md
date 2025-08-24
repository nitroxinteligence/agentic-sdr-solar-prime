# Plano de Ação para Correção de Confusão com Mensagens Fragmentadas

**Diagnóstico:** O agente perde o contexto e reinicia o fluxo de conversa quando recebe múltiplas mensagens curtas e rápidas do usuário. A causa é o `MessageBuffer` que combina essas mensagens em um texto incoerente, confundindo o LLM, que então descarta o histórico e volta ao início do prompt.

## Fase 1: Aprimoramento da Resiliência do Agente (Prompt Engineering)

- [ ] **Tarefa 1.1: Criar uma "Regra de Interpretação de Buffer" no Prompt**
    - **Arquivo:** `app/prompts/prompt-agente.md`
    - **Ação:** Adicionar uma nova regra de alta prioridade na seção `<anti_hallucination_system>`. Esta regra irá explicar ao LLM que uma mensagem de usuário com múltiplas linhas (`\n`) é resultado de um buffer e que cada linha deve ser considerada. A instrução principal será para focar na última linha que contém a informação mais relevante para o estágio atual da conversa, enquanto ignora as linhas anteriores se elas forem contextualmente irrelevantes (como saudações repetidas).

- [ ] **Tarefa 1.2: Eliminar Enumerações nos Templates do Prompt**
    - **Arquivo:** `app/prompts/prompt-agente.md`
    - **Ação:** Revisar todos os `<template>` nos fluxos de conversa e reescrever aqueles que usam listas numeradas (`1.`, `2.`) para um formato de parágrafo único e conversacional. Isso garante que as respostas do agente sejam coesas e não sejam divididas pelo `MessageSplitter`.

## Fase 2: Melhoria da Experiência do Usuário

- [ ] **Tarefa 2.1: Ajustar o Timeout do `MessageBuffer`**
    - **Arquivo:** `app/config.py`
    - **Ação:** Reduzir o `message_buffer_timeout` para um valor menor (ex: 3.0 segundos). Isso diminuirá a janela de tempo para agrupar mensagens, tornando menos provável que pensamentos distintos do usuário sejam combinados em uma única mensagem.

## Fase 3: Validação

- [ ] **Tarefa 3.1: Teste de Cenário de Mensagens Picotadas**
    - **Ação:** Simular o envio de múltiplas mensagens curtas e rápidas, incluindo informações relevantes misturadas com saudações ou texto irrelevante.
    - **Verificação:** Confirmar que o agente agora consegue extrair a informação relevante da última mensagem, ignora o ruído das mensagens anteriores e responde de forma contextual, sem reiniciar o fluxo da conversa.

**Conclusão Esperada:** Ao educar o LLM sobre como lidar com entradas fragmentadas e ao ajustar o comportamento do buffer, o agente se tornará mais resiliente a padrões de digitação variados, eliminando a perda de contexto e as respostas alucinadas.