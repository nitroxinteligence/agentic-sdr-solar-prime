# TODO - Correção Definitiva do Fluxo Multimodal (Análise de Causa Raiz)

- [x] **Análise Forense:**
  - [x] Identificada a causa raiz: A ordem das operações em `process_message` estava incorreta. `LeadManager` e `ContextAnalyzer` eram executados com estado desatualizado, antes do processamento de mídia.

- [x] **Refatorar a Ordem de Operações em `agentic_sdr_stateless.py`:**
  - [x] Mover o bloco de processamento de mídia (`if media_data: ...`) para o **início** do método `process_message`.
  - [x] Garantir que o `lead_info` seja atualizado com o `extracted_bill_value` **antes** de qualquer outra análise.
  - [x] Unificar a mensagem do usuário com o `media_context` **antes** de adicioná-la ao histórico.
  - [x] Executar `lead_manager.extract_lead_info` e `context_analyzer.analyze_context` **APÓS** o processamento de mídia e a atualização do histórico.

- [x] **Simplificar `prompt_builder.py`:**
  - [x] Confirmado que o parâmetro `media_context` foi removido da função `build_user_prompt` e que a lógica depende apenas do `conversation_history`.

- [ ] **Publicação:**
  - [ ] Adicionar o arquivo modificado ao git.
  - [ ] Criar um commit claro e descritivo que explique a correção da ordem de operações.
  - [ ] Enviar as alterações para o repositório remoto.

- [ ] **Validação Final:**
  - [ ] Testar o fluxo com uma imagem de conta de luz para confirmar que o agente reconhece o valor e prossegue para a próxima pergunta de qualificação.