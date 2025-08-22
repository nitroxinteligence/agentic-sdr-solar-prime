2025-08-22 22:02:05.085 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 22:02:05.654 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 22:02:06.284 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-22 22:02:06.342 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 22:02:06.342 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 22:02:06.343 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-22 22:02:06.343 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-22 22:02:06.343 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-22 22:02:06.352 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 22:02:06.353 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 22:02:06.353 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 22:02:06.353 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 22:02:06.353 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 22:02:06.354 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 22:02:06.354 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 22:02:06.354 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 22:02:06.354 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 22:02:06.355 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 22:02:06.357 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 22:02:06.624 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 22:02:07.240 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 22:02:07.841 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-22 22:02:08.381 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-22 22:02:08.406 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 22:02:08.407 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 22:02:08.408 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
INFO:     Application startup complete.
2025-08-22 22:02:08.408 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:38386 - "GET /health HTTP/1.1" 200 OK
2025-08-22 22:02:26.350 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:54962 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-22 22:02:26.544 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-22 22:02:26.545 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:02:26.539Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:54962 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-22 22:02:26.583 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:54962 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 22:02:26.584 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 22:02:26.584 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 22:02:26.584 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'Agende pra mim uma reuniao para segunda-feira as 10h por favor', 'sender': '558182986181', 'type': 'text'}
2025-08-22 22:02:26.724 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 22:02:26.724 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QE2MqxBG0BGAwCOij21PSvcvBhbA3dV1Zea8adSPB-VQQ&oe=68B615CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:02:26.716Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:54962 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 22:02:26.788 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 22:02:26.788 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QE2MqxBG0BGAwCOij21PSvcvBhbA3dV1Zea8adSPB-VQQ&oe=68B615CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:02:26.779Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:54962 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:43112 - "GET /health HTTP/1.1" 200 OK
2025-08-22 22:02:41.652 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 62}
2025-08-22 22:02:42.322 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 9cb528b7-83eb-4c38-9af2-1925c73bb568, Phone: 558182986181
2025-08-22 22:02:43.371 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 22:02:43.372 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 22:02:44.198 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 22:02:44.198 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 22:02:44.198 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 22:02:44.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 22:02:44.200 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 22:02:44.202 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 22:02:44.537 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 22:02:45.109 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 22:02:45.713 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 22:02:47.560 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-22 22:02:47.595 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 22:02:47.596 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 22:02:47.596 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 63, 'lead_name': 'Mateus'}
2025-08-22 22:02:47.596 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 22:02:47.597 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): Agende pra mim uma reuniao para segunda-feira as 10h por favor...
2025-08-22 22:02:47.836 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 64, 'updated_at': '2025-08-22T22:02:47.599929'}}
2025-08-22 22:02:49.982 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Claro, Mateus! Verificarei a disponibilidade do Leonardo para segunda-feira às 10h e te aviso. 😉

...
2025-08-22 22:02:49.982 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-22 22:02:49.983 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 129 chars
2025-08-22 22:02:53.548 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Erro de status 404 para POST https://evoapi-evolution-api.fzvgou.easypanel.host/chat/updatePresence/SDR%20IA%20SolarPrime: {"status":404,"error":"Not Found","response":{"message":["Cannot POST /chat/updatePresence/SDR%20IA%20SolarPrime"]}}
2025-08-22 22:02:53.549 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Erro ao simular digitação: Client error '404 Not Found' for url 'https://evoapi-evolution-api.fzvgou.easypanel.host/chat/updatePresence/SDR%20IA%20SolarPrime'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
2025-08-22 22:02:56.735 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Reconectando ao Evolution API...
2025-08-22 22:02:58.638 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 96, 'delay_used': 2.45, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 22:02:58.644 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 22:02:58.644 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:44062 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 22:02:59.330 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:44062 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 22:02:59.615 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:44062 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-22 22:03:05.140 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-22 22:03:05.140 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:03:05.128Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:50540 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-22 22:03:05.166 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:50540 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 22:03:05.166 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 22:03:05.167 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 22:03:05.167 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'AGENDE UMA REUNIAO PARA AS 10H SEGUNDA-FEIRA', 'sender': '558182986181', 'type': 'text'}
2025-08-22 22:03:05.312 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 22:03:05.312 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QE2MqxBG0BGAwCOij21PSvcvBhbA3dV1Zea8adSPB-VQQ&oe=68B615CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:03:05.305Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:50540 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 22:03:05.362 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 22:03:05.362 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QE2MqxBG0BGAwCOij21PSvcvBhbA3dV1Zea8adSPB-VQQ&oe=68B615CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T19:03:05.354Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:50540 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 22:03:06.744 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:50540 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 22:03:06.745 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 22:03:06.746 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:50556 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:49028 - "GET /health HTTP/1.1" 200 OK
INFO:     172.233.20.117:59058 - "GET / HTTP/1.0" 200 OK
WARNING:  Invalid HTTP request received.
INFO:     172.233.20.117:59070 - "GET /nice%20ports%2C/Trinity.txt.bak HTTP/1.0" 404 Not Found
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
INFO:     172.233.20.117:59090 - "OPTIONS / HTTP/1.0" 405 Method Not Allowed
INFO:     172.233.20.117:59092 - "OPTIONS / HTTP/1.0" 405 Method Not Allowed
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
WARNING:  Invalid HTTP request received.
INFO:     172.233.20.117:59194 - "GET / HTTP/1.1" 200 OK
INFO:     172.233.20.117:59220 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     172.233.20.117:59246 - "GET / HTTP/1.1" 200 OK
INFO:     172.233.20.117:59252 - "GET /webui HTTP/1.1" 404 Not Found
INFO:     172.233.20.117:59262 - "GET / HTTP/1.1" 200 OK
INFO:     172.233.20.117:59270 - "GET /owa/ HTTP/1.1" 404 Not Found
INFO:     172.233.20.117:59278 - "GET /owa/ HTTP/1.1" 404 Not Found
2025-08-22 22:03:20.482 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 44}
2025-08-22 22:03:22.637 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 9cb528b7-83eb-4c38-9af2-1925c73bb568, Phone: 558182986181
2025-08-22 22:03:23.701 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 22:03:23.701 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 22:03:25.284 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 22:03:25.284 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 22:03:25.285 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 22:03:25.285 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 22:03:25.285 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 22:03:25.286 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 22:03:25.286 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 22:03:25.286 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 22:03:25.286 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 22:03:25.286 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 22:03:25.290 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 22:03:25.559 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 22:03:26.142 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 22:03:26.735 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
WARNING:  Invalid HTTP request received.
2025-08-22 22:03:27.262 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-22 22:03:27.293 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 22:03:27.294 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 22:03:27.294 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 65, 'lead_name': 'Mateus'}
2025-08-22 22:03:27.295 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 22:03:27.295 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): AGENDE UMA REUNIAO PARA AS 10H SEGUNDA-FEIRA...
2025-08-22 22:03:27.521 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 66, 'updated_at': '2025-08-22T22:03:27.297922'}}
2025-08-22 22:03:30.312 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Claro, Mateus! Verificarei a disponibilidade do Leonardo para segunda-feira às 10h e te aviso. 😉

...
2025-08-22 22:03:30.312 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-22 22:03:30.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 129 chars
2025-08-22 22:03:33.577 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Erro de status 404 para POST https://evoapi-evolution-api.fzvgou.easypanel.host/chat/updatePresence/SDR%20IA%20SolarPrime: {"status":404,"error":"Not Found","response":{"message":["Cannot POST /chat/updatePresence/SDR%20IA%20SolarPrime"]}}
2025-08-22 22:03:33.577 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Erro ao simular digitação: Client error '404 Not Found' for url 'https://evoapi-evolution-api.fzvgou.easypanel.host/chat/updatePresence/SDR%20IA%20SolarPrime'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404
2025-08-22 22:03:36.309 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Reconectando ao Evolution API...
INFO:     172.233.20.117:44814 - "GET / HTTP/1.1" 200 OK
2025-08-22 22:03:38.213 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 96, 'delay_used': 2.35, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 22:03:38.428 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 22:03:38.429 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:43246 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 22:03:38.886 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:43246 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:60950 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46322 - "GET /health HTTP/1.1" 200 OK