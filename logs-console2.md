2025-08-23 16:03:44.537 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-23 16:03:45.438 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-23 16:03:45.444 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-23 16:03:45.444 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-23 16:03:46.291 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-23 16:03:46.291 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-23 16:03:46.291 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-23 16:03:46.292 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-23 16:03:46.292 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-23 16:03:46.292 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-23 16:03:46.314 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-23 16:03:46.320 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 16:03:46.320 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-23 16:03:46.320 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 16:03:46.320 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 16:03:46.326 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 16:03:46.327 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 16:03:46.327 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 16:03:46.327 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 16:03:46.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 16:03:46.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 16:03:46.328 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 16:03:46.328 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 16:03:46.516 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-23 16:03:46.520 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 16:03:47.157 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 16:03:48.982 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 80f8d8da-e503-44d7-96da-41dfa892805a
2025-08-23 16:03:48.982 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55818298... (Tentativa 1)
2025-08-23 16:03:48.983 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55818298...
2025-08-23 16:03:49.201 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:03:50.614 | INFO     | app.integrations.supabase_client:create_follow_up:325 | Follow-up criado: 46c242fc-47f4-4e56-a2f7-cc69c8903c65
2025-08-23 16:03:50.614 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up agendado: IMMEDIATE_REENGAGEMENT para 55819649... (Tentativa 1)
2025-08-23 16:03:50.617 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ⏰ Status Redis atualizado: followup_30min_sent para 55819649...
2025-08-23 16:03:50.945 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 16:03:51.570 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-23 16:03:52.100 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 16:03:52.153 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 16:03:52.154 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-23 16:03:52.154 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-23 16:03:52.154 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-23 16:03:52.154 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-23 16:03:52.162 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-23 16:03:52.163 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-23 16:03:52.163 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-23 16:03:52.170 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-23 16:03:52.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-23 16:03:52.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-23 16:03:52.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-23 16:03:52.171 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-23 16:03:52.172 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-23 16:03:52.172 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-23 16:03:52.172 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-23 16:03:52.176 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-23 16:03:52.803 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-23 16:03:53.019 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:03:53.639 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-23 16:03:54.204 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-23 16:03:54.746 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 32 variações de estágios mapeadas
2025-08-23 16:03:54.768 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-23 16:03:54.768 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
INFO:     Application startup complete.
2025-08-23 16:03:54.769 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-23 16:03:54.769 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:43988 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:04:02.763 | INFO     | app.services.followup_executor_service:enqueue_pending_followups:58 | 📋 2 follow-ups pendentes encontrados.
2025-08-23 16:04:03.946 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 80f8d8da-e503-44d7-96da-41dfa892805a enfileirado.
2025-08-23 16:04:04.548 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 80f8d8da-e503-44d7-96da-41dfa892805a
2025-08-23 16:04:06.953 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 ✅ Follow-up 46c242fc-47f4-4e56-a2f7-cc69c8903c65 enfileirado.
2025-08-23 16:04:10.377 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Tool parsing error: Erro de regex ao parsear tools: unbalanced parenthesis at position 20. Resposta: 

<RESPOSTA_FINAL>Claro! Sem problemas. Eu tinha perguntado qual destes quatro modelos de soluções energéticas seria do seu interesse: 1. Instalação de usina própria 2. Aluguel de lote para instalação... | Data: {'component': 'Tool parsing error'}
2025-08-23 16:04:22.595 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 8.89, 'message_length': 258, 'recipient': '558182986181', 'type': 'typing'}
INFO:     127.0.0.1:45430 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:04:33.666 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 258, 'delay_used': 2.44, 'recipient': '558182986181', 'type': 'text'}
2025-08-23 16:04:34.301 | ERROR    | app.integrations.supabase_client:update_follow_up_status:375 | Erro ao atualizar follow-up: Erro ao atualizar follow-up
2025-08-23 16:04:34.302 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro ao processar tarefa 80f8d8da-e503-44d7-96da-41dfa892805a: Erro ao atualizar follow-up | Data: {'component': 'FollowUp Worker'}
2025-08-23 16:04:34.885 | ERROR    | app.integrations.supabase_client:update_follow_up_status:375 | Erro ao atualizar follow-up: Erro ao atualizar follow-up
2025-08-23 16:04:34.887 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 16:04:34.887 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:46506 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 16:04:34.888 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:46508 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 16:04:34.889 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro no loop de consumo: Erro ao atualizar follow-up | Data: {'component': 'FollowUp Worker'}
2025-08-23 16:04:39.890 | INFO     | app.utils.logger:log_with_emoji:75 | 🔔 🚀 Processando tarefa de follow-up: 46c242fc-47f4-4e56-a2f7-cc69c8903c65
2025-08-23 16:04:40.125 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro não relacionado a quota. Todas as tentativas falharam: contents must not be empty
2025-08-23 16:04:40.125 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro ao chamar modelo: contents must not be empty
2025-08-23 16:04:40.126 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro no modelo primário: contents must not be empty
2025-08-23 16:04:40.126 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Modelo primário falhou. Acionando fallback para o3-mini.
2025-08-23 16:04:48.980 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Usando modelo fallback: o3-mini
2025-08-23 16:04:48.980 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Tool parsing error: Erro de regex ao parsear tools: unbalanced parenthesis at position 20. Resposta: <RESPOSTA_FINAL>Olá! Aqui é a Helen Vieira da Solarprime. Em que posso te ajudar hoje com a sua conta de luz e economia de energia?</RESPOSTA_FINAL>... | Data: {'component': 'Tool parsing error'}
2025-08-23 16:04:51.246 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:04:51.861 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:04:52.459 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
2025-08-23 16:04:54.039 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:04:54.645 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:04:55.252 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
2025-08-23 16:04:57.685 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558196491408 | Data: {'duration_seconds': 3.41, 'message_length': 115, 'recipient': '558196491408', 'type': 'typing'}
INFO:     127.0.0.1:47370 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:05:03.265 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558196491408 | Data: {'message_length': 115, 'delay_used': 5.0, 'recipient': '558196491408', 'type': 'text'}
2025-08-23 16:05:03.925 | ERROR    | app.integrations.supabase_client:update_follow_up_status:375 | Erro ao atualizar follow-up: Erro ao atualizar follow-up
2025-08-23 16:05:03.925 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro ao processar tarefa 46c242fc-47f4-4e56-a2f7-cc69c8903c65: Erro ao atualizar follow-up | Data: {'component': 'FollowUp Worker'}
2025-08-23 16:05:04.527 | ERROR    | app.integrations.supabase_client:update_follow_up_status:375 | Erro ao atualizar follow-up: Erro ao atualizar follow-up
2025-08-23 16:05:04.528 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/send-message de evolution-api | Data: {'event': 'SEND_MESSAGE', 'endpoint': '/whatsapp/send-message', 'source': 'evolution-api'}
2025-08-23 16:05:04.528 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: SEND_MESSAGE
INFO:     10.11.0.4:51100 - "POST /webhook/evolution/send-message HTTP/1.1" 200 OK
2025-08-23 16:05:04.529 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em FollowUp Worker: Erro no loop de consumo: Erro ao atualizar follow-up | Data: {'component': 'FollowUp Worker'}
INFO:     127.0.0.1:60934 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:05:53.069 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:05:53.310 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:05:53.531 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
2025-08-23 16:05:55.847 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:05:56.683 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:05:57.283 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
INFO:     127.0.0.1:37078 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:60084 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:06:53.761 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:06:53.980 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:06:54.566 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
2025-08-23 16:06:57.512 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:06:57.730 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:06:57.954 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
INFO:     127.0.0.1:55592 - "GET /health HTTP/1.1" 200 OK
INFO:     127.0.0.1:47114 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:07:55.300 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:07:55.865 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:07:56.405 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
2025-08-23 16:07:58.494 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55818298...
2025-08-23 16:07:58.699 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819813...
2025-08-23 16:07:59.271 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ Lead não encontrado para monitoramento: 55819649...
INFO:     127.0.0.1:48018 - "GET /health HTTP/1.1" 200 OK
2025-08-23 16:08:06.918 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:48036 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 16:08:06.920 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:48046 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-23 16:08:06.921 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-23 16:08:06.922 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:355 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:48058 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
INFO:     127.0.0.1:38280 - "GET /health HTTP/1.1" 200 OK