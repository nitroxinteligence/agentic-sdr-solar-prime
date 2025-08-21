✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-21 14:35:39.008 | INFO     | app.utils.logger:log_with_emoji:140 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-21 14:35:39.014 | INFO     | app.integrations.redis_client:connect:39 | ✅ Conectado ao Redis com sucesso! URL: redis_redis:6379
2025-08-21 14:35:39.014 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Redis pronto
2025-08-21 14:35:39.913 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Supabase pronto
2025-08-21 14:35:39.913 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-21 14:35:39.914 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-21 14:35:40.590 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Message Splitter inicializado (max=200 chars, smart=ativada)
2025-08-21 14:35:40.591 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-21 14:35:40.591 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-21 14:35:40.616 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-21 14:35:40.624 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ FollowUp Scheduler pronto
2025-08-21 14:35:40.625 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-21 14:35:40.625 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 14:35:40.625 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado com persistência Redis pronto
2025-08-21 14:35:40.626 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-21 14:35:40.837 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Erro ao obter credenciais: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})
2025-08-21 14:35:40.838 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Credenciais não disponíveis para construir serviço
2025-08-21 14:35:40.839 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Não foi possível construir serviço - autorização OAuth necessária
2025-08-21 14:35:40.839 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: Erro ao conectar Google Calendar: OAuth 2.0 não autorizado. Execute /google/auth para autorizar
2025-08-21 14:35:40.839 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em AgenticSDRStateless: Erro na inicialização: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 14:35:40.840 | WARNING  | app.utils.logger:log_with_emoji:140 | ⚠️ ⚠️ FollowUp Services não iniciados: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given
2025-08-21 14:35:40.840 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 14:35:40.847 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Sistema: 🚀 Inicializando AgenticSDR Stateless...
2025-08-21 14:35:40.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 14:35:40.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 14:35:40.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 14:35:40.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 14:35:40.848 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 14:35:40.849 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 14:35:40.849 | INFO     | app.utils.logger:log_with_emoji:140 | ✅ 📊 ConversationMonitor inicializado com persistência Redis pronto
2025-08-21 14:35:40.849 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ ✅ ConversationMonitor: Loop de monitoramento iniciado
2025-08-21 14:35:41.035 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Erro ao obter credenciais: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})
2025-08-21 14:35:41.036 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Credenciais não disponíveis para construir serviço
2025-08-21 14:35:41.036 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: ❌ Não foi possível construir serviço - autorização OAuth necessária
2025-08-21 14:35:41.037 | ERROR    | app.utils.logger:log_with_emoji:140 | ❌ Service: Erro ao conectar Google Calendar: OAuth 2.0 não autorizado. Execute /google/auth para autorizar
2025-08-21 14:35:41.037 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em AgenticSDRStateless: Erro na inicialização: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given | Data: {'component': 'AgenticSDRStateless'}
2025-08-21 14:35:41.037 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em AgenticSDR: Falha no pré-aquecimento: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given | Data: {'component': 'AgenticSDR'}
2025-08-21 14:35:41.038 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em SDR IA Solar Prime: Erro na inicialização: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given | Data: {'component': 'SDR IA Solar Prime'}
ERROR:    Traceback (most recent call last):
  File "/app/app/decorators/error_handler.py", line 39, in wrapper
    result = await func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/app/services/calendar_service_100_real.py", line 52, in initialize
    raise Exception("OAuth 2.0 não autorizado. Execute /google/auth para autorizar")
Exception: OAuth 2.0 não autorizado. Execute /google/auth para autorizar

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 732, in lifespan
    async with self.lifespan_context(app) as maybe_state:
  File "/usr/local/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/app/main.py", line 103, in lifespan
    await test_agent.initialize()
  File "/app/app/agents/agentic_sdr_stateless.py", line 66, in initialize
    await self.calendar_service.initialize()
  File "/app/app/decorators/error_handler.py", line 50, in wrapper
    emoji_logger.system_warning(
TypeError: EmojiLogger.system_warning() takes 2 positional arguments but 3 were given

ERROR:    Application startup failed. Exiting.