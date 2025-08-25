2025-08-25 20:09:30.873 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-25 20:09:30.898 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-25 20:09:30.905 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-25 20:09:30.906 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto | Data: {'data': {'url': 'redis_redis:6379'}}
2025-08-25 20:09:31.312 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-25 20:09:31.313 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=10.0s, max=10)
2025-08-25 20:09:31.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'data': {'timeout': '10.0s'}}
2025-08-25 20:09:31.313 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=250, smart=ativada)
2025-08-25 20:09:31.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'data': {'max_length': 250}}
2025-08-25 20:09:31.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:09:31.328 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:09:31.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversation Monitor pronto
2025-08-25 20:09:31.329 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'data': {'modules': 'Core + Services'}}
2025-08-25 20:09:31.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Service pronto
2025-08-25 20:09:31.339 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-25 20:09:31.350 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:09:31.351 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:09:31.351 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:09:31.361 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:09:31.362 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:09:31.362 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:09:31.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:09:31.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:09:31.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:09:31.363 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:09:31.364 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:09:31.542 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-25 20:09:31.547 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:09:32.176 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:09:33.315 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:09:33.887 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:09:34.452 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:09:34.502 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:09:34.503 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:09:34.504 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'data': {'status': 'sistema pronto'}}
2025-08-25 20:09:34.504 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services pronto
2025-08-25 20:09:34.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-25 20:09:34.515 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:09:34.515 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:09:34.516 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:09:34.526 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:09:34.526 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:09:34.526 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:09:34.527 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:09:34.527 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:09:34.527 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:09:34.527 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:09:34.528 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:09:34.532 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:09:35.125 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:09:35.882 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:09:36.444 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:09:37.009 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:09:37.042 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:09:37.043 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
2025-08-25 20:09:37.043 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 6144.5}
INFO:     127.0.0.1:59150 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:09:43.923 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35296 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 20:09:44.379 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 20:09:44.379 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:691 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T17:09:39.346Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35296 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 20:09:44.471 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:35296 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 20:09:44.472 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 20:09:44.472 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 20:09:44.472 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'nao entendi?', 'sender': '558182986181', 'type': 'text'}
2025-08-25 20:09:44.474 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 12}
2025-08-25 20:09:44.474 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'nao entendi?...', ID: 3AB9B96C25D1489CB22F
2025-08-25 20:09:45.498 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:09:45.502 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:09:45.502 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558182986181@s.whatsapp.net",
      "pushName": "Mateus M",
      "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T17:09:39.607Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 20:09:45.502 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:09:45.503 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 20:09:45.504 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:09:46.109 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:35296 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:09:46.110 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f, Nome: 'Mateus M'
2025-08-25 20:09:46.111 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: a7914686-490e-4944-bd0e-10a7c177e27e
2025-08-25 20:09:46.111 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a7914686-490e-4944-bd0e-10a7c177e27e, Phone: 558182986181
2025-08-25 20:09:46.111 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:09:46.111 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.6s)
INFO:     10.11.0.4:35304 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:09:47.175 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:09:47.176 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:695 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:35318 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:09:47.178 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35334 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:09:47.179 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:09:47.179 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:09:47.179 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 20:09:47.994 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:09:48.529 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:09:49.098 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:09:50.520 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:09:50.520 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:09:50.521 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:09:50.528 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:09:50.528 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:09:50.529 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:09:50.532 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:09:50.819 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:09:51.391 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:09:51.637 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35334 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 20:09:52.013 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:09:52.641 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:09:52.677 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:09:52.678 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:09:52.678 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 13, 'lead_name': 'Mateus M'}
2025-08-25 20:09:52.678 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:09:52.679 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'nao entendi?...'
2025-08-25 20:09:52.680 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:09:52.680 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 14 mensagens
2025-08-25 20:09:52.681 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 20:09:52.683 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: None
2025-08-25 20:09:52.684 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 20:09:52.684 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 14 msgs
2025-08-25 20:09:52.684 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 20:09:52.684 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 4.7s
⏳ Rate Limiter: Aguardando 5.7s para kommo...
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:09:59.080 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
2025-08-25 20:09:59.080 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
INFO:     10.11.0.4:56726 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
INFO:     127.0.0.1:38144 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:10:15.566 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Opa, Mateus, peço desculpas! Isso foi uma falha aqui no meu sistema. Eu já estava ve...'
2025-08-25 20:10:15.567 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 20:10:15.567 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'nao entendi?...' -> '<RESPOSTA_FINAL>Opa, Mateus, peço desculpas! Isso ...'
2025-08-25 20:10:15.567 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Opa, Mateus, peço desculpas! Isso foi uma falha aqui no meu sistema. Eu já estava ve...'
2025-08-25 20:10:16.655 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 20:10:17.246 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 20:10:22.827 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.91, 'message_length': 149, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 20:10:27.814 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 149, 'delay_used': 2.24, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:10:28.770 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:47898 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:10:37.655 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.45, 'message_length': 153, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:48486 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:10:44.183 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 153, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:10:44.184 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 20:10:44.184 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'nao entendi?...' -> 'Opa, Mateus, peço desculpas! Isso foi uma falha aq...'
2025-08-25 20:11:06.225 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55138 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 20:11:08.800 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 20:11:08.800 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:691 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T17:11:08.792Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:55138 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 20:11:08.816 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:55138 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 20:11:08.817 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 20:11:08.818 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 20:11:08.818 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'sim, eai?', 'sender': '558182986181', 'type': 'text'}
2025-08-25 20:11:08.820 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 9}
2025-08-25 20:11:08.821 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'sim, eai?...', ID: 3A72F734C8AD519206E0
2025-08-25 20:11:09.563 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558182986181@s.whatsapp.net",
      "pushName": "Mateus M",
      "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T17:11:09.052Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:11:09.564 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 20:11:09.565 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:11:09.812 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:55138 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:11:09.813 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f, Nome: 'Mateus M'
2025-08-25 20:11:09.814 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: a7914686-490e-4944-bd0e-10a7c177e27e
2025-08-25 20:11:09.814 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a7914686-490e-4944-bd0e-10a7c177e27e, Phone: 558182986181
2025-08-25 20:11:09.814 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:11:09.814 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.3s)
INFO:     10.11.0.4:55144 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:11:10.904 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55144 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:11:10.905 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:11:10.905 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:695 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:55138 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:11:10.906 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55148 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:11:10.907 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:11:10.907 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:695 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:55162 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:11:10.908 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:11:10.908 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:11:10.908 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
INFO:     127.0.0.1:60126 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:11:11.721 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:11:12.350 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:11:12.899 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:11:13.947 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:11:13.948 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:11:13.948 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:11:13.964 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:11:13.965 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:11:13.965 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:11:13.966 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:11:13.966 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:11:13.966 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:11:13.966 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:11:13.966 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:11:13.969 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:11:14.224 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:11:14.779 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:11:15.353 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:11:16.190 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:11:16.216 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:11:16.217 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:11:16.218 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 15, 'lead_name': 'Mateus M'}
2025-08-25 20:11:16.218 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:11:16.218 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'sim, eai?...'
2025-08-25 20:11:16.219 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:11:16.219 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 16 mensagens
2025-08-25 20:11:16.220 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'positivo', 'score': 0.2, 'confidence': 0.7}, Urgência: normal
2025-08-25 20:11:16.222 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: None
2025-08-25 20:11:16.222 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 20:11:16.222 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 16 msgs
2025-08-25 20:11:16.222 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 20:11:16.223 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 4.9s
⏳ Rate Limiter: Aguardando 5.9s para kommo...
⚠️ Rate Limiter: Usando burst para kommo
INFO:     10.11.0.4:40096 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 20:11:22.815 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
2025-08-25 20:11:22.816 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
2025-08-25 20:11:26.934 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: 'Mateus, qual daqueles horários que te passei fica melhor para você? Só para lembrar: amanhã (terça) ...'
2025-08-25 20:11:26.935 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 20:11:26.935 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-25 20:11:26.936 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 223 chars
2025-08-25 20:11:26.936 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'sim, eai?...' -> '<RESPOSTA_FINAL>Mateus, qual daqueles horários que...'
2025-08-25 20:11:26.936 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Mateus, qual daqueles horários que te passei fica melhor para você? Só para lembrar:...'
2025-08-25 20:11:28.249 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 20:11:28.482 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 20:11:38.517 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.46, 'message_length': 190, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:56844 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:11:45.469 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 190, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:11:45.470 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 20:11:45.470 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'sim, eai?...' -> 'Mateus, qual daqueles horários que te passei fica ...'
2025-08-25 20:11:46.280 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55790 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:12:03.547 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45316 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 20:12:06.931 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 20:12:06.931 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:691 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T17:12:06.921Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:45316 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 20:12:06.955 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:45316 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 20:12:06.956 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 20:12:06.956 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 20:12:06.956 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'pode ser amanha as 10h', 'sender': '558182986181', 'type': 'text'}
2025-08-25 20:12:06.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 22}
2025-08-25 20:12:06.958 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'pode ser amanha as 10h...', ID: 3A83D3AEB857DB6D9D92
2025-08-25 20:12:07.645 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558182986181@s.whatsapp.net",
      "pushName": "Mateus M",
      "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T17:12:07.174Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-08-25 20:12:07.646 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 20:12:07.647 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:12:07.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:45316 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:12:07.864 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f, Nome: 'Mateus M'
2025-08-25 20:12:07.865 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: a7914686-490e-4944-bd0e-10a7c177e27e
2025-08-25 20:12:07.865 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a7914686-490e-4944-bd0e-10a7c177e27e, Phone: 558182986181
2025-08-25 20:12:07.866 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:12:07.866 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.2s)
INFO:     10.11.0.4:45326 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:12:08.942 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45326 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:12:08.942 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:12:08.943 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:695 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:45316 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:12:08.944 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:12:08.944 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:12:08.944 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 20:12:10.059 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:12:10.669 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:12:11.665 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
INFO:     127.0.0.1:42138 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:12:12.706 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:12:12.707 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:12:12.707 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:12:12.714 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:12:12.714 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:12:12.714 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:12:12.715 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:12:12.715 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:12:12.715 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:12:12.715 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:12:12.715 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:12:12.718 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:12:12.964 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:12:14.020 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:12:15.119 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:12:15.675 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:12:15.709 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:12:15.710 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:12:15.710 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 17, 'lead_name': 'Mateus M'}
2025-08-25 20:12:15.711 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:12:15.711 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'pode ser amanha as 10h...'
2025-08-25 20:12:15.712 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:12:15.713 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 18 mensagens
2025-08-25 20:12:15.713 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 20:12:15.715 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: None
2025-08-25 20:12:15.716 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 20:12:15.716 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 18 msgs
2025-08-25 20:12:15.716 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 20:12:15.716 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 3.5s
⏳ Rate Limiter: Aguardando 4.5s para kommo...
⚠️ Rate Limiter: Usando burst para kommo
INFO:     10.11.0.4:40712 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 20:12:20.830 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
2025-08-25 20:12:20.830 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
2025-08-25 20:12:25.209 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Perfeito, Mateus! Combinado para amanhã, terça-feira, às 10h. Para eu te enviar o co...'
2025-08-25 20:12:25.210 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 20:12:25.210 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'pode ser amanha as 10h...' -> '<RESPOSTA_FINAL>Perfeito, Mateus! Combinado para a...'
2025-08-25 20:12:25.210 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Perfeito, Mateus! Combinado para amanhã, terça-feira, às 10h. Para eu te enviar o co...'
2025-08-25 20:12:25.898 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 20:12:26.118 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 20:12:34.518 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.19, 'message_length': 146, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 20:12:39.800 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 146, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:12:39.800 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 20:12:39.801 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'pode ser amanha as 10h...' -> 'Perfeito, Mateus! Combinado para amanhã, terça-fei...'
2025-08-25 20:12:40.618 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:47024 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:56504 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:12:59.239 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45078 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 20:13:02.221 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 20:13:02.222 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:691 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T17:13:02.214Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:45078 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 20:13:02.244 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:45078 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 20:13:02.244 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 20:13:02.244 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 20:13:02.245 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'matheuscdsgn@gmail.com', 'sender': '558182986181', 'type': 'text'}
2025-08-25 20:13:02.246 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 22}
2025-08-25 20:13:02.246 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'matheuscdsgn@gmail.com...', ID: 3AFD39E6CD314730428A
2025-08-25 20:13:02.954 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:13:02.954 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:13:02.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": [
    {
      "remoteJid": "558182986181@s.whatsapp.net",
      "pushName": "Mateus M",
      "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T17:13:02.466Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 20:13:02.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 20:13:02.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 20:13:02.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-08-25 20:13:02.955 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 20:13:02.956 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 20:13:02.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 20:13:02.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 20:13:02.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 20:13:02.957 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 20:13:03.181 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:45078 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:13:03.182 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f, Nome: 'Mateus M'
2025-08-25 20:13:03.182 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: a7914686-490e-4944-bd0e-10a7c177e27e
2025-08-25 20:13:03.182 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a7914686-490e-4944-bd0e-10a7c177e27e, Phone: 558182986181
2025-08-25 20:13:03.183 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:13:03.183 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.2s)
INFO:     10.11.0.4:52012 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:13:04.262 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52012 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:13:04.263 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:13:04.263 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:695 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:45078 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:13:04.265 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:13:04.265 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:13:04.265 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 20:13:05.076 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:13:05.789 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:13:06.420 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:13:07.546 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:13:07.546 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:13:07.547 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:13:07.554 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:13:07.554 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:13:07.554 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:13:07.555 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:13:07.555 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:13:07.555 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:13:07.555 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:13:07.555 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:13:07.558 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:13:07.790 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:13:08.576 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:13:09.140 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:13:09.675 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:13:09.701 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:13:09.702 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:13:09.702 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 19, 'lead_name': 'Mateus M'}
2025-08-25 20:13:09.702 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:13:09.702 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'matheuscdsgn@gmail.com...'
2025-08-25 20:13:09.704 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:13:09.704 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 20 mensagens
2025-08-25 20:13:09.705 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 20:13:09.707 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: None
2025-08-25 20:13:09.708 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Detectadas mudanças no lead 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f. Sincronizando com o DB. | Data: {'changes': {'email': 'matheuscdsgn@gmail.com', 'qualification_score': 25}}
2025-08-25 20:13:09.928 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f atualizado no Supabase.
2025-08-25 20:13:09.928 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 20:13:09.929 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 20 msgs
2025-08-25 20:13:09.929 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 20:13:09.929 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 25, 'tags': ['Usina Investimento']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 4.6s
⏳ Rate Limiter: Aguardando 5.6s para kommo...
INFO:     127.0.0.1:39336 - "GET /health HTTP/1.1" 200 OK
⚠️ Rate Limiter: Usando burst para kommo
INFO:     10.11.0.4:43702 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 20:13:16.080 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 25, 'tags': ['Usina Investimento']}}
2025-08-25 20:13:16.080 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
2025-08-25 20:13:20.463 | INFO     | app.utils.logger:log_with_emoji:75 | 📅 Verificando disponibilidade interna para 2025-08-26 10:00...
2025-08-25 20:13:20.679 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Horário 10:00 está livre.
2025-08-25 20:13:21.634 | INFO     | app.integrations.supabase_client:create_lead_qualification:522 | ✅ Qualificação criada para lead 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f
2025-08-25 20:13:21.634 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Registro de qualificação criado para o evento: t781v7elq20m5c3h89pmd55dso
2025-08-25 20:13:21.634 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Workflow pós-agendamento executado com as devidas tratativas de erro.
2025-08-25 20:13:22.092 | INFO     | app.integrations.supabase_client:create_follow_up:342 | Follow-up criado: 3256bbf1-7a22-40fd-96e9-a77c584e664a
2025-08-25 20:13:22.092 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado para 558182986181 em 24h
2025-08-25 20:13:22.092 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 Lembrete de 24h agendado para Mateus M.
2025-08-25 20:13:22.562 | INFO     | app.integrations.supabase_client:create_follow_up:342 | Follow-up criado: ae820a31-5ec8-4609-b9a9-cb57cb2baaa3
2025-08-25 20:13:22.562 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado para 558182986181 em 2h
2025-08-25 20:13:22.562 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 Lembrete de 2h agendado para Mateus M.
2025-08-25 20:13:22.562 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Tool executado: calendar.schedule_meeting
2025-08-25 20:13:30.299 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Prontinho, Mateus! Reunião agendada com sucesso para amanhã, terça-feira (26/08), às...'
2025-08-25 20:13:30.300 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 20:13:30.300 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'matheuscdsgn@gmail.com...' -> '<RESPOSTA_FINAL>Prontinho, Mateus! Reunião agendad...'
2025-08-25 20:13:30.300 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Prontinho, Mateus! Reunião agendada com sucesso para amanhã, terça-feira (26/08), às...'
2025-08-25 20:13:31.014 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 20:13:31.243 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
INFO:     127.0.0.1:56762 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:13:42.634 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 5.43, 'message_length': 223, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 20:13:51.591 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 223, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 20:13:51.591 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 20:13:51.591 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'matheuscdsgn@gmail.com...' -> 'Prontinho, Mateus! Reunião agendada com sucesso pa...'
2025-08-25 20:13:52.670 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:42648 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK