# TODO - Plano de Correção Definitiva do Erro 'NoneType' e 'RuntimeWarning'

## 1. Diagnóstico e Análise (Concluído)

- [x] Analisar o novo log de erro para identificar a `RuntimeWarning` como a causa raiz.
- [x] Revisar o histórico de conversas para entender a evolução do problema.
- [x] Identificar a falha arquitetural: uso de uma biblioteca síncrona (`supabase-py`) dentro de funções `async` sem o tratamento adequado, causando condições de corrida.

## 2. Implementação da Correção (Arquitetural e Defensiva)

- [x] **Corrigir o `TypeError` em `app/api/webhooks.py`:**
    -   Na função `process_message_with_agent`, modificar a chamada para `redis_client.cache_conversation` para lidar com o caso em que `lead` é `None`, usando `lead["id"] if lead else None`.

- [x] **Refatorar `app/integrations/supabase_client.py` para ser verdadeiramente assíncrono:**
    -   Importar `asyncio`.
    -   Envolver as chamadas síncronas `.execute()` dentro de `asyncio.to_thread()` em todas as funções `async def` relevantes (`get_lead_by_phone`, `create_conversation`, `save_message`, etc.).
    -   Converter `_increment_message_count` para uma função síncrona, pois ela é chamada de dentro do wrapper `to_thread`.

## 3. Verificação e Testes

- [ ] Revisar as alterações para garantir que o padrão `asyncio.to_thread` foi aplicado corretamente e que o `TypeError` foi corrigido.
- [ ] Realizar um "teste mental" do fluxo de um novo lead para confirmar que a condição de corrida foi eliminada.
- [ ] Monitorar os logs após o deploy para garantir que tanto o `TypeError` quanto a `RuntimeWarning` desapareceram.

## 4. Publicação (Com Confiança Máxima)

- [ ] Após a verificação completa, criar um commit único e claro.
- [ ] A mensagem do commit será: `fix(core): Corrige TypeError e RuntimeWarning no processamento de mensagens`.
- [ ] Publicar as alterações no repositório do GitHub.