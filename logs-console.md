INFO:     10.11.0.4:47832 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 20:41:17.512 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 20:41:17.513 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:41:17.506Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:47832 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 20:41:17.526 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:47832 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-21 20:41:17.527 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de nova mensagem
2025-08-21 20:41:17.527 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-21 20:41:17.528 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'seria o 3 mesmo', 'sender': '558182986181', 'type': 'text'}
2025-08-21 20:41:17.634 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 20:41:17.634 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:41:17.628Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:47832 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 20:41:17.668 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 20:41:17.669 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T17:41:17.657Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:47832 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 20:41:27.538 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 2 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 46}
2025-08-21 20:41:28.605 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: d5483ddd-8f2c-4898-bade-9261f3fae5cd, Phone: 558182986181
2025-08-21 20:41:29.692 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-21 20:41:29.692 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-21 20:41:30.134 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 20:41:30.135 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 20:41:30.135 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 20:41:30.135 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 20:41:30.135 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 20:41:30.136 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 20:41:30.136 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 20:41:30.137 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 20:41:30.137 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 20:41:30.140 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 20:41:30.433 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 20:41:30.973 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 20:41:31.578 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 20:41:32.072 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 20:41:32.102 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 20:41:32.103 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 20:41:32.104 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 10, 'lead_name': None}
2025-08-21 20:41:32.104 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-21 20:41:32.104 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): compra de energia com desconto
seria o 3 mesmo...
2025-08-21 20:41:32.105 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 📊 Analisando estágio - Msgs: 11 (👤 11 user, 🤖 0 assistant)
2025-08-21 20:41:35.399 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Maravilha, Mateus! Estava conversando agora pouco com vários empresários e observei que grande parte...
2025-08-21 20:41:35.399 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=361, primeiros 200 chars: Maravilha, Mateus! Estava conversando agora pouco com vários empresários e observei que grande parte deles já recebem algum tipo de desconto na conta de luz, devido ao alto valor pago, mas por conta d
2025-08-21 20:41:35.399 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO | Data: {'component': 'extract_final_response'}
2025-08-21 20:41:35.400 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em extract_final_response: 📝 Conteúdo original (primeiros 200 chars): Maravilha, Mateus! Estava conversando agora pouco com vários empresários e observei que grande parte deles já recebem algum tipo de desconto na conta de luz, devido ao alto valor pago, mas por conta d... | Data: {'component': 'extract_final_response'}
2025-08-21 20:41:35.400 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔒 Usando resposta segura para evitar vazamento de raciocínio interno
2025-08-21 20:41:38.178 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 1.81, 'message_length': 45, 'recipient': '558182986181', 'type': 'typing'}
2025-08-21 20:41:41.775 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 45, 'delay_used': 2.55, 'recipient': '558182986181', 'type': 'text'}
INFO:     127.0.0.1:60444 - "GET /health HTTP/1.1" 200 OK
2025-08-21 20:41:42.550 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-21 20:41:42.551 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:386 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:41232 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-21 20:41:42.552 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:47104 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK