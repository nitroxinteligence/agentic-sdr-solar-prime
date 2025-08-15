# Diagnóstico Completo e Plano de Ação para Instabilidade do Agente

## 1. Resumo Executivo

O agente SDR (Helen Vieira) está apresentando um comportamento degradado e inconsistente em produção, caracterizado por perda de contexto, falha na execução de ferramentas (Google Calendar), alucinação temporal e quebra de regras do prompt. A análise do código-fonte e dos logs revela que a causa raiz não é um único bug, mas uma combinação de problemas arquiteturais e lógicos que se manifestam sob a carga e o ambiente de produção.

Os principais pilares da falha são:

1.  **Gestão de Estado Inadequada:** O uso de uma instância singleton para o agente (`AgenticSDR`) é a causa mais provável da perda de contexto e repetição, pois o estado da conversa de múltiplos usuários é compartilhado e corrompido.
2.  **Falta de Consciência Situacional:** O agente não recebe informações essenciais como a data e a hora atuais, o que o torna incapaz de tomar decisões temporais corretas (ex: agendar para um horário que já passou).
3.  **Acionamento de Ferramentas Frágil:** A lógica para decidir quando usar o `calendar_service` é baseada em uma simples correspondência de palavras-chave, falhando em capturar a real intenção do usuário.
4.  **Contexto de Conversa Limitado:** O agente só recebe as últimas 10 mensagens do histórico, o que é insuficiente para manter a coerência em conversas mais longas.

Este documento detalha cada problema, sua causa raiz e um plano de ação para estabilizar o sistema e torná-lo robusto para o ambiente de produção.

---

## 2. Análise Detalhada dos Problemas

### Problema 1: Perda de Contexto e Repetição de Mensagens

-   **Sintomas:** O agente se perde no fluxo, repete as mesmas perguntas e frases, e parece não ter memória de interações anteriores.
-   **Causa Raiz:** A classe `AgenticSDR` é implementada como um **singleton** (`_singleton_instance`). Em um ambiente de produção com múltiplos usuários simultâneos, a mesma instância do agente é compartilhada entre todas as conversas. Isso faz com que o `self.conversation_history` de um usuário seja sobrescrito ou misturado com o de outro, levando à perda total de contexto.
-   **Agravante:** A função `_generate_response` limita o histórico enviado ao LLM a apenas 10 mensagens (`recent_history = self.conversation_history[-11:-1]`). Mesmo em uma conversa com um único usuário, isso garante que o agente "esqueça" o início da interação, levando a repetições.

### Problema 2: Falha na Integração com Google Calendar

-   **Sintomas:** O agente não consulta a agenda, não oferece horários reais e não agenda reuniões, apesar de ser uma de suas funções principais.
-   **Causa Raiz 1 (Acionamento por Palavra-chave):** O `TeamCoordinator` decide chamar o `calendar_service` baseado em uma lista fixa de palavras-chave (ex: "agendar", "reunião"). Uma frase natural do usuário como "pode ser hoje?" não aciona o serviço, pois não contém as palavras exatas. A lógica não captura a **intenção** de agendamento.
-   **Causa Raiz 2 (Configuração de Ambiente):** A autenticação com APIs do Google é altamente sensível ao ambiente. O fato de funcionar em desenvolvimento e falhar em produção aponta para um problema de configuração. Causas comuns incluem:
    -   O `GOOGLE_OAUTH_REFRESH_TOKEN` foi gerado para `localhost` e é inválido no domínio de produção.
    -   A URL do servidor de produção não está na lista de URIs de redirecionamento autorizados no Google Cloud Console.
    -   As credenciais (JSON ou variáveis de ambiente) não estão acessíveis ou configuradas corretamente no contêiner de produção.

### Problema 3: Falta de Consciência Temporal

-   **Sintoma:** O agente sugere agendar uma reunião para um horário que já passou (ex: sugerir 14h30 quando já são 17h10).
-   **Causa Raiz:** O agente não tem acesso à informação do dia e hora atuais. A função `_build_prompt` não injeta um timestamp ou data/hora no contexto enviado ao LLM. Sem essa informação, o modelo não tem como raciocinar sobre a validade temporal dos horários que sugere.

### Problema 4: Quebra de Regras do Prompt

-   **Sintoma:** O agente sugere ligar para o lead, uma ação explicitamente proibida no prompt.
-   **Causa Raiz:** Este é um sintoma direto da perda de contexto e da sobrecarga de regras. Quando o histórico da conversa é inconsistente e o prompt é excessivamente longo e complexo, o LLM tende a ignorar restrições específicas e reverter para um comportamento padrão de "assistente prestativo", que considera uma ligação uma ação lógica.

## 3. Plano de Ação Corretivo

As seguintes ações são propostas para corrigir as falhas identificadas e estabilizar o agente.

### Ação 1: Refatorar a Gestão de Estado (Correção de Contexto)

-   **Objetivo:** Isolar o estado de cada conversa para garantir que não haja mais contaminação entre usuários.
-   **Passos:**
    1.  **Eliminar o Singleton:** Remover o padrão singleton de `app/agents/agentic_sdr_refactored.py`. Em vez de `get_agentic_agent()`, cada requisição no webhook (`process_message_with_agent`) deve criar uma **nova instância** de `AgenticSDR`.
    2.  **Passar Estado via Parâmetros:** O histórico da conversa e as informações do lead, que hoje são atributos de instância (`self.conversation_history`), devem ser carregados no início da requisição e passados como argumentos para as funções que precisam deles. Isso torna o agente sem estado (stateless), que é a prática recomendada para aplicações web concorrentes.

### Ação 2: Aprimorar o Contexto do Prompt

-   **Objetivo:** Fornecer ao agente todo o contexto necessário para tomar decisões inteligentes e coerentes.
-   **Passos:**
    1.  **Aumentar Janela de Histórico:** Na função `_generate_response`, modificar a extração de histórico. Em vez das últimas 10 mensagens, enviar um histórico mais substancial (ex: as últimas 50 mensagens ou um resumo inteligente das interações anteriores).
    2.  **Injetar Data e Hora no Prompt:** Na função `_build_prompt`, adicionar a data e a hora atuais ao prompt do sistema. Ex: `Data e hora atuais: 2025-08-14 17:10 (America/Sao_Paulo)`.
    3.  **Simplificar o Prompt:** Revisar o `prompt-agente.md` para remover redundâncias e simplificar as regras, tornando-as mais diretas e fáceis de serem seguidas pelo LLM.

### Ação 3: Robustecer o Acionamento de Ferramentas

-   **Objetivo:** Mudar de uma detecção baseada em palavras-chave para uma detecção baseada em intenção.
-   **Passos:**
    1.  **Análise de Intenção:** Aprimorar o `ContextAnalyzer` para que a `action_needed` seja mais precisa. Em vez de apenas palavras-chave, ele pode usar um modelo de linguagem menor ou regras mais sofisticadas para identificar a intenção de "agendar", "perguntar sobre preço", etc.
    2.  **Acionamento por Intenção:** Modificar o `TeamCoordinator` para usar o campo `action_needed` do contexto como o principal gatilho para chamar os serviços, em vez de depender apenas de palavras-chave na mensagem mais recente.

### Ação 4: Validar Configurações de Produção

-   **Objetivo:** Garantir que as credenciais e configurações do Google Calendar para o ambiente de produção estejam corretas.
-   **Passos:**
    1.  **Re-autenticação OAuth:** Gerar um novo `GOOGLE_OAUTH_REFRESH_TOKEN` a partir do ambiente de produção, acessando a URL `/google/auth` do servidor em produção.
    2.  **Verificar Google Cloud Console:** Garantir que o URI de redirecionamento OAuth e as origens de JavaScript autorizadas no Google Cloud Console incluam o domínio do servidor de produção.
    3.  **Logs de Diagnóstico:** Adicionar logs detalhados no `CalendarServiceReal` e no `GoogleOAuthHandler` para registrar qual método de autenticação está sendo usado e se as credenciais estão sendo carregadas corretamente em produção.

Ao implementar estas quatro ações, o sistema se tornará mais estável, contextualizado e confiável, resolvendo os problemas críticos observados em produção.