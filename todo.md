# TODO - 2025-08-22

## Problema Principal
O agente continua a responder de forma conversacional a pedidos diretos de agendamento, em vez de executar a ferramenta de calendário diretamente. Adicionalmente, a funcionalidade do indicador de digitação ("typing") está a causar erros 400.

## Plano de Ação

1.  **Corrigir o Indicador de Digitação (`evolution.py`):**
    -   [ ] Ler o ficheiro `app/integrations/evolution.py`.
    -   [ ] Modificar o método `send_typing` para usar o endpoint correto (`/chat/sendPresence/{self.instance_name}`).
    -   [ ] Corrigir o payload da requisição para incluir o parâmetro `delay` em milissegundos, conforme exigido pela API.

2.  **Corrigir a Lógica de Agendamento Direto (`agentic_sdr_stateless.py`):**
    -   [ ] Ler o ficheiro `app/agents/agentic_sdr_stateless.py`.
    -   [ ] Na função `process_message`, dentro do bloco que deteta a intenção de `agendamento`, remover a chamada final ao `model_manager.get_response`.
    -   [ ] Implementar uma lógica para formatar diretamente o resultado da ferramenta `check_availability` numa resposta final para o utilizador, garantindo que a resposta seja direta e funcional.

3.  **Verificação Final:**
    -   [ ] Após as correções, testar novamente o fluxo de agendamento direto para garantir que a ferramenta é chamada e o resultado é apresentado corretamente.
    -   [ ] Monitorizar os logs para confirmar que os erros 400 do indicador de digitação foram resolvidos.