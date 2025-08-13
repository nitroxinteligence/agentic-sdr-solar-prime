# Relatório de Diagnóstico: Loop Infinito do Agente SDR

## 1. Resumo do Problema

O agente SDR está preso em um loop infinito, respondendo repetidamente com a mesma saudação inicial ("Bom dia! Tudo bem? Me chamo Helen Vieira...") para todas as mensagens do usuário, incluindo a resposta do usuário com seu nome. O agente não consegue sair do **Estágio 0 (Coleta de Nome)**, impedindo qualquer progresso na conversa.

## 2. Análise do Log de Eventos

A análise do `logs-console.md` revela um padrão claro que causa o loop:

1.  **Primeira Mensagem do Usuário (`oi`)**:
    *   `20:05:57`: O webhook recebe a mensagem "oi".
    *   `20:06:27`: Após um **delay de 30 segundos** (causado pelo `MessageBuffer`), a mensagem é processada.
    *   O agente (corretamente) identifica que é um novo lead, determina o estágio como `estágio_0_coleta_nome`.
    *   `20:06:40`: O agente responde com a saudação padrão e a pergunta "como posso te chamar?".

2.  **Segunda Mensagem do Usuário (`mateus`)**:
    *   `20:07:00`: O webhook recebe a resposta "mateus".
    *   `20:07:30`: Novamente, após um **delay de 30 segundos**, a mensagem é processada.
    *   O histórico da conversa é carregado (`3 mensagens`).
    *   **PONTO CRÍTICO**: O log `Campo alterado: qualification_score` aparece, mas **nenhum log de "Nome detectado" é gerado**. Isso prova que a lógica de extração de nome falhou.
    *   Como o nome não foi detectado, o `ContextAnalyzer` novamente define o estágio como `estágio_0_coleta_nome`.
    *   `20:07:40`: O agente, preso no Estágio 0, envia **exatamente a mesma saudação inicial de novo**.

3.  **Conclusão do Log**: O ciclo se repete indefinidamente porque o estado da conversa (ter o nome do lead) nunca é atualizado.

## 3. Diagnóstico da Causa Raiz

### Causa Primária: Falha na Lógica de Detecção de Nome

O problema central está na lógica responsável por identificar o nome do usuário no histórico da conversa, localizada nos arquivos `app/core/context_analyzer.py` e `app/core/lead_manager.py`.

- **O que deveria acontecer**: Após o agente perguntar "como posso te chamar?", a lógica deveria identificar a próxima mensagem do usuário ("mateus") como sendo o nome.
- **O que está acontecendo**: A implementação da verificação contextual está falhando. Embora o código para verificar a mensagem anterior (`prev_msg`) exista, ele não está funcionando como esperado. A ausência do log `🎯 Nome detectado no contexto` confirma que a condição para extrair o nome nunca é satisfeita.

**Bug Específico**: A lógica em `ContextAnalyzer._determine_stage` e `LeadManager.extract_lead_info` que verifica a mensagem anterior para identificar o nome do lead contém uma falha sutil que a impede de funcionar corretamente. Sem essa detecção contextual, o sistema não tem como saber que o nome "mateus" foi fornecido e, portanto, nunca avança para o "Estágio 1".

### Causa Secundária: Latência Excessiva do Buffer de Mensagens

O `MessageBuffer` está configurado com um **timeout de 30 segundos** (`message_buffer_timeout`). Isso causa uma péssima experiência para o usuário, que precisa esperar 30 segundos por cada resposta, tornando o loop ainda mais problemático. Para uma conversa fluida, esse valor é excessivamente alto.

## 4. Conflitos e Bugs Adicionais Encontrados

Durante a análise, outros problemas foram identificados na arquitetura do `app/`:

1.  **Instanciação Ineficiente de Serviços**: No arquivo `app/agents/agentic_sdr_refactored.py`, dentro do método `_sync_lead_changes`, uma nova instância de `CRMServiceReal` é criada a cada chamada (`crm = CRMServiceReal()`). Isso é ineficiente e deve ser substituído pelo uso de uma instância singleton, assim como os outros serviços no `TeamCoordinator`.
2.  **Lógica de Extração de Resposta Frágil**: A função `extract_final_response` em `app/api/webhooks.py` depende estritamente da presença das tags `<RESPOSTA_FINAL>`. Embora exista um fallback, o log mostra que o modelo de linguagem nem sempre inclui as tags, forçando o sistema a adicioná-las manualmente (`Tags ausentes - adicionando automaticamente`). Isso indica uma falta de robustez na conformidade do LLM com o prompt.
3.  **Falta de Validação de Histórico**: O agente depende 100% do histórico carregado do Supabase. Se o histórico falhar ao carregar ou vier corrompido, o agente não tem um mecanismo de fallback e reinicia a conversa, o que pode ter contribuído para o loop.

## 5. Recomendações de Correção

Para resolver o loop e melhorar a robustez do sistema, recomendo as seguintes ações:

1.  **Corrigir a Detecção de Nome (Crítico)**:
    *   **Ação**: Refatorar a lógica em `app/core/context_analyzer.py` e `app/core/lead_manager.py`.
    *   **Sugestão**: Em vez de depender apenas da mensagem anterior, o `ContextAnalyzer` deve ter um estado mais explícito. Ao determinar que está no `estágio_0_coleta_nome`, ele deve "saber" que a próxima mensagem do usuário é, com alta probabilidade, o nome, e tratá-la como tal, independentemente do conteúdo exato da mensagem anterior.

2.  **Reduzir o Timeout do Buffer de Mensagens**:
    *   **Ação**: Alterar a variável de ambiente `MESSAGE_BUFFER_TIMEOUT` para um valor baixo.
    *   **Sugestão**: Um valor entre **1 e 3 segundos** é o ideal para agrupar mensagens rápidas sem criar uma latência perceptível.

3.  **Otimizar a Instanciação de Serviços**:
    *   **Ação**: Modificar `_sync_lead_changes` em `app/agents/agentic_sdr_refactored.py` para usar a instância de serviço do `TeamCoordinator` em vez de criar uma nova.
    *   **Sugestão**: `crm_service = self.team_coordinator.services.get("crm")`.

4.  **Robustecer a Extração da Resposta Final**:
    *   **Ação**: Melhorar a função `extract_final_response` em `app/api/webhooks.py`.
    *   **Sugestão**: Adicionar uma lógica que, se as tags `<RESPOSTA_FINAL>` não forem encontradas, a função deve assumir que *toda* a resposta do modelo é a resposta final, em vez de usar um fallback genérico. Isso evita a perda da resposta gerada pela IA.

A aplicação dessas correções resolverá o loop infinito, melhorará drasticamente a responsividade do agente e tornará o sistema mais estável e eficiente.
