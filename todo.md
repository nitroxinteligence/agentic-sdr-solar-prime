# TODO - Plano de Correção do Erro 'NoneType' no Message Buffer

## 1. Diagnóstico e Análise (Concluído)

- [x] Analisar o rastreamento do erro para identificar o local exato da falha (`app/services/message_buffer.py`).
- [x] Revisar o fluxo de dados desde o webhook (`app/api/webhooks.py`) até o `MessageBuffer`.
- [x] Identificar a causa raiz: Lógica inadequada no tratamento de mensagens na fila, levando a `last_message_obj` ser `None` ou a lista `valid_messages` estar vazia.

## 2. Implementação da Correção

- [x] **Refatorar `_process_queue` em `app/services/message_buffer.py`:**
    -   Simplificar a lógica de coleta de mensagens para ser mais direta e menos propensa a erros de condição de corrida.
    -   Garantir que a lista de mensagens seja sempre válida antes de chamar `_process_messages`.
    -   Adicionar tratamento de exceção mais específico para `asyncio.TimeoutError`.

- [x] **Adicionar Validações em `_process_messages` em `app/services/message_buffer.py`:**
    -   Adicionar uma verificação explícita no início da função para garantir que a lista `messages` não seja `None` e não esteja vazia.
    -   Filtrar quaisquer valores `None` que possam ter sido inseridos na lista de mensagens.
    -   Mover a verificação de `last_message_data` para o início da função para evitar acessos a `None`.

## 3. Verificação e Testes

- [ ] Revisar as alterações para garantir que o código está limpo, segue as convenções do projeto e resolve o problema de forma eficaz.
- [ ] (Opcional, se houver testes existentes) Executar os testes unitários relacionados ao `MessageBuffer` para garantir que a funcionalidade principal não foi quebrada.
- [ ] Monitorar os logs após o deploy para confirmar que o erro não ocorre mais.

## 4. Publicação

- [ ] Após a validação, criar um commit com uma mensagem clara descrevendo a correção.
- [ ] Publicar as alterações no repositório do GitHub.
