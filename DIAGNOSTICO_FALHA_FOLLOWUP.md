# PRD: Diagnóstico e Correção da Falha no Envio de Mensagens de Follow-up

**Data:** 2025-09-05
**Autor:** Agente Gemini
**Status:** Concluído

---

## 1. Resumo do Problema

O sistema de follow-up automático está falhando em sua etapa final. Embora os follow-ups sejam corretamente agendados no banco de dados e processados pelo backend (enfileirados no Redis), a mensagem de texto correspondente não é enviada ao usuário final no WhatsApp. A falha ocorre de forma silenciosa, sem gerar erros explícitos nos logs, o que dá a falsa impressão de que o sistema está operando normalmente.

## 2. Análise e Diagnóstico

A investigação foi dividida em duas frentes: análise dos logs de execução e uma revisão detalhada do código-fonte dos microsserviços envolvidos.

### 2.1. Análise dos Logs (`logs-console.md`)

-   **Criação e Enfileiramento Confirmados:** Os logs mostram claramente que os follow-ups são criados com sucesso no Supabase (`Follow-up criado: <ID>`) e, em seguida, enfileirados no Redis pelo `FollowUpSchedulerService` (`Follow-up <ID> enfileirado no Redis.`).
-   **Ausência Crítica de Logs de Execução:** O ponto central do diagnóstico é a **ausência total de logs** provenientes do `FollowUpWorker`. Não há registros de processamento de tarefas (`🚀 Processando tarefa de follow-up...`), de envio de mensagens ou de sucesso/falha na execução.
-   **Conclusão da Análise de Logs:** A falha ocorre precisamente no `FollowUpWorker`. As tarefas chegam à fila do Redis, mas o worker não as consome ou falha silenciosamente no início de seu processamento, antes de qualquer log ser registrado.

### 2.2. Análise do Código-Fonte (`app/**`)

O fluxo de um follow-up é o seguinte:

1.  `ConversationMonitor` detecta inatividade.
2.  `FollowUpManagerService` cria o registro do follow-up no Supabase com status `pending`.
3.  `FollowUpSchedulerService` (`followup_executor_service.py`) busca os registros `pending` e os adiciona à fila `followup_tasks` no Redis.
4.  `FollowUpWorker` (`followup_worker.py`) consome a tarefa da fila, gera a mensagem e a envia. **Este é o ponto da falha.**

Ao inspecionar o `FollowUpWorker`, nota-se que ele utiliza o cliente `evolution_client` para enviar a mensagem final, especificamente o método `send_text_message`.

Uma análise aprofundada do arquivo `app/integrations/evolution.py` revelou uma inconsistência crítica:

-   O método `send_text_message` utiliza um método auxiliar `_format_phone` que apenas limpa e padroniza o número com o DDI `55`. No entanto, ele **não anexa o sufixo obrigatório `@s.whatsapp.net`** ao número de telefone antes de enviá-lo à API da Evolution.
-   Em contraste, outros métodos no mesmo arquivo (como `send_reaction` e `send_reply`) e em outros serviços (como `followup_service_100_real.py`) anexam corretamente o sufixo, formatando o destinatário como `f"{phone}@s.whatsapp.net"`.

## 3. Causa Raiz

A causa raiz do problema é a **formatação incorreta do número de telefone no método `send_text_message` do `EvolutionAPIClient`**. A ausência do sufixo `@s.whatsapp.net` faz com que a API da Evolution não reconheça o destinatário como um usuário válido do WhatsApp. A API, em vez de retornar um erro claro (como um status `400 Bad Request`), parece descartar a requisição silenciosamente. Como nosso código não espera por essa falha silenciosa, o `FollowUpWorker` conclui sua execução sem gerar logs de erro, resultando no comportamento observado.

## 4. Solução Proposta

A solução consiste em corrigir a formatação do número de telefone dentro do método `send_text_message` em `app/integrations/evolution.py`, garantindo que o sufixo `@s.whatsapp.net` seja sempre anexado ao número do destinatário no payload da requisição.

## 5. Plano de Implementação

1.  **Arquivo a ser Modificado:** `app/integrations/evolution.py`
2.  **Método:** `send_text_message`
3.  **Modificação:** Alterar a construção do payload para formatar o número de telefone corretamente.

    -   **Trecho de código a ser alterado:**
        ```python
        payload = {
            "number": phone,
            "text": message,
            "delay": int(settings.delay_between_messages * 1000)
        }
        ```
    -   **Correção Proposta:**
        ```python
        payload = {
            "number": f"{phone}@s.whatsapp.net",
            "text": message,
            "delay": int(settings.delay_between_messages * 1000)
        }
        ```
    -   **Observação:** A chamada para `self._format_phone(phone)` no início do método já garante que o número esteja limpo e com o DDI `55`, então a única alteração necessária é na construção do payload.

## 6. Verificação e Testes

1.  **Monitoramento de Logs:** Após a aplicação da correção, monitorar os logs em tempo real para confirmar o aparecimento de entradas do `FollowUpWorker`, como `🚀 Processando tarefa...` e `✅ Follow-up ... executado`.
2.  **Teste Funcional:** Disparar um cenário que agende um follow-up (ex: deixar uma conversa inativa por 30 minutos) e verificar se a mensagem é efetivamente recebida no WhatsApp.
3.  **Teste de Regressão:** Realizar testes em outras funcionalidades que enviam mensagens (ex: resposta do agente, agendamento de reunião) para garantir que a alteração não introduziu efeitos colaterais.
