✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-09-06 01:50:34.025 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-09-06 01:50:34.067 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-09-06 01:50:34.074 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-09-06 01:50:34.074 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto | Data: {'data': {'url': 'redis_redis:6379'}}
2025-09-06 01:50:34.338 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-09-06 01:50:34.338 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=20.0s, max=10)
2025-09-06 01:50:34.338 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'data': {'timeout': '20.0s'}}
2025-09-06 01:50:34.338 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=250, smart=ativada)
2025-09-06 01:50:34.338 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'data': {'max_length': 250}}
2025-09-06 01:50:34.347 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-06 01:50:34.347 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-06 01:50:34.347 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversation Monitor pronto
2025-09-06 01:50:34.347 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'data': {'modules': 'Core + Services'}}
2025-09-06 01:50:34.355 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Service pronto
2025-09-06 01:50:34.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler (Redis Mode) pronto
2025-09-06 01:50:34.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto | Data: {'data': {'interval': '1800s'}}
2025-09-06 01:50:34.371 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-09-06 01:50:34.380 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-09-06 01:50:34.380 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-09-06 01:50:34.380 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-09-06 01:50:34.387 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-09-06 01:50:34.388 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-09-06 01:50:34.388 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-09-06 01:50:34.388 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-09-06 01:50:34.389 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-09-06 01:50:34.389 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-09-06 01:50:34.389 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-06 01:50:34.389 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-06 01:50:34.588 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-09-06 01:50:34.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-09-06 01:50:34.868 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:77 | 📋 2 follow-ups pendentes encontrados.
2025-09-06 01:50:34.869 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-09-06 01:50:36.247 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up d505f5a0-0cdb-4d54-b336-6eb6d3366ad8 enfileirado no Redis.
2025-09-06 01:50:37.553 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 3ce9faa7-7f7f-4e98-9b2f-09664c332a2e enfileirado no Redis.
2025-09-06 01:50:37.555 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-09-06 01:50:38.150 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-09-06 01:50:38.673 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-06 01:50:38.725 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-09-06 01:50:38.726 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-09-06 01:50:38.726 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker (Redis Mode) pronto
2025-09-06 01:50:38.727 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto | Data: {'data': {'queue': 'followup_tasks'}}
2025-09-06 01:50:38.738 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-09-06 01:50:38.738 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-09-06 01:50:38.739 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-09-06 01:50:38.747 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-09-06 01:50:38.747 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-09-06 01:50:38.747 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-09-06 01:50:38.748 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-09-06 01:50:38.748 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-09-06 01:50:38.748 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-09-06 01:50:38.748 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-06 01:50:38.748 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-06 01:50:38.751 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-09-06 01:50:39.000 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-09-06 01:50:39.002 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: d505f5a0-0cdb-4d54-b336-6eb6d3366ad8
2025-09-06 01:50:40.798 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-09-06 01:50:41.365 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-09-06 01:50:42.115 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-06 01:50:42.137 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-09-06 01:50:42.137 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
INFO:     Application startup complete.
2025-09-06 01:50:42.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'data': {'status': 'sistema pronto'}}
2025-09-06 01:50:42.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services pronto | Data: {'data': {'redis_workers': '✅ Com Redis Workers'}}
2025-09-06 01:50:42.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 8070.49}
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:40652 - "GET /health HTTP/1.1" 200 OK
2025-09-06 01:50:55.807 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51512 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-09-06 01:51:03.891 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Typing enviado para 558197880587 (duração: 8.48s, tamanho: 264)
2025-09-06 01:51:14.517 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Mensagem de texto enviada para 558197880587 (tamanho: 264, delay: 5.0s)
2025-09-06 01:51:14.819 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up d505f5a0-0cdb-4d54-b336-6eb6d3366ad8 executado e enviado com sucesso.
2025-09-06 01:51:14.820 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 3ce9faa7-7f7f-4e98-9b2f-09664c332a2e
INFO:     127.0.0.1:46730 - "GET /health HTTP/1.1" 200 OK
2025-09-06 01:51:17.002 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:47768 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-09-06 01:51:33.471 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:58896 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-09-06 01:51:37.925 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Typing enviado para 558196491408 (duração: 4.32s, tamanho: 218)
2025-09-06 01:51:44.360 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Mensagem de texto enviada para 558196491408 (tamanho: 218, delay: 5.0s)
2025-09-06 01:51:44.981 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up 3ce9faa7-7f7f-4e98-9b2f-09664c332a2e executado e enviado com sucesso.
INFO:     127.0.0.1:49616 - "GET /health HTTP/1.1" 200 OK
2025-09-06 01:51:46.379 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51828 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:43696 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54616 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54800 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46316 - "GET /health HTTP/1.1" 200 OK
2025-09-06 01:54:13.857 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41676 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-09-06 01:54:13.859 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41674 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-09-06 01:54:13.860 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-09-06 01:54:13.861 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:784 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41682 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-09-06 01:54:13.862 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41696 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:32894 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41232 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39074 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39602 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56904 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41514 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34138 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59336 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:48852 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     10.11.0.4:48852 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:40822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42666 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46610 - "GET /health HTTP/1.1" 200 OK
2025-09-06 01:59:40.592 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-09-06 01:59:40.592 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-09-06 01:59:40.592 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558195554978@s.whatsapp.net",
      "profilePicUrl": null,
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-09-05T22:59:40.323Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558195554978@s.whatsapp.net",
    "profilePicUrl": null,
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558195554978@s.whatsapp.net",
  "profilePicUrl": null,
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558195554978@s.whatsapp.net",
  "profilePicUrl": null,
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-09-06 01:59:40.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'profilePicUrl', 'instanceId']
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558195554978@s.whatsapp.net'
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558195554978'
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558195554978' (válido: True)
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'None' (válido: False)
2025-09-06 01:59:40.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-09-06 01:59:40.594 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: pushName. Phone: '558195554978', PushName: 'None'
INFO:     10.11.0.4:45540 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-09-06 01:59:46.976 | INFO     | app.integrations.supabase_client:create_follow_up:345 | Follow-up criado: d0285411-6e21-41c3-af1d-3dd9eaa472ad
2025-09-06 01:59:46.977 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298... (Tentativa 1)
2025-09-06 01:59:46.978 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔄 Status da conversa para 55818298... atualizado para: followup_30min_sent
INFO:     127.0.0.1:53762 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58600 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59152 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33976 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:01:48.983 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:01:49.611 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:01:50.205 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:01:50.795 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:01:51.044 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:01:51.644 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:01:52.257 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:01:52.520 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:01:52.753 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:44100 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39626 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:02:51.309 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:02:51.555 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:02:51.772 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:02:51.996 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:02:52.230 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:02:52.457 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:02:52.967 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:02:53.187 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:02:53.414 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:57854 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48464 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:03:52.216 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:03:52.458 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:03:52.683 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:03:52.911 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:03:53.132 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:03:53.354 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:03:53.634 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:03:53.857 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:03:54.076 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:43154 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55136 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:04:53.002 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:04:53.623 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:04:53.873 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:04:54.152 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:04:54.370 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:04:54.593 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:04:54.813 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:04:55.062 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:04:55.281 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:36212 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44604 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:05:54.387 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:05:54.616 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:05:54.845 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:05:55.068 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:05:55.296 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:05:55.532 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:05:55.758 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:05:55.975 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:05:56.193 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:60246 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58670 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:06:55.482 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:06:55.721 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:06:56.336 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:06:56.562 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:06:57.182 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:06:57.408 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:06:57.634 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:06:57.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:06:58.078 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:38896 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44922 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:07:56.762 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:07:56.994 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:07:57.215 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:07:58.223 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:07:58.436 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:07:58.653 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:07:58.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:07:59.082 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:07:59.297 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:48298 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33848 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:08:57.867 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:08:58.506 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:08:59.114 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:08:59.713 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:09:00.334 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:09:00.556 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:09:01.156 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:09:01.380 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:09:01.611 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:58812 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:09:29.656 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/connection-update de evolution-api | Data: {'event': 'CONNECTION_UPDATE', 'endpoint': '/whatsapp/connection-update', 'source': 'evolution-api'}
2025-09-06 02:09:29.657 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Connection status update: {'event': 'connection.update', 'instance': 'SDR IA SolarPrime', 'data': {'instance': 'SDR IA SolarPrime', 'state': 'connecting', 'statusReason': 200}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-09-05T23:09:29.451Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55946 - "POST /webhook/evolution/connection-update HTTP/1.1" 200 OK
2025-09-06 02:09:30.850 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/connection-update de evolution-api | Data: {'event': 'CONNECTION_UPDATE', 'endpoint': '/whatsapp/connection-update', 'source': 'evolution-api'}
2025-09-06 02:09:30.850 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Connection status update: {'event': 'connection.update', 'instance': 'SDR IA SolarPrime', 'data': {'instance': 'SDR IA SolarPrime', 'wuid': '558195554978@s.whatsapp.net', 'profileName': 'Mateus M', 'profilePictureUrl': None, 'state': 'open', 'statusReason': 200}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-09-05T23:09:30.845Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55946 - "POST /webhook/evolution/connection-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:39188 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:09:59.554 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:09:59.789 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:09:59.997 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:10:01.376 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:10:01.601 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:10:02.201 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:10:02.420 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:10:02.634 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:10:02.856 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:59848 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36922 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:11:00.623 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:11:00.867 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:11:01.481 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:11:02.806 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:11:03.406 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:11:04.010 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:11:04.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:11:04.859 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:11:05.083 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:37346 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33414 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:12:01.930 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:12:02.167 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:12:02.397 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:12:04.592 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:12:04.805 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:12:05.022 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:12:05.300 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:12:05.516 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:12:05.743 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:47946 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41960 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:13:02.879 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:13:03.113 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:13:03.336 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:13:05.249 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:13:05.482 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:13:05.711 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:13:06.359 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:13:06.587 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:13:06.889 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:34934 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34262 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:14:03.769 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:14:04.004 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:14:04.233 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:14:05.934 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:14:06.153 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:14:06.366 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:14:07.101 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:14:07.318 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:14:07.531 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:50664 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51368 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:15:04.485 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:15:05.109 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:15:05.706 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:15:06.579 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:15:06.798 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:15:07.410 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:15:07.756 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:15:07.976 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:15:08.195 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:54948 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37812 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:16:06.530 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:16:07.168 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:16:07.752 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:16:08.345 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:16:08.937 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:16:09.545 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:16:09.772 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:16:10.370 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:16:10.589 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:57864 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54972 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:17:08.024 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:17:08.635 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:17:09.243 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:17:10.382 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:17:10.606 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:17:10.827 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:17:11.043 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:17:11.263 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:17:11.489 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:42510 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41790 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:18:10.075 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:18:10.318 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:18:10.547 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:18:11.655 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:18:11.893 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:18:12.514 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:18:13.130 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:18:13.356 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:18:13.576 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:32934 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59956 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:19:10.861 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:19:11.138 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:19:11.758 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:19:13.738 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:19:14.335 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:19:14.608 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:19:14.851 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:19:15.091 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:19:15.727 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:44148 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:52782 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:46750 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:20:12.353 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:20:12.580 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:20:13.184 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:20:15.068 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:20:15.279 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:20:15.489 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:20:16.304 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:20:16.531 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:20:16.754 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:59122 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:20:37.792 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:77 | 📋 1 follow-ups pendentes encontrados.
2025-09-06 02:20:38.239 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up d0285411-6e21-41c3-af1d-3dd9eaa472ad enfileirado no Redis.
2025-09-06 02:20:38.240 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: d0285411-6e21-41c3-af1d-3dd9eaa472ad
INFO:     127.0.0.1:33526 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:20:53.143 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ extract_final_response - Tag <RESPOSTA_FINAL> não encontrada. Usando fallback de segurança. | Data: {'raw_response': 'Opa Mateus, tudo joia? Só passando para confirmar se aquele horário que sugeri, na segunda-feira às 10h da manhã, fica bom para você conversar com o Leonardo e entender melhor sua economia.'}
2025-09-06 02:20:58.917 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33500 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-09-06 02:21:01.667 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Typing enviado para 558182986181 (duração: 3.12s, tamanho: 63)
2025-09-06 02:21:06.868 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Mensagem de texto enviada para 558182986181 (tamanho: 63, delay: 5.0s)
2025-09-06 02:21:07.122 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Follow-up d0285411-6e21-41c3-af1d-3dd9eaa472ad executado e enviado com sucesso.
2025-09-06 02:21:07.676 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52790 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-09-06 02:21:13.434 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:21:13.653 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:21:13.877 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:21:15.712 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:21:15.939 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:21:16.161 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:21:16.980 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:21:17.216 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:21:17.437 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:39316 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43100 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:22:14.691 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:22:14.922 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:22:15.141 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:22:16.376 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:22:16.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:22:16.820 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:22:17.649 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:22:17.873 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:22:18.136 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:54636 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53158 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:23:15.397 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:23:15.639 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:23:15.860 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:23:17.038 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:23:17.256 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:23:17.473 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:23:18.360 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:23:18.574 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:23:18.801 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:59060 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52920 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:24:16.283 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:24:16.528 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:24:16.754 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:24:17.685 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:24:18.267 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:24:18.489 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:24:19.426 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:24:19.642 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:24:19.866 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:58202 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59412 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:25:17.009 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:25:17.244 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:25:17.462 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:25:19.086 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:25:19.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:25:19.524 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:25:20.145 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:25:20.365 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:25:20.943 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:45290 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54284 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:26:17.891 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:26:18.123 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:26:18.339 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:26:19.748 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:26:19.960 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:26:20.202 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:26:21.163 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:26:21.375 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
INFO:     127.0.0.1:54008 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:26:21.590 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:48544 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:27:19.139 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:27:19.752 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:27:20.359 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:27:20.962 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:27:21.184 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:27:21.771 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:60812 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:27:22.370 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:27:22.971 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:27:23.610 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:48386 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:28:20.782 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:28:21.417 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:28:21.649 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:28:21.986 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
INFO:     127.0.0.1:45800 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:28:22.202 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:28:22.417 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:28:23.820 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:28:24.034 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:28:24.246 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:58578 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:29:21.919 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:29:22.154 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
INFO:     127.0.0.1:42636 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:29:22.373 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:29:22.639 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:29:22.854 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:29:23.078 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
2025-09-06 02:29:24.476 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:29:24.693 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:29:24.910 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:37846 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41846 - "GET /health HTTP/1.1" 200 OK
2025-09-06 02:30:22.801 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558182986181 pausada.
2025-09-06 02:30:23.026 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558197880587 pausada.
2025-09-06 02:30:23.235 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Fora do horário comercial. Verificação de inatividade para 558196491408 pausada.
INFO:     127.0.0.1:40384 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39878 - "GET /health HTTP/1.1" 200 OK