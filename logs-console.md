✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-15 18:21:27.428 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-15 18:21:27.434 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-15 18:21:27.435 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-15 18:21:28.094 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-15 18:21:28.095 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=10.0s, max=10)
2025-08-15 18:21:28.095 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '10.0s'}
2025-08-15 18:21:28.095 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-15 18:21:28.095 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-15 18:21:28.096 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-15 18:21:28.103 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-15 18:21:28.309 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-15 18:21:28.314 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-15 18:21:28.322 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ ⚠️ FollowUp Executor não iniciado: cannot import name 'start_followup_executor' from 'app.services.followup_executor_service' (/app/app/services/followup_executor_service.py)
2025-08-15 18:21:28.322 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless) - tentativa 1/3...
2025-08-15 18:21:28.322 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-15 18:21:28.331 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-15 18:21:28.331 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-15 18:21:28.331 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-15 18:21:28.331 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-15 18:21:28.332 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-15 18:21:28.332 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-15 18:21:28.332 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-15 18:21:28.333 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-15 18:21:28.336 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-15 18:21:28.343 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-15 18:21:28.343 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-15 18:21:28.344 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-15 18:21:28.344 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-15 18:21:28.344 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-15 18:21:28.344 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-15 18:21:28.345 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-15 18:21:28.345 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-15 18:21:28.349 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-15 18:21:28.666 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Conectado como: leonardofvieira00@gmail.com
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:53428 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:21:53.596 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51562 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.598 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51518 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.599 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51550 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.600 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51544 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.601 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51502 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.601 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51528 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.602 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51504 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.603 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51546 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.603 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51490 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.604 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51566 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.605 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51562 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.606 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51578 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.607 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51582 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.608 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51596 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.609 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51602 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.610 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51616 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.611 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51626 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.612 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51636 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.613 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51646 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.613 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51660 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.614 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51674 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.705 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51674 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.712 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51674 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.713 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51660 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.714 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51674 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.714 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51636 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.715 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51646 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.716 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51626 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.723 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51626 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:21:53.725 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51636 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
INFO:     127.0.0.1:41510 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:22:20.736 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:20.748 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:20.881 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:20.891 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.025 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.034 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.169 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.186 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.260 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.263 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.267 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33452 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.268 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33466 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.269 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33442 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.270 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33430 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.273 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33394 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.274 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33410 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.277 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33396 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.278 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33418 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.278 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:51680 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:21.279 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:33414 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:29.292 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-15 18:22:30.353 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:22:30.353 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:22:30.331Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:22:30.368 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:22:30.368 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:22:30.349Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:22:30.391 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-15 18:22:30.392 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi boa tarde', 'sender': '558182986181', 'type': 'text'}
2025-08-15 18:22:30.672 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:22:30.672 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:22:30.665Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-15 18:22:30.730 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:22:30.730 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:22:30.722Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33482 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:22:40.739 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 12}
2025-08-15 18:22:42.450 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 355d0a84-835b-4e6b-9d22-36d3338993bb, Phone: 558182986181
2025-08-15 18:22:43.952 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-15 18:22:43.952 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-15 18:22:43.953 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-15 18:22:43.953 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-15 18:22:43.954 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-15 18:22:43.954 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-15 18:22:43.954 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-15 18:22:43.954 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-15 18:22:43.955 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-15 18:22:43.955 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-15 18:22:43.963 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-15 18:22:43.964 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-15 18:22:43.964 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-15 18:22:43.964 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-15 18:22:43.964 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-15 18:22:43.965 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-15 18:22:43.965 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-15 18:22:43.965 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=355d0a84-835b-4e6b-9d22-36d3338993bb para phone=558182986181
2025-08-15 18:22:43.965 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: 355d0a84-835b-4e6b-9d22-36d3338993bb
2025-08-15 18:22:44.593 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): oi boa tarde...
2025-08-15 18:22:46.412 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-15 18:22:46.413 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 2 (👤 2 user, 🤖 0 assistant)
2025-08-15 18:22:46.413 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi boa tarde...'
2025-08-15 18:22:46.417 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi boa tarde...'
2025-08-15 18:22:46.417 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-15 18:22:46.418 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-15 18:22:46.418 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-15 18:22:47.506 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-15T18:22:47.269702'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': None, 'bill_value': None, 'interested': True}
2025-08-15 18:22:48.091 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-15 18:22:48.446 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-15 18:22:48.730 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-15 18:22:49.118 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 6372980
2025-08-15 18:22:49.481 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:45780 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:22:49.493 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 6372980
2025-08-15 18:22:49.493 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-15 18:22:49.493 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-15 18:22:49.496 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '0.500', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-15 18:22:49.496 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '0.500', 'threshold': '0.350', 'reason': 'threshold_dinamico'}
2025-08-15 18:22:50.025 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado: leonardofvieira00@gmail.com
2025-08-15 18:22:50.254 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ calendar executado com sucesso | Data: {'result': 'Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?'}
2025-08-15 18:22:50.255 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-15 18:22:50.256 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-15 18:22:50.256 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-15 18:22:50.686 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-15 18:22:50.686 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-15 18:22:50.915 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-15 18:22:55.691 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-15 18:22:55.692 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento...
2025-08-15 18:22:55.692 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=845, primeiros 200 chars: Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?

**[Raciocínio interno e análise]**

VALIDAÇÃO PRÉ-RESP
2025-08-15 18:22:55.694 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=845, primeiros 200 chars: Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?

**[Raciocínio interno e análise]**

VALIDAÇÃO PRÉ-RESP
2025-08-15 18:22:55.695 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-15 18:22:55.695 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 144 chars
2025-08-15 18:23:00.995 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.4, 'message_length': 144, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:55426 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:23:06.846 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 144, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-15 18:23:06.846 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Olá! Tudo bem? Me chamo Helen Vieira, sou consulto', 'recipient': '558182986181', 'type': 'text'}
2025-08-15 18:23:06.847 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB07EA71CC015CDA754985D99AD948C63B3472F
2025-08-15 18:23:08.315 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-15 18:23:08.316 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:52236 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-15 18:23:08.316 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:23:09.144 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 15:53
2025-08-15 18:23:09.145 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-15 18:23:12.073 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:23:12.081 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-15 18:23:12.081 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-15 18:23:13.390 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-15 18:23:14.217 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:23:14.218 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:23:14.212Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:23:14.242 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-15 18:23:14.244 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-15 18:23:14.249 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:23:14.249 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:23:14.241Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:23:14.544 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:23:14.544 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:23:14.537Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-15 18:23:14.598 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:23:14.598 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:23:14.590Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52250 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-15 18:23:24.249 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 6}
2025-08-15 18:23:24.709 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 355d0a84-835b-4e6b-9d22-36d3338993bb, Phone: 558182986181
2025-08-15 18:23:25.846 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-15 18:23:25.846 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-15 18:23:25.847 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-15 18:23:25.847 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-15 18:23:25.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-15 18:23:25.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-15 18:23:25.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-15 18:23:25.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-15 18:23:25.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-15 18:23:25.849 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-15 18:23:25.856 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-15 18:23:25.857 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-15 18:23:25.857 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-15 18:23:25.857 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-15 18:23:25.858 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-15 18:23:25.858 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-15 18:23:25.858 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 5, 'lead_name': None}
2025-08-15 18:23:25.858 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=355d0a84-835b-4e6b-9d22-36d3338993bb para phone=558182986181
2025-08-15 18:23:25.859 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: 355d0a84-835b-4e6b-9d22-36d3338993bb
2025-08-15 18:23:26.657 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-15 18:23:26.975 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-15 18:23:27.215 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-15 18:23:27.521 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-15 18:23:27.521 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): mateus...
2025-08-15 18:23:28.187 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-15 18:23:28.187 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 6 (👤 4 user, 🤖 2 assistant)
2025-08-15 18:23:28.188 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi boa tarde...'
2025-08-15 18:23:28.188 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi boa tarde...'
2025-08-15 18:23:28.189 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-15 18:23:28.189 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'olá! tudo bem? me chamo helen vieira, sou consulto...'
2025-08-15 18:23:28.189 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-15 18:23:28.189 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-15 18:23:28.189 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-15 18:23:28.190 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 NOME DETECTADO: Mateus
2025-08-15 18:23:28.190 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: name | Data: {'old': None, 'new': 'Mateus'}
2025-08-15 18:23:28.190 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 10.0}
2025-08-15 18:23:28.190 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['name', 'qualification_score']}
2025-08-15 18:23:28.190 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-15 18:23:29.023 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-15T18:23:28.795436'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': None, 'bill_value': None, 'interested': True}
2025-08-15 18:23:29.590 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst allowance para kommo
2025-08-15 18:23:29.856 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst allowance para kommo
2025-08-15 18:23:30.242 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
🚫 Rate Limiter: Bloqueando kommo. Aguarde 5.8s
⏳ Rate Limiter: Aguardando 6.8s para kommo...
INFO:     127.0.0.1:48040 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:23:38.233 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 6372980
2025-08-15 18:23:38.556 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 6372980
2025-08-15 18:23:38.557 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-15 18:23:38.557 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-15 18:23:38.558 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '0.000', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-15 18:23:38.558 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-15 18:23:38.558 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-15 18:23:39.363 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-15 18:23:39.364 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-15 18:23:39.369 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:39.470 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-15 18:23:42.180 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.325 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.469 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.607 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.614 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53926 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.615 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:60066 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.616 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53924 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.617 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53940 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.618 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53938 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.619 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53950 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.620 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53960 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.620 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53962 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.621 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53968 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.622 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53966 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.622 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:53986 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.624 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54002 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.625 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54004 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.626 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54030 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.626 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54028 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.627 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.628 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.629 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.630 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.631 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.757 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.758 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.759 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.760 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.761 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.762 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.763 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.764 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.764 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.765 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.766 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.767 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.768 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.769 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.770 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.771 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.772 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.773 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.977 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:42.989 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.122 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.133 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.267 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.274 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.275 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.276 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.277 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.278 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.278 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.280 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.283 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.284 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.285 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54050 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.286 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.287 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.288 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.294 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.296 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.297 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54060 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.298 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54046 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.298 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.308 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.309 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.411 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.419 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.420 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.422 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54038 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:43.424 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:54074 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-15 18:23:47.772 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-15 18:23:47.773 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: Raciocínio interno e análise:
1. Qual estágio estou? (1)
2. Completei pré-requisitos do estágio atua...
2025-08-15 18:23:47.773 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=900, primeiros 200 chars: Raciocínio interno e análise:
1. Qual estágio estou? (1)
2. Completei pré-requisitos do estágio atual? (Não, preciso apresentar as 4 soluções)
3. Estou seguindo template obrigatório? (Sim)
4. Vou form
2025-08-15 18:23:47.774 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=900, primeiros 200 chars: Raciocínio interno e análise:
1. Qual estágio estou? (1)
2. Completei pré-requisitos do estágio atual? (Não, preciso apresentar as 4 soluções)
3. Estou seguindo template obrigatório? (Sim)
4. Vou form
2025-08-15 18:23:47.774 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Perfeito, Mateus! Hoje na Solarprime nós temos quatro modelos de soluções energéticas: 1) Instalação de usina própria - você fica dono da usina ao final 2) Aluguel de lote para instalação de usina própria - sua usina em nosso terreno 3) Compra de energia com desconto - economia imediata de 20% 4) Usina de investimento - renda passiva com energia solar Qual desses modelos seria do seu interesse?
2025-08-15 18:23:47.775 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 397 chars
2025-08-15 18:23:47.775 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📱 Mensagem das 4 soluções formatada com quebras de linha | Data: {'original_length': 397, 'formatted_length': 400}
2025-08-15 18:23:47.775 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem dividida em 1 partes | Data: {'phone': '558182986181', 'original_length': 397}
2025-08-15 18:23:52.793 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 7.33, 'message_length': 400, 'recipient': '558182986181', 'type': 'typing'}
2025-08-15 18:24:02.317 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 400, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-15 18:24:02.317 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Perfeito, Mateus! Hoje na Solarprime nós temos qua', 'recipient': '558182986181', 'type': 'text'}
2025-08-15 18:24:02.318 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 1/1 enviado. ID: 3EB0BB158C10E395727D3FA5E7479923271361DF
2025-08-15 18:24:04.237 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-15 18:24:04.238 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:54000 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-15 18:24:04.239 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:36540 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:24:05.056 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 15:54
2025-08-15 18:24:05.056 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
INFO:     127.0.0.1:37208 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:24:08.278 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
2025-08-15 18:56:30.635 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56172 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:56:30.637 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-15 18:56:30.638 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56168 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-15 18:56:30.639 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56186 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:56:30.640 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-15 18:56:30.640 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56196 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-15 18:56:30.641 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56204 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:56:30.642 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56214 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-15 18:56:30.643 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-15 18:56:30.643 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56230 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-15 18:56:30.644 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-15 18:56:30.645 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56238 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:33810 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:56:53.495 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:56:53.496 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '120363416504607484@newsletter', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:56:53.479Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:45190 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:56:53.496 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-delete de evolution-api | Data: {'event': 'CHATS_DELETE', 'endpoint': '/whatsapp/chats-delete', 'source': 'evolution-api'}
2025-08-15 18:56:53.497 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_DELETE
INFO:     10.11.0.4:45196 - "POST /webhook/whatsapp/chats-delete HTTP/1.1" 200 OK
INFO:     127.0.0.1:39584 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:57:25.378 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ Follow-up agendado no banco: IMMEDIATE_REENGAGEMENT para 55818298...
2025-08-15 18:57:25.379 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up 30min agendado: 55818298...