# Diagnóstico e Plano de Sincronização para Agente de Produção v2

## 1. Reavaliação do Diagnóstico (Pós-Pesquisa)

Após uma análise mais profunda do código, dos logs e das melhores práticas de mercado para 2025, o diagnóstico inicial foi confirmado e refinado. O agente não está apenas com bugs, mas sofre de **falhas arquiteturais** que o tornam inadequado para um ambiente de produção.

-   **Causa Raiz Principal (Confirmada): Arquitetura Stateful com Singleton.** A tentativa de gerenciar o estado da conversa (memória) em uma única instância global (`singleton`) é o erro arquitetural primário. Em produção, múltiplas requisições (usuários) acessam o mesmo objeto, corrompendo o histórico de conversas umas das outras. A solução **não é** criar um sistema stateful complexo, mas sim adotar uma **arquitetura 100% stateless**, que é o padrão ouro para serviços web escaláveis e robustos.

-   **Causa Raiz Secundária (Confirmada): Falta de Contexto Essencial.** O agente opera "cego" para informações críticas. A falta do **histórico completo da conversa** e da **data/hora atual** no prompt o impede de manter a coerência e tomar decisões lógicas, levando a repetições e sugestões absurdas (como agendar para horários que já passaram).

-   **Causa Raiz Terciária (Confirmada): Lógica de Negócio Frágil.** O acionamento de ferramentas críticas (como o Google Calendar) por simples palavras-chave é ineficaz. O sistema precisa entender a **intenção** do usuário.

## 2. A Arquitetura Correta: Simples, Robusta e Stateless

Para resolver os problemas de forma definitiva e com **complexidade zero**, propomos uma arquitetura stateless, onde cada mensagem do WhatsApp é processada de forma independente e autocontida.

**O Novo Fluxo de Execução:**

1.  **Webhook Recebe a Mensagem:** O `webhooks.py` recebe a chamada da Evolution API.
2.  **Criação de um "Contexto de Execução":** Em vez de usar uma instância de agente compartilhada, para cada nova mensagem, nós criamos um objeto de contexto de curta duração. Este objeto é responsável por:
    a.  Carregar do Supabase **todo** o histórico da conversa para aquele usuário específico (`phone`).
    b.  Carregar as informações do lead (`lead_info`).
    c.  Obter a data e hora atuais.
3.  **Agente se Torna uma Função Pura:** A classe `AgenticSDR` deixa de ter estado (`self.conversation_history`, etc.). Sua função `process_message` é refatorada para receber o "Contexto de Execução" como um argumento. Ela usa o contexto para gerar uma resposta e retorna o resultado, sem alterar seu próprio estado.
4.  **Fim da Requisição:** O contexto daquela execução é descartado. A próxima mensagem do mesmo usuário iniciará um novo ciclo, carregando o histórico atualizado.

**Vantagens desta Abordagem:**
-   **Robustez:** Cada conversa é perfeitamente isolada. Não há risco de contaminação de dados entre usuários.
-   **Escalabilidade:** A arquitetura se torna horizontalmente escalável. Você pode ter múltiplas instâncias do seu servidor rodando em paralelo sem nenhum problema de estado compartilhado.
-   **Simplicidade:** Mantemos a lógica modular, mas eliminamos a complexidade e os perigos do gerenciamento de estado na memória da aplicação.

## 3. Plano de Ação Definitivo (Zero Complexidade)

### Ação 1: Implementar a Arquitetura Stateless (Correção Imediata de Contexto e Repetição)

-   **Objetivo:** Isolar cada conversa, eliminando a causa raiz da instabilidade.
-   **Passos:**
    1.  **Remover Singleton:** Em `app/agents/agentic_sdr_refactored.py`, eliminar o padrão singleton (`_singleton_instance`, `_singleton_lock`, e a função `get_agentic_agent`).
    2.  **Refatorar `AgenticSDR`:**
        -   O método `__init__` deve continuar inicializando os módulos (ModelManager, etc.), mas não mais os atributos de estado (`self.conversation_history`, `self.current_lead_info`, etc.).
        -   O método `process_message` deve ser modificado para aceitar `conversation_history` e `lead_info` como parâmetros, em vez de acessá-los de `self`.
    3.  **Centralizar o Carregamento de Contexto:** Em `app/api/webhooks.py`, na função `process_message_with_agent`, antes de chamar o agente:
        a.  Criar uma **nova instância** de `AgenticSDR` a cada chamada: `agent = AgenticSDR()`.
        b.  Carregar o histórico completo da conversa do Supabase (limite de 200 mensagens).
        c.  Chamar o agente passando o histórico e as informações do lead: `response = await agent.process_message(message, history, lead_info, metadata)`.

### Ação 2: Enriquecer o Prompt com Contexto Essencial (Correção de Lógica e Alucinação)

-   **Objetivo:** Dar ao LLM a informação necessária para raciocinar corretamente.
-   **Passos:**
    1.  **Injetar Data/Hora:** Em `app/agents/agentic_sdr_refactored.py`, na função `_build_prompt`, adicionar a data e hora atuais no topo do prompt. A informação deve vir dos metadados da requisição.
        -   Exemplo: `prompt_parts.insert(0, f"Data e hora atuais: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")`
    2.  **Enviar Histórico Completo:** Na função `_generate_response`, remover a limitação de 10 mensagens. Enviar um histórico mais longo (ex: 200 últimas mensagens).

### Ação 3: Robustecer o Acionamento do Google Calendar

-   **Objetivo:** Garantir que o agendamento de reuniões funcione de forma confiável.
-   **Passos:**
    1.  **Acionamento por Intenção:** No `TeamCoordinator`, a função `analyze_service_need` deve ser aprimorada. Além de palavras-chave, ela deve considerar o `user_intent` e `conversation_stage` do `ContextAnalyzer` para aumentar o score do `calendar_service` quando a intenção for de agendamento.
    2.  **Validação de Credenciais em Produção:**
        -   **Gerar Novo Refresh Token:** É **mandatório** acessar a URL `/google/auth` **a partir do servidor de produção** para gerar um novo `refresh_token` que seja válido para o domínio de produção.
        -   **Verificar Google Cloud Console:** Adicionar a URL do domínio de produção (ex: `https://seu-app.easypanel.host`) à lista de "Origens de JavaScript autorizadas" e "URIs de redirecionamento autorizados" nas credenciais OAuth 2.0 no Google Cloud.

### Ação 4: Simplificar e Otimizar o Prompt Principal

-   **Objetivo:** Reduzir a complexidade do prompt para melhorar a adesão do LLM às regras críticas.
-   **Passos:**
    1.  **Revisar `prompt-agente.md`:** Analisar o prompt em busca de seções redundantes ou conflitantes (conforme o arquivo `ajustes-prompt.md`).
    2.  **Priorizar Regras Críticas:** Mover as regras mais importantes (como "NÃO OFEREÇA PARA LIGAR") para o topo da seção de regras, tornando-as mais visíveis para o modelo.
    3.  **Remover Instruções Desnecessárias:** Eliminar instruções que já são cobertas pela lógica do código (ex: como formatar a resposta final, que já é tratada pelo `ResponseFormatter`).

Ao seguir este plano, transformaremos o agente de um protótipo instável para uma aplicação de produção simples, stateless e robusta, resolvendo as falhas de forma estrutural.