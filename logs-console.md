✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-09-05 20:57:59.766 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-09-05 20:57:59.794 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-09-05 20:57:59.798 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-09-05 20:57:59.799 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto | Data: {'data': {'url': 'redis_redis:6379'}}
2025-09-05 20:58:00.049 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-09-05 20:58:00.049 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=20.0s, max=10)
2025-09-05 20:58:00.049 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'data': {'timeout': '20.0s'}}
2025-09-05 20:58:00.049 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=250, smart=ativada)
2025-09-05 20:58:00.050 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'data': {'max_length': 250}}
2025-09-05 20:58:00.059 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-05 20:58:00.060 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-05 20:58:00.060 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversation Monitor pronto
2025-09-05 20:58:00.060 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'data': {'modules': 'Core + Services'}}
2025-09-05 20:58:00.069 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Service pronto
2025-09-05 20:58:00.081 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler (Redis Mode) pronto
2025-09-05 20:58:00.082 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto | Data: {'data': {'interval': '1800s'}}
2025-09-05 20:58:00.092 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-09-05 20:58:00.102 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-09-05 20:58:00.103 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-09-05 20:58:00.104 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-09-05 20:58:00.113 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-09-05 20:58:00.114 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-09-05 20:58:00.114 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-09-05 20:58:00.114 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-09-05 20:58:00.115 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-09-05 20:58:00.115 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-09-05 20:58:00.115 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-05 20:58:00.115 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-05 20:58:00.319 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-09-05 20:58:00.324 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-09-05 20:58:00.842 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-09-05 20:58:01.072 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead ed59d1e3-ff55-4737-a336-23d2b25d55c5. Tipo: IMMEDIATE_REENGAGEMENT
2025-09-05 20:58:01.073 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
2025-09-05 20:58:01.299 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead ed59d1e3-ff55-4737-a336-23d2b25d55c5. Tipo: IMMEDIATE_REENGAGEMENT
2025-09-05 20:58:01.300 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
2025-09-05 20:58:02.020 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-09-05 20:58:02.583 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-09-05 20:58:03.156 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-05 20:58:03.235 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-09-05 20:58:03.236 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-09-05 20:58:03.237 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker (Redis Mode) pronto
2025-09-05 20:58:03.237 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto | Data: {'data': {'queue': 'followup_tasks'}}
2025-09-05 20:58:03.245 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-09-05 20:58:03.246 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-09-05 20:58:03.246 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-09-05 20:58:03.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-09-05 20:58:03.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-09-05 20:58:03.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-09-05 20:58:03.254 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-09-05 20:58:03.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-09-05 20:58:03.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-09-05 20:58:03.255 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-05 20:58:03.255 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-05 20:58:03.258 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-09-05 20:58:03.497 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-09-05 20:58:03.706 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead ed59d1e3-ff55-4737-a336-23d2b25d55c5. Tipo: DAILY_NURTURING
2025-09-05 20:58:03.706 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 📅 Status Redis atualizado: followup_24h_sent para 55818298...
2025-09-05 20:58:04.272 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-09-05 20:58:04.999 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-09-05 20:58:05.675 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-05 20:58:05.697 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-09-05 20:58:05.698 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-09-05 20:58:05.698 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'data': {'status': 'sistema pronto'}}
2025-09-05 20:58:05.699 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services pronto | Data: {'data': {'redis_workers': '✅ Com Redis Workers'}}
2025-09-05 20:58:05.699 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 5904.88}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:59856 - "GET /health HTTP/1.1" 200 OK
2025-09-05 20:58:15.607 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:37688 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-09-05 20:58:16.012 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-09-05 20:58:16.013 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:780 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-09-05T17:58:15.983Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:37688 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-09-05 20:58:16.020 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-09-05 20:58:16.020 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:780 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-09-05T17:58:16.011Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:37688 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-09-05 20:58:16.071 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:37688 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-09-05 20:58:16.072 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-09-05 20:58:16.072 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-09-05 20:58:16.073 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando mídia. Message key: {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3A2C8B3DCCDBE49A2786', 'senderLid': '129472024072320@lid'}
2025-09-05 20:58:16.073 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum tipo de mídia reconhecido encontrado no payload
2025-09-05 20:58:16.073 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-09-05 20:58:16.130 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-09-05 20:58:16.131 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-09-05 20:58:16.131 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558182986181@s.whatsapp.net",
      "pushName": "Mateus M",
      "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGWXcCi56K8FmDOY0mAhV4EIvlBU4M5vTVC5sgx7kuS_g&oe=68C8528D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-09-05T17:58:16.113Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-09-05 20:58:16.131 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-09-05 20:58:16.131 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-09-05 20:58:16.132 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGWXcCi56K8FmDOY0mAhV4EIvlBU4M5vTVC5sgx7kuS_g&oe=68C8528D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-09-05 20:58:16.132 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-09-05 20:58:16.132 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGWXcCi56K8FmDOY0mAhV4EIvlBU4M5vTVC5sgx7kuS_g&oe=68C8528D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGWXcCi56K8FmDOY0mAhV4EIvlBU4M5vTVC5sgx7kuS_g&oe=68C8528D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-09-05 20:58:16.133 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-09-05 20:58:16.134 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-09-05 20:58:16.134 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-09-05 20:58:16.424 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:37688 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-09-05 20:58:16.425 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-09-05 20:58:16.425 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.3s)
INFO:     10.11.0.4:37694 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-09-05 20:58:17.075 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔄 Processando 1 mensagens combinadas para 558182986181 (total: 2 chars)
2025-09-05 20:58:17.075 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'oi...', ID: 3A2C8B3DCCDBE49A2786
2025-09-05 20:58:17.792 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: ed59d1e3-ff55-4737-a336-23d2b25d55c5, Nome: 'Mateus M'
2025-09-05 20:58:17.793 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: f0faa62a-55a3-4bd3-9bce-99b299d0a9d5
2025-09-05 20:58:17.793 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: f0faa62a-55a3-4bd3-9bce-99b299d0a9d5, Phone: 558182986181
2025-09-05 20:58:18.485 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-09-05 20:58:18.485 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-09-05 20:58:18.485 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-09-05 20:58:19.238 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-09-05 20:58:19.814 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-09-05 20:58:20.329 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-05 20:58:21.475 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-09-05 20:58:21.476 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-09-05 20:58:21.476 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-09-05 20:58:21.484 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-09-05 20:58:21.484 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-09-05 20:58:21.484 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-09-05 20:58:21.484 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-09-05 20:58:21.485 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-09-05 20:58:21.485 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-09-05 20:58:21.485 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-09-05 20:58:21.485 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-09-05 20:58:21.488 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-09-05 20:58:21.793 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-09-05 20:58:21.954 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead ed59d1e3-ff55-4737-a336-23d2b25d55c5. Tipo: IMMEDIATE_REENGAGEMENT
2025-09-05 20:58:21.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
2025-09-05 20:58:22.404 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-09-05 20:58:22.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-09-05 20:58:23.515 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-09-05 20:58:23.549 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-09-05 20:58:23.550 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-09-05 20:58:23.550 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 15, 'lead_name': 'Mateus M'}
2025-09-05 20:58:23.550 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-09-05 20:58:23.551 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'oi...'
2025-09-05 20:58:23.552 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-09-05 20:58:23.552 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 16 mensagens
2025-09-05 20:58:23.553 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-09-05 20:58:23.553 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: 500.0
2025-09-05 20:58:23.553 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-09-05 20:58:23.553 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 16 msgs
2025-09-05 20:58:23.554 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-09-05 20:58:23.554 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Compra com Desconto', 'name': 'Mateus M', 'bill_value': 500.0, 'phone': '558182986181', 'qualification_score': 40, 'tags': ['Compra com Desconto']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 5.2s
⏳ Rate Limiter: Aguardando 6.2s para kommo...
2025-09-05 20:58:26.232 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:33432 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
⚠️ Rate Limiter: Usando burst para kommo
2025-09-05 20:58:30.470 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Compra com Desconto', 'name': 'Mateus M', 'bill_value': 500.0, 'phone': '558182986181', 'qualification_score': 40, 'tags': ['Compra com Desconto']}}
2025-09-05 20:58:30.470 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
INFO:     10.11.0.4:33432 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
INFO:     127.0.0.1:51334 - "GET /health HTTP/1.1" 200 OK
2025-09-05 20:58:52.123 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Mateus, que bom que retornou. Como já estamos no finalzinho do dia, a agenda do Leon...'
2025-09-05 20:58:52.123 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-09-05 20:58:52.124 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'oi...' -> '<RESPOSTA_FINAL>Mateus, que bom que retornou. Como...'
2025-09-05 20:58:52.124 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Mateus, que bom que retornou. Como já estamos no finalzinho do dia, a agenda do Leon...'
2025-09-05 20:58:54.035 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-09-05 20:58:54.674 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-09-05 20:59:04.839 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Typing enviado para 558182986181 (duração: 4.31s, tamanho: 164)
INFO:     127.0.0.1:51006 - "GET /health HTTP/1.1" 200 OK
2025-09-05 20:59:10.954 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Evolution API - Mensagem de texto enviada para 558182986181 (tamanho: 164, delay: 5.0s)
2025-09-05 20:59:10.955 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-09-05 20:59:10.955 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'oi...' -> 'Mateus, que bom que retornou. Como já estamos no f...'
2025-09-05 20:59:11.646 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:42138 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:34952 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38506 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35158 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35672 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33852 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59228 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42246 - "GET /health HTTP/1.1" 200 OK
2025-09-05 21:03:31.387 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-09-05 21:03:31.388 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:784 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:44370 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-09-05 21:03:31.389 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:44372 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:50814 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34684 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:46818 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40782 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44912 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55782 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41556 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42760 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59196 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44900 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36922 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41118 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47692 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45550 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40056 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43610 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36120 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60222 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48574 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43678 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43924 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49076 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55928 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56334 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35244 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49662 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33276 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39294 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50138 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41594 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57378 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57040 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:44894 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:34978 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36802 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:48282 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58808 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43430 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38718 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56136 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59736 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42230 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39830 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37994 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41638 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39048 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:45366 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59146 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36886 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57522 - "GET /health HTTP/1.1" 200 OK
2025-09-05 21:29:36.492 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead ed59d1e3-ff55-4737-a336-23d2b25d55c5. Tipo: IMMEDIATE_REENGAGEMENT
2025-09-05 21:29:36.495 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
INFO:     127.0.0.1:46738 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32992 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:57526 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:56862 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:36134 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:53218 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     10.11.0.4:53218 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed
INFO:     127.0.0.1:42822 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35658 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:51334 - "GET /webhook/evolution HTTP/1.1" 405 Method Not Allowed