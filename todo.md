# TODO - Correção do Processamento de Mídia

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o log `Mensagem sem conteúdo`, indicando que mensagens de mídia são ignoradas.
- [x] **Diagnosticar Causa Raiz**: Concluir que `extract_message_content` só lida com texto e que `_handle_media_message` em `app/api/webhooks.py` é um placeholder não implementado, fazendo com que o fluxo de processamento seja encerrado prematuramente para mídias.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/api/webhooks.py`**:
    - [x] **Implementar `_handle_media_message`**: Adicionar a lógica para detectar e extrair dados de mídia (imagem, documento, etc.) do payload da mensagem do WhatsApp. A função deve retornar um dicionário com o `type` e o `content` (base64) da mídia.
    - [x] **Ajustar `process_new_message`**: Alterar a função para que ela chame `_handle_media_message` e continue o processamento mesmo que não haja conteúdo de texto, desde que haja mídia.
    - [x] **Ajustar `process_message_with_agent`**: Modificar a assinatura da função para aceitar `media_data` e passá-lo para o `execution_context` do agente.

- [x] **Verificar `app/agents/agentic_sdr_stateless.py`**:
    - [x] Confirmar que a lógica que recebe `media_data` do `execution_context` e o passa para o `MultimodalProcessor` está correta e funcional.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar os arquivos modificados.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a implementação do processamento de mídia.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
