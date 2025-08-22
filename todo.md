# Plano de Ação para Correção e Melhoria do Agente SDR

Este documento descreve as tarefas necessárias para resolver os problemas críticos identificados no relatório de diagnóstico e para melhorar a robustez e inteligência do sistema.

---

### Fase 1: Correção Imediata e Estabilização

*Objetivo: Fazer o agente voltar a responder de forma consistente e obter visibilidade sobre as falhas.*

- [ ] **Melhorar Logging do `ModelManager`:**
    - [ ] Em `app/core/model_manager.py`, adicionar logs que mostrem:
        - O `system_prompt` completo enviado ao modelo.
        - O número de mensagens do histórico.
        - A resposta bruta (raw) recebida do modelo antes de qualquer parsing.
- [ ] **Implementar Truncamento de Histórico:**
    - [ ] Em `app/agents/agentic_sdr_stateless.py`, na função `_generate_response`, limitar o histórico de conversa enviado ao modelo para as últimas 100-500 mensagens para evitar sobrecarga de contexto.
- [ ] **Simplificar o Tratamento de Erros Imediato:**
    - [ ] No bloco `except` principal de `process_message`, garantir que o traceback completo do erro seja logado para facilitar a depuração futura.
- [ ] **Revisar a Função `extract_final_response`:**
    - [ ] Em `app/api/webhooks.py`, adicionar um log de alerta quando a tag `<RESPOSTA_FINAL>` não for encontrada na resposta do LLM, registrando a resposta bruta que foi recebida.

---

### Fase 2: Refatoração e Aumento da Robustez

*Objetivo: Substituir componentes frágeis por soluções mais inteligentes e reestruturar o código para melhor manutenção.*

- [ ] **Refatorar a Função `process_message`:**
    - [ ] Em `app/agents/agentic_sdr_stateless.py`, quebrar a função `process_message` em um pipeline de métodos menores e com responsabilidade única (ex: `_handle_media`, `_update_lead_from_history`, `_execute_intent_bypass`, `_run_llm_flow`).
- [ ] **Substituir Extração por Regex por LLM:**
    - [ ] Criar uma nova função no `ModelManager` chamada `get_structured_response` que força o LLM a responder em formato JSON.
    - [ ] Em `app/core/lead_manager.py`, substituir as funções `_extract_name`, `_extract_email`, `_extract_bill_value` por uma única chamada ao `get_structured_response` que extrai todas as entidades de uma vez.
    - [ ] Em `app/core/context_analyzer.py`, fazer o mesmo para `_extract_intent` e outras análises.
- [ ] **Centralizar o Acesso ao Banco de Dados:**
    - [ ] Remover as importações diretas do `supabase_client` de dentro dos métodos do agente.
    - [ ] Passar o `supabase_client` como uma dependência no construtor ou nos métodos, ou criar uma camada de serviço de dados dedicada.
- [ ] **Implementar Exceções Customizadas:**
    - [ ] Em `app/exceptions/__init__.py`, definir exceções como `LLMResponseError`, `ToolExecutionError`, `DataExtractionError`.
    - [ ] Usar essas exceções nos blocos `try...except` para um tratamento de erro mais granular e inteligente.

---