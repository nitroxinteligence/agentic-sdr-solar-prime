# Diagnóstico e Plano de Ação: Refatoração do Fluxo de Reagendamento

## 1. Diagnóstico da Causa Raiz

Após uma análise completa de todos os módulos do diretório `@app`, a causa raiz dos problemas recorrentes no fluxo de reagendamento foi identificada. O problema não está em uma única função, mas em uma **falha arquitetural fundamental**: o uso de um sistema de "bypass de intenção" (`_handle_intent_bypass`).

Este sistema tenta atalhar o fluxo de processamento para intenções como "reagendamento", "cancelamento" e "agendamento", removendo o LLM do processo de decisão. Essa abordagem, embora pareça eficiente, é inerentemente frágil e a fonte dos erros observados.

### Pontos de Falha:

1.  **Extração de Entidades Frágil:** O sistema de bypass depende da função `_extract_schedule_details` (que usa `dateparser`) para extrair data e hora. Ferramentas como `dateparser` não possuem o contexto completo da conversa. Quando um usuário diz `"quero reagendar para as 10h"`, a ferramenta pode extrair a hora, mas a data se torna ambígua (é hoje? amanhã? a data da reunião original?). O bypass não consegue lidar com essa ambiguidade.

2.  **Lógica de Fallback Mal Localizada:** Para contornar a extração frágil, uma lógica de fallback foi adicionada em `_execute_single_tool` para buscar a data da última reunião agendada no banco de dados. Isso é um "remendo" que trata o sintoma, não a causa. Ele cria complexidade e pontos de falha adicionais (ex: o que acontece se não houver uma reunião anterior?).

3.  **Experiência do Usuário Prejudicada:** Ao encontrar uma ambiguidade que não consegue resolver, o sistema de bypass falha abruptamente e retorna uma mensagem de erro genérica, como a que foi vista nos logs. Ele remove a capacidade do agente de fazer uma pergunta de esclarecimento simples e natural, como "Claro, para qual dia seria o reagendamento às 10h?".

4.  **Complexidade Acidental:** A lógica para uma única ação (reagendar) está espalhada por múltiplos arquivos e funções (`process_message`, `_handle_intent_bypass`, `_extract_schedule_details`, `_execute_single_tool`), tornando o código difícil de entender, depurar e manter.

Em resumo, **a tentativa de ser "mais esperto" que o LLM com um atalho rígido resultou em um sistema menos inteligente e mais propenso a erros.**

## 2. Novo Plano Estratégico

A solução definitiva é abandonar a arquitetura de bypass e unificar o fluxo de processamento, confiando na capacidade de raciocínio do LLM para gerenciar todas as interações, incluindo o reagendamento.

### Pilares da Nova Estratégia:

1.  **Eliminar o Bypass de Intenção:** A função `_handle_intent_bypass` será removida. Todas as mensagens, sem exceção, serão processadas pelo fluxo principal do LLM (`_generate_llm_response`).

2.  **Centralizar a Inteligência no LLM:** O LLM, com acesso ao histórico completo da conversa, se tornará o único responsável por interpretar a intenção do usuário. Ele será capaz de:
    *   Entender o contexto de um pedido de reagendamento (ex: "reagendar nossa conversa de amanhã").
    *   Fazer perguntas de esclarecimento de forma natural se a informação for incompleta ("Para qual dia você gostaria de mudar?").
    *   Coletar todas as informações necessárias (`date`, `time`) antes de invocar a ferramenta.

3.  **Tornar as Ferramentas Mais Robustas e Autocontidas:** A lógica de negócio deve residir dentro do serviço que a executa, não no orquestrador.
    *   A lógica de fallback para encontrar a data de uma reunião existente será movida de `_execute_single_tool` para dentro do método `reschedule_meeting` no `CalendarServiceReal`. A ferramenta se tornará mais inteligente e autônoma.

4.  **Aprimorar o Prompt do Agente:** O `prompt-agente.md` será atualizado com diretrizes claras sobre como o LLM deve lidar com solicitações de agendamento e reagendamento, reforçando a importância de obter todos os dados necessários antes de chamar uma ferramenta.

Esta nova arquitetura irá simplificar drasticamente o código, eliminar a fragilidade do sistema atual, melhorar a experiência do usuário e alavancar o poder do LLM para o qual o sistema foi projetado.

## 3. Próximos Passos

Um arquivo `todo.md` será criado com as tarefas detalhadas para implementar esta nova estratégia. A execução começará imediatamente após sua aprovação.
