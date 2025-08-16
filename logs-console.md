✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-16 01:01:10.451 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-16 01:01:10.456 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-16 01:01:10.456 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-16 01:01:11.131 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-16 01:01:11.131 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-16 01:01:11.131 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-16 01:01:11.132 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-16 01:01:11.132 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-16 01:01:11.132 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-16 01:01:11.139 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto | Data: {'check_interval': '1min', 'types': '30min, 24h'}
2025-08-16 01:01:11.140 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless) - tentativa 1/3...
2025-08-16 01:01:11.140 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 01:01:11.148 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 01:01:11.148 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 01:01:11.149 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 01:01:11.149 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 01:01:11.149 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 01:01:11.149 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 01:01:11.149 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 01:01:11.150 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-16 01:01:11.150 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 01:01:11.152 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 01:01:11.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 01:01:11.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 01:01:11.161 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 01:01:11.162 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 01:01:11.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 01:01:11.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 01:01:11.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-16 01:01:11.162 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
2025-08-16 01:01:11.163 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service inicializado para FollowUp Executor
2025-08-16 01:01:11.163 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Executor pronto
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:39728 - "GET /health HTTP/1.1" 200 OK
2025-08-16 01:01:21.639 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-16 01:01:22.827 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-16 01:01:22.828 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T22:01:22.821Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-16 01:01:22.849 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-16 01:01:22.850 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi, boa noite', 'sender': '558182986181', 'type': 'text'}
2025-08-16 01:01:23.190 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 01:01:23.190 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFkA9vkVEFZzSUiB5I-Ly8if_en-Ue8Y1P3eJcdb3EoEw&oe=68ACDB4D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T22:01:23.184Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 01:01:23.230 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-16 01:01:23.231 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QFkA9vkVEFZzSUiB5I-Ly8if_en-Ue8Y1P3eJcdb3EoEw&oe=68ACDB4D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T22:01:23.225Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-16 01:01:24.164 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 01:01:24.171 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-16 01:01:24.171 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:60666 - "POST /webhook/whatsapp/chats-upsert HTTP/1.1" 200 OK
2025-08-16 01:01:38.280 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 13}
2025-08-16 01:01:39.770 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: eacc6f54-e04d-4341-8783-ec6173be2ccd, Phone: 558182986181
2025-08-16 01:01:41.249 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏭 Criando instância stateless do AgenticSDR...
2025-08-16 01:01:41.249 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-16 01:01:41.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-16 01:01:41.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-16 01:01:41.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-16 01:01:41.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-16 01:01:41.250 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-16 01:01:41.251 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-16 01:01:41.251 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📅 Calendar Service pronto
2025-08-16 01:01:41.251 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 📊 CRM Service pronto
2025-08-16 01:01:41.258 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: 🔄 FollowUp Service pronto
2025-08-16 01:01:41.258 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎯 TeamCoordinator inicializado pronto | Data: {'services': ['calendar', 'crm', 'followup']}
2025-08-16 01:01:41.258 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-16 01:01:41.258 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-16 01:01:41.259 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'TeamCoordinator']}
2025-08-16 01:01:41.259 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ AgenticSDR Stateless pronto pronto
2025-08-16 01:01:41.259 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-16 01:01:41.259 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔍 WEBHOOK: Usando conversation_id=eacc6f54-e04d-4341-8783-ec6173be2ccd para phone=558182986181
2025-08-16 01:01:41.260 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chamando process_message com conversation_id: eacc6f54-e04d-4341-8783-ec6173be2ccd
2025-08-16 01:01:41.488 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 💬 Processando (stateless): oi, boa noite...
2025-08-16 01:01:42.141 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (user)
2025-08-16 01:01:42.141 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 📊 Analisando estágio - Msgs: 2 (👤 2 user, 🤖 0 assistant)
2025-08-16 01:01:42.141 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=0): 'oi, boa noite...'
2025-08-16 01:01:42.145 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 🔍 Analisando msg do usuário (idx=1): 'oi, boa noite...'
2025-08-16 01:01:42.145 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Campo alterado: qualification_score | Data: {'old': None, 'new': 0}
2025-08-16 01:01:42.145 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Sincronizando mudanças com CRM e Supabase | Data: {'fields': ['qualification_score']}
2025-08-16 01:01:42.600 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Iniciando sync imediato com Kommo CRM
2025-08-16 01:01:43.467 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Lead atualizado no Supabase | Data: {'fields': ['current_stage', 'updated_at'], 'data': {'current_stage': 'INITIAL_CONTACT', 'updated_at': '2025-08-16T01:01:43.255714'}}
🔍 DEBUG: create_or_update_lead chamado com: {'name': None, 'phone': '558182986181', 'qualification_score': 0, 'bill_value': None, 'interested': True}
2025-08-16 01:01:44.861 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-16 01:01:45.089 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-16 01:01:45.323 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 📈 40 estágios mapeados
2025-08-16 01:01:45.611 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🏷️ Nome do lead para Kommo: 'Lead WhatsApp 6181'
🔍 DEBUG: Preparando lead: {'name': 'Lead WhatsApp 6181', 'price': 0, 'pipeline_id': 11672895, 'custom_fields_values': [], '_embedded': {'tags': [{'name': 'sync_automático'}, {'name': 'SDR_IA'}]}}
🔍 DEBUG: Campos customizados preparados: [{'field_id': 392802, 'values': [{'value': '558182986181'}]}]
🔍 DEBUG: Atualizando lead existente: 6792762
2025-08-16 01:01:45.955 | INFO     | app.utils.logger:log_with_emoji:140 | 📝 ℹ️ Kommo recebido: sem evento específico
INFO:     10.11.0.4:45244 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-16 01:01:45.956 | INFO     | app.utils.logger:log_with_emoji:140 | 💼 CRM: ✅ Lead ATUALIZADO no Kommo: None - ID: 6792762
2025-08-16 01:01:45.956 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com Kommo CRM | Data: {'result': {'success': True, 'message': 'Lead criado/atualizado no Kommo: None'}}
2025-08-16 01:01:45.957 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Lead sincronizado com CRM
2025-08-16 01:01:45.957 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Análise de necessidade de serviços | Data: {'calendar': '0.500', 'crm': '0.000', 'followup': '0.000', 'threshold': 0.4}
2025-08-16 01:01:45.957 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🎯 Executando calendar | Data: {'score': '0.500', 'threshold': '0.350', 'reason': 'threshold_dinamico'}
2025-08-16 01:01:46.144 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-16 01:01:46.148 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-16 01:01:46.403 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Service: ✅ Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-16 01:01:46.599 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: ✅ calendar executado com sucesso | Data: {'result': 'Tenho estes horários disponíveis amanhã: 09:00, 10:00, 11:00. Qual prefere?'}
2025-08-16 01:01:46.600 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 01:01:46.600 | INFO     | app.services.knowledge_service:__init__:33 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-16 01:01:46.600 | INFO     | app.services.knowledge_service:search_knowledge_base:53 | 📚 Carregando TODA a knowledge_base para enriquecer resposta...
2025-08-16 01:01:47.007 | INFO     | app.services.knowledge_service:search_knowledge_base:68 | ✅ Encontrados 67 documentos
2025-08-16 01:01:47.007 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🧠 Knowledge base: 67 itens encontrados
2025-08-16 01:01:47.136 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔌 Sessão CRM fechada com segurança
INFO:     127.0.0.1:38664 - "GET /health HTTP/1.1" 200 OK
2025-08-16 01:01:49.271 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-16 01:01:49.272 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ ✅ Resposta formatada com tags: 250 chars
2025-08-16 01:01:49.904 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 💾 Mensagem salva (assistant)
2025-08-16 01:01:49.905 | INFO     | app.utils.logger:log_with_emoji:140 | 💬 ✅ Resposta gerada: <RESPOSTA_FINAL>Boa noite! Que maravilha que a reunião foi agendada com sucesso!  Ôxe, que coisa boa...
2025-08-16 01:01:49.905 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=250, primeiros 200 chars: <RESPOSTA_FINAL>Boa noite! Que maravilha que a reunião foi agendada com sucesso!  Ôxe, que coisa boa!  A gente se fala mais amanhã, viu?  Qualquer coisa pode me chamar! Tenha uma ótima noite e um exce
2025-08-16 01:01:49.906 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔎 extract_final_response recebeu: tipo=<class 'str'>, tamanho=250, primeiros 200 chars: <RESPOSTA_FINAL>Boa noite! Que maravilha que a reunião foi agendada com sucesso!  Ôxe, que coisa boa!  A gente se fala mais amanhã, viu?  Qualquer coisa pode me chamar! Tenha uma ótima noite e um exce
2025-08-16 01:01:49.907 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📝 Resposta completa antes de dividir: Boa noite! Que maravilha que a reunião foi agendada com sucesso! Ôxe, que coisa boa! A gente se fala mais amanhã, viu? Qualquer coisa pode me chamar! Tenha uma ótima noite e um excelente final de semana. Até mais!
2025-08-16 01:01:49.907 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📏 Tamanho: 213 chars
2025-08-16 01:01:49.917 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Mensagem dividida em 2 partes | Data: {'phone': '558182986181', 'original_length': 213}
2025-08-16 01:01:55.148 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.78, 'message_length': 149, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 01:02:00.597 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 01:02:00.598 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:35756 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 01:02:00.599 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 149, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 01:02:00.599 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Boa noite! Que maravilha que a reunião foi agendad', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 01:02:00.599 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 1/2 enviado. ID: 3EB0AFB0F22E76558BE55285232CF04F20768EA8
2025-08-16 01:02:01.147 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35756 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 01:02:04.349 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.62, 'message_length': 63, 'recipient': '558182986181', 'type': 'typing'}
2025-08-16 01:02:09.230 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'message_length': 63, 'delay_used': 2.94, 'recipient': '558182986181', 'type': 'text'}
2025-08-16 01:02:09.230 | INFO     | app.utils.logger:log_with_emoji:140 | 📤 Enviando text para 558182986181 | Data: {'preview': 'Tenha uma ótima noite e um excelente final de sema', 'recipient': '558182986181', 'type': 'text'}
2025-08-16 01:02:09.230 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Chunk 2/2 enviado. ID: 3EB084EF67C1280CA86FE0202B1715AD64964897
2025-08-16 01:02:10.306 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-16 01:02:10.306 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:385 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:40072 - "POST /webhook/whatsapp/send-message HTTP/1.1" 200 OK
2025-08-16 01:02:10.307 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40084 - "POST /webhook/whatsapp/messages-update HTTP/1.1" 200 OK
2025-08-16 01:02:10.763 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ⏰ Follow-up de 30min agendado para 558182986181 às 08:00
2025-08-16 01:02:10.764 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 📋 Follow-up sequencial: 24h será agendado apenas se usuário não responder ao de 30min