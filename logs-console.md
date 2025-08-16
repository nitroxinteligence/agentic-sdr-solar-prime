genticSDR...
2025-08-16 18:07:12.549 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 18:07:12.549 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 18:07:12.549 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 18:07:12.550 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 18:07:12.550 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 18:07:12.550 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 18:07:12.550 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 18:07:12.551 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 18:07:12.551 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 18:07:12.559 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 18:07:12.559 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 18:07:12.560 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 18:07:12.560 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 18:07:12.560 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 18:07:12.560 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 18:07:12.560 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 89, 'lead_name': 'Mateus'}
2025-08-16 18:07:12.561 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=e012388d-bea3-4362-9cd2-37ee07076dbb para phone=558182986181
2025-08-16 18:07:12.561 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: e012388d-bea3-4362-9cd2-37ee07076dbb
2025-08-16 18:07:13.292 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 18:07:13.570 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 18:07:13.822 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 18:07:14.176 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-16 18:07:14.177 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): ok...
2025-08-16 18:07:14.829 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 18:07:14.830 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 90 (👤 46 user, 🤖 44 assistant)
2025-08-16 18:07:14.831 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 18:07:14.831 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 18:07:14.832 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-16 18:07:14.832 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'boa noite! tudo bem? me chamo helen vieira, sou co...'
2025-08-16 18:07:14.832 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-16 18:07:14.832 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-16 18:07:14.832 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-16 18:07:14.835 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '0.000', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 18:07:14.835 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 18:07:14.837 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 18:07:15.241 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 18:07:15.242 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-16 18:07:20.850 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 18:07:21.111 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 18:07:21.112 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Service: ⚠️ Tentativa de agendar no sábado
2025-08-16 18:07:21.112 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Tool executado: calendar.schedule_meeting
INFO:     127.0.0.1:39132 - "GET /health HTTP/1.1" 200 OK
2025-08-16 18:07:27.041 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 18:07:27.042 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: ```xml
<RESPOSTA_FINAL>
Opa, Mateus! Que arretado que você quer agendar! O Leonardo não atende nos f...
2025-08-16 18:07:27.042 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=358, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>
Opa, Mateus! Que arretado que você quer agendar! O Leonardo não atende nos finais de semana, só de segunda a sexta, das 8h às 17h. Mas já anotei seu interesse aqui. 😉 Me diz um
2025-08-16 18:07:27.043 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=358, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>
Opa, Mateus! Que arretado que você quer agendar! O Leonardo não atende nos finais de semana, só de segunda a sexta, das 8h às 17h. Mas já anotei seu interesse aqui. 😉 Me diz um
2025-08-16 18:07:27.043 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Opa, Mateus! Que arretado que você quer agendar! O Leonardo não atende nos finais de semana, só de segunda a sexta, das 8h às 17h. Mas já anotei seu interesse aqui. Me diz uma coisa: qual seria o melhor dia e horário pra você durante a semana? Aí eu já verifico a disponibilidade dele e te confirmo tudinho.
2025-08-16 18:07:27.043 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 307 chars
2025-08-16 18:07:27.054 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem dividida em 2 partes | Data: {'phone': '558182986181', 'original_length': 307}
2025-08-16 18:07:29.949 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.89, 'message_length': 164, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 18:07:37.153 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 164, 'delay_used': 2.67, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:07:37.154 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Opa, Mateus! Que arretado que você quer agendar! O', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:07:37.154 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 1/2 enviado. ID: 3EB03D8377F3DF8254A57084AE4EA0B9EF7409FC
2025-08-16 18:07:37.312 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 18:07:37.312 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:37478 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 18:07:38.232 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:37478 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:07:42.962 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.87, 'message_length': 142, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 18:07:48.080 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 142, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:07:48.080 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Me diz uma coisa: qual seria o melhor dia e horári', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:07:48.080 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 2/2 enviado. ID: 3EB0F52244EE591D5F57C635EDA16E68FE0CA3E5
2025-08-16 18:07:49.159 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 18:07:49.159 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:38324 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 18:07:49.160 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38336 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:07:49.603 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 18:07:49.604 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
INFO:     127.0.0.1:43598 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:52214 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:51298 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37256 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47916 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:55470 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40758 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39994 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:54288 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:36364 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58752 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38398 - "GET /health HTTP/1.1" 200 OK
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38564 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38564 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     10.11.0.4:38554 - "GET /webhook/whatsapp HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:49592 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40082 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40472 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60442 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:35222 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:40560 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:38274 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53724 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:58070 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:33384 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:56408 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:39464 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37770 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47962 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:37268 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41344 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:43740 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:42548 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:32842 - "GET /health HTTP/1.1" 200 OK
2025-08-16 18:23:10.831 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51120 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-16 18:23:16.417 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-16 18:23:16.417 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:23:16.386Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-16 18:23:16.425 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-16 18:23:16.425 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:23:16.416Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-16 18:23:16.448 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-16 18:23:16.450 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'pode ser na segunda-feira entao as 10h pode ser?', 'sender': '558182986181', 'type': 'text'}
2025-08-16 18:23:16.784 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 18:23:16.784 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGoWYKGE4ct4_MAL0NURewmOSPo8zb7lSbsJNalCC8pEQ&oe=68ADF48D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:23:16.777Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 18:23:16.829 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 18:23:16.829 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGoWYKGE4ct4_MAL0NURewmOSPo8zb7lSbsJNalCC8pEQ&oe=68ADF48D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:23:16.823Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 18:23:17.702 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:23:17.715 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 18:23:17.716 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 18:23:17.734 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:23:17.739 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 18:23:17.740 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:49098 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 18:23:31.877 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 48}
2025-08-16 18:23:33.132 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: e012388d-bea3-4362-9cd2-37ee07076dbb, Phone: 558182986181
2025-08-16 18:23:35.427 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 18:23:35.428 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 18:23:35.428 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 18:23:35.429 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 18:23:35.429 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 18:23:35.429 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 18:23:35.429 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 18:23:35.429 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 18:23:35.430 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 18:23:35.430 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 18:23:35.439 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 18:23:35.439 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 18:23:35.439 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 93, 'lead_name': 'Mateus'}
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=e012388d-bea3-4362-9cd2-37ee07076dbb para phone=558182986181
2025-08-16 18:23:35.440 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: e012388d-bea3-4362-9cd2-37ee07076dbb
INFO:     127.0.0.1:51102 - "GET /health HTTP/1.1" 200 OK
2025-08-16 18:23:36.990 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 18:23:37.279 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 18:23:37.543 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 18:23:37.875 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-16 18:23:37.875 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): pode ser na segunda-feira entao as 10h pode ser?...
2025-08-16 18:23:39.674 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 18:23:39.675 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 94 (👤 48 user, 🤖 46 assistant)
2025-08-16 18:23:39.676 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 18:23:39.677 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 18:23:39.677 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-16 18:23:39.677 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'boa noite! tudo bem? me chamo helen vieira, sou co...'
2025-08-16 18:23:39.678 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-16 18:23:39.678 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-16 18:23:39.678 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-16 18:23:39.681 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 BOOST Calendar por contexto de agendamento conversacional
2025-08-16 18:23:39.681 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 BOOST Calendar por conversation_stage avançado
2025-08-16 18:23:39.681 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '1.000', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 18:23:39.682 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '1.000', 'threshold': '0.250', 'reason': 'threshold_dinamico'}
2025-08-16 18:23:39.682 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📅 Data padrão assumida: amanhã
2025-08-16 18:23:39.686 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 18:23:39.956 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 18:23:39.956 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Service: ⚠️ Tentativa de agendar no domingo
2025-08-16 18:23:39.957 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 18:23:39.957 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 18:23:40.383 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 18:23:40.383 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-16 18:23:46.327 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 18:23:46.327 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: ```xml
<RESPOSTA_FINAL>Que massa, Mateus! Segunda-feira às 10h está perfeito! 😉 Vou agendar agora me...
2025-08-16 18:23:46.327 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=289, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>Que massa, Mateus! Segunda-feira às 10h está perfeito! 😉 Vou agendar agora mesmo sua reunião com o Leonardo Ferraz para apresentar tudo sobre energia solar. Me passa seu melhor 
2025-08-16 18:23:46.328 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=289, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>Que massa, Mateus! Segunda-feira às 10h está perfeito! 😉 Vou agendar agora mesmo sua reunião com o Leonardo Ferraz para apresentar tudo sobre energia solar. Me passa seu melhor 
2025-08-16 18:23:46.329 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Que massa, Mateus! Segunda-feira às 10h está perfeito! Vou agendar agora mesmo sua reunião com o Leonardo Ferraz para apresentar tudo sobre energia solar. Me passa seu melhor e-mail para eu te enviar o convite com o link da reunião, certo?
2025-08-16 18:23:46.329 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 239 chars
2025-08-16 18:23:46.330 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem dividida em 2 partes | Data: {'phone': '558182986181', 'original_length': 239}
2025-08-16 18:23:49.274 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.29, 'message_length': 154, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 18:23:55.821 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 154, 'delay_used': 2.72, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:23:55.821 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Que massa, Mateus! Segunda-feira às 10h está perfe', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:23:55.822 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 1/2 enviado. ID: 3EB04D046BD6BCE8C29A844E4E84367D25935124
2025-08-16 18:23:55.829 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 18:23:55.830 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:53724 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 18:23:56.692 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:53724 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:24:01.633 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.08, 'message_length': 84, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:60352 - "GET /health HTTP/1.1" 200 OK
2025-08-16 18:24:06.975 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 84, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:24:06.975 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Me passa seu melhor e-mail para eu te enviar o con', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:24:06.975 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 2/2 enviado. ID: 3EB052549FB9C84D9051F714273960CCB2B7B3A9
2025-08-16 18:24:08.190 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 18:24:08.191 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:41868 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 18:24:08.192 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:24:08.657 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 18:24:08.657 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-16 18:24:11.611 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-16 18:24:14.514 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-16 18:24:14.515 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:24:14.507Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-16 18:24:14.544 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-16 18:24:14.546 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'matheuscdsgn@gmail.com', 'sender': '558182986181', 'type': 'text'}
2025-08-16 18:24:14.871 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 18:24:14.872 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGoWYKGE4ct4_MAL0NURewmOSPo8zb7lSbsJNalCC8pEQ&oe=68ADF48D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:24:14.867Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 18:24:14.920 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 18:24:14.921 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QGoWYKGE4ct4_MAL0NURewmOSPo8zb7lSbsJNalCC8pEQ&oe=68ADF48D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T15:24:14.916Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 18:24:15.880 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:24:15.886 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 18:24:15.886 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 18:24:15.897 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 18:24:15.902 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 18:24:15.903 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41884 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 18:24:29.762 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 22}
2025-08-16 18:24:30.948 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: e012388d-bea3-4362-9cd2-37ee07076dbb, Phone: 558182986181
2025-08-16 18:24:33.159 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 18:24:33.160 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 18:24:33.160 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 18:24:33.160 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 18:24:33.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 18:24:33.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 18:24:33.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 18:24:33.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 18:24:33.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 18:24:33.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 18:24:33.173 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 18:24:33.173 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 18:24:33.173 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 18:24:33.173 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 18:24:33.174 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 18:24:33.174 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 18:24:33.174 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 97, 'lead_name': 'Mateus'}
2025-08-16 18:24:33.174 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=e012388d-bea3-4362-9cd2-37ee07076dbb para phone=558182986181
2025-08-16 18:24:33.174 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: e012388d-bea3-4362-9cd2-37ee07076dbb
2025-08-16 18:24:34.884 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 18:24:35.130 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 18:24:35.392 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 18:24:35.751 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-16 18:24:35.751 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): matheuscdsgn@gmail.com...
2025-08-16 18:24:36.790 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 18:24:36.790 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 98 (👤 50 user, 🤖 48 assistant)
2025-08-16 18:24:36.791 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 18:24:36.791 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 18:24:36.792 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-16 18:24:36.792 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'boa noite! tudo bem? me chamo helen vieira, sou co...'
2025-08-16 18:24:36.792 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-16 18:24:36.792 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-16 18:24:36.792 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-16 18:24:36.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 BOOST Calendar por conversation_stage avançado
2025-08-16 18:24:36.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '0.300', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 18:24:36.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '0.300', 'threshold': '0.250', 'reason': 'threshold_dinamico'}
2025-08-16 18:24:36.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📅 Data padrão assumida: amanhã
2025-08-16 18:24:36.798 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 18:24:37.049 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 18:24:37.049 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Service: ⚠️ Tentativa de agendar no domingo
2025-08-16 18:24:37.050 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 18:24:37.050 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 18:24:37.479 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 18:24:37.480 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
INFO:     127.0.0.1:34868 - "GET /health HTTP/1.1" 200 OK
2025-08-16 18:24:41.938 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ ⚠️ Frase proibida detectada: aguarde
2025-08-16 18:24:41.939 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ ⚠️ Resposta inválida - usando fallback
2025-08-16 18:24:42.787 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 18:24:42.788 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: <RESPOSTA_FINAL>Como posso ajudar você com energia solar hoje? ☀️</RESPOSTA_FINAL>...
2025-08-16 18:24:42.788 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=82, primeiros 200 chars: <RESPOSTA_FINAL>Como posso ajudar você com energia solar hoje? ☀️</RESPOSTA_FINAL>
2025-08-16 18:24:42.789 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=82, primeiros 200 chars: <RESPOSTA_FINAL>Como posso ajudar você com energia solar hoje? ☀️</RESPOSTA_FINAL>
2025-08-16 18:24:42.789 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Como posso ajudar você com energia solar hoje?
2025-08-16 18:24:42.789 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 46 chars
2025-08-16 18:24:47.810 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.12, 'message_length': 46, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 18:24:52.187 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 46, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:24:52.187 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Como posso ajudar você com energia solar hoje?', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 18:24:52.187 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB0BE3A021AD959CEA58057042D2A2A8278D0EA
2025-08-16 18:24:52.865 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 18:24:52.866 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:39178 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 18:24:54.086 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 18:24:54.087 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-16 18:24:54.088 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39178 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK