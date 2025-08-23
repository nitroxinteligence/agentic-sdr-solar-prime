# 🧠 GEMINI.md - Guia de Contexto do Projeto Agentic SDR SolarPrime

## 1. Visão Geral do Projeto

O **Agentic SDR SolarPrime** é um sistema de IA conversacional projetado para atuar como um Sales Development Representative (SDR) para a empresa SolarPrime. O agente, chamado **Helen Vieira**, interage com leads via WhatsApp para qualificá-los, apresentar soluções de energia solar, responder a objeções e agendar reuniões.

**Objetivos Principais:**
-   Automatizar o processo de qualificação de leads.
-   Manter conversas naturais e humanizadas.
-   Integrar-se a sistemas externos para agendamento (Google Calendar) e gestão de leads (Kommo CRM).
-   Operar de forma escalável e resiliente.

## 2. Arquitetura Stateless

O núcleo do sistema é a sua **arquitetura stateless**, implementada na classe `AgenticSDRStateless` (`app/agents/agentic_sdr_stateless.py`).

-   **Isolamento por Requisição:** Cada mensagem recebida do usuário cria uma nova instância do agente. Não há estado (como histórico de conversa ou informações do lead) armazenado na memória do agente entre as interações.
-   **Contexto Explícito:** Todo o contexto necessário para o processamento (histórico, dados do lead, etc.) é carregado do banco de dados (Supabase) a cada nova mensagem e passado para o agente através de um `execution_context`.
-   **Benefícios:** Esta abordagem garante que o sistema seja *thread-safe*, escalável horizontalmente e robusto, pois não há risco de contaminação de estado entre conversas simultâneas.

## 3. Componentes Principais

A codebase está organizada de forma modular para separar as responsabilidades:

-   `main.py`: Ponto de entrada da aplicação FastAPI. Gerencia o ciclo de vida (startup/shutdown) e inicializa os serviços principais.
-   `app/config.py`: Centraliza todas as configurações do sistema, carregadas a partir de variáveis de ambiente (`.env`).
-   `app/api/`: Contém os endpoints da API, incluindo o webhook principal (`webhooks.py`) que recebe as mensagens da Evolution API (WhatsApp).
-   `app/agents/`: O cérebro do sistema. `agentic_sdr_stateless.py` orquestra o fluxo de resposta, interagindo com os outros módulos.
-   `app/prompts/`: Armazena o prompt principal (`prompt-agente.md`) que define a persona, as regras e as capacidades do agente Helen.
-   `app/core/`: Módulos de baixo nível que realizam tarefas específicas como análise de contexto (`context_analyzer.py`), extração de informações do lead (`lead_manager.py`), processamento de mídia (`multimodal_processor.py`) e gerenciamento de modelos de linguagem (`model_manager.py`).
-   `app/services/`: Lógica de negócio de alto nível que interage com sistemas externos.
    -   `calendar_service_100_real.py`: Gerencia a integração com o Google Calendar.
    -   `crm_service_100_real.py`: Gerencia a integração com o Kommo CRM.
    -   `followup_service_100_real.py`: Lida com o agendamento de follow-ups.
-   `app/integrations/`: Clientes de API para comunicação com serviços externos como Supabase, Redis e Evolution API.

## 4. Fluxo de Mensagem (End-to-End)

1.  **Recebimento:** A **Evolution API** envia um webhook com uma nova mensagem para `app/api/webhooks.py`.
2.  **Buffer:** A mensagem é adicionada a um `MessageBuffer` (`app/services/message_buffer.py`) que agrupa mensagens rápidas do mesmo usuário para processá-las como uma única entrada.
3.  **Criação de Contexto:** Após o buffer, a função `create_agent_with_context` é chamada. Ela usa o número de telefone para buscar o histórico do lead e da conversa no **Supabase**.
4.  **Instanciação do Agente:** Uma nova instância do `AgenticSDRStateless` é criada, recebendo o `execution_context` com todos os dados carregados.
5.  **Processamento:** O agente:
    a.  Processa qualquer mídia recebida (imagens, áudios) com o `MultimodalProcessor`.
    b.  Usa o `LeadManager` e o `ContextAnalyzer` para extrair informações e entender a intenção.
    c.  Chama o `ModelManager` para gerar uma resposta do LLM (Gemini), que pode incluir uma resposta textual ou uma chamada de ferramenta.
6.  **Execução de Ferramentas:** Se o LLM retornar uma chamada de ferramenta (ex: `[TOOL: calendar.schedule_meeting]`), o agente a executa através do serviço correspondente.
7.  **Resposta Final:** O resultado da ferramenta é usado para gerar uma nova resposta final para o usuário.
8.  **Envio:** A resposta é dividida em partes menores, se necessário, pelo `MessageSplitter` e enviada de volta ao usuário via **Evolution API**.

## 5. Integrações Externas

-   **Supabase:** Usado como banco de dados principal para persistir todas as informações: leads, conversas, mensagens, follow-ups e base de conhecimento.
-   **Kommo CRM:** O sistema de gestão de relacionamento com o cliente. O agente sincroniza dados do lead, atualiza estágios no pipeline de vendas e adiciona tags contextuais.
-   **Google Calendar:** Utilizado para agendar, reagendar e cancelar reuniões. A integração é feita via **OAuth 2.0**, permitindo que o agente atue em nome de um usuário real e crie eventos com links do Google Meet.
-   **Evolution API:** A ponte de comunicação com o WhatsApp.
-   **Redis:** Usado para cache (melhorando a performance) e como broker para o sistema de follow-ups.

## 6. Sistema de Ferramentas (Tool Calling)

O agente interage com os serviços através de um sistema de "Tool Calling". O LLM é instruído a gerar uma string formatada quando precisa executar uma ação.

-   **Sintaxe:** `[TOOL: service.method | param1=value1]`
-   **Exemplo:** `[TOOL: calendar.schedule_meeting | date=2025-08-25 | time=11:00]`
-   **Executor:** O método `_execute_single_tool` em `agentic_sdr_stateless.py` parseia essa string e direciona a chamada para o serviço e método corretos.
-   **Benefício:** Esta abordagem impede que o LLM "alucine" ou invente informações, pois ele é forçado a usar as ferramentas para obter dados do mundo real (como horários disponíveis) ou para executar ações.

## 7. Configuração e Execução

-   **Configuração:** Todas as chaves de API, URLs e parâmetros de comportamento são gerenciados no arquivo `.env`.
-   **Execução:** A aplicação é iniciada com o comando `uvicorn main:app --host 0.0.0.0 --port 8000`.
-   **Docker:** O projeto inclui um `Dockerfile` para facilitar o deploy em contêineres.
-   **Dependências:** Todas as bibliotecas Python necessárias estão listadas em `requirements.txt`.
