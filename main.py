✅ Usando variáveis de ambiente do servidor (EasyPanel)
2025-08-25 18:27:47.894 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-25 18:27:49.038 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-25 18:27:49.044 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-25 18:27:49.044 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-25 18:27:49.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-25 18:27:49.890 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-25 18:27:49.890 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-25 18:27:49.890 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-25 18:27:49.890 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-25 18:27:49.891 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-25 18:27:49.915 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-25 18:27:49.924 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 18:27:49.924 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-25 18:27:49.924 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 18:27:49.925 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 18:27:49.933 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 18:27:49.934 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 18:27:49.934 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 18:27:49.936 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 18:27:49.937 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 18:27:49.937 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 18:27:49.937 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 18:27:49.937 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 18:27:50.135 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-25 18:27:50.140 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 18:27:50.410 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 18:27:51.611 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 18:27:52.151 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 18:27:52.664 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 18:27:52.703 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 18:27:52.705 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 18:27:52.705 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-25 18:27:52.705 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-25 18:27:52.705 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-25 18:27:52.712 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 18:27:52.713 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 18:27:52.713 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 18:27:52.722 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 18:27:52.722 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 18:27:52.722 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 18:27:52.723 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 18:27:52.723 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 18:27:52.723 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 18:27:52.723 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 18:27:52.724 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 18:27:52.726 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 18:27:53.344 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 18:27:53.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 18:27:54.395 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 18:27:54.925 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 18:27:54.956 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 18:27:54.958 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 18:27:54.958 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-25 18:27:54.959 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:36260 - "GET /health HTTP/1.1" 200 OK
2025-08-25 18:27:59.538 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 18:27:59.772 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:41136 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 18:27:59.773 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 18:28:00.012 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ CONTACTS_UPDATE ignorado - faltando: telefone válido. Phone: '', PushName: 'Mateus M'
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 18:28:00.625 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 18:28:00.635 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 18:28:00.636 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:549 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 18:28:04.116 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/presence-update HTTP/1.1" 200 OK
2025-08-25 18:28:04.269 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/messages-upsert HTTP/1.1" 200 OK
2025-08-25 18:28:04.270 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 18:28:04.270 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 18:28:04.270 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi', 'sender': '558182986181', 'type': 'text'}
2025-08-25 18:28:04.272 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 2}
2025-08-25 18:28:04.272 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: 'oi...', ID: 3A582642FD8623352847
2025-08-25 18:28:04.736 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 18:28:04.737 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:545 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T15:27:59.169Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41138 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 18:28:04.738 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-25 18:28:04.738 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:545 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T15:27:59.215Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:41136 - "POST /webhook/evolution/chats-update HTTP/1.1" 200 OK
2025-08-25 18:28:04.739 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhum lead existente encontrado - será criado novo
2025-08-25 18:28:04.740 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhuma conversa existente - será criada nova
2025-08-25 18:28:05.353 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Nova conversa criada - ID: c8dcb97d-3866-4e37-869e-a80a6c69a710
2025-08-25 18:28:05.354 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: c8dcb97d-3866-4e37-869e-a80a6c69a710, Phone: 558182986181
2025-08-25 18:28:07.073 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 18:28:07.073 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 18:28:07.073 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 18:28:07.535 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 18:28:07.535 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 18:28:07.536 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 18:28:07.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 18:28:07.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 18:28:07.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 18:28:07.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 18:28:07.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 18:28:07.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 18:28:07.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 18:28:07.545 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 18:28:07.548 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 18:28:08.200 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 18:28:08.758 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 18:28:09.650 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 18:28:10.387 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 18:28:10.421 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 18:28:10.422 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 18:28:10.423 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Não identificado'}
2025-08-25 18:28:10.424 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 18:28:10.424 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'oi...'
2025-08-25 18:28:10.425 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 18:28:10.426 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 2 mensagens
2025-08-25 18:28:10.426 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 18:28:10.432 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 18:28:10.435 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 18:28:10.435 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'None', Valor: None
2025-08-25 18:28:10.435 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 18:28:10.436 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: None, Histórico: 2 msgs
2025-08-25 18:28:10.436 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Iniciando criação de novo lead para 558182986181 com nome 'None'.
2025-08-25 18:28:10.670 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'name': None, 'lead_id': 'fa08a649-4a56-41fa-a97e-dc00d6cee27d', 'table': 'leads', 'count': 1}
2025-08-25 18:28:10.670 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando criar lead no Kommo para o lead_id fa08a649-4a56-41fa-a97e-dc00d6cee27d.
INFO:     10.11.0.4:35084 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 18:28:11.581 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 18:28:11.582 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
INFO:     10.11.0.4:35084 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 18:28:12.208 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
2025-08-25 18:28:12.208 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
2025-08-25 18:28:22.320 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Olá, boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar...'
2025-08-25 18:28:22.321 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 18:28:22.321 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'oi...' -> '<RESPOSTA_FINAL>Olá, boa tarde!! Me chamo Helen Vi...'
2025-08-25 18:28:22.321 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Olá, boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar...'
2025-08-25 18:28:24.182 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 18:28:24.808 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 18:28:24.810 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/connection-update de evolution-api | Data: {'event': 'CONNECTION_UPDATE', 'endpoint': '/whatsapp/connection-update', 'source': 'evolution-api'}
2025-08-25 18:28:24.810 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Connection status update: {'event': 'connection.update', 'instance': 'SDR IA SolarPrime', 'data': {'instance': 'SDR IA SolarPrime', 'state': 'connecting', 'statusReason': 200}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T15:28:23.149Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
2025-08-25 18:28:24.811 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/connection-update de evolution-api | Data: {'event': 'CONNECTION_UPDATE', 'endpoint': '/whatsapp/connection-update', 'source': 'evolution-api'}
2025-08-25 18:28:24.812 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Connection status update: {'event': 'connection.update', 'instance': 'SDR IA SolarPrime', 'data': {'instance': 'SDR IA SolarPrime', 'wuid': '558195554978@s.whatsapp.net', 'profileName': 'Mateus M', 'profilePictureUrl': None, 'state': 'open', 'statusReason': 200}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution', 'date_time': '2025-08-25T15:28:24.517Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:53886 - "POST /webhook/evolution/connection-update HTTP/1.1" 200 OK
INFO:     10.11.0.4:53894 - "POST /webhook/evolution/connection-update HTTP/1.1" 200 OK