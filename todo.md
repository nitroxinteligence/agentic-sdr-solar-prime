# TODO - Correção de AttributeError em Webhook

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o `AttributeError: 'str' object has no attribute 'get'`.
- [x] **Diagnosticar Causa Raiz**: Concluir que a função `process_new_message` em `app/api/webhooks.py` não lida corretamente com payloads que contêm um único objeto de mensagem em vez de um array, fazendo com que o loop itere sobre as chaves (strings) do dicionário.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/api/webhooks.py`**:
    - [x] Refatorar o início da função `process_new_message` para normalizar o payload `data`.
    - [x] A lógica deve verificar se `data` é um dicionário e, em caso afirmativo, envolvê-lo em uma lista (ex: `messages = [data]`). Se já for uma lista, deve usá-la diretamente.
    - [x] Isso garante que o loop `for message in messages:` sempre opere sobre uma lista de dicionários, tornando a função resiliente a ambas as estruturas de payload.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção do `AttributeError`.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
