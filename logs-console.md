2025-08-23 23:11:40.673 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 35}
2025-08-23 23:11:41.749 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 2d4ddd4a-a718-43af-8e05-4496151458ed, Phone: 558182986181
2025-08-23 23:11:42.431 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-23 23:11:42.431 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-23 23:11:43.243 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 23:11:43.243 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 23:11:43.243 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 23:11:43.253 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 23:11:43.253 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 23:11:43.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 23:11:43.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 23:11:43.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 23:11:43.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 23:11:43.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 23:11:43.255 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 23:11:43.257 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 23:11:43.516 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-23 23:11:44.027 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 23:11:44.595 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 23:11:45.129 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 23:11:45.164 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 23:11:45.165 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 23:11:45.166 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 23, 'lead_name': 'Segunda'}
2025-08-23 23:11:45.166 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-23 23:11:45.166 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): entao agende para o dia 25 as 14h30...
2025-08-23 23:11:45.418 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 24, 'updated_at': '2025-08-23T23:11:45.170231'}}
2025-08-23 23:11:45.418 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181'}}
2025-08-23 23:11:45.418 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181'}}
INFO:     127.0.0.1:42610 - "GET /health HTTP/1.1" 200 OK
2025-08-23 23:11:56.282 | INFO     | app.utils.logger:log_with_emoji:75 | 📅 Verificando disponibilidade interna para 2025-08-25 14:30...
2025-08-23 23:11:56.501 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Service: Conflito de agendamento detectado para o horário 14:30.
2025-08-23 23:11:56.716 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Service: Erro ao verificar disponibilidade: name 'time' is not defined
2025-08-23 23:11:56.718 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Tool executado: calendar.schedule_meeting
2025-08-23 23:12:12.686 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: <RESPOSTA_FINAL>
Poxa, Mateus, fui confirmar o agendamento aqui e esse horário das 14h30 na segunda-...
2025-08-23 23:12:19.181 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.24, 'message_length': 138, 'recipient': '558182986181', 'type': 'typing'}
2025-08-23 23:12:24.607 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 138, 'delay_used': 1.87, 'recipient': '558182986181', 'type': 'text'}
2025-08-23 23:12:24.826 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 23:12:24.826 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:34842 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
INFO:     127.0.0.1:51434 - "GET /health HTTP/1.1" 200 OK
2025-08-23 23:12:25.881 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:34842 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 23:12:34.610 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.76, 'message_length': 157, 'recipient': '558182986181', 'type': 'typing'}
2025-08-23 23:12:41.542 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 157, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-23 23:12:41.551 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 23:12:41.552 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:57892 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 23:12:42.610 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57892 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 23:12:55.793 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:38042 - "GET /health HTTP/1.1" 200 OK
2025-08-23 23:12:59.473 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 23:12:59.473 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:12:59.468Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 23:12:59.489 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-23 23:12:59.489 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-23 23:12:59.490 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-23 23:12:59.490 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'segunda mesmo', 'sender': '558182986181', 'type': 'text'}
2025-08-23 23:12:59.579 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-23 23:12:59.795 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 23:12:59.796 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:12:59.788Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 23:12:59.830 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 23:12:59.830 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:12:59.824Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 23:13:00.927 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 23:13:00.939 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-23 23:13:00.939 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-23 23:13:00.948 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 23:13:00.953 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-23 23:13:00.954 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-23 23:13:03.314 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 23:13:03.315 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:13:03.308Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 23:13:03.330 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-23 23:13:03.331 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-23 23:13:03.331 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-23 23:13:03.331 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'terça estarei ocupado', 'sender': '558182986181', 'type': 'text'}
2025-08-23 23:13:03.634 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 23:13:03.634 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:13:03.627Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 23:13:03.674 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 23:13:03.674 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T20:13:03.668Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40240 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 23:13:14.574 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 2 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 35}
2025-08-23 23:13:15.654 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 2d4ddd4a-a718-43af-8e05-4496151458ed, Phone: 558182986181
2025-08-23 23:13:16.330 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-23 23:13:16.330 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-23 23:13:16.788 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 23:13:16.788 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 23:13:16.789 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 23:13:16.797 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 23:13:16.797 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 23:13:16.797 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 23:13:16.798 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 23:13:16.798 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 23:13:16.798 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 23:13:16.798 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 23:13:16.798 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 23:13:16.801 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 23:13:17.055 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-23 23:13:17.596 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 23:13:18.094 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 23:13:18.598 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 23:13:18.626 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 23:13:18.626 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 23:13:18.627 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 25, 'lead_name': 'Segunda'}
2025-08-23 23:13:18.627 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-23 23:13:18.627 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): segunda mesmo
terça estarei ocupado...
2025-08-23 23:13:19.226 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 26, 'updated_at': '2025-08-23T23:13:18.628349'}}
2025-08-23 23:13:19.226 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181'}}
2025-08-23 23:13:19.226 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181'}}
INFO:     127.0.0.1:49320 - "GET /health HTTP/1.1" 200 OK
2025-08-23 23:13:28.226 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: [TOOL: calendar.check_availability]...