✅ Usando variáveis de ambiente do servidor (EasyPanel)
INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-21 19:34:05.195 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-21 19:34:05.199 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-21 19:34:05.199 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-21 19:34:05.447 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-21 19:34:05.448 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-21 19:34:05.448 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-21 19:34:05.448 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-21 19:34:05.448 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-21 19:34:05.448 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-21 19:34:05.471 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-21 19:34:05.477 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-21 19:34:05.477 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ ⚠️ FollowUp Services não iniciados: 'EmojiLogger' object has no attribute 'system_event'
2025-08-21 19:34:05.477 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 19:34:05.484 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDR: Falha no pré-aquecimento: 'EmojiLogger' object has no attribute 'system_event' | Data: {'component': 'AgenticSDR'}
2025-08-21 19:34:05.485 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em SDR IA Solar Prime: Erro na inicialização: 'EmojiLogger' object has no attribute 'system_event' | Data: {'component': 'SDR IA Solar Prime'}
ERROR:    Traceback (most recent call last):
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 732, in lifespan
    async with self.lifespan_context(app) as maybe_state:
  File "/usr/local/lib/python3.11/contextlib.py", line 210, in __aenter__
    return await anext(self.gen)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/app/main.py", line 103, in lifespan
    await test_agent.initialize()
  File "/app/app/agents/agentic_sdr_stateless.py", line 51, in initialize
    emoji_logger.system_event("🚀 Inicializando AgenticSDR Stateless...")
    ^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'EmojiLogger' object has no attribute 'system_event'

ERROR:    Application startup failed. Exiting.