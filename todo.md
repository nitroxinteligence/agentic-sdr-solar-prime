# TODO - Correção de Schema Mismatch no Update do Lead

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o erro `PGRST204 - Could not find the 'processed_message_count' column`.
- [x] **Diagnosticar Causa Raiz**: Concluir que a chave `processed_message_count`, usada para controle de lógica, está sendo indevidamente enviada para a camada de persistência, onde não há uma coluna correspondente.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/api/webhooks.py`**:
    - [x] Antes da chamada `supabase_client.update_lead`, remover a chave `processed_message_count` do dicionário `updated_lead_info`. Isso garante que apenas os dados pertencentes ao schema da tabela `leads` sejam enviados para a atualização.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção do schema mismatch.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
