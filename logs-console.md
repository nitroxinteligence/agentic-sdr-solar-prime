✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-13 19:31:08.846 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.2
2025-08-13 19:31:08.852 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-13 19:31:08.852 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-13 19:31:09.396 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-13 19:31:09.396 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=30.0s, max=10)
2025-08-13 19:31:09.397 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '30.0s'}
2025-08-13 19:31:09.397 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-13 19:31:09.397 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-13 19:31:09.397 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-13 19:31:09.398 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto | Data: {'check_interval': '1min', 'types': '30min, 24h'}
2025-08-13 19:31:09.398 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (tentativa 1/3)...
2025-08-13 19:31:09.398 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏗️ Criando instância singleton do AgenticSDR...
2025-08-13 19:31:09.407 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Modular...
2025-08-13 19:31:09.407 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-13 19:31:09.407 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-13 19:31:09.407 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-13 19:31:09.407 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-13 19:31:09.408 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-13 19:31:09.408 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-13 19:31:09.409 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-13 19:31:09.410 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-13 19:31:09.418 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-13 19:31:09.418 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Modular inicializado com sucesso! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Singleton AgenticSDR criado e inicializado pronto
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:31:09.419 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR pronto | Data: {'status': 'pré-aquecido com sucesso'}
2025-08-13 19:31:09.420 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-13 19:31:09.420 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ✅ FollowUp Executor inicializado
2025-08-13 19:31:09.420 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 🔄 Iniciando FollowUp Executor
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:37426 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60260 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:31:57.886 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:52490 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-13 19:32:00.362 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-13 19:32:00.362 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:336 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:32:00.352Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52490 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-13 19:32:00.409 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:52490 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-13 19:32:00.410 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'olá, tudo bem?', 'sender': '558182986181', 'type': 'text'}
2025-08-13 19:32:00.706 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:32:00.707 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:32:00.693Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52490 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:32:00.784 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-13 19:32:00.784 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:341 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHwskJvbW1sZRLFAOR_OT0z0FqgbJBSjvKnhLm2tvxkMQ&oe=68AA000D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-13T16:32:00.774Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:52490 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-13 19:32:10.700 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:38904 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:45480 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:32:30.744 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 14}
2025-08-13 19:32:31.985 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Nova instância do AgenticSDR criada! pronto
2025-08-13 19:32:32.795 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: ecea05ac-d529-4557-90e3-c7a2eaacd7c6, Phone: 558182986181
2025-08-13 19:32:33.480 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=ecea05ac-d529-4557-90e3-c7a2eaacd7c6 para phone=558182986181
2025-08-13 19:32:33.480 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: ecea05ac-d529-4557-90e3-c7a2eaacd7c6
2025-08-13 19:32:34.076 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Recebida: olá, tudo bem?...
2025-08-13 19:32:35.491 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 📚 Histórico carregado: 1 mensagens
2025-08-13 19:32:35.496 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-13 19:32:35.496 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM | Data: {'fields': ['qualification_score']}
2025-08-13 19:32:35.497 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-13 19:32:36.522 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-13T19:32:36.306891'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': False}
2025-08-13 19:32:37.100 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-13 19:32:37.377 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-13 19:32:37.646 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 35 estágios mapeados
2025-08-13 19:32:37.963 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Criando novo lead com dados: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [{'field_id': 392802, 'values': [{'value': '558182986181'}]}], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Response status: 200
🔍 DEBUG: Response JSON: {'_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads'}}, '_embedded': {'leads': [{'id': 5906496, 'request_id': '0', '_links': {'self': {'href': 'https://leonardofvieira00.kommo.com/api/v4/leads/5906496'}}}]}}
2025-08-13 19:32:38.447 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead CRIADO no Kommo: None - ID: 5906496
2025-08-13 19:32:38.871 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:50968 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 19:32:38.882 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-13 19:32:38.883 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-13 19:32:38.884 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:32:38.884 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-13 19:32:38.884 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-13 19:32:39.296 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-13 19:32:39.296 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-13 19:32:39.297 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: ✅ Prompt completo carregado de prompt-agente.md
2025-08-13 19:32:39.301 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:50968 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-13 19:32:39.402 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
2025-08-13 19:32:42.543 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendim...
2025-08-13 19:32:42.543 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=149, primeiros 200 chars: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?

2025-08-13 19:32:42.544 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em extract_final_response: 🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO | Data: {'component': 'extract_final_response'}
2025-08-13 19:32:42.544 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em extract_final_response: 📝 Conteúdo original (primeiros 200 chars): Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
... | Data: {'component': 'extract_final_response'}
2025-08-13 19:32:42.544 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔒 Usando resposta segura para evitar vazamento de raciocínio interno
2025-08-13 19:32:42.545 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=149, primeiros 200 chars: Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?

2025-08-13 19:32:42.546 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em extract_final_response: 🚨 TAGS <RESPOSTA_FINAL> NÃO ENCONTRADAS - BLOQUEANDO VAZAMENTO | Data: {'component': 'extract_final_response'}
2025-08-13 19:32:42.546 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em extract_final_response: 📝 Conteúdo original (primeiros 200 chars): Bom dia! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?
... | Data: {'component': 'extract_final_response'}
2025-08-13 19:32:42.546 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔒 Usando resposta segura para evitar vazamento de raciocínio interno
2025-08-13 19:32:42.547 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Oi! Me dê só um minutinho que já te respondo!
2025-08-13 19:32:42.547 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 45 chars
2025-08-13 19:32:44.720 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 1.95, 'message_length': 45, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:34876 - "GET /health HTTP/1.1" 200 OK
2025-08-13 19:32:48.910 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 45, 'delay_used': 1.92, 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:32:48.910 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Oi! Me dê só um minutinho que já te respondo!', 'recipient': '558182986181', 'type': 'text'}
2025-08-13 19:32:48.911 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem enviada com sucesso. ID: 3EB0BC526B50F72BA51F3A8FE436EA857E56E233
2025-08-13 19:32:49.577 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-13 19:32:49.578 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:345 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:57682 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-13 19:32:50.056 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 17:02
2025-08-13 19:32:50.057 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min
2025-08-13 19:32:50.057 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:57682 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK