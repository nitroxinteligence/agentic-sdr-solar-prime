2025-08-22 17:12:28.313 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 17:12:28.313 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 17:12:28.313 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para audioMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 17:12:28.313 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/v/t62.7117-24/536937209_1...
2025-08-22 17:12:28.313 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: audio)
2025-08-22 17:12:28.616 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 17:12:28.617 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T14:12:28.610Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:50594 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 17:12:28.778 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 5994 bytes
2025-08-22 17:12:28.778 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 17:12:28.778 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 17:12:28.781 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 17:12:28.782 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 5978 bytes
2025-08-22 17:12:28.783 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 5978 bytes
2025-08-22 17:12:28.783 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido audio de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'audio'}
2025-08-22 17:12:29.151 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:50594 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 17:12:29.156 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 17:12:29.156 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:50594 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 17:12:43.917 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-22 17:12:44.602 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 829c2529-dff3-4cfe-9027-42619ff6aacf, Phone: 558182986181
2025-08-22 17:12:45.320 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 17:12:45.320 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 17:12:46.163 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 17:12:46.163 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 17:12:46.164 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 17:12:46.164 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 17:12:46.165 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 17:12:46.165 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 17:12:46.165 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 17:12:46.166 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 17:12:46.166 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 17:12:46.166 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 17:12:46.169 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 17:12:46.456 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 17:12:47.094 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 17:12:47.760 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 17:12:48.965 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 17:12:48.994 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 17:12:48.995 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 17:12:48.995 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 13, 'lead_name': None}
2025-08-22 17:12:48.995 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 17:12:48.995 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): ...
2025-08-22 17:12:48.996 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 📎 Mídia do tipo image/jpeg adicionada de forma genérica ao prompt.
2025-08-22 17:12:49.973 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 🎤 Áudio transcrito: 21 caracteres
2025-08-22 17:12:50.220 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 14, 'updated_at': '2025-08-22T17:12:49.977999'}}
2025-08-22 17:12:50.222 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Gemini: Erro na API: module 'google.generativeai.types' has no attribute 'Part' | Data: {'component': 'Gemini'}
2025-08-22 17:12:50.462 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Erro Gemini: module 'google.generativeai.types' has no attribute 'Part'...
2025-08-22 17:12:50.463 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-22 17:12:50.463 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 104 chars
INFO:     127.0.0.1:39874 - "GET /health HTTP/1.1" 200 OK
2025-08-22 17:12:54.018 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.3, 'message_length': 71, 'recipient': '558182986181', 'type': 'typing'}
2025-08-22 17:12:59.457 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 71, 'delay_used': 2.27, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 17:12:59.467 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 17:12:59.467 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:55930 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 17:13:00.234 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55930 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK