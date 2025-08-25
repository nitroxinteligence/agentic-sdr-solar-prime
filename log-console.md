=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
      "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
    }
  ],
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T16:56:32.822Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 19:56:33.306 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 19:56:33.306 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 19:56:33.306 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: [
  {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  }
]
2025-08-25 19:56:33.306 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 19:56:33.307 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 19:56:33.308 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 19:56:33.308 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 19:56:33.308 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 19:56:33.308 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:56:33.898 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:53322 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 19:56:33.899 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 3fcc96a6-42ce-4ff2-9b98-2b8c28a2a85f, Nome: 'Mateus M'
2025-08-25 19:56:33.900 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: a7914686-490e-4944-bd0e-10a7c177e27e
2025-08-25 19:56:33.900 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a7914686-490e-4944-bd0e-10a7c177e27e, Phone: 558182986181
2025-08-25 19:56:33.901 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 19:56:33.901 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:56:33.901 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  },
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T16:56:32.849Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 19:56:33.901 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - campo 'remoteJid' RAW: '558182986181@s.whatsapp.net'
2025-08-25 19:56:33.902 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 0 - telefone extraído de remoteJid: '558182986181'
2025-08-25 19:56:33.903 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 19:56:33.903 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '558182986181' (válido: True)
2025-08-25 19:56:33.903 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 19:56:33.903 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:56:34.129 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Lead 558182986181 já possui nome 'Mateus M', não sobrescrevendo com 'Mateus M'
INFO:     10.11.0.4:51496 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 19:56:34.792 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:53322 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 19:56:34.793 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 19:56:34.794 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:667 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:51510 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 19:56:34.795 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51520 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 19:56:34.796 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51538 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 19:56:34.798 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 19:56:34.798 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:667 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:51532 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 19:56:34.799 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 19:56:34.799 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:667 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:51544 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 19:56:34.800 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 19:56:34.800 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 19:56:34.800 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 19:56:36.455 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 19:56:37.147 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 19:56:37.834 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 19:56:39.308 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 19:56:39.308 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 19:56:39.309 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 19:56:39.318 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 19:56:39.318 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 19:56:39.318 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 19:56:39.319 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 19:56:39.319 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 19:56:39.319 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 19:56:39.319 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 19:56:39.319 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 19:56:39.322 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 19:56:39.566 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 19:56:40.128 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 19:56:40.715 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 19:56:41.343 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 19:56:41.375 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 19:56:41.376 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 19:56:41.376 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 9, 'lead_name': 'Mateus M'}
2025-08-25 19:56:41.376 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 19:56:41.376 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'recebo nao...'
2025-08-25 19:56:41.377 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 19:56:41.378 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 10 mensagens
2025-08-25 19:56:41.378 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 19:56:41.380 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'Mateus M', Valor: None
2025-08-25 19:56:41.380 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 19:56:41.380 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: Mateus M, Histórico: 10 msgs
2025-08-25 19:56:41.380 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 19:56:41.380 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
🚫 Rate Limiter: Bloqueando kommo. Aguarde 4.0s
⏳ Rate Limiter: Aguardando 5.0s para kommo...
⚠️ Rate Limiter: Usando burst para kommo
INFO:     10.11.0.4:50346 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 19:56:47.047 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'chosen_flow': 'Usina Investimento', 'name': 'Mateus M', 'phone': '558182986181', 'qualification_score': 20, 'tags': ['Usina Investimento']}}
2025-08-25 19:56:47.047 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
INFO:     127.0.0.1:44044 - "GET /health HTTP/1.1" 200 OK
2025-08-25 19:57:01.268 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Entendi! Hoje você paga em média R$3.000 na sua conta, certo? Ótimo, hoje temos uma ...'
2025-08-25 19:57:01.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 19:57:01.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'recebo nao...' -> '<RESPOSTA_FINAL>Entendi! Hoje você paga em média R...'
2025-08-25 19:57:01.269 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Entendi! Hoje você paga em média R$3.000 na sua conta, certo? Ótimo, hoje temos uma ...'
2025-08-25 19:57:01.980 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 19:57:02.202 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 19:57:12.630 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 En