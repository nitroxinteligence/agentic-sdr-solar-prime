✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-13 19:49:25.636 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.2
2025-08-13 19:49:25.642 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-13 19:49:25.642 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-13 19:49:26.259 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-13 19:49:26.259 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=30.0s, max=10)
2025-08-13 19:49:26.259 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '30.0s'}
2025-08-13 19:49:26.259 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-13 19:49:26.260 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-13 19:49:26.260 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-13 19:49:26.260 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto | Data: {'check_interval': '1min', 'types': '30min, 24h'}
2025-08-13 19:49:26.261 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (tentativa 1/3)...
2025-08-13 19:49:26.261 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏗️ Criando instância singleton do AgenticSDR...
2025-08-13 19:49:26.269 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Modular...
2025-08-13 19:49:26.270 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-13 19:49:26.270 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-13 19:49:26.270 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-13 19:49:26.270 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-13 19:49:26.271 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-13 19:49:26.271 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-13 19:49:26.272 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-13 19:49:26.273 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-13 19:49:26.282 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-13 19:49:26.282 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Modular inicializado com sucesso! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Singleton AgenticSDR criado e inicializado pronto
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR pronto | Data: {'status': 'pré-aquecido com sucesso'}
2025-08-13 19:49:26.283 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-13 19:49:26.284 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ✅ FollowUp Executor inicializado
2025-08-13 19:49:26.284 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 🔄 Iniciando FollowUp Executor
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:37706 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:49:33.452 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39854 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:49:38.676 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39860 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:49:56.367 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35312 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:49:56.986 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 19:49:56.987 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:49:56.980Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35312 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 19:49:57.009 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:35312 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 19:49:57.010 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-13 19:49:57.326 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:49:57.327 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:49:57.320Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35312 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:49:57.380 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:49:57.380 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:49:57.373Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:35312 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:40090 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:50:07.280 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59926 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:50:27.504 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-13 19:50:27.953 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:50:28.773 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 0281cc8c-b994-4a96-a054-e692fff97b6b, Phone: 558182986181
2025-08-13 19:50:29.796 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=0281cc8c-b994-4a96-a054-e692fff97b6b para phone=558182986181
2025-08-13 19:50:29.797 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: 0281cc8c-b994-4a96-a054-e692fff97b6b
2025-08-13 19:50:30.436 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: oi...
2025-08-13 19:50:31.453 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 1 mensagens
2025-08-13 19:50:31.458 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 19:50:31.458 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 19:50:31.458 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 19:50:32.492 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T19:50:32.259896'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
INFO:     127.0.0.1:39748 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:50:33.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:50:33.565 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:50:33.856 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 19:50:34.119 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Criando novo lead com dados: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [{'field_id': 392802, 'values': [{'value': '558182986181'}]}], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
2025-08-13 19:50:34.661 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:44124 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
🔍 DEBUG: Response status: 200
🔍 DEBUG: Response JSON: {'_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads'}}, '_embedded': {'leads': [{'id': 5922534, 'request_id': '0', '_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads/5922534'}}}]}}
2025-08-13 19:50:34.668 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead CRIADO no Kommo: None - ID: 5922534
2025-08-13 19:50:35.335 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:44124 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 19:50:35.337 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 19:50:35.338 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 19:50:35.338 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:50:35.339 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:50:35.339 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 19:50:35.750 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 19:50:35.751 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 19:50:35.752 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 19:50:35.856 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 19:50:39.129 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-13 19:50:39.130 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 181 chars
2025-08-13 19:50:39.130 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realiz...
2025-08-13 19:50:39.131 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:50:39.132 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:50:39.133 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-13 19:50:39.133 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 148 chars
2025-08-13 19:50:44.373 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 3.31, 'message_length': 148, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 19:50:49.901 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 148, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:50:49.902 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Bom dia! Tudo bem? Me chamo Helen Vieira, sou cons', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:50:49.902 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB078BFF3BF816B0467131854383F37A2DDFBDA
2025-08-13 19:50:50.776 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 19:50:50.776 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:59176 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 19:50:51.263 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 17:20
2025-08-13 19:50:51.263 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 19:50:51.264 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:59176 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 19:50:57.300 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:50:58.186 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 19:50:58.186 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:50:58.179Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 19:50:58.198 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 19:50:58.198 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:50:58.190Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 19:50:58.225 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 19:50:58.226 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-13 19:50:58.525 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:50:58.526 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:50:58.516Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:50:58.585 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:50:58.585 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:50:58.578Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:50:59.625 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 19:50:59.630 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-13 19:50:59.631 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41974 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:40100 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:51:28.657 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 6}
2025-08-13 19:51:29.123 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:51:29.123 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 0281cc8c-b994-4a96-a054-e692fff97b6b, Phone: 558182986181
2025-08-13 19:51:29.774 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=0281cc8c-b994-4a96-a054-e692fff97b6b para phone=558182986181
2025-08-13 19:51:29.775 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: 0281cc8c-b994-4a96-a054-e692fff97b6b
2025-08-13 19:51:30.540 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:51:30.845 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:51:31.131 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 19:51:31.364 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Erro ao verificar estágio no Kommo: 'NoneType' object has no attribute 'get'
2025-08-13 19:51:31.364 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: mateus...
2025-08-13 19:51:32.391 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 3 mensagens
2025-08-13 19:51:32.392 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 19:51:32.393 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 19:51:32.393 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 19:51:33.189 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T19:51:32.979794'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
INFO:     127.0.0.1:51978 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:51:33.940 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:51:34.223 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:51:34.493 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 19:51:34.767 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 5922534
2025-08-13 19:51:35.348 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:59534 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 19:51:35.364 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 5922534
2025-08-13 19:51:35.365 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 19:51:35.365 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 19:51:35.365 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:51:35.365 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 19:51:35.778 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 19:51:35.778 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 19:51:35.779 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 19:51:35.880 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 19:51:38.168 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-13 19:51:38.169 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 181 chars
2025-08-13 19:51:38.169 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realiz...
2025-08-13 19:51:38.169 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:51:38.170 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:51:38.170 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-13 19:51:38.170 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 148 chars
2025-08-13 19:51:43.189 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.55, 'message_length': 148, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 19:51:47.956 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 148, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:51:47.957 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Bom dia! Tudo bem? Me chamo Helen Vieira, sou cons', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:51:47.957 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB059C6833858399D831163F45343F090476CCA
2025-08-13 19:51:48.629 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 19:51:48.630 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:35924 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 19:51:49.070 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 17:21
2025-08-13 19:51:49.070 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 19:51:49.071 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35924 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 19:51:49.173 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
INFO:     127.0.0.1:34632 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:52:29.303 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:52:29.815 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 19:52:29.816 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:52:29.809Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 19:52:29.829 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 19:52:29.830 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-13 19:52:30.152 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:52:30.153 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:52:30.145Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:52:30.190 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:52:30.191 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:52:30.184Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:52:31.266 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 19:52:31.275 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-13 19:52:31.276 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:38666 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:48338 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:52:59.866 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 6}
2025-08-13 19:53:00.312 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:53:00.312 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 0281cc8c-b994-4a96-a054-e692fff97b6b, Phone: 558182986181
2025-08-13 19:53:00.965 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=0281cc8c-b994-4a96-a054-e692fff97b6b para phone=558182986181
2025-08-13 19:53:00.965 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: 0281cc8c-b994-4a96-a054-e692fff97b6b
2025-08-13 19:53:01.767 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:53:02.085 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:53:02.448 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 19:53:02.686 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ Erro ao verificar estágio no Kommo: 'NoneType' object has no attribute 'get'
2025-08-13 19:53:02.687 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: mateus...
2025-08-13 19:53:03.761 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 5 mensagens
2025-08-13 19:53:03.763 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 19:53:03.763 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 19:53:03.763 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 19:53:04.196 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T19:53:03.978917'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
INFO:     127.0.0.1:59796 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:53:04.929 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:53:05.194 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:53:05.438 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 19:53:05.755 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 5922534
2025-08-13 19:53:06.141 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 5922534
2025-08-13 19:53:06.142 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 19:53:06.142 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 19:53:06.142 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:53:06.142 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 19:53:06.569 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 19:53:06.569 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 19:53:06.570 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 19:53:06.575 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:50606 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 19:53:06.676 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 19:53:08.968 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-13 19:53:08.969 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 181 chars
2025-08-13 19:53:08.969 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realiz...
2025-08-13 19:53:08.969 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:53:08.971 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 19:53:08.972 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-13 19:53:08.972 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 148 chars
2025-08-13 19:53:14.199 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.87, 'message_length': 148, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 19:53:19.289 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 148, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:53:19.290 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Bom dia! Tudo bem? Me chamo Helen Vieira, sou cons', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:53:19.290 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB0AF8D6B42E3245CC982156F34C3C2C7B194F6
2025-08-13 19:53:19.994 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 19:53:19.994 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:51138 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 19:53:20.833 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 17:23
2025-08-13 19:53:20.834 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 19:53:20.834 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:51138 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 19:53:20.936 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança