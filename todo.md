# Plano de Ação: Correção Definitiva do Fallback para OpenAI

*Objetivo: Garantir que o fallback para o modelo OpenAI seja executado com sucesso quando o modelo primário (Gemini) falhar, resolvendo o erro "Todos os modelos falharam".*

---

### Fase 1: Diagnóstico e Instrumentação

- [x] **1.1. Analisar Configurações:**
  - [x] Ler o arquivo `app/config.py` para verificar como as variáveis `FALLBACK_AI_MODEL` e `OPENAI_API_KEY` são carregadas no sistema. O problema pode ser uma configuração ausente ou incorreta.

- [ ] **1.2. Adicionar Logging Detalhado:**
  - [ ] Modificar `app/core/model_manager.py` para adicionar logs explícitos que confirmem:
    - Se a inicialização do `fallback_model` (OpenAI) foi bem-sucedida ou falhou durante o startup.
    - O momento exato em que a lógica de `get_response` tenta acionar o `fallback_model` após a falha do primário.
    - A mensagem de erro específica vinda da API da OpenAI, caso a chamada falhe.

---

### Fase 2: Correção

- [x] **2.1. Implementar a Correção:**
  - [x] Com base na análise dos novos logs, aplicar a correção necessária. As possíveis ações são:
    - [ ] **Ação A (Se for configuração):** Garantir que o `fallback_model` seja inicializado corretamente, mesmo que as variáveis de ambiente não estejam presentes, e logar um aviso claro.
    - [x] **Ação B (Se for erro na API):** Ajustar o payload da mensagem para a OpenAI ou corrigir o tratamento de erro no método `OpenAI.achat`.
    - [ ] **Ação C (Se for lógica de controle):** Corrigir o fluxo no método `get_response` para garantir que a chamada ao `_try_model` com o `fallback_model` seja sempre executada após a falha do primário.

---

### Fase 3: Validação e Limpeza

- [ ] **3.1. Validar a Correção:**
  - [ ] Executar um cenário de teste que force a falha do Gemini para confirmar que o fallback para OpenAI agora funciona e retorna uma resposta.
  - [ ] Analisar os logs para verificar se o fluxo de fallback está ocorrendo sem erros.

- [ ] **3.2. Limpeza (Opcional):**
  - [ ] Remover os logs de depuração adicionais após a confirmação de que o problema foi resolvido, ou movê-los para um nível de log `DEBUG`.