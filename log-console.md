✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-08-25 17:55:01.987 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
2025-08-25 17:55:02.864 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
INFO:     Waiting for application startup.
2025-08-25 17:55:02.869 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-25 17:55:02.870 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-25 17:55:03.144 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-25 17:55:03.145 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-25 17:55:03.145 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-25 17:55:03.146 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-25 17:55:03.146 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-25 17:55:03.146 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-25 17:55:03.174 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-25 17:55:03.184 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 17:55:03.184 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-25 17:55:03.185 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 17:55:03.185 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 17:55:03.193 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 17:55:03.194 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 17:55:03.194 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 17:55:03.195 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 17:55:03.196 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 17:55:03.196 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 17:55:03.196 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 17:55:03.196 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 17:55:03.399 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-25 17:55:03.403 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 17:55:03.658 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 17:55:04.562 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 17:55:05.153 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 17:55:05.748 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 17:55:05.778 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 17:55:05.779 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 17:55:05.780 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-25 17:55:05.780 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-25 17:55:05.780 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-25 17:55:05.790 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 17:55:05.790 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 17:55:05.790 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 17:55:05.801 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 17:55:05.801 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 17:55:05.801 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 17:55:05.802 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 17:55:05.802 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 17:55:05.802 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 17:55:05.802 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 17:55:05.803 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 17:55:05.805 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 17:55:06.060 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 17:55:06.602 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 17:55:07.343 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 17:55:08.064 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 17:55:08.089 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 17:55:08.090 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 17:55:08.090 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
INFO:     Application startup complete.
2025-08-25 17:55:08.091 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:51686 - "GET /health HTTP/1.1" 200 OK
2025-08-25 17:55:18.594 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:58422 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 17:55:18.905 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 17:55:18.906 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:531 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T14:55:18.832Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:58422 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 17:55:18.907 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 17:55:18.907 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:531 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T14:55:18.835Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:58432 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 17:55:18.908 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:58444 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 17:55:18.908 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 17:55:18.909 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 17:55:18.909 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-25 17:55:18.911 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-25 17:55:18.912 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'oi...', ID: 3A4DB01CC82273D2A64A
2025-08-25 17:55:19.394 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 17:55:19.395 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:58444 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 17:55:19.395 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhum lead existente encontrado - será criado novo
2025-08-25 17:55:19.396 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhuma conversa existente - será criada nova
2025-08-25 17:55:19.610 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Nova conversa criada - ID: e43a707d-868a-405f-ba91-8a6048eef630
2025-08-25 17:55:19.611 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: e43a707d-868a-405f-ba91-8a6048eef630, Phone: 558182986181
2025-08-25 17:55:20.642 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 17:55:20.644 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:58444 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 17:55:20.646 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 17:55:20.646 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 17:55:20.646 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 17:55:21.112 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 17:55:21.113 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 17:55:21.113 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 17:55:21.121 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 17:55:21.122 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 17:55:21.122 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 17:55:21.122 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 17:55:21.123 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 17:55:21.123 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 17:55:21.123 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 17:55:21.123 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 17:55:21.129 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 17:55:21.372 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 17:55:22.005 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 17:55:22.571 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 17:55:23.105 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 17:55:23.133 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 17:55:23.134 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 17:55:23.134 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Não identificado'}
2025-08-25 17:55:23.135 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 17:55:23.135 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'oi...'
2025-08-25 17:55:23.137 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 17:55:23.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 2 mensagens
2025-08-25 17:55:23.138 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 17:55:23.141 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 17:55:23.144 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 17:55:23.145 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'None', Valor: None
2025-08-25 17:55:23.145 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 17:55:23.145 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: None, Histórico: 2 msgs
2025-08-25 17:55:23.146 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Iniciando criação de novo lead para 558182986181 com nome 'None'.
2025-08-25 17:55:23.376 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'name': None, 'lead_id': 'b3b25dc8-d507-457e-92fd-adbbb98c6877', 'table': 'leads', 'count': 1}
2025-08-25 17:55:23.376 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando criar lead no Kommo para o lead_id b3b25dc8-d507-457e-92fd-adbbb98c6877.
INFO:     10.11.0.4:58444 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 17:55:24.219 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 17:55:24.219 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
2025-08-25 17:55:24.220 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
2025-08-25 17:55:24.220 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
2025-08-25 17:55:30.278 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o se...'
2025-08-25 17:55:30.279 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 17:55:30.279 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'oi...' -> '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira,...'
2025-08-25 17:55:30.280 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o se...'
2025-08-25 17:55:31.696 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 17:55:32.305 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
INFO:     127.0.0.1:46216 - "GET /health HTTP/1.1" 200 OK
2025-08-25 17:55:40.461 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.69, 'message_length': 141, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 17:55:45.328 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 141, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 17:55:45.329 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 17:55:45.329 | ERROR    | app.services.message_buffer:_process_queue:84 | Erro ao processar queue para 558182986181: 'EmojiLogger' object has no attribute 'conversation_success'
2025-08-25 17:55:46.397 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:45658 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 17:55:59.253 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:54872 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 17:56:00.457 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 17:56:00.458 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:531 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T14:56:00.451Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:54872 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 17:56:00.482 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:54872 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 17:56:00.482 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 17:56:00.483 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 17:56:00.483 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'mateus', 'sender': '558182986181', 'type': 'text'}
2025-08-25 17:56:00.484 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 6}
2025-08-25 17:56:00.485 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'mateus...', ID: 3A5B9904A780BD0E9F18
2025-08-25 17:56:01.581 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 17:56:01.582 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:54872 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 17:56:01.583 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: b3b25dc8-d507-457e-92fd-adbbb98c6877, Nome: 'None'
2025-08-25 17:56:01.583 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhuma conversa existente - será criada nova
2025-08-25 17:56:01.833 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Nova conversa criada - ID: 224fe517-4467-4bf3-859b-740c90933f12
2025-08-25 17:56:01.833 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 224fe517-4467-4bf3-859b-740c90933f12, Phone: 558182986181
2025-08-25 17:56:01.834 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 17:56:01.835 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:54888 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 17:56:02.531 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:54872 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 17:56:02.534 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 17:56:02.534 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:535 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:54890 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 17:56:02.536 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 17:56:02.536 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 17:56:02.536 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 17:56:03.287 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 17:56:03.885 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 17:56:04.639 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 17:56:05.720 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 17:56:05.720 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 17:56:05.721 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 17:56:05.729 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 17:56:05.730 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 17:56:05.731 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 17:56:05.733 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 17:56:06.342 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 17:56:07.397 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 17:56:08.162 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 17:56:08.730 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 17:56:08.757 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 17:56:08.758 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 17:56:08.758 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': None}
2025-08-25 17:56:08.759 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 17:56:08.759 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'mateus...'
2025-08-25 17:56:08.760 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 17:56:08.760 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 2 mensagens
2025-08-25 17:56:08.761 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 17:56:08.761 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 17:56:08.763 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 17:56:08.763 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'None', Valor: None
2025-08-25 17:56:08.764 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Detectadas mudanças no lead b3b25dc8-d507-457e-92fd-adbbb98c6877. Sincronizando com o DB. | Data: {'changes': {'qualification_score': 10}}
2025-08-25 17:56:09.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead b3b25dc8-d507-457e-92fd-adbbb98c6877 atualizado no Supabase.
2025-08-25 17:56:09.003 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 17:56:09.004 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: None, Histórico: 2 msgs
2025-08-25 17:56:09.004 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 17:56:09.004 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 10}}
2025-08-25 17:56:09.005 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 10}}
2025-08-25 17:56:09.005 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
INFO:     127.0.0.1:34148 - "GET /health HTTP/1.1" 200 OK
2025-08-25 17:56:21.239 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Perfeito, Mateus! Para eu entender qual a melhor solução para você, me diz por favor...'
2025-08-25 17:56:21.240 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 17:56:21.241 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'mateus...' -> '<RESPOSTA_FINAL>Perfeito, Mateus! Para eu entender...'
2025-08-25 17:56:21.241 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Perfeito, Mateus! Para eu entender qual a melhor solução para você, me diz por favor...'
2025-08-25 17:56:22.737 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 17:56:22.958 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 17:56:33.141 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 4.94, 'message_length': 192, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:36166 - "GET /health HTTP/1.1" 200 OK
2025-08-25 17:56:40.477 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 192, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 17:56:40.477 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 17:56:40.478 | ERROR    | app.services.message_buffer:_process_queue:84 | Erro ao processar queue para 558182986181: 'EmojiLogger' object has no attribute 'conversation_success'
2025-08-25 17:56:41.619 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}