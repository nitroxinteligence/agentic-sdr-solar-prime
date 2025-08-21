INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-21 19:51:39.674 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-21 19:51:39.678 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-21 19:51:39.679 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-21 19:51:40.299 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-21 19:51:40.299 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-21 19:51:40.299 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-21 19:51:40.300 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-21 19:51:40.300 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-21 19:51:40.300 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-21 19:51:40.321 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-21 19:51:40.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-21 19:51:40.329 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 19:51:40.329 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 19:51:40.329 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 19:51:40.330 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 19:51:40.330 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 19:51:40.330 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 19:51:40.330 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 19:51:40.330 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 19:51:40.331 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 19:51:40.535 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-21 19:51:40.539 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 19:51:40.809 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 19:51:41.672 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 19:51:41.991 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 19:51:42.320 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 19:51:42.349 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 19:51:42.349 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 19:51:42.350 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-21 19:51:42.350 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-21 19:51:42.350 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 19:51:42.358 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 19:51:42.358 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 19:51:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 19:51:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 19:51:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 19:51:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 19:51:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 19:51:42.360 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 19:51:42.360 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 19:51:42.362 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 19:51:42.629 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 19:51:43.162 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 19:51:43.419 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-21 19:51:43.756 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 19:51:43.775 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 19:51:43.775 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 19:51:43.776 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-21 19:51:43.776 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:36478 - "GET /health HTTP/1.1" 200 OK
2025-08-21 19:51:49.293 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 19:51:49.293 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:51:49.284Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:51460 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 19:51:49.312 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:51460 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-21 19:51:49.313 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de nova mensagem
2025-08-21 19:51:49.313 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-21 19:51:49.314 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-21 19:51:49.414 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 19:51:49.414 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:51:49.407Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:51460 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 19:51:49.451 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 19:51:49.451 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:51:49.444Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:51460 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 19:51:50.819 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51460 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 19:52:04.329 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-21 19:52:05.028 | ERROR    | app.integrations.supabase_client:get_conversation_by_phone:192 | Erro ao buscar conversa por telefone 558182986181: {'message': 'column conversations.qualification_score does not exist', 'code': '42703', 'hint': None, 'details': None}
2025-08-21 19:52:05.632 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 93cc8680-fb35-4f59-90f6-5841976b63a3, Phone: 558182986181
2025-08-21 19:52:06.287 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-21 19:52:06.288 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-21 19:52:06.730 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 19:52:06.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 19:52:06.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 19:52:06.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 19:52:06.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 19:52:06.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 19:52:06.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 19:52:06.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 19:52:06.732 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 19:52:06.735 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 19:52:07.023 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 19:52:07.904 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 19:52:08.425 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 19:52:08.880 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 19:52:08.917 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 19:52:08.917 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 19:52:08.917 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-21 19:52:08.918 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
Unclosed client session
client_session: <aiohttp.client.ClientSession object at 0x7c801bc7ead0>
Unclosed connector
connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7c801bcf84b0>, 2321279.549179313)])']
connector: <aiohttp.connector.TCPConnector object at 0x7c801bc7c550>
Unclosed client session
client_session: <aiohttp.client.ClientSession object at 0x7c801bbbf610>
Unclosed connector
connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7c801bcf8360>, 2321279.586175252)])']
connector: <aiohttp.connector.TCPConnector object at 0x7c801bc430d0>