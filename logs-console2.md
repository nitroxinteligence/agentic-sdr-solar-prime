✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-08-23 20:24:32.324 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-23 20:24:33.872 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-23 20:24:33.886 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-23 20:24:33.887 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-23 20:24:34.727 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-23 20:24:34.728 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-23 20:24:34.728 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-23 20:24:34.728 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-23 20:24:34.728 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-23 20:24:34.728 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-23 20:24:34.755 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-23 20:24:34.762 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 20:24:34.762 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-23 20:24:34.763 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 20:24:34.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 20:24:34.769 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 20:24:34.770 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 20:24:34.770 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 20:24:34.771 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 20:24:34.771 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 20:24:34.771 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 20:24:34.771 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 20:24:34.771 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 20:24:34.971 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-23 20:24:34.976 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 20:24:35.741 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 20:24:36.370 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298... Criando lead básico.
2025-08-23 20:24:36.993 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'table': 'leads', 'count': 1}
2025-08-23 20:24:37.825 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 0b6c2402-f5df-49bc-91ce-8385e509d0ef
2025-08-23 20:24:37.826 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298... (Tentativa 1)
2025-08-23 20:24:37.827 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
2025-08-23 20:24:38.424 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813... Criando lead básico.
2025-08-23 20:24:39.031 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558198132001', 'table': 'leads', 'count': 1}
2025-08-23 20:24:40.244 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 65c3db87-9955-4228-90ac-75016d9fc15e
2025-08-23 20:24:40.244 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55819813... (Tentativa 1)
2025-08-23 20:24:40.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55819813...
2025-08-23 20:24:40.890 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649... Criando lead básico.
2025-08-23 20:24:41.484 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558196491408', 'table': 'leads', 'count': 1}
2025-08-23 20:24:42.708 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 808b67d8-e097-427f-833a-a4036ce8b7af
2025-08-23 20:24:42.709 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55819649... (Tentativa 1)
2025-08-23 20:24:42.714 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55819649...
2025-08-23 20:24:42.968 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 20:24:43.529 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 20:24:44.080 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 20:24:44.152 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 20:24:44.153 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 20:24:44.153 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-23 20:24:44.153 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-23 20:24:44.153 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-23 20:24:44.161 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 20:24:44.161 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 20:24:44.162 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 20:24:44.170 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 20:24:44.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 20:24:44.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 20:24:44.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 20:24:44.172 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 20:24:44.172 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 20:24:44.172 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 20:24:44.172 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 20:24:44.176 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 20:24:44.777 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 20:24:46.001 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 20:24:46.567 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 20:24:47.103 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 20:24:47.130 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 20:24:47.131 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 20:24:47.131 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-23 20:24:47.131 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:36700 - "GET /health HTTP/1.1" 200 OK
2025-08-23 20:24:51.359 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 3 follow-ups pendentes encontrados.
2025-08-23 20:24:52.547 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 0b6c2402-f5df-49bc-91ce-8385e509d0ef enfileirado.
2025-08-23 20:24:52.773 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 0b6c2402-f5df-49bc-91ce-8385e509d0ef
2025-08-23 20:24:55.192 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 65c3db87-9955-4228-90ac-75016d9fc15e enfileirado.
2025-08-23 20:24:56.022 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 808b67d8-e097-427f-833a-a4036ce8b7af enfileirado.
2025-08-23 20:25:02.683 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Tag <RESPOSTA_FINAL> não encontrada na resposta do LLM. | Data: {'raw_response': 'Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?'}
2025-08-23 20:25:11.294 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.1, 'message_length': 144, 'recipient': '558182986181', 'type': 'typing'}
2025-08-23 20:25:14.568 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-23 20:25:15.214 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 20:25:15.215 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:15.210Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 20:25:15.265 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 20:25:15.265 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:15.259Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 20:25:15.303 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-23 20:25:15.304 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-23 20:25:15.304 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-23 20:25:15.305 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-23 20:25:15.587 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 20:25:15.587 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGOpEH2PMLfFF-b19nbtmwlnvMuJ6Btm0ykHiPtrYEHAw&oe=68B72F0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:15.580Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 20:25:15.649 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 20:25:15.649 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGOpEH2PMLfFF-b19nbtmwlnvMuJ6Btm0ykHiPtrYEHAw&oe=68B72F0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:15.643Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 20:25:16.579 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 144, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-23 20:25:17.196 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up 0b6c2402-f5df-49bc-91ce-8385e509d0ef executado e enviado com sucesso.
2025-08-23 20:25:17.197 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 20:25:17.198 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 20:25:17.200 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 65c3db87-9955-4228-90ac-75016d9fc15e
2025-08-23 20:25:18.637 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33478 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:25:18.639 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33486 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:25:18.639 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-23 20:25:18.640 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:60280 - "GET /health HTTP/1.1" 200 OK
2025-08-23 20:25:19.760 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-23 20:25:20.998 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 20:25:20.998 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:20.992Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 20:25:21.007 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-23 20:25:21.007 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:21.002Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-23 20:25:21.014 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-23 20:25:21.015 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-23 20:25:21.015 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-23 20:25:21.015 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-23 20:25:21.316 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 20:25:21.317 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGOpEH2PMLfFF-b19nbtmwlnvMuJ6Btm0ykHiPtrYEHAw&oe=68B72F0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:21.311Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 20:25:21.354 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 20:25:21.355 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGOpEH2PMLfFF-b19nbtmwlnvMuJ6Btm0ykHiPtrYEHAw&oe=68B72F0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T17:25:21.348Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 20:25:30.417 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 2 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 9}
2025-08-23 20:25:32.268 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Tag <RESPOSTA_FINAL> não encontrada na resposta do LLM. | Data: {'raw_response': 'Oi, tudo bem? Vi que você se interessou em saber mais sobre energia solar. Por aqui, quem vai te ajudar com isso sou eu, Helen. Pra gente começar, como prefere que eu te chame?'}
2025-08-23 20:25:32.866 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 9524c313-dfdf-4d84-9943-042a70f62d57, Phone: 558182986181
2025-08-23 20:25:34.307 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-23 20:25:34.308 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-23 20:25:35.143 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 20:25:35.143 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 20:25:35.145 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 20:25:35.156 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 20:25:35.157 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 20:25:35.157 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 20:25:35.157 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 20:25:35.158 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 20:25:35.158 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 20:25:35.158 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 20:25:35.158 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 20:25:35.161 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 20:25:36.035 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 20:25:37.212 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 20:25:38.779 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 20:25:39.317 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 20:25:39.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 20:25:39.345 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 20:25:39.345 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-23 20:25:39.345 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-23 20:25:39.346 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): oi
mateus...
2025-08-23 20:25:39.958 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'name': 'Mateus', 'current_stage': 'INTERESTED', 'qualification_score': 20, 'preferences': {'interests': [], 'objections': []}, 'processed_message_count': 2, 'updated_at': '2025-08-23T20:25:39.351134'}}
2025-08-23 20:25:40.898 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181'}}
2025-08-23 20:25:40.899 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181'}}
INFO:     10.11.0.4:39436 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-23 20:25:42.324 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558198132001 | Data: {'duration_seconds': 4.74, 'message_length': 176, 'recipient': '558198132001', 'type': 'typing'}
INFO:     127.0.0.1:51898 - "GET /health HTTP/1.1" 200 OK
2025-08-23 20:25:49.579 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 20:25:49.580 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:39710 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 20:25:49.581 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558198132001 | Data: {'message_length': 176, 'delay_used': 5.0, 'recipient': '558198132001', 'type': 'text'}
2025-08-23 20:25:49.828 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up 65c3db87-9955-4228-90ac-75016d9fc15e executado e enviado com sucesso.
2025-08-23 20:25:49.830 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 808b67d8-e097-427f-833a-a4036ce8b7af
2025-08-23 20:25:50.503 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39710 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:25:50.505 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39724 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:25:58.525 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Tag <RESPOSTA_FINAL> não encontrada na resposta do LLM. | Data: {'raw_response': 'Olá! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?'}
2025-08-23 20:26:06.380 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558196491408 | Data: {'duration_seconds': 2.62, 'message_length': 144, 'recipient': '558196491408', 'type': 'typing'}
2025-08-23 20:26:11.174 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558196491408 | Data: {'message_length': 144, 'delay_used': 5.0, 'recipient': '558196491408', 'type': 'text'}
2025-08-23 20:26:11.752 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up 808b67d8-e097-427f-833a-a4036ce8b7af executado e enviado com sucesso.
2025-08-23 20:26:11.754 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 20:26:11.754 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:45840 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 20:26:12.207 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45840 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:26:12.648 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45840 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 20:26:13.535 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: <RESPOSTA_FINAL>Olá Mateus, tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei rea...
INFO:     127.0.0.1:37374 - "GET /health HTTP/1.1" 200 OK
2025-08-23 20:26:23.743 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.12, 'message_length': 108, 'recipient': '558182986181', 'type': 'typing'}