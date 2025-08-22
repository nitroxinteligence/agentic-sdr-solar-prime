# ERRO NO FOLLOW-UP:

2025-08-22 16:46:07.042 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 1 follow-ups pendentes encontrados.
2025-08-22 16:46:07.500 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 20a41c35-1b2c-4c60-855e-441dc289f59b enfileirado.
2025-08-22 16:46:07.501 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 20a41c35-1b2c-4c60-855e-441dc289f59b
2025-08-22 16:46:10.198 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro ao processar tarefa 20a41c35-1b2c-4c60-855e-441dc289f59b: module 'google.generativeai.types' has no attribute 'Content' | Data: {'component': 'FollowUp Worker'}

---

# OUTRO ERRO:

2025-08-22 16:46:22.898 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Erro: 'list' object has no attribute 'lower' | Data: {'component': 'AgenticSDRStateless'}
2025-08-22 16:46:22.899 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Traceback: Traceback (most recent call last):
  File "/app/app/agents/agentic_sdr_stateless.py", line 173, in process_message
    new_lead_info = self.lead_manager.extract_lead_info(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/core/lead_manager.py", line 68, in extract_lead_info
    content = msg.get("content", "").lower()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'lower'
 | Data: {'component': 'AgenticSDRStateless'}
INFO:     127.0.0.1:45252 - "GET /health HTTP/1.1" 200 OK

---

# LOG COMPLETO:

✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-08-22 16:45:48.886 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-22 16:45:49.662 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-22 16:45:49.666 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-22 16:45:49.666 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-22 16:45:50.276 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-22 16:45:50.295 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-22 16:45:50.302 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 16:45:50.302 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-22 16:45:50.302 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 16:45:50.302 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 16:45:50.303 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 16:45:50.303 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 16:45:50.303 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 16:45:50.303 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 16:45:50.304 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 16:45:50.304 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 16:45:50.304 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 16:45:50.521 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-22 16:45:50.525 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 16:45:50.806 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 16:45:52.269 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 20a41c35-1b2c-4c60-855e-441dc289f59b
2025-08-22 16:45:52.270 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298...
2025-08-22 16:45:52.271 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Follow-up 30min agendado: 55818298...
2025-08-22 16:45:52.807 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 16:45:53.408 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 16:45:53.958 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 16:45:53.992 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 16:45:53.993 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 16:45:53.994 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-22 16:45:53.994 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-22 16:45:53.994 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-22 16:45:54.001 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 16:45:54.001 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 16:45:54.002 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 16:45:54.002 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 16:45:54.002 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 16:45:54.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 16:45:54.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 16:45:54.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 16:45:54.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 16:45:54.003 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 16:45:54.006 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 16:45:54.272 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 16:45:54.784 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 16:45:55.358 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-22 16:45:55.894 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 16:45:55.912 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 16:45:55.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 16:45:55.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-22 16:45:55.914 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:58340 - "GET /health HTTP/1.1" 200 OK
2025-08-22 16:45:58.751 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-22 16:45:59.204 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-22 16:45:59.204 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:45:59.185Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-22 16:45:59.496 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:45:59.496 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:45:59.488Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:45:59.727 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-22 16:45:59.773 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 16:45:59.774 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 16:45:59.774 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 16:45:59.774 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para audioMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 16:45:59.774 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/v/t62.7117-24/537224019_1...
2025-08-22 16:45:59.775 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: audio)
2025-08-22 16:46:00.087 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:46:00.088 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:46:00.080Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.253 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 9578 bytes
2025-08-22 16:46:00.254 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 16:46:00.254 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 16:46:00.266 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 16:46:00.273 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 9563 bytes
2025-08-22 16:46:00.273 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 9563 bytes
2025-08-22 16:46:00.274 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido audio de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'audio'}
2025-08-22 16:46:00.638 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.657 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.657 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:00.661 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.678 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60362 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.681 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.682 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:00.693 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.714 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.720 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.720 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:00.733 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.734 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:00.737 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:46:00.743 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.743 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:00.759 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:46:00.760 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60378 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:46:07.042 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 1 follow-ups pendentes encontrados.
2025-08-22 16:46:07.500 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 20a41c35-1b2c-4c60-855e-441dc289f59b enfileirado.
2025-08-22 16:46:07.501 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 20a41c35-1b2c-4c60-855e-441dc289f59b
2025-08-22 16:46:10.198 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro ao processar tarefa 20a41c35-1b2c-4c60-855e-441dc289f59b: module 'google.generativeai.types' has no attribute 'Content' | Data: {'component': 'FollowUp Worker'}
2025-08-22 16:46:10.816 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:44808 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-22 16:46:15.318 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-22 16:46:16.740 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 829c2529-dff3-4cfe-9027-42619ff6aacf, Phone: 558182986181
2025-08-22 16:46:18.559 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 16:46:18.559 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 16:46:19.187 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 16:46:19.188 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 16:46:19.188 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 16:46:19.189 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 16:46:19.189 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 16:46:19.190 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 16:46:19.190 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 16:46:19.190 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 16:46:19.190 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 16:46:19.191 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 16:46:19.193 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 16:46:19.478 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 16:46:20.006 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 16:46:20.581 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 16:46:21.199 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 16:46:21.228 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 16:46:21.229 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 16:46:21.229 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 3, 'lead_name': None}
2025-08-22 16:46:21.229 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 16:46:21.230 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): ...
2025-08-22 16:46:21.231 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 📎 Mídia do tipo image/jpeg adicionada de forma genérica ao prompt.
2025-08-22 16:46:22.895 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 🎤 Áudio transcrito: 61 caracteres
2025-08-22 16:46:22.898 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Erro: 'list' object has no attribute 'lower' | Data: {'component': 'AgenticSDRStateless'}
2025-08-22 16:46:22.899 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Traceback: Traceback (most recent call last):
  File "/app/app/agents/agentic_sdr_stateless.py", line 173, in process_message
    new_lead_info = self.lead_manager.extract_lead_info(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/core/lead_manager.py", line 68, in extract_lead_info
    content = msg.get("content", "").lower()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'lower'
 | Data: {'component': 'AgenticSDRStateless'}
INFO:     127.0.0.1:45252 - "GET /health HTTP/1.1" 200 OK
2025-08-22 16:46:29.793 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.08, 'message_length': 46, 'recipient': '558182986181', 'type': 'typing'}
2025-08-22 16:46:33.993 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 46, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 16:46:34.003 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 16:46:34.003 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:43686 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 16:46:34.851 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:43686 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK