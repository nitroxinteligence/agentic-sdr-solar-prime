# Plano de Análise e Correção Definitiva do Agente

O agente está sofrendo de "amnésia" e respondendo de forma genérica, ignorando o prompt do sistema e o histórico da conversa. A causa raiz não está no `model_manager`, mas sim na forma como o contexto e o histórico são montados e enviados ao modelo.

## Tarefas

1.  **[CONCLUÍDO] Análise Profunda do Fluxo de Dados:** Rastrear o ciclo de vida de uma mensagem, desde o recebimento no webhook (`webhooks.py`) até a montagem do prompt no agente (`agentic_sdr_stateless.py`) e o envio final ao modelo (`model_manager.py`).

2.  **[CONCLUÍDO] Identificação da Causa Raiz:** O problema foi localizado em `app/agents/agentic_sdr_stateless.py`. A estratégia de "injetar" o contexto dinâmico (informações do lead, análise da conversa) diretamente no prompt do sistema está causando um conflito, fazendo com que o modelo ignore suas instruções de persona e o histórico.

3.  **[EM ANDAMENTO] Refatorar a Injeção de Contexto:** Implementar uma abordagem mais robusta e clara. Em vez de poluir o prompt do sistema, o contexto dinâmico será formatado e adicionado como a **última mensagem do usuário** no histórico enviado ao modelo. Isso separa a identidade central do agente (system prompt) do contexto da tarefa atual (última mensagem), dando o peso correto a cada um.

4.  **[PENDENTE] Implementar a Correção:** Substituir a função `_generate_response` em `app/agents/agentic_sdr_stateless.py` pela nova versão refatorada.

5.  **[PENDENTE] Publicar a Correção:** Após a implementação, adicionar, comitar e enviar a correção final para o repositório.