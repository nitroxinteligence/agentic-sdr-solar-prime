INFO:     Started server process [1]
INFO:     Waiting for application startup.
2025-08-21 19:42:29.075 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando SDR IA Solar Prime v0.3
2025-08-21 19:42:29.080 | INFO     | app.integrations.redis_client:connect:35 | ✅ Conectado ao Redis: redis_redis:6379
2025-08-21 19:42:29.081 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Redis pronto
2025-08-21 19:42:29.338 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Supabase pronto
2025-08-21 19:42:29.339 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Buffer Inteligente inicializado (timeout=15.0s, max=10)
2025-08-21 19:42:29.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Buffer pronto | Data: {'timeout': '15.0s'}
2025-08-21 19:42:29.339 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Message Splitter inicializado (max=200, smart=ativada)
2025-08-21 19:42:29.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Message Splitter pronto | Data: {'max_length': 200}
2025-08-21 19:42:29.339 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema Refatorado pronto | Data: {'modules': 'Core + Services'}
2025-08-21 19:42:29.361 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔐 GoogleOAuthHandler inicializado
2025-08-21 19:42:29.367 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Scheduler pronto
2025-08-21 19:42:29.368 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 19:42:29.368 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 19:42:29.368 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 19:42:29.369 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 19:42:29.553 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 🔄 Access token renovado com sucesso
2025-08-21 19:42:29.557 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 19:42:29.831 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 19:42:30.906 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 19:42:31.191 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-21 19:42:31.474 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 19:42:31.534 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 19:42:31.535 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 19:42:31.535 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Worker pronto
2025-08-21 19:42:31.535 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ FollowUp Services (Scheduler & Worker) pronto
2025-08-21 19:42:31.535 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🔥 Pré-aquecendo AgenticSDR (Stateless)...
2025-08-21 19:42:31.543 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-21 19:42:31.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo prim ilde;rio Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-21 19:42:31.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-21 19:42:31.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': False, 'reasoning_enabled': True}
2025-08-21 19:42:31.544 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto
2025-08-21 19:42:31.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-21 19:42:31.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-21 19:42:31.545 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-21 19:42:31.545 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-21 19:42:31.548 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-21 19:42:31.832 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth: leonardofvieira00@gmail.com
2025-08-21 19:42:32.909 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-21 19:42:33.181 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
2025-08-21 19:42:33.472 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 20 estágios mapeados
2025-08-21 19:42:33.499 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-21 19:42:33.500 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-21 19:42:33.500 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AgenticSDR (Stateless) pronto | Data: {'status': 'sistema pronto'}
2025-08-21 19:42:33.500 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ SDR IA Solar Prime pronto | Data: {'startup_ms': 3000.0}
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:46950 - "GET /health HTTP/1.1" 200 OK
2025-08-21 19:42:43.326 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:40498 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-21 19:42:45.048 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-21 19:42:45.049 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CHATS_UPDATE update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:42:44.982Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40498 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-21 19:42:45.322 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 19:42:45.323 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:42:45.156Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40498 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-21 19:42:45.331 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:40498 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-21 19:42:45.331 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de nova mensagem
2025-08-21 19:42:45.332 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-21 19:42:45.332 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Webhook Message Processing: 'EmojiLogger' object has no attribute 'evolution_receive' | Data: {'component': 'Webhook Message Processing'}
2025-08-21 19:42:45.332 | ERROR    | app.api.webhooks:process_new_message:497 | Erro detalhado no processamento:
Traceback (most recent call last):

  File "/root/.local/bin/uvicorn", line 7, in <module>
    sys.exit(main())
    │   │    └ <Command main>
    │   └ <built-in function exit>
    └ <module 'sys' (built-in)>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1442, in __call__
    return self.main(*args, **kwargs)
           │    │     │       └ {}
           │    │     └ ()
           │    └ <function Command.main at 0x73b0f3a96480>
           └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1363, in main
    rv = self.invoke(ctx)
         │    │      └ <click.core.Context object at 0x73b0f4a967d0>
         │    └ <function Command.invoke at 0x73b0f3a96160>
         └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1226, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           │   │      │    │           │   └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │   │      │    │           └ <click.core.Context object at 0x73b0f4a967d0>
           │   │      │    └ <function main at 0x73b0f369a660>
           │   │      └ <Command main>
           │   └ <function Context.invoke at 0x73b0f3a953a0>
           └ <click.core.Context object at 0x73b0f4a967d0>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 794, in invoke
    return callback(*args, **kwargs)
           │         │       └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │         └ ()
           └ <function main at 0x73b0f369a660>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 410, in main
    run(
    └ <function run at 0x73b0f3a8b880>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 577, in run
    server.run()
    │      └ <function Server.run at 0x73b0f397ccc0>
    └ <uvicorn.server.Server object at 0x73b0f3ab2650>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/server.py", line 65, in run
    return asyncio.run(self.serve(sockets=sockets))
           │       │   │    │             └ None
           │       │   │    └ <function Server.serve at 0x73b0f397cd60>
           │       │   └ <uvicorn.server.Server object at 0x73b0f3ab2650>
           │       └ <function run at 0x73b0f46d0ea0>
           └ <module 'asyncio' from '/usr/local/lib/python3.11/asyncio/__init__.py'>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           │      │   └ <coroutine object Server.serve at 0x73b0f38775b0>
           │      └ <function Runner.run at 0x73b0f3d04cc0>
           └ <asyncio.runners.Runner object at 0x73b0f36aaf10>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           │    │     │                  └ <Task pending name='Task-1' coro=<Server.serve() running at /root/.local/lib/python3.11/site-packages/uvicorn/server.py:69> w...
           │    │     └ <cyfunction Loop.run_until_complete at 0x73b0f36d2260>
           │    └ <uvloop.Loop running=True closed=False debug=False>
           └ <asyncio.runners.Runner object at 0x73b0f36aaf10>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
                   └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x73b0d2b80310>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__
    return await self.app(scope, receive, send)
                 │    │   │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2ba0c...
                 │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
                 │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
                 │    └ <fastapi.applications.FastAPI object at 0x73b0d2cf7090>
                 └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x73b0d2b80310>
  File "/root/.local/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
                           │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2ba0c...
                           │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
                           └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
  File "/root/.local/lib/python3.11/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2ba0c...
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │    └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x73b0d2b08d50>
          └ <fastapi.applications.FastAPI object at 0x73b0d2cf7090>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x73b0d2cd28e0>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │    └ <starlette.middleware.cors.CORSMiddleware object at 0x73b0d2b77450>
          └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x73b0d2b08d50>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x73b0d2cd28e0>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │    └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x73b0d2b83b10>
          └ <starlette.middleware.cors.CORSMiddleware object at 0x73b0d2b77450>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
          │                            │    │    │     │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x73b0d2cd28e0>
          │                            │    │    │     │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │                            │    │    │     └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │                            │    │    └ <starlette.requests.Request object at 0x73b0d2c97d90>
          │                            │    └ <fastapi.routing.APIRouter object at 0x73b0d2cf4290>
          │                            └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x73b0d2b83b10>
          └ <function wrap_app_handling_exceptions at 0x73b0f25367a0>
  File "/root/.local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2b23f60>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          └ <fastapi.routing.APIRouter object at 0x73b0d2cf4290>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2b23f60>
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │    └ <bound method Router.app of <fastapi.routing.APIRouter object at 0x73b0d2cf4290>>
          └ <fastapi.routing.APIRouter object at 0x73b0d2cf4290>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
          │     │      │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2b23f60>
          │     │      │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │     │      └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │     └ <function Route.handle at 0x73b0f2537e20>
          └ APIRoute(path='/webhook/whatsapp/{event_type}', name='whatsapp_dynamic_webhook', methods=['POST'])
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2b23f60>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │    └ <function request_response.<locals>.app at 0x73b0ee508180>
          └ APIRoute(path='/webhook/whatsapp/{event_type}', name='whatsapp_dynamic_webhook', methods=['POST'])
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
          │                            │    │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2b23f60>
          │                            │    │        │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │                            │    │        └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          │                            │    └ <starlette.requests.Request object at 0x73b0d42ce190>
          │                            └ <function request_response.<locals>.app.<locals>.app at 0x73b0d2a094e0>
          └ <function wrap_app_handling_exceptions at 0x73b0f25367a0>
  File "/root/.local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2a093a0>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          └ <function request_response.<locals>.app.<locals>.app at 0x73b0d2a094e0>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 75, in app
    await response(scope, receive, send)
          │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x73b0d2a093a0>
          │        │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x73b0d2b...
          │        └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.6.109', 8000), '...
          └ <starlette.responses.JSONResponse object at 0x73b0d29264d0>
  File "/root/.local/lib/python3.11/site-packages/starlette/responses.py", line 162, in __call__
    await self.background()
          │    └ <fastapi.background.BackgroundTasks object at 0x73b0d2bef810>
          └ <starlette.responses.JSONResponse object at 0x73b0d29264d0>
  File "/root/.local/lib/python3.11/site-packages/starlette/background.py", line 45, in __call__
    await task()
          └ <starlette.background.BackgroundTask object at 0x73b0d2b3b110>
  File "/root/.local/lib/python3.11/site-packages/starlette/background.py", line 28, in __call__
    await self.func(*self.args, **self.kwargs)
          │    │     │    │       │    └ {}
          │    │     │    │       └ <starlette.background.BackgroundTask object at 0x73b0d2b3b110>
          │    │     │    └ ({'key': {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3AFDB6D0C91B450D13D9', 'senderLid': '1294720240...
          │    │     └ <starlette.background.BackgroundTask object at 0x73b0d2b3b110>
          │    └ <function process_new_message at 0x73b0d2cd2700>
          └ <starlette.background.BackgroundTask object at 0x73b0d2b3b110>

> File "/app/app/api/webhooks.py", line 464, in process_new_message
    emoji_logger.evolution_receive(
    └ <app.utils.logger.EmojiLogger object at 0x73b0f20bab90>

AttributeError: 'EmojiLogger' object has no attribute 'evolution_receive'
2025-08-21 19:42:45.465 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-21 19:42:45.465 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:384 | CONTACTS_UPDATE update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QEnyMBMF_9O8rTJPaDnSGGRwMO23qi7fr4Z1iAU643uLA&oe=68B48C0D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-21T16:42:45.459Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:40498 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK