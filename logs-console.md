2025-08-21 20:14:39.683 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 20:14:40.217 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 20:14:40.260 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 20:14:40.261 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 20:14:40.261 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-21 20:14:40.261 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-21 20:14:40.261 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 20:14:40.268 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 20:14:40.268 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 20:14:40.268 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 20:14:40.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 20:14:40.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 20:14:40.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 20:14:40.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 20:14:40.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 20:14:40.270 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 20:14:40.272 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 20:14:40.511 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 20:14:41.099 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 20:14:41.653 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-21 20:14:42.755 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 20:14:42.777 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 20:14:42.778 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 20:14:42.778 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-21 20:14:42.778 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:35062 - "GET /health HTTP/1.1" 200 OK
2025-08-21 20:14:44.147 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 20:14:46.349 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 20:14:46.349 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:14:46.333Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 20:14:46.359 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 20:14:46.359 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:14:46.354Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 20:14:46.374 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-21 20:14:46.375 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de nova mensagem
2025-08-21 20:14:46.375 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-21 20:14:46.375 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-21 20:14:46.463 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 20:14:46.463 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:14:46.455Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 20:14:46.517 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 20:14:46.517 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:14:46.511Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 20:14:47.228 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 20:14:48.789 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-21 20:14:48.793 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-21 20:14:48.793 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:386 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:43788 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     10.11.0.4:41898 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
2025-08-21 20:15:01.747 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-21 20:15:02.461 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: d5483ddd-8f2c-4898-bade-9261f3fae5cd, Phone: 558182986181
2025-08-21 20:15:03.537 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-21 20:15:03.538 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-21 20:15:04.342 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 20:15:04.343 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 20:15:04.343 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 20:15:04.343 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 20:15:04.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 20:15:04.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 20:15:04.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 20:15:04.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 20:15:04.344 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 20:15:04.347 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 20:15:04.617 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
INFO:     10.11.0.4:41898 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
2025-08-21 20:15:05.276 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 20:15:06.027 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 20:15:06.865 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 20:15:06.893 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 20:15:06.894 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 20:15:06.895 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 4, 'lead_name': None}
2025-08-21 20:15:06.895 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-21 20:15:06.895 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): oi...
2025-08-21 20:15:06.896 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 📊 Analisando estágio - Msgs: 5 (👤 5 user, 🤖 0 assistant)
2025-08-21 20:15:06.897 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi...'
2025-08-21 20:15:06.901 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi...'
2025-08-21 20:15:06.901 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=2): 'oi...'
2025-08-21 20:15:06.901 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=3): 'oi...'
2025-08-21 20:15:06.901 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🔍 Analisando msg do usuário (idx=4): 'oi...'
2025-08-21 20:15:06.902 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Erro: argument of type 'NoneType' is not iterable | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 20:15:06.903 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Traceback: Traceback (most recent call last):
  File "/app/app/agents/agentic_sdr_stateless.py", line 138, in process_message
    new_lead_info = self.lead_manager.extract_lead_info(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/core/lead_manager.py", line 159, in extract_lead_info
    self.calculate_qualification_score(lead_info)
  File "/app/app/core/lead_manager.py", line 194, in calculate_qualification_score
    if "comercial" in property_type or "empresa" in property_type:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: argument of type 'NoneType' is not iterable
 | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 20:15:06.903 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=69, primeiros 200 chars: Desculpe, tive um problema ao processar sua mensagem. Pode repetir? 🤔
2025-08-21 20:15:06.904 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO | Data: {'component': 'extract_final_response'}
2025-08-21 20:15:06.904 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 📝 Conteúdo original (primeiros 200 chars): Desculpe, tive um problema ao processar sua mensagem. Pode repetir? 🤔... | Data: {'component': 'extract_final_response'}
2025-08-21 20:15:06.904 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔒 Usando resposta segura para evitar vazamento de raciocínio interno
INFO:     10.11.0.4:41898 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
2025-08-21 20:15:09.500 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.24, 'message_length': 45, 'recipient': '558182986181', 'type': 'typing'}
INFO:     10.11.0.4:41898 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:41898 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
2025-08-21 20:15:13.554 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 45, 'delay_used': 2.12, 'recipient': '558182986181', 'type': 'text'}
2025-08-21 20:15:13.560 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-21 20:15:13.560 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:386 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:41898 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
INFO:     127.0.0.1:60880 - "GET /health HTTP/1.1" 200 OK
2025-08-21 20:15:14.183 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41898 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK