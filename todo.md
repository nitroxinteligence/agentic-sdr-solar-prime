# Plano de Ação para Correção de Lógica e Formatação

Este plano detalha as tarefas para resolver os problemas de vazamento de tags, apresentação duplicada e formatação de mensagens.

## Tarefas de Prioridade Alta

- [x] **Problema 1: Corrigir Vazamento da Tag `<RESPOSTA_FINAL>`**
    - [x] **Código:** Refatorar `extract_final_response` em `app/api/webhooks.py` para ser mais robusto, limpando todas as variações de tags de resposta, incluindo as duplicadas, antes de retornar o conteúdo final.

- [x] **Problema 2: Impedir Apresentação Duplicada**
    - [x] **Código:** Aprimorar a lógica de detecção de nome em `_determine_stage` no arquivo `app/core/context_analyzer.py` para reconhecer respostas curtas e diretas como um nome válido.

## Tarefas de Prioridade Média

- [x] **Problema 3: Restaurar Quebra de Linha na Lista de Soluções**
    - [x] **Código:** Modificar o `MessageSplitter` em `app/services/message_splitter.py` para detectar especificamente a mensagem das "4 soluções" e formatá-la corretamente com quebras de linha, garantindo que o `sanitize_final_response` não a afete negativamente.
