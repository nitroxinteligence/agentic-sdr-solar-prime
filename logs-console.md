2025-08-25 20:37:58.661 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Erro de status 400 para POST https://evoapi-evolution-api.fzvgou.easypanel.host/chat/getBase64FromMediaMessage/SDR%20IA%20SolarPrime: {"status":400,"error":"Bad Request","response":{"message":["AggregateError"]}}
2025-08-25 20:37:58.662 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Exceção ao buscar mídia em base64: Client error '400 Bad Request' for url 'https://evoapi-evolution-api.fzvgou.easypanel.host/chat/getBase64FromMediaMessage/SDR%20IA%20SolarPrime'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/400
2025-08-25 20:37:58.663 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Falha no download de fallback para documentMessage: Não foi possível obter os bytes da mídia. | Data: {'component': 'Falha no download de fallback para documentMessage'}
2025-08-25 20:37:58.663 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido error de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'error'}
2025-08-25 20:37:58.664 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-25 20:37:58.664 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: '...', ID: 3A68963E5146F9336DE6
2025-08-25 20:37:59.356 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 9c2bb788-7efc-408c-859f-07669786b765, Nome: 'Mateus M'
2025-08-25 20:37:59.356 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: 25d7c06b-a1b0-4e38-b38c-0ed491591677
2025-08-25 20:37:59.357 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 25d7c06b-a1b0-4e38-b38c-0ed491591677, Phone: 558182986181
2025-08-25 20:38:00.005 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:38:00.005 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:38:00.005 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 20:38:00.986 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:38:01.590 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:38:02.190 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:38:03.443 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:38:03.444 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:38:03.444 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:38:03.452 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:38:03.452 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:38:03.452 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:38:03.453 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:38:03.453 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:38:03.453 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:38:03.453 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:38:03.454 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:38:03.456 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:38:03.915 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:38:04.629 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:38:05.211 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:38:05.999 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:38:06.037 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:38:06.038 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:38:06.038 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 17, 'lead_name': 'Mateus M'}
2025-08-25 20:38:06.038 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:38:06.038 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: '...'
2025-08-25 20:38:06.040 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:38:06.042 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: ❌ ERRO CRÍTICO NO AGENTE: Desculpe, não consegui obter a mídia que você enviou. | Data: {'traceback': 'Traceback (most recent call last):\n  File "/app/app/agents/agentic_sdr_stateless.py", line 128, in process_message\n    conversation_history, lead_info = await self._update_context(message, conversation_history, lead_info, execution_context.get("media"))\n                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/app/app/agents/agentic_sdr_stateless.py", line 196, in _update_context\n    raise ValueError(media_data.get("content", "Erro ao processar mídia."))\nValueError: Desculpe, não consegui obter a mídia que você enviou.\n', 'component': 'AgenticSDRStateless'}
2025-08-25 20:38:06.042 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ AGENTIC ERROR: 💥 FALHA NO PROCESSAMENTO - 558182986181: '...' -> ERRO: Desculpe, não consegui obter a mídia que você envi...