# Plano de Ação Estratégico: Estabilização e Refinamento do Agente

*Objetivo: Resolver os erros de parsing de ferramentas, garantir a robustez da comunicação com o LLM, tratar leads não encontrados e estabilizar as operações de follow-up no banco de dados.*

---

### Fase 1: Resolução do Erro de Parsing de Ferramentas (`re.error: unbalanced parenthesis`)

-   [x] **1.1. Analisar a Resposta Bruta do LLM:**
    -   **Status:** Concluído. A análise dos logs fornecidos anteriormente (`Resposta: <RESPOSTA_FINAL>Claro! Sem problemas. Eu tinha perguntado qual destes quatro modelos de soluções energéticas seria do seu interesse: 1. Instalação de usina própria 2. Aluguel de lote para instalação...`) indica que o LLM está gerando texto que, embora não seja uma tool call, contém caracteres que podem confundir a regex (como números seguidos de ponto e parênteses).
    -   **Justificativa:** A causa raiz é a geração de texto pelo LLM que se assemelha a uma regex malformada, mesmo que não seja uma tool call.

-   [ ] **1.2. Aprimorar a Regex de Parsing de Tools:**
    -   **Ação:** A regex atual `r'\\\[TOOL:\s*([^|\]+?)\s*(?:\|\s*([^\]*))?\\\]'` já escapa os colchetes. O problema não é a regex em si, mas o `re.findall` tentando interpretar o *conteúdo* da resposta do LLM como uma regex. A solução mais robusta é garantir que o LLM não gere esses caracteres de forma que quebre o parser.
    -   **Justificativa:** A correção principal virá do prompting.

-   [x] **1.3. Reforçar Prompting para Saída de Ferramentas:**
    -   **Ação:** Modificar `app/prompts/prompt-agente.md` para incluir instruções explícitas ao LLM para **nunca** gerar caracteres como `(`, `)`, `[`, `]`, `{`, `}` ou `.` em seu texto de resposta final de forma que possa ser confundido com sintaxe de tool ou regex. Enfatizar a importância de uma saída limpa e bem-formada.
    -   **Justificativa:** Atacar a raiz do problema, instruindo o LLM a evitar padrões que causam o erro.

---

### Fase 2: Tratamento de Respostas Vazias/Inválidas do LLM (`contents must not be empty`)

-   [x] **2.1. Investigar Causa Raiz da Resposta Vazia:**
    -   **Ação:** Este erro (`contents must not be empty`) geralmente ocorre quando o LLM não consegue gerar uma resposta válida, possivelmente devido a um prompt muito restritivo, contexto vazio ou filtros de segurança. Vou adicionar uma instrução no prompt para que o LLM sempre retorne uma resposta, mesmo que seja um fallback simples.
    -   **Justificativa:** Garantir que o LLM sempre forneça uma saída, mesmo em cenários difíceis.

-   [ ] **2.2. Implementar Retry Estratégico para LLM:**
    -   **Ação:** A lógica de retry já existe no `ModelManager`. Vou garantir que o prompt instrua o LLM a não retornar respostas vazias, o que deve reduzir a ocorrência desse erro.
    -   **Justificativa:** Aumentar a resiliência contra falhas intermitentes do LLM.

---

### Fase 3: Gerenciamento de Leads e Monitoramento

-   [x] **3.1. Tratar "Lead não encontrado para monitoramento":**
    -   **Ação:** Em `app/services/conversation_monitor.py`, no método `_check_inactive_conversations`, antes de chamar `followup_manager_service.handle_conversation_inactivity`, vou garantir que o `lead` seja válido. Se o lead não for encontrado, vou criar um lead básico no Supabase para esse número de telefone.
    -   **Justificativa:** Evitar warnings desnecessários e garantir que todas as mensagens sejam associadas a um lead, mesmo que seja um novo contato.

---

### Fase 4: Estabilização das Operações de Follow-up no Banco de Dados

-   [x] **4.1. Debugar "Erro ao atualizar follow-up":**
    -   **Ação:** Adicionar logs mais detalhados no método `update_follow_up_status` em `app/integrations/supabase_client.py`. Registrarei o `follow_up_id`, o `status` e o `update_data` completo que está sendo enviado.
    -   **Justificativa:** Identificar a causa exata da falha na atualização do status do follow-up.

---

### Fase 5: Testes e Validação

-   [ ] **5.1. Testes Automatizados:**
    -   [ ] Escrever testes unitários para as correções implementadas.
-   [ ] **5.2. Validação Manual:**
    -   [ ] Executar cenários de ponta a ponta para confirmar que todos os problemas foram resolvidos e que o agente opera de forma estável.