# Relatório de Diagnóstico: Duplicação de Leads no Supabase e Kommo CRM

**Data:** 23 de Agosto de 2025
**Autor:** Agente Gemini
**Status:** Análise Concluída

---

## 1. Resumo do Problema (Sintoma)

O sistema está criando múltiplos registros para o mesmo lead no banco de dados do Supabase e, consequentemente, no Kommo CRM. As evidências mostram leads sendo criados com nomes incorretos (extraídos do conteúdo da mensagem, como "Segunda" ou "Isso Mesmo"), indicando uma falha no fluxo de identificação e persistência de novos contatos.

-   **Impacto:** Crítico. A duplicação de dados corrompe a integridade do banco de dados, polui o funil do CRM, impede o rastreamento correto da jornada do lead e causa confusão para a equipe de vendas.

## 2. Análise da Causa Raiz

A investigação profunda do código-fonte, focada no fluxo de processamento de novas mensagens, revelou uma falha arquitetural na lógica de "get-or-create" do lead.

### Falha Principal: Criação Prematura de Leads no Webhook

1.  **Local da Falha:** A causa raiz está na função `process_message_with_agent` no arquivo `app/api/webhooks.py`.

2.  **Lógica Defeituosa:** O código atual implementa a seguinte sequência:
    a. Recebe uma mensagem de um número de telefone (`phone`).
    b. Tenta buscar o lead no Supabase com `get_lead_by_phone(phone)`.
    c. **Se o lead não for encontrado (`if not lead`), ele imediatamente cria um novo registro no Supabase** usando apenas o número de telefone, antes mesmo de qualquer análise de conteúdo.

3.  **Consequência Direta:** Esta abordagem "criar na primeira falha" é extremamente frágil e causa a duplicação por vários motivos:
    *   **Criação com Dados Incompletos:** Um lead é persistido no banco de dados sem informações essenciais, como o nome. Isso leva à criação de "leads fantasmas".
    *   **Extração de Nomes Incorretos:** Como o lead já existe (mesmo que de forma incompleta), o `LeadManager` tenta extrair um nome da primeira mensagem, que geralmente não é um nome, resultando em leads chamados "Segunda", "Ok", ou "terça estarei ocupado".
    *   **Condições de Corrida:** Se duas mensagens chegarem em rápida sucessão, ou se houver uma pequena latência na busca do banco de dados, ambos os processos podem falhar em encontrar o lead e ambos tentarão criá-lo, resultando em duplicatas diretas.

### Análise da Suspeita sobre o Redis

Sua suspeita sobre o Redis foi investigada. O Redis é utilizado para cache de conversas e para locks distribuídos (principalmente no agendamento de calendário), mas **não é a causa raiz deste problema**. A falha não está na tecnologia de cache, mas na lógica de aplicação que decide *quando* criar um novo lead. A criação prematura no webhook ocorreria com ou sem o Redis.

## 3. Solução Estratégica Proposta

A solução correta e robusta é centralizar e atrasar a criação do lead, garantindo que ele só seja persistido quando tivermos informações mínimas e uma intenção clara.

### Pilares da Solução:

1.  **Remover a Lógica de Criação do Webhook:** A função `process_message_with_agent` em `app/api/webhooks.py` deve ser modificada para **apenas buscar** o lead (`get_lead_by_phone`). A criação (`create_lead`) deve ser completamente removida deste arquivo. O `lead_info` será passado para o agente como um dicionário existente ou um dicionário vazio.

2.  **Centralizar a Criação no Agente:** A responsabilidade de criar o lead (tanto no Supabase quanto no Kommo) deve ser movida para o método `_sync_external_services` dentro de `app/agents/agentic_sdr_stateless.py`.

3.  **Condicionar a Criação à Existência de um Nome:** A lógica em `_sync_external_services` já possui a condição correta: `if lead_info.get("name") and not lead_info.get("kommo_lead_id"):`. Vamos expandir essa lógica para também criar o lead no Supabase nesse mesmo momento.

### Novo Fluxo Corrigido:

1.  **Webhook (`webhooks.py`):**
    *   Recebe a mensagem.
    *   Chama `get_lead_by_phone`.
    *   Se o lead existe, passa o `lead_info` para o agente.
    *   Se o lead **não existe**, passa um `lead_info` **vazio** (`{}`) para o agente. **Nenhuma criação ocorre aqui.**

2.  **Agente (`agentic_sdr_stateless.py`):**
    *   O agente processa a conversa e o `LeadManager` extrai o nome do lead, populando o `lead_info`.
    *   O método `_sync_external_services` é chamado.
    *   A condição `if lead_info.get("name")` agora é o gatilho.
    *   **Dentro deste `if`**, o agente primeiro cria o lead no Supabase, obtém o ID, e em seguida cria o lead no Kommo.

Esta abordagem garante que um lead só seja criado quando tivermos um nome, eliminando a criação de registros fantasmas e resolvendo o problema de duplicação de forma definitiva.