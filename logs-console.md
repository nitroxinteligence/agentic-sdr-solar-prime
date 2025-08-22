✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-21 21:52:59.402 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-21 21:52:59.407 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-21 21:52:59.408 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-21 21:53:00.061 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-21 21:53:00.061 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-21 21:53:00.061 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-21 21:53:00.062 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-21 21:53:00.062 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-21 21:53:00.062 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-21 21:53:00.090 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-21 21:53:00.099 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-21 21:53:00.100 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 21:53:00.100 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 21:53:00.100 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 21:53:00.101 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 21:53:00.101 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-21 21:53:00.101 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 21:53:00.101 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 21:53:00.102 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 21:53:00.102 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 21:53:00.316 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-21 21:53:00.320 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 21:53:00.596 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 21:53:01.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 21:53:02.063 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 21:53:02.562 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 21:53:02.596 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 21:53:02.597 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 21:53:02.598 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-21 21:53:02.598 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-21 21:53:02.599 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 21:53:02.607 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 21:53:02.608 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 21:53:02.608 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 21:53:02.608 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 21:53:02.609 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-21 21:53:02.609 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 21:53:02.609 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 21:53:02.610 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 21:53:02.610 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 21:53:02.612 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 21:53:02.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 21:53:03.568 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 21:53:04.137 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-21 21:53:04.938 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 21:53:04.959 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 21:53:04.960 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 21:53:04.960 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-21 21:53:04.960 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:33700 - "GET /health HTTP/1.1" 200 OK
2025-08-21 21:53:07.795 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 21:53:08.409 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 21:53:08.409 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:411 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T18:53:08.404Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 21:53:08.600 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 21:53:08.600 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:411 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T18:53:08.592Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 21:53:09.113 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-21 21:53:09.114 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-21 21:53:09.114 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-21 21:53:09.114 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Mensagem sem conteúdo de texto ou mídia de 558182986181
2025-08-21 21:53:09.310 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 21:53:09.311 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:411 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T18:53:09.300Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 21:53:10.076 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55062 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK'


---

INFO:     10.11.0.4:35122 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found

---



2025-08-21 22:29:02.233 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: cb6ad959-a036-410b-a1f5-7c5ab70f86d7
2025-08-21 22:29:02.235 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298...
2025-08-21 22:29:02.826 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 1 follow-ups pendentes encontrados.
2025-08-21 22:29:03.036 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Follow-up 30min agendado: 55818298...
2025-08-21 22:29:03.039 | ERROR    | app.services.followup_worker:_process_task:63 | Task de follow-up sem ID, descartando.
2025-08-21 22:29:03.651 | ERROR    | app.integrations.supabase_client:update_follow_up_status:375 | Erro ao atualizar follow-up: {'message': 'new row for relation "follow_ups" violates check constraint "follow_ups_status_check"', 'code': '23514', 'hint': None, 'details': 'Failing row contains (cb6ad959-a036-410b-a1f5-7c5ab70f86d7, 496cdc7c-290e-4dbf-8940-9e7167382cdf, 2025-08-21 22:29:02.005515+00, reengagement, , queued, null, null, 2025-08-21 22:29:02.005549+00, 2025-08-21 22:29:03.58742+00, {"source": "conversation_monitor", "original_type": "IMMEDIATE_R..., IMMEDIATE_REENGAGEMENT, null, medium, 0, null, null, null, null, 558182986181).'}
2025-08-21 22:29:03.651 | ERROR    | app.services.followup_executor_service:enqueue_pending_followups:97 | ❌ Erro ao enfileirar follow-up cb6ad959-a036-410b-a1f5-7c5ab70f86d7: {'message': 'new row for relation "follow_ups" violates check constraint "follow_ups_status_check"', 'code': '23514', 'hint': None, 'details': 'Failing row contains (cb6ad959-a036-410b-a1f5-7c5ab70f86d7, 496cdc7c-290e-4dbf-8940-9e7167382cdf, 2025-08-21 22:29:02.005515+00, reengagement, , queued, null, null, 2025-08-21 22:29:02.005549+00, 2025-08-21 22:29:03.58742+00, {"source": "conversation_monitor", "original_type": "IMMEDIATE_R..., IMMEDIATE_REENGAGEMENT, null, medium, 0, null, null, null, null, 558182986181).'}
INFO:     127.0.0.1:41746 - "GET /health HTTP/1.1" 200 OK
