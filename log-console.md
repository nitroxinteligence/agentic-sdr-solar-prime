2025-08-25 20:03:39.253 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '[TOOL: calendar.check_availability]...'
2025-08-25 20:03:39.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 20:03:39.255 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-25 20:03:39.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 68 chars
2025-08-25 20:03:39.256 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'legal...' -> '<RESPOSTA_FINAL>[TOOL: calendar.check_availability...'
2025-08-25 20:03:39.256 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>[TOOL: calendar.check_availability]</RESPOSTA_FINAL>...'
2025-08-25 20:03:40.317 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 20:03:40.891 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 20:03:45.534 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.21, 'message_length': 35, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 20:03:49.825 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 35, 'delay_used': 2.01, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:03:49.826 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 20:03:49.826 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'legal...' -> '[TOOL: calendar.check_availability]...'
2025-08-25 20:03:50.724 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55168 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK