# TODO - Plano de Correção Definitiva do Erro 'NoneType'

## 1. Diagnóstico e Análise (Concluído)

- [x] Revisar todo o codebase do diretório `@app/**` para reavaliar o fluxo de dados.
- [x] Analisar o erro persistente e o histórico de correções para entender por que as soluções anteriores falharam.
- [x] Identificar a causa raiz refinada: Falha na validação do objeto `original_message` antes de ser passado para `process_message_with_agent`, permitindo que um valor `None` cause um `TypeError`.

## 2. Implementação da Correção (Cirúrgica e Defensiva)

- [x] **Adicionar Validação Robusta em `app/api/webhooks.py`:**
    -   Na função `process_message_with_agent`, antes de qualquer outra lógica, implementar uma verificação explícita para garantir que `original_message` não é `None` e é um dicionário. Se a validação falhar, a função deve registrar um erro claro e retornar imediatamente, prevenindo a propagação do erro.

- [x] **Adicionar Validação em `app/services/message_buffer.py`:**
    -   Na função `_process_messages`, adicionar uma verificação para garantir que `last_message_data` é um dicionário antes de passá-lo para `process_message_with_agent`. Isso cria uma segunda camada de defesa.

## 3. Verificação e Testes

- [ ] Revisar as alterações para garantir que o código está limpo, eficiente e segue as melhores práticas de programação defensiva.
- [ ] Realizar um "teste mental" do fluxo completo, desde o webhook até o agente, para confirmar que a nova validação cobre todas as possíveis falhas.
- [ ] Monitorar os logs após o deploy para garantir que o erro foi permanentemente eliminado.

## 4. Publicação (Com Confiança)

- [ ] Apenas após a verificação completa e a certeza de que a solução é robusta, criar um commit único e claro.
- [ ] A mensagem do commit será: `fix(core): Adiciona validação defensiva para prevenir TypeError em webhooks e message_buffer`.
- [ ] Publicar as alterações no repositório do GitHub.
