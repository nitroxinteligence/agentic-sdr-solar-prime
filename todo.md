# TODO - Correção da Falha no Processamento de Mídia

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o log `Mensagem sem conteúdo de texto ou mídia`, que indica que a mensagem de imagem foi descartada.
- [x] **Diagnosticar Causa Raiz**: Concluir que `process_new_message` em `app/api/webhooks.py` não itera sobre o array de mensagens do payload da Evolution API, tratando o array como um único objeto e falhando ao extrair os dados.
- [x] **Identificar Problema Secundário**: Notar que `extract_message_content` não extrai legendas de mensagens de mídia.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/api/webhooks.py`**:
    - [x] Em `process_new_message`, adicionar um loop `for message in data:` para processar cada mensagem individualmente dentro do array recebido.
    - [x] Mover toda a lógica de processamento de mensagem para dentro deste novo loop.
    - [x] Melhorar a função `extract_message_content` para que ela também extraia a legenda (`caption`) de mensagens de imagem, vídeo e documento.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção do processamento de mídia.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
