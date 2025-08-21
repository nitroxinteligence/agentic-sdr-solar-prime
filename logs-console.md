2025-08-21 20:27:38.541 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-21 20:27:38.542 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): oi...
2025-08-21 20:27:38.543 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 📊 Analisando estágio - Msgs: 6 (👤 6 user, 🤖 0 assistant)
2025-08-21 20:27:38.544 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi...'
2025-08-21 20:27:38.547 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi...'
2025-08-21 20:27:38.548 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=2): 'oi...'
2025-08-21 20:27:38.548 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=3): 'oi...'
2025-08-21 20:27:38.548 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=4): 'oi...'
2025-08-21 20:27:38.548 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=5): 'oi...'
2025-08-21 20:27:38.550 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Erro: '(' was never closed (prompt_builder.py, line 47) | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 20:27:38.551 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Traceback: Traceback (most recent call last):
  File "/app/app/agents/agentic_sdr_stateless.py", line 148, in process_message
    response = await self._generate_response(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/agents/agentic_sdr_stateless.py", line 497, in _generate_response
    from app.prompts.prompt_builder import PromptBuilder
  File "/app/app/prompts/prompt_builder.py", line 47
    prompt = (
             ^
SyntaxError: '(' was never closed
 | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 20:27:38.551 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=69, primeiros 200 chars: Desculpe, tive um problema ao processar sua mensagem. Pode repetir? 🤔
2025-08-21 20:27:38.552 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO | Data: {'component': 'extract_final_response'}
2025-08-21 20:27:38.552 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 📝 Conteúdo original (primeiros 200 chars): Desculpe, tive um problema ao processar sua mensagem. Pode repetir? 🤔... | Data: {'component': 'extract_final_response'}
2025-08-21 20:27:38.552 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔒 Usando resposta segura para evitar vazamento de raciocínio interno
2025-08-21 20:27:41.761 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 1.72, 'message_length': 45, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:51012 - "GET /health HTTP/1.1" 200 OK
2025-08-21 20:27:45.273 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 45, 'delay_used': 2.97, 'recipient': '558182986181', 'type': 'text'}
2025-08-21 20:27:45.282 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-21 20:27:45.283 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:386 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:39962 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-21 20:27:45.901 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39962 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK