'/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-23 21:38:44.154 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:353 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGOpEH2PMLfFF-b19nbtmwlnvMuJ6Btm0ykHiPtrYEHAw&oe=68B72F0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-23T18:38:44.131Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:49996 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-23 21:38:45.122 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:49996 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 21:38:45.129 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-23 21:38:45.129 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:49996 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-23 21:38:58.807 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 41}
2025-08-23 21:38:59.478 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: a23b5821-09ad-4e0d-9ffb-eee99a45e6d9, Phone: 558182986181
2025-08-23 21:39:00.191 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-23 21:39:00.191 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-23 21:39:01.035 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 21:39:01.035 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 21:39:01.036 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 21:39:01.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 21:39:01.046 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 21:39:01.046 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 21:39:01.046 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 21:39:01.047 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 21:39:01.047 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 21:39:01.047 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 21:39:01.048 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 21:39:01.050 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 21:39:01.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 21:39:01.864 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 21:39:02.594 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 21:39:03.181 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 21:39:03.226 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 21:39:03.227 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 21:39:03.227 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 23, 'lead_name': None}
2025-08-23 21:39:03.228 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-23 21:39:03.228 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): oi, quero reagendar para as 10h por favor...
2025-08-23 21:39:03.462 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 24, 'updated_at': '2025-08-23T21:39:03.233504'}}
2025-08-23 21:39:03.462 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Intenção 'reagendamento' detectada. Usando fluxo de bypass.
2025-08-23 21:39:03.911 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Tool executado: calendar.reschedule_meeting
2025-08-23 21:39:04.159 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Desculpe, tive um problema ao processar sua solicitação: Não consegui entender a nova data e hora. P...
2025-08-23 21:39:04.159 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-23 21:39:04.160 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 219 chars
INFO:     127.0.0.1:48084 - "GET /health HTTP/1.1" 200 OK