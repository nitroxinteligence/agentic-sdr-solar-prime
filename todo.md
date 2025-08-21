# TODO - Plano de Correção do Agente

## Tarefa 1: Corrigir a Retenção de Contexto

- [x] **Modificar `app/core/lead_manager.py`**:
    - [x] Alterar a função `extract_lead_info` para que ela não re-processe o histórico inteiro a cada chamada.
    - [x] A lógica deve iterar apenas sobre as mensagens mais recentes (as que ainda não foram processadas) para extrair novas informações e adicioná-las ao `existing_lead_info`.
    - [x] Garantir que as informações existentes (como `name`, `bill_value`, etc.) não sejam sobrescritas com `None` se não forem encontradas nas mensagens mais recentes.

- [x] **Verificar `app/agents/agentic_sdr_stateless.py`**:
    - [x] Confirmar que o `lead_info` atualizado é sempre passado corretamente para as funções subsequentes e retornado no final do processamento.

## Tarefa 2: Corrigir o Message Splitter

- [x] **Modificar `app/config.py`**:
    - [x] Alterar o valor padrão de `message_max_length` de `4000` para um valor mais apropriado para o WhatsApp, como `450`, para garantir que mensagens longas sejam divididas.

- [x] **Verificar `app/api/webhooks.py`**:
    - [x] Confirmar que a lógica de loop que envia os `chunks` da mensagem está correta e não há condições que possam fazê-la falhar.

## Tarefa 3: Publicar Correções

- [ ] **Executar `git add .`**: Adicionar todos os arquivos modificados.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara descrevendo as correções.
- [ ] **Executar `git push`**: Enviar as correções para o repositório remoto.
