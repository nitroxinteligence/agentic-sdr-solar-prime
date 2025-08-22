INFO:     10.11.0.4:45362 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 16:50:25.737 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 16:50:25.738 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 16:50:25.738 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para audioMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 16:50:25.738 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/v/t62.7117-24/538271982_2...
2025-08-22 16:50:25.738 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: audio)
2025-08-22 16:50:25.755 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:50:25.756 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:50:25.748Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:45362 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:50:26.059 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:50:26.059 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:50:26.051Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:45362 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:50:26.193 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 4490 bytes
2025-08-22 16:50:26.193 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 16:50:26.193 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 16:50:26.195 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 16:50:26.196 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 4478 bytes
2025-08-22 16:50:26.196 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 4478 bytes
2025-08-22 16:50:26.197 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido audio de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'audio'}
2025-08-22 16:50:26.691 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45362 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:50:26.700 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:50:26.701 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:45362 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:50:41.336 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-22 16:50:42.795 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 829c2529-dff3-4cfe-9027-42619ff6aacf, Phone: 558182986181
2025-08-22 16:50:44.874 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 16:50:44.874 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 16:50:45.912 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 16:50:45.912 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 16:50:45.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 16:50:45.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 16:50:45.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 16:50:45.913 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 16:50:45.914 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 16:50:45.914 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 16:50:45.914 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 16:50:45.914 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 16:50:45.917 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 16:50:46.179 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 16:50:46.794 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 16:50:47.363 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
INFO:     127.0.0.1:45788 - "GET /health HTTP/1.1" 200 OK
2025-08-22 16:50:48.406 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 16:50:48.439 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 16:50:48.440 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 16:50:48.441 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 5, 'lead_name': None}
2025-08-22 16:50:48.441 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 16:50:48.441 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): ...
2025-08-22 16:50:48.443 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 📎 Mídia do tipo image/jpeg adicionada de forma genérica ao prompt.
2025-08-22 16:50:49.245 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 🎤 Áudio transcrito: 22 caracteres
2025-08-22 16:50:49.250 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Erro: 'list' object has no attribute 'lower' | Data: {'component': 'AgenticSDRStateless'}
2025-08-22 16:50:49.251 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: Traceback: Traceback (most recent call last):
  File "/app/app/agents/agentic_sdr_stateless.py", line 173, in process_message
    new_lead_info = self.lead_manager.extract_lead_info(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/core/lead_manager.py", line 68, in extract_lead_info
    content = msg.get("content", "").lower()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'list' object has no attribute 'lower'
 | Data: {'component': 'AgenticSDRStateless'}