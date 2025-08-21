# TODO - Correção de TypeError em MessageBuffer

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o `TypeError: MessageBuffer.add_message() got an unexpected keyword argument 'media_data'`.
- [x] **Diagnosticar Causa Raiz**: Concluir que a assinatura do método `add_message` em `app/services/message_buffer.py` não foi atualizada para aceitar o novo argumento `media_data` que foi adicionado na chamada da função em `app/api/webhooks.py`.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/services/message_buffer.py`**:
    - [x] Alterar a assinatura do método `add_message` para aceitar `media_data: Optional[Dict] = None`.
    - [x] Incluir `media_data` no dicionário da mensagem que é colocado na fila.
    - [x] Atualizar a lógica em `_process_messages` para extrair `media_data` da última mensagem e passá-lo para `process_message_with_agent`.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção do `TypeError`.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
