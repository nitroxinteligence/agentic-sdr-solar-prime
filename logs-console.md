INFO:     10.11.0.4:57216 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 17:23:50.755 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 39}
2025-08-16 17:23:51.226 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: e012388d-bea3-4362-9cd2-37ee07076dbb, Phone: 558182986181
2025-08-16 17:23:53.824 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 17:23:53.825 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 17:23:53.826 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 17:23:53.826 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 17:23:53.826 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 17:23:53.834 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 17:23:53.835 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 17:23:53.835 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 17:23:53.835 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 17:23:53.835 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 17:23:53.836 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 17:23:53.836 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 73, 'lead_name': 'Mateus'}
2025-08-16 17:23:53.836 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=e012388d-bea3-4362-9cd2-37ee07076dbb para phone=558182986181
2025-08-16 17:23:53.836 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: e012388d-bea3-4362-9cd2-37ee07076dbb
2025-08-16 17:23:54.599 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 17:23:54.831 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 17:23:55.053 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 17:23:55.352 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-16 17:23:55.353 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): eu quero agendar uma reuniao pra amanha...
2025-08-16 17:23:56.032 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 17:23:56.032 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 74 (👤 38 user, 🤖 36 assistant)
2025-08-16 17:23:56.033 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 17:23:56.037 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 17:23:56.038 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-16 17:23:56.038 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'boa noite! tudo bem? me chamo helen vieira, sou co...'
2025-08-16 17:23:56.038 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-16 17:23:56.038 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-16 17:23:56.039 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-16 17:23:56.041 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 BOOST Calendar por interesse demonstrado
2025-08-16 17:23:56.042 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '1.000', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 17:23:56.042 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '1.000', 'threshold': '0.350', 'reason': 'threshold_dinamico'}
2025-08-16 17:23:56.234 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-16 17:23:56.239 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 17:23:56.529 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 17:23:56.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ calendar executado com sucesso | Data: {'result': 'Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?'}
2025-08-16 17:23:56.796 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 17:23:56.796 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 17:23:56.796 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 17:23:57.217 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 17:23:57.217 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-16 17:24:01.855 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 17:24:01.856 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: ```xml
<RESPOSTA_FINAL>Oi Mateus! Tudo certo? 😉  O Leonardo está disponível amanhã às 09:00, 10:00 e...
2025-08-16 17:24:01.856 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=238, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>Oi Mateus! Tudo certo? 😉  O Leonardo está disponível amanhã às 09:00, 10:00 e 11:00. Qual horário te serve melhor?  Assim que você escolher, eu já agendo a reunião e te mando o 
2025-08-16 17:24:01.858 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=238, primeiros 200 chars: ```xml
<RESPOSTA_FINAL>Oi Mateus! Tudo certo? 😉  O Leonardo está disponível amanhã às 09:00, 10:00 e 11:00. Qual horário te serve melhor?  Assim que você escolher, eu já agendo a reunião e te mando o 
2025-08-16 17:24:01.858 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Oi Mateus! Tudo certo? O Leonardo está disponível amanhã às 09:00, 10:00 e 11:00. Qual horário te serve melhor? Assim que você escolher, eu já agendo a reunião e te mando o link, beleza?
2025-08-16 17:24:01.858 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 186 chars
INFO:     127.0.0.1:36902 - "GET /health HTTP/1.1" 200 OK
2025-08-16 17:24:07.097 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 5.11, 'message_length': 186, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 17:24:14.461 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 186, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 17:24:14.461 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Oi Mateus! Tudo certo? O Leonardo está disponível ', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 17:24:14.462 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB06CDB61FDCA6EEC2E42550B2C10D451E7466E
2025-08-16 17:24:15.147 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 17:24:15.147 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:56250 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 17:24:15.596 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 17:24:15.596 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-16 17:24:15.597 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56250 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 17:24:15.598 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56262 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 17:24:15.599 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 17:24:15.599 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 17:24:19.344 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-16 17:24:23.088 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-16 17:24:23.089 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T14:24:23.083Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-16 17:24:23.108 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-16 17:24:23.109 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'pode ser as 10h', 'sender': '558182986181', 'type': 'text'}
2025-08-16 17:24:23.448 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 17:24:23.449 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEE0AGHGqZRWnM_TqpWx78CXbbWEfDljHvcDgXcG2SgrQ&oe=68ADBC4D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T14:24:23.442Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 17:24:23.484 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 17:24:23.485 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEE0AGHGqZRWnM_TqpWx78CXbbWEfDljHvcDgXcG2SgrQ&oe=68ADBC4D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-16T14:24:23.477Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:56268 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:41466 - "GET /health HTTP/1.1" 200 OK
2025-08-16 17:24:38.431 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 15}
2025-08-16 17:24:39.064 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: e012388d-bea3-4362-9cd2-37ee07076dbb, Phone: 558182986181
2025-08-16 17:24:40.921 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 17:24:40.922 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 17:24:40.922 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 17:24:40.923 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 17:24:40.923 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 17:24:40.923 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 17:24:40.923 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 17:24:40.924 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 17:24:40.924 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 17:24:40.924 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 17:24:40.932 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 17:24:40.932 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 17:24:40.933 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 17:24:40.933 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 17:24:40.933 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 17:24:40.933 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 17:24:40.934 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 77, 'lead_name': 'Mateus'}
2025-08-16 17:24:40.934 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=e012388d-bea3-4362-9cd2-37ee07076dbb para phone=558182986181
2025-08-16 17:24:40.934 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: e012388d-bea3-4362-9cd2-37ee07076dbb
2025-08-16 17:24:42.084 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 17:24:42.400 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 17:24:42.650 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 17:24:43.057 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-16 17:24:43.058 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): pode ser as 10h...
2025-08-16 17:24:43.685 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 17:24:43.686 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 78 (👤 40 user, 🤖 38 assistant)
2025-08-16 17:24:43.687 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 17:24:43.687 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 17:24:43.688 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=4): 'mateus...'
2025-08-16 17:24:43.688 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📋 Verificando msg anterior do assistant: 'boa noite! tudo bem? me chamo helen vieira, sou co...'
2025-08-16 17:24:43.688 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Pergunta de nome detectada: 'como posso te chamar'
2025-08-16 17:24:43.688 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎯 Potencial nome: 'mateus' (1 palavras)
2025-08-16 17:24:43.688 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🎉 NOME DETECTADO COM SUCESSO: Mateus
2025-08-16 17:24:43.690 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 BOOST Calendar por contexto de agendamento conversacional
2025-08-16 17:24:43.691 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '1.000', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 17:24:43.691 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '1.000', 'threshold': '0.350', 'reason': 'threshold_dinamico'}
2025-08-16 17:24:43.693 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 17:24:43.954 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 17:24:44.179 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ calendar executado com sucesso | Data: {'result': 'Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?'}
2025-08-16 17:24:44.179 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 17:24:44.179 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 17:24:44.581 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 17:24:44.581 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-16 17:24:48.587 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 17:24:48.588 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: <RESPOSTA_FINAL>Que ótimo, Mateus! O Leonardo está disponível amanhã às 10h! 😊 Vou agendar a reunião...
2025-08-16 17:24:48.588 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=226, primeiros 200 chars: <RESPOSTA_FINAL>Que ótimo, Mateus! O Leonardo está disponível amanhã às 10h! 😊 Vou agendar a reunião agora mesmo e te enviar o convite por e-mail com o link do Google Meet.  Qualquer dúvida, pode me c
2025-08-16 17:24:48.589 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=226, primeiros 200 chars: <RESPOSTA_FINAL>Que ótimo, Mateus! O Leonardo está disponível amanhã às 10h! 😊 Vou agendar a reunião agora mesmo e te enviar o convite por e-mail com o link do Google Meet.  Qualquer dúvida, pode me c
2025-08-16 17:24:48.589 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Que ótimo, Mateus! O Leonardo está disponível amanhã às 10h! Vou agendar a reunião agora mesmo e te enviar o convite por e-mail com o link do Google Meet. Qualquer dúvida, pode me chamar!
2025-08-16 17:24:48.589 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 187 chars
2025-08-16 17:24:50.604 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 5.08, 'message_length': 187, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 17:24:57.930 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 187, 'delay_used': 2.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 17:24:57.931 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Que ótimo, Mateus! O Leonardo está disponível aman', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 17:24:57.931 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB06E0AAA0FA6AEBDCBBFC71C17F080674329F5
2025-08-16 17:24:58.638 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 17:24:58.639 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:38084 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 17:24:59.066 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 17:24:59.066 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-16 17:24:59.067 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38084 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 17:24:59.068 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38096 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 17:24:59.069 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 17:24:59.069 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:38100 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:37002 - "GET /health HTTP/1.1" 200 OK