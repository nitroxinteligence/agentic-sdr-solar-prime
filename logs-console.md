✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-13 20:34:05.539 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.2
2025-08-13 20:34:05.543 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-13 20:34:05.544 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-13 20:34:06.380 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-13 20:34:06.381 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=10.0s, max=10)
2025-08-13 20:34:06.381 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '10.0s'}
2025-08-13 20:34:06.381 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-13 20:34:06.381 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-13 20:34:06.381 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-13 20:34:06.382 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto | Data: {'check_interval': '1min', 'types': '30min, 24h'}
2025-08-13 20:34:06.382 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (tentativa 1/3)...
2025-08-13 20:34:06.383 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏗️ Criando instância singleton do AgenticSDR...
2025-08-13 20:34:06.390 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Modular...
2025-08-13 20:34:06.390 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-13 20:34:06.390 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-13 20:34:06.390 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-13 20:34:06.390 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-13 20:34:06.391 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-13 20:34:06.391 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-13 20:34:06.391 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-13 20:34:06.392 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-13 20:34:06.400 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-13 20:34:06.401 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-13 20:34:06.401 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-13 20:34:06.401 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-13 20:34:06.401 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Modular inicializado com sucesso! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-13 20:34:06.402 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Singleton AgenticSDR criado e inicializado pronto
2025-08-13 20:34:06.402 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 20:34:06.402 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR pronto | Data: {'status': 'pré-aquecido com sucesso'}
2025-08-13 20:34:06.402 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-13 20:34:06.402 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ✅ FollowUp Executor inicializado
2025-08-13 20:34:06.403 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 🔄 Iniciando FollowUp Executor
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:39074 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:53444 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50568 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:59462 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:49498 - "GET /health HTTP/1.1" 200 OK
2025-08-13 20:36:34.066 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 20:36:34.359 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 20:36:34.360 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:36:34.350Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 20:36:34.372 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 20:36:34.373 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:36:34.365Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 20:36:34.403 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 20:36:34.404 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-13 20:36:34.713 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 20:36:34.713 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:36:34.703Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 20:36:34.964 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 20:36:34.965 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:36:34.959Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:57700 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 20:36:44.411 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-13 20:36:45.651 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 20:36:46.482 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd, Phone: 558182986181
INFO:     127.0.0.1:56614 - "GET /health HTTP/1.1" 200 OK
2025-08-13 20:36:48.506 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd para phone=558182986181
2025-08-13 20:36:48.506 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd
2025-08-13 20:36:48.721 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: oi...
2025-08-13 20:36:49.402 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 1 mensagens
2025-08-13 20:36:49.408 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 20:36:49.408 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 20:36:49.408 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 20:36:50.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T20:36:50.208124'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
2025-08-13 20:36:51.749 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 20:36:52.081 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 20:36:52.328 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 20:36:52.655 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Criando novo lead com dados: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [{'field_id': 392802, 'values': [{'value': '558182986181'}]}], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Response status: 200
🔍 DEBUG: Response JSON: {'_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads'}}, '_embedded': {'leads': [{'id': 5982274, 'request_id': '0', '_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads/5982274'}}}]}}
2025-08-13 20:36:53.298 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead CRIADO no Kommo: None - ID: 5982274
2025-08-13 20:36:53.612 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 20:36:53.612 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 20:36:53.612 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 20:36:53.613 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 20:36:53.613 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 20:36:54.021 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 20:36:54.021 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 20:36:54.022 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 20:36:54.026 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:56712 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 20:36:54.028 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:56722 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 20:36:54.129 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 20:36:56.818 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-13 20:36:56.819 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 181 chars
2025-08-13 20:36:56.820 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realiz...
2025-08-13 20:36:56.820 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 20:36:56.821 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 20:36:56.822 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-13 20:36:56.822 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 148 chars
2025-08-13 20:37:02.059 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.63, 'message_length': 148, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 20:37:06.905 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 148, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 20:37:06.906 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Bom dia! Tudo bem? Me chamo Helen Vieira, sou cons', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 20:37:06.906 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB089F6E1BAF6B72B6FA8CEE93B101A0EA63EA9
2025-08-13 20:37:08.354 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 20:37:08.355 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:41430 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 20:37:08.356 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 20:37:09.560 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 18:07
2025-08-13 20:37:09.560 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 20:37:11.019 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 20:37:13.708 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 20:37:13.708 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:37:13.702Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 20:37:13.723 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 20:37:13.724 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:37:13.717Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 20:37:13.730 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 20:37:13.731 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'Mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-13 20:37:14.045 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 20:37:14.046 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:37:14.039Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 20:37:14.081 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 20:37:14.081 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T17:37:14.075Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 20:37:15.102 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-13 20:37:15.109 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-13 20:37:15.109 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41432 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:53984 - "GET /health HTTP/1.1" 200 OK
2025-08-13 20:37:23.823 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 6}
2025-08-13 20:37:25.010 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 20:37:25.010 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd, Phone: 558182986181
2025-08-13 20:37:26.042 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd para phone=558182986181
2025-08-13 20:37:26.042 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: a6fd5bc9-2d09-48ac-ad0a-d3015e63c4fd
2025-08-13 20:37:26.795 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 20:37:27.024 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 20:37:27.364 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 20:37:27.694 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 20:37:27.695 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: Mateus...
2025-08-13 20:37:29.099 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 3 mensagens
2025-08-13 20:37:29.100 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 20:37:29.100 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 20:37:29.100 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 20:37:30.278 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T20:37:29.700813'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
2025-08-13 20:37:30.840 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 20:37:31.119 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 20:37:31.364 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-13 20:37:31.862 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 5982274
2025-08-13 20:37:32.167 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:50704 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 20:37:32.180 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 5982274
2025-08-13 20:37:32.180 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 20:37:32.180 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 20:37:32.181 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 20:37:32.181 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 20:37:32.587 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 20:37:32.588 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 20:37:32.588 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 20:37:32.690 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 20:37:35.007 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-13 20:37:35.007 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 181 chars
2025-08-13 20:37:35.008 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realiz...
2025-08-13 20:37:35.008 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 20:37:35.009 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=181, primeiros 200 chars: <RESPOSTA_FINAL>Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?</RESPOSTA_FINAL>
2025-08-13 20:37:35.010 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
2025-08-13 20:37:35.010 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 148 chars
2025-08-13 20:37:40.028 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.64, 'message_length': 148, 'recipient': '558182986181', 'type': 'typing'}
2025-08-13 20:37:44.878 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 148, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 20:37:44.879 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Bom dia! Tudo bem? Me chamo Helen Vieira, sou cons', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 20:37:44.879 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB01B974590427FAFCE72EBF1682312F4C9B5BA
2025-08-13 20:37:45.558 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 20:37:45.558 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:39644 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 20:37:46.747 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 18:07
2025-08-13 20:37:46.747 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 20:37:46.748 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:39644 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:56010 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:50868 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47396 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47100 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:41624 - "GET /health HTTP/1.1" 200 OK
2025-08-13 20:40:03.471 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-13 20:40:03.471 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:55142 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-13 20:40:03.472 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:55140 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK