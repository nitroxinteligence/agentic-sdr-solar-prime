# TODO - Correção da Falha no Download de Mídia

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o log `Mensagem sem conteúdo de texto ou mídia`, que indica que a mensagem de imagem foi descartada.
- [x] **Diagnosticar Causa Raiz**: Concluir que `_handle_media_message` em `app/api/webhooks.py` falha porque espera dados de mídia em base64 no payload, mas a Evolution API envia uma URL para download. A etapa de download está ausente.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/api/webhooks.py`**:
    - [x] Refatorar a função `_handle_media_message` para que ela detecte a presença de uma URL de mídia no payload da mensagem.
    - [x] Se uma URL for encontrada, a função deve chamar `evolution_client.download_media(message)` para baixar e descriptografar o conteúdo da mídia.
    - [x] A função deve então converter os bytes da mídia baixada para uma string base64 e retorná-la no formato esperado pelo `MultimodalProcessor`.
    - [x] Adicionar tratamento de erro para o caso de o download falhar.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a implementação do download de mídia.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
