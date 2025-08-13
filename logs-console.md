✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-13 15:54:30.825 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.2
2025-08-13 15:54:30.829 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-13 15:54:30.829 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-13 15:54:31.646 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-13 15:54:31.647 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=30.0s, max=10)
2025-08-13 15:54:31.647 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '30.0s'}
2025-08-13 15:54:31.647 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-13 15:54:31.647 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-13 15:54:31.647 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-13 15:54:31.648 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto | Data: {'check_interval': '1min', 'types': '30min, 24h'}
2025-08-13 15:54:31.648 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (tentativa 1/3)...
2025-08-13 15:54:31.648 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏗️ Criando instância singleton do AgenticSDR...
2025-08-13 15:54:31.655 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Modular...
2025-08-13 15:54:31.656 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-13 15:54:31.656 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-13 15:54:31.656 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-13 15:54:31.656 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-13 15:54:31.656 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-13 15:54:31.657 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-13 15:54:31.657 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-13 15:54:31.658 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-13 15:54:31.670 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-13 15:54:31.670 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-13 15:54:31.671 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-13 15:54:31.671 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-13 15:54:31.671 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Modular inicializado com sucesso! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-13 15:54:31.671 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Singleton AgenticSDR criado e inicializado pronto
2025-08-13 15:54:31.672 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 15:54:31.672 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR pronto | Data: {'status': 'pré-aquecido com sucesso'}
2025-08-13 15:54:31.672 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-13 15:54:31.672 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ✅ FollowUp Executor inicializado
2025-08-13 15:54:31.672 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 🔄 Iniciando FollowUp Executor
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:56870 - "GET /health HTTP/1.1" 200 OK
2025-08-13 15:54:38.641 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60402 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 15:54:43.946 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 15:54:46.777 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 15:54:46.777 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T12:54:46.758Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 15:54:46.792 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 15:54:46.792 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T12:54:46.771Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 15:54:46.818 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 15:54:46.820 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-13 15:54:46.954 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 15:54:46.955 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QG2ppDtGZ3w_pO4Cq0gtN6rcsazIDdzH5cJPMzXMkX38w&oe=68A9C7CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T12:54:46.947Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 15:54:47.020 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 15:54:47.020 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QG2ppDtGZ3w_pO4Cq0gtN6rcsazIDdzH5cJPMzXMkX38w&oe=68A9C7CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T12:54:47.010Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 15:54:48.638 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 15:54:48.647 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-13 15:54:48.647 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:53120 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:33864 - "GET /health HTTP/1.1" 200 OK
2025-08-13 15:55:16.836 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-13 15:55:17.662 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 15:55:17.662 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: b9c709f4-4f2e-4883-a919-cff1d3f83225, Phone: 558182986181
2025-08-13 15:55:19.094 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=b9c709f4-4f2e-4883-a919-cff1d3f83225 para phone=558182986181
2025-08-13 15:55:19.094 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: b9c709f4-4f2e-4883-a919-cff1d3f83225
2025-08-13 15:55:19.312 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: oi...
2025-08-13 15:55:19.318 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 15:55:19.318 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 15:55:19.318 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 15:55:19.900 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: Erro ao sincronizar com CRM: 'CRMServiceReal' object has no attribute 'sync_new_leads'
2025-08-13 15:55:19.901 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Service: Sync parcial: None
2025-08-13 15:55:24.177 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: [Raciocínio interno: Ok, preciso iniciar a conversa de forma acolhedora e me apresentar como Helen d...
2025-08-13 15:55:24.177 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=462, primeiros 200 chars: [Raciocínio interno: Ok, preciso iniciar a conversa de forma acolhedora e me apresentar como Helen da SolarPrime, buscando entender a situação do cliente com a conta de luz para, quem sabe, já qualifi
2025-08-13 15:55:24.179 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=462, primeiros 200 chars: [Raciocínio interno: Ok, preciso iniciar a conversa de forma acolhedora e me apresentar como Helen da SolarPrime, buscando entender a situação do cliente com a conta de luz para, quem sabe, já qualifi
2025-08-13 15:55:24.179 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Olá! Tudo bem? Sou a Helen, consultora de energia solar da SolarPrime. Que bom que você entrou em contato! Como posso te ajudar hoje? Conta pra mim, como está sua relação com a conta de luz atualmente?
2025-08-13 15:55:24.179 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 201 chars
2025-08-13 15:55:24.189 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem dividida em 2 partes | Data: {'phone': '558182986181', 'original_length': 201}
2025-08-13 15:55:29.430 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.04, 'message_length': 133, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 15:55:34.822 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 133, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 15:55:34.822 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Olá! Tudo bem? Sou a Helen, consultora de energia ', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 15:55:34.822 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 1/2 enviado. ID: 3EB02982602A9F8F18BB2FD450A6D60A855280C2
2025-08-13 15:55:34.829 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 15:55:34.829 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:59940 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 15:55:35.481 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59940 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:37774 - "GET /health HTTP/1.1" 200 OK
2025-08-13 15:55:40.630 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.74, 'message_length': 67, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 15:55:45.260 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 67, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 15:55:45.260 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Conta pra mim, como está sua relação com a conta d', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 15:55:45.260 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 2/2 enviado. ID: 3EB0191175ADF2C09FF122D671F72C34ABB9DF01
2025-08-13 15:55:46.711 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 15:55:46.712 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:40092 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 15:55:46.712 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40106 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 15:55:47.188 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 13:25
2025-08-13 15:55:47.189 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
INFO:     127.0.0.1:43254 - "GET /health HTTP/1.1" 200 OK
2025-08-13 15:56:17.420 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:34730 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 15:56:17.421 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:34736 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 15:56:17.424 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:34736 - "POST /webhook/kommo/events HTTP/1.1" 200 OK