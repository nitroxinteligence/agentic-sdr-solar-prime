# FOLLOW-UP DE REENGAJAMENTO NAO ESTÁ FUNCIONANDO, ATÉ EXECUTA COMO VOCE PODE VER NO LOG ABAIXO, PORÉM ELE NAO ENVIA A MENSAGEM PARA O USUÁRIO NO WHATSAPP:

2025-08-22 09:47:22.382 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: b4acc30b-72fb-4acf-b82a-fac02e2f99ce
2025-08-22 09:47:22.382 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298...
2025-08-22 09:47:22.383 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Follow-up 30min agendado: 55818298...
INFO:     127.0.0.1:59190 - "GET /health HTTP/1.1" 200 OK
2025-08-22 09:47:34.122 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 1 follow-ups pendentes encontrados.
2025-08-22 09:47:34.727 | ERROR    | app.services.followup_worker:_process_task:63 | Task de follow-up sem ID, descartando.
2025-08-22 09:47:35.308 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up b4acc30b-72fb-4acf-b82a-fac02e2f99ce enfileirado.

2025-08-22 10:47:25.168 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 96febbd6-a7a4-4c05-afbe-1278d8c67c38
2025-08-22 10:47:25.170 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298...
2025-08-22 10:47:25.404 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 1 follow-ups pendentes encontrados.
2025-08-22 10:47:25.981 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🚫 Limite de follow-ups atingido para o lead 2a9e74ec-ba90-46f5-b665-cf4fdc313d8c.
2025-08-22 10:47:26.199 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Follow-up 30min agendado: 55818298...

---

# AQUI ESTÁ O MOMENTO EM QUE O MULTIMODAL INICIA, PORÉM O AGENTE ALUCINA COMPLETAMENTE:

INFO:     10.11.0.4:43262 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 08:16:34.932 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 08:16:34.933 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 08:16:34.933 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para imageMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 08:16:34.933 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/o1/v/t24/f2/m234/AQNSjF7B...
2025-08-22 08:16:34.933 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: image)
2025-08-22 08:16:35.595 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 08:16:35.596 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QELLBsfa_ene0DPmXeVh_qYfgbKrsCwGt2R0_2e2yWkHA&oe=68B534CD&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T05:16:35.135Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:43262 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 08:16:37.070 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 2092314 bytes
2025-08-22 08:16:37.070 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 08:16:37.070 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 08:16:37.071 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 08:16:37.081 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 2092291 bytes
2025-08-22 08:16:37.081 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 2092291 bytes
2025-08-22 08:16:37.090 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido image de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'image'}
2025-08-22 08:16:52.223 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-22 08:16:54.000 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: bef7ae0a-2b39-418f-83d7-a8b00005188a, Phone: 558182986181
2025-08-22 08:16:58.337 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 08:16:58.338 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 08:17:01.264 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 08:17:01.265 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 08:17:01.265 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 08:17:01.265 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 08:17:01.265 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 08:17:01.266 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 08:17:01.266 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 08:17:01.266 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 08:17:01.266 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 08:17:01.267 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 08:17:01.270 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 08:17:01.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
INFO:     127.0.0.1:54552 - "GET /health HTTP/1.1" 200 OK
2025-08-22 08:17:02.568 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 08:17:03.534 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 08:17:04.284 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 08:17:04.312 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 08:17:04.312 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 08:17:04.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 29, 'lead_name': 'Mateus'}
2025-08-22 08:17:04.313 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 08:17:04.313 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): ...
2025-08-22 08:17:06.495 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 📸 OCR extraiu 463 caracteres
2025-08-22 08:17:06.496 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 ✅ Imagem processada: 2160x3840
2025-08-22 08:17:06.498 | INFO     | app.utils.logger:log_with_emoji:75 | 📱 📎 Mídia processada com sucesso
2025-08-22 08:17:06.715 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Estado do lead sincronizado com o banco de dados. | Data: {'changes': {'processed_message_count': 30, 'updated_at': '2025-08-22T08:17:06.501186'}}
2025-08-22 08:17:06.716 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 📊 Analisando estágio - Msgs: 30 (👤 16 user, 🤖 14 assistant)
2025-08-22 08:17:09.846 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Mateus, infelizmente não consegui extrair o valor da sua conta de luz. Para prosseguirmos com o agen...
2025-08-22 08:17:09.846 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-22 08:17:09.847 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 274 chars
2025-08-22 08:17:13.816 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.03, 'message_length': 70, 'recipient': '558182986181', 'type': 'typing'}
2025-08-22 08:17:18.749 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 70, 'delay_used': 2.51, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 08:17:18.756 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 08:17:18.756 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:35264 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 08:17:19.839 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35264 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 08:17:23.757 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.35, 'message_length': 170, 'recipient': '558182986181', 'type': 'typing'}
2025-08-22 08:17:30.017 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 170, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 08:17:30.233 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 08:17:30.233 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:57078 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 08:17:30.873 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57078 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK

---

# ERRO AO PROCESSAR ÁUDIOS:

 '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 16:15:24.048 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 16:15:24.048 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 16:15:24.050 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para audioMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 16:15:24.052 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/v/t62.7117-24/534910767_1...
2025-08-22 16:15:24.053 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: image)
2025-08-22 16:15:24.243 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 11018 bytes
2025-08-22 16:15:24.243 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 16:15:24.245 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 16:15:24.271 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 16:15:24.277 | WARNING  | app.integrations.evolution:decrypt_whatsapp_media:793 | MAC não corresponde - esperado: 7989a3caba79ff890a6d, calculado: b1e180f3496e5379d6da
2025-08-22 16:15:24.294 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 11008 bytes
2025-08-22 16:15:24.294 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 11008 bytes
2025-08-22 16:15:24.297 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido audio de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'audio'}
2025-08-22 16:15:24.298 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:15:24.298 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:15:24.255Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:15:25.597 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:15:25.608 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:15:25.609 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:15:25.618 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:15:25.624 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-22 16:15:25.625 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:57026 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-22 16:15:39.785 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-22 16:15:40.478 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'table': 'leads', 'count': 1}
2025-08-22 16:15:40.703 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 829c2529-dff3-4cfe-9027-42619ff6aacf, Phone: 558182986181
2025-08-22 16:15:41.764 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-22 16:15:41.765 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-22 16:15:42.287 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-22 16:15:42.288 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-22 16:15:42.331 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-22 16:15:42.332 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-22 16:15:42.332 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-22 16:15:42.357 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-22 16:15:42.358 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-22 16:15:42.359 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-22 16:15:42.360 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-22 16:15:42.361 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-22 16:15:42.692 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-22 16:15:42.798 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-22 16:15:43.114 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-22 16:15:43.881 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-22 16:15:44.508 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-22 16:15:45.074 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-22 16:15:45.566 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-22 16:15:45.567 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-22 16:15:45.568 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-22 16:15:45.568 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-22 16:15:45.569 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: Processando (stateless): ...
2025-08-22 16:15:46.251 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Service: Erro ao processar áudio: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.1.1-1+b1 Copyright (c) 2000-2025 the FFmpeg developers
  built with gcc 14 (Debian 14.2.0-19)
  configuration: --prefix=/usr --extra-version=1+b1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --disable-libmfx --disable-omx --enable-gnutls --enable-libaom --enable-libass --enable-libbs2b --enable-libcdio --enable-libcodec2 --enable-libdav1d --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libglslang --enable-libgme --enable-libgsm --enable-libharfbuzz --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzimg --enable-openal --enable-opencl --enable-opengl --disable-sndio --enable-libvpl --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-chromaprint --enable-frei0r --enable-ladspa --enable-libbluray --enable-libcaca --enable-libdvdnav --enable-libdvdread --enable-libjack --enable-libpulse --enable-librabbitmq --enable-librist --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libx264 --enable-libzmq --enable-libzvbi --enable-lv2 --enable-sdl2 --enable-libplacebo --enable-librav1e --enable-pocketsphinx --enable-librsvg --enable-libjxl --enable-shared
  libavutil      59. 39.100 / 59. 39.100
  libavcodec     61. 19.101 / 61. 19.101
  libavformat    61.  7.100 / 61.  7.100
  libavdevice    61.  3.100 / 61.  3.100
  libavfilter    10.  4.100 / 10.  4.100
  libswscale      8.  3.100 /  8.  3.100
  libswresample   5.  3.100 /  5.  3.100
  libpostproc    58.  3.100 / 58.  3.100
[cache @ 0x623eddce0840] Statistics, cache hits:0 cache misses:1
[in#0 @ 0x623eddcdff00] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

2025-08-22 16:15:46.254 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-22 16:15:46.257 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 2274 chars
2025-08-22 16:15:50.343 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 1.77, 'message_length': 41, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:60494 - "GET /health HTTP/1.1" 200 OK
2025-08-22 16:15:54.030 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 41, 'delay_used': 2.9, 'recipient': '558182986181', 'type': 'text'}
2025-08-22 16:15:54.038 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-22 16:15:54.038 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:352 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:53566 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-22 16:15:54.841 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:53566 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-22 16:15:55.803 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.43, 'message_length': 187, 'recipient': '558182986181', 'type': 'typing'}

---

# PROCESSANDO DOCUMENTOS:

2025-08-22 16:16:46.342 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:38692 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-22 16:16:46.343 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-22 16:16:46.343 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-22 16:16:46.344 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Webhook para documentMessage não continha 'media' ou 'body'. Tentando download como fallback.
2025-08-22 16:16:46.345 | INFO     | app.integrations.evolution:download_media:835 | Baixando mídia de: https://mmg.whatsapp.net/v/t62.7119-24/537821557_1...
2025-08-22 16:16:46.345 | INFO     | app.integrations.evolution:download_media:837 | MediaKey presente - mídia será descriptografada (tipo: image)
2025-08-22 16:16:46.439 | INFO     | app.integrations.evolution:download_media:850 | Mídia baixada com sucesso: 76506 bytes
2025-08-22 16:16:46.440 | INFO     | app.integrations.evolution:download_media:854 | Iniciando descriptografia da mídia...
2025-08-22 16:16:46.440 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:763 | MediaKey decodificada: 32 bytes
2025-08-22 16:16:46.440 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:780 | IV: 16 bytes, Cipher Key: 32 bytes, MAC Key: 32 bytes
2025-08-22 16:16:46.445 | WARNING  | app.integrations.evolution:decrypt_whatsapp_media:793 | MAC não corresponde - esperado: 89d4d8aec475c97292e8, calculado: 684c7585fb25ee69b9d8
2025-08-22 16:16:46.448 | INFO     | app.integrations.evolution:decrypt_whatsapp_media:812 | Mídia descriptografada com sucesso: 76496 bytes
2025-08-22 16:16:46.448 | INFO     | app.integrations.evolution:download_media:861 | Mídia descriptografada: 76496 bytes
2025-08-22 16:16:46.453 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido document de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'document'}
2025-08-22 16:16:46.540 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-22 16:16:46.540 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:350 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHi_12aJLqPrwdylfV4OxcjY3CbWuF1h8LXnYZirIxU7A&oe=68B5A54D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-22T13:16:46.532Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:38692 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-22 16:16:47.481 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}