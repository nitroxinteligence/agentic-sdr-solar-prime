✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-08-24 01:39:22.738 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-24 01:39:23.454 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-24 01:39:23.458 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-24 01:39:23.458 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-24 01:39:24.137 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-24 01:39:24.138 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-24 01:39:24.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-24 01:39:24.138 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-24 01:39:24.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-24 01:39:24.139 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-24 01:39:24.158 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-24 01:39:24.166 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:39:24.166 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-24 01:39:24.167 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:39:24.167 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:39:24.175 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:39:24.175 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:39:24.175 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:39:24.176 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:39:24.176 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:39:24.176 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:39:24.176 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:39:24.177 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:39:24.387 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-24 01:39:24.390 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:39:25.023 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:39:26.192 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:39:26.745 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-24 01:39:27.275 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-24 01:39:27.338 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:39:27.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:39:27.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-24 01:39:27.340 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-24 01:39:27.340 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-24 01:39:27.349 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:39:27.349 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:39:27.350 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:39:27.360 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:39:27.360 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:39:27.360 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:39:27.361 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:39:27.361 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:39:27.361 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:39:27.362 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:39:27.362 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:39:27.364 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:39:27.958 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:39:28.478 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:39:28.987 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-24 01:39:29.506 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
INFO:     Application startup complete.
2025-08-24 01:39:29.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:39:29.530 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:39:29.530 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-24 01:39:29.531 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:54336 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:50772 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-24 01:39:51.376 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:39:51.715 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:39:51.716 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:51.711Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:39:51.737 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:39:51.737 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:51.732Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:39:51.769 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:39:51.770 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:39:51.770 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:39:51.770 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:39:51.772 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-24 01:39:52.423 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:39:52.653 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 24b56566-a232-447a-bf29-57282be23e33, Phone: 558182986181
2025-08-24 01:39:52.654 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:52.654 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:52.058Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35626 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.307 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.308 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:52.606Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35618 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.308 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.309 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:52.100Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35628 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.309 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.310 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:53.020Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35626 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.310 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.310 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:52.288Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40104 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.311 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:40112 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:39:53.312 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:39:53.312 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:39:53.312 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'boa', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:39:53.314 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40116 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.315 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.315 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:52.646Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40120 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.316 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-24 01:39:53.316 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-24 01:39:53.753 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:39:53.753 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:39:53.753 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:39:53.762 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:39:53.762 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:39:53.762 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:39:53.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:39:53.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:39:53.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:39:53.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:39:53.763 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:39:53.766 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:39:53.767 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:40124 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:39:53.767 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:39:53.768 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:39:53.768 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'noite', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:39:53.769 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.770 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:53.339Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40120 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:53.770 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:39:53.770 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:39:53.365Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40116 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:39:54.019 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:39:54.138 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40116 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-24 01:39:54.146 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-24 01:39:54.146 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:40116 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-24 01:39:54.541 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:39:55.142 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-24 01:39:56.259 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-24 01:39:56.285 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:39:56.287 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:39:56.287 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Não identificado'}
2025-08-24 01:39:56.287 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-24 01:39:56.287 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): oi...
INFO:     127.0.0.1:43964 - "GET /health HTTP/1.1" 200 OK
2025-08-24 01:40:04.741 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: <RESPOSTA_FINAL>Boa noite!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o se...
2025-08-24 01:40:08.844 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56588 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:40:13.893 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.03, 'message_length': 141, 'recipient': '558182986181', 'type': 'typing'}
2025-08-24 01:40:14.296 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:40:19.099 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 141, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-24 01:40:19.101 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-24 01:40:19.102 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-24 01:40:20.103 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-24 01:40:21.556 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:40:21.557 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:40:21.552Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:40:21.572 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:40:21.572 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:40:21.572 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:40:21.572 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'me chamo mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:40:21.573 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 15}
2025-08-24 01:40:22.008 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:40:22.009 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:40:21.874Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:32842 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:40:22.224 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 00acd82a-8253-4ad2-ac10-ee0d2d948ad4, Phone: 558182986181
2025-08-24 01:40:22.225 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:40:22.225 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:40:21.900Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:32852 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:40:22.888 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-24 01:40:22.889 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-24 01:40:23.361 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:40:23.361 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:40:23.361 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:40:23.371 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:40:23.371 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:40:23.371 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:40:23.372 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:40:23.372 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:40:23.372 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:40:23.372 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:40:23.373 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:40:23.375 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:40:23.613 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:40:23.737 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:32852 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-24 01:40:23.743 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-24 01:40:23.743 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:32852 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-24 01:40:24.185 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:40:24.870 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-24 01:40:25.401 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-24 01:40:25.424 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:40:25.425 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:40:25.426 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Não identificado'}
2025-08-24 01:40:25.426 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-24 01:40:25.426 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): me chamo mateus...
2025-08-24 01:40:25.428 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Iniciando criação de novo lead para 558182986181 com nome 'Mateus'.
2025-08-24 01:40:26.090 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'name': 'Mateus', 'lead_id': 'b81b1079-2916-461b-ad4c-b9a2f29f1a96', 'table': 'leads', 'count': 1}
2025-08-24 01:40:26.090 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando criar lead no Kommo para o lead_id b81b1079-2916-461b-ad4c-b9a2f29f1a96.
INFO:     10.11.0.4:32852 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-24 01:40:27.500 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181'}}
2025-08-24 01:40:27.500 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181'}}
INFO:     127.0.0.1:39440 - "GET /health HTTP/1.1" 200 OK
2025-08-24 01:40:31.224 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: <RESPOSTA_FINAL>Perfeito, Mateus! Para eu entender qual a melhor solução para você, me diz por favor...
2025-08-24 01:40:42.943 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 5.59, 'message_length': 192, 'recipient': '558182986181', 'type': 'typing'}
2025-08-24 01:40:50.738 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 192, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-24 01:40:50.759 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-24 01:40:50.759 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:57008 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-24 01:40:51.667 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57008 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:34922 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53838 - "GET /health HTTP/1.1" 200 OK
2025-08-24 01:41:50.691 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59306 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:41:51.651 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:41:51.652 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:51.646Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59306 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:41:51.667 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59306 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:41:51.668 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:41:51.669 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:41:51.669 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': '400', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:41:51.670 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 3}
2025-08-24 01:41:52.359 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:52.359 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:51.967Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59306 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:52.581 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 5881d247-3cea-45ad-bf36-4e99161cca52, Phone: 558182986181
2025-08-24 01:41:52.582 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:52.582 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:51.995Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59316 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:53.249 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:41:53.251 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-24 01:41:53.251 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-24 01:41:53.710 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:41:53.710 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:41:53.711 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:41:53.719 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:41:53.719 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:41:53.719 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:41:53.720 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:41:53.720 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:41:53.720 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:41:53.720 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:41:53.720 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:41:53.723 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:41:53.961 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:41:54.485 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:41:54.503 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:41:54.503 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:54.497Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:41:54.519 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:41:54.520 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:41:54.520 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:41:54.520 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': '4000mil alias', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:41:54.700 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:41:54.708 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-24 01:41:54.714 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-24 01:41:54.714 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-24 01:41:54.821 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:54.821 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:54.816Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:54.852 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:54.852 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:54.846Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:54.991 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-24 01:41:55.636 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-24 01:41:55.659 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:41:55.660 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:41:55.660 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Mateus'}
2025-08-24 01:41:55.660 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-24 01:41:55.660 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): 400...
2025-08-24 01:41:55.661 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Detectadas mudanças no lead b81b1079-2916-461b-ad4c-b9a2f29f1a96. Sincronizando com o DB. | Data: {'changes': {'bill_value': 400.0, 'current_stage': 'INTERESTED', 'qualification_score': 30}}
2025-08-24 01:41:55.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead b81b1079-2916-461b-ad4c-b9a2f29f1a96 atualizado no Supabase.
2025-08-24 01:41:55.889 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'bill_value': 400.0, 'phone': '558182986181'}}
2025-08-24 01:41:55.973 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:41:55.974 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:55.968Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:41:55.989 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:41:55.990 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:41:55.990 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:41:55.991 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': '4mil e pouco', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:41:56.275 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:41:56.321 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:56.321 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:56.316Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:56.497 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:56.497 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:56.492Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
INFO:     10.11.0.4:59328 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-24 01:41:57.084 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'bill_value': 400.0, 'phone': '558182986181'}}
2025-08-24 01:41:59.122 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:41:59.123 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:59.117Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:41:59.138 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:41:59.139 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:41:59.139 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:41:59.139 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'as vezes até 5mil', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:41:59.224 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-24 01:41:59.442 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:59.442 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:59.436Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:41:59.470 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:41:59.470 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:41:59.465Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:01.923 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:42:01.924 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:01.914Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:42:01.939 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:50430 - "GET /health HTTP/1.1" 200 OK
2025-08-24 01:42:02.189 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:42:02.190 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:42:02.190 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:42:02.190 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'por isso quero a soluçao', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:42:02.242 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:02.242 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:02.235Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:02.301 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:02.302 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:02.295Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:02.833 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:42:02.834 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:02.828Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:42:02.851 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:42:02.851 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:42:02.852 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:42:02.852 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'de energia', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:42:03.153 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:03.153 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:03.148Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:03.184 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:03.184 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:03.178Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59328 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:09.692 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: <RESPOSTA_FINAL>Certo! E como você se chama? Assim a nossa conversa flui melhor.</RESPOSTA_FINAL>...
2025-08-24 01:42:18.552 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.56, 'message_length': 64, 'recipient': '558182986181', 'type': 'typing'}
2025-08-24 01:42:23.290 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 64, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-24 01:42:23.297 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-24 01:42:23.298 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:356 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:59972 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-24 01:42:24.227 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59972 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-24 01:42:29.718 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59982 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:36316 - "GET /health HTTP/1.1" 200 OK
2025-08-24 01:42:32.876 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-24 01:42:32.876 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:32.488Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:59982 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-24 01:42:32.877 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:36610 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-24 01:42:32.878 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-24 01:42:32.878 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-24 01:42:32.879 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus, já disse antes', 'sender': '558182986181', 'type': 'text'}
2025-08-24 01:42:32.879 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:32.880 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:32.807Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:36624 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:32.880 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-24 01:42:32.880 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:354 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFgugPPax2PxOjOijCR5n7KXz1uazT9Aug8oWl2WvDWlg&oe=68B7674D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T22:42:32.836Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:36640 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-24 01:42:32.881 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 22}
2025-08-24 01:42:33.557 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 5881d247-3cea-45ad-bf36-4e99161cca52, Phone: 558182986181
2025-08-24 01:42:34.225 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-24 01:42:34.225 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-24 01:42:34.723 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-24 01:42:34.723 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-24 01:42:34.723 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-24 01:42:34.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-24 01:42:34.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-24 01:42:34.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-24 01:42:34.731 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-24 01:42:34.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-24 01:42:34.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-24 01:42:34.732 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-24 01:42:34.732 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-24 01:42:34.735 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-24 01:42:35.009 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-24 01:42:35.504 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-24 01:42:36.044 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-24 01:42:36.572 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-24 01:42:36.592 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-24 01:42:36.593 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-24 01:42:36.594 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 3, 'lead_name': 'Mateus'}
2025-08-24 01:42:36.594 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-24 01:42:36.594 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): mateus, já disse antes...
2025-08-24 01:42:36.595 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'bill_value': 400.0, 'phone': '558182986181'}}
2025-08-24 01:42:37.748 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'bill_value': 400.0, 'phone': '558182986181'}}
INFO:     10.11.0.4:36640 - "POST /webhook/kommo/events HTTP/1.1" 200 OK