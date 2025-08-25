2025-08-25 20:48:35.604 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Iniciando processamento de 1 nova(s) mensagem(ns)
2025-08-25 20:48:35.604 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Processando mensagem de 558182986181
2025-08-25 20:48:35.605 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando mídia. Message key: {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3ABBAFA2BF384251E840', 'senderLid': '129472024072320@lid'}
2025-08-25 20:48:35.605 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload para documentMessage sem mídia direta. Tentando endpoint getBase64FromMediaMessage.
2025-08-25 20:48:35.605 | ERROR    | app.utils.logger:log_with_emoji:75 | 🚨 Erro Evolution: Exceção inesperada ao buscar mídia em base64: 'EmojiLogger' object has no attribute 'evolution_info'
2025-08-25 20:48:35.605 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ get_media_as_base64 falhou para documentMessage. Tentando fallback com download_media...
2025-08-25 20:48:35.606 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando download direto da mídia para documentMessage
2025-08-25 20:48:35.606 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Iniciando download_media para tipo: document
2025-08-25 20:48:35.606 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Erro inesperado ao baixar mídia: EmojiLogger.system_info() takes 2 positional arguments but 3 were given: Tipo: TypeError | Data: {'component': 'Erro inesperado ao baixar mídia: EmojiLogger.system_info() takes 2 positional arguments but 3 were given'}
2025-08-25 20:48:35.606 | ERROR    | app.integrations.evolution:download_media:985 | EmojiLogger.system_info() takes 2 positional arguments but 3 were given
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
           │    └ <function Command.main at 0x72aa5be86480>
           └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1363, in main
    rv = self.invoke(ctx)
         │    │      └ <click.core.Context object at 0x72aa5ce365d0>
         │    └ <function Command.invoke at 0x72aa5be86160>
         └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1226, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           │   │      │    │           │   └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │   │      │    │           └ <click.core.Context object at 0x72aa5ce365d0>
           │   │      │    └ <function main at 0x72aa5b99e7a0>
           │   │      └ <Command main>
           │   └ <function Context.invoke at 0x72aa5be853a0>
           └ <click.core.Context object at 0x72aa5ce365d0>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 794, in invoke
    return callback(*args, **kwargs)
           │         │       └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │         └ ()
           └ <function main at 0x72aa5b99e7a0>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 410, in main
    run(
    └ <function run at 0x72aa5bea3880>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 577, in run
    server.run()
    │      └ <function Server.run at 0x72aa5bd70cc0>
    └ <uvicorn.server.Server object at 0x72aa5bee2250>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/server.py", line 65, in run
    return asyncio.run(self.serve(sockets=sockets))
           │       │   │    │             └ None
           │       │   │    └ <function Server.serve at 0x72aa5bd70d60>
           │       │   └ <uvicorn.server.Server object at 0x72aa5bee2250>
           │       └ <function run at 0x72aa5cb64ea0>
           └ <module 'asyncio' from '/usr/local/lib/python3.11/asyncio/__init__.py'>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           │      │   └ <coroutine object Server.serve at 0x72aa5bc8f5b0>
           │      └ <function Runner.run at 0x72aa5c0b0cc0>
           └ <asyncio.runners.Runner object at 0x72aa5b9af450>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           │    │     │                  └ <Task pending name='Task-1' coro=<Server.serve() running at /root/.local/lib/python3.11/site-packages/uvicorn/server.py:69> w...
           │    │     └ <cyfunction Loop.run_until_complete at 0x72aa5b9da330>
           │    └ <uvloop.Loop running=True closed=False debug=False>
           └ <asyncio.runners.Runner object at 0x72aa5b9af450>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi
    result = await app(  # type: ignore[func-returns-value]
                   └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x72aa3eb6cd10>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/middleware/proxy_headers.py", line 70, in __call__
    return await self.app(scope, receive, send)
                 │    │   │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4e20...
                 │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
                 │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
                 │    └ <fastapi.applications.FastAPI object at 0x72aa3b121ed0>
                 └ <uvicorn.middleware.proxy_headers.ProxyHeadersMiddleware object at 0x72aa3eb6cd10>
  File "/root/.local/lib/python3.11/site-packages/fastapi/applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
                           │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4e20...
                           │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
                           └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
  File "/root/.local/lib/python3.11/site-packages/starlette/applications.py", line 123, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <bound method RequestResponseCycle.send of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4e20...
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │    └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x72aa3af51690>
          └ <fastapi.applications.FastAPI object at 0x72aa3b121ed0>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/errors.py", line 164, in __call__
    await self.app(scope, receive, _send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x72aa59126660>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │    └ <starlette.middleware.cors.CORSMiddleware object at 0x72aa3af51210>
          └ <starlette.middleware.errors.ServerErrorMiddleware object at 0x72aa3af51690>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/cors.py", line 85, in __call__
    await self.app(scope, receive, send)
          │    │   │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x72aa59126660>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │    └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x72aa3af51490>
          └ <starlette.middleware.cors.CORSMiddleware object at 0x72aa3af51210>
  File "/root/.local/lib/python3.11/site-packages/starlette/middleware/exceptions.py", line 65, in __call__
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
          │                            │    │    │     │      │        └ <function ServerErrorMiddleware.__call__.<locals>._send at 0x72aa59126660>
          │                            │    │    │     │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │                            │    │    │     └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │                            │    │    └ <starlette.requests.Request object at 0x72aa3eb6e350>
          │                            │    └ <fastapi.routing.APIRouter object at 0x72aa3db1c610>
          │                            └ <starlette.middleware.exceptions.ExceptionMiddleware object at 0x72aa3af51490>
          └ <function wrap_app_handling_exceptions at 0x72aa5a946840>
  File "/root/.local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc7b00>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          └ <fastapi.routing.APIRouter object at 0x72aa3db1c610>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 756, in __call__
    await self.middleware_stack(scope, receive, send)
          │    │                │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc7b00>
          │    │                │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │    │                └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │    └ <bound method Router.app of <fastapi.routing.APIRouter object at 0x72aa3db1c610>>
          └ <fastapi.routing.APIRouter object at 0x72aa3db1c610>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 776, in app
    await route.handle(scope, receive, send)
          │     │      │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc7b00>
          │     │      │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │     │      └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │     └ <function Route.handle at 0x72aa5a947ec0>
          └ APIRoute(path='/webhook/evolution/{event_type}', name='whatsapp_dynamic_webhook', methods=['POST'])
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 297, in handle
    await self.app(scope, receive, send)
          │    │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc7b00>
          │    │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │    │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │    └ <function request_response.<locals>.app at 0x72aa3eb72200>
          └ APIRoute(path='/webhook/evolution/{event_type}', name='whatsapp_dynamic_webhook', methods=['POST'])
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 77, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
          │                            │    │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc7b00>
          │                            │    │        │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │                            │    │        └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          │                            │    └ <starlette.requests.Request object at 0x72aa3db32090>
          │                            └ <function request_response.<locals>.app.<locals>.app at 0x72aa3afc7920>
          └ <function wrap_app_handling_exceptions at 0x72aa5a946840>
  File "/root/.local/lib/python3.11/site-packages/starlette/_exception_handler.py", line 53, in wrapped_app
    await app(scope, receive, sender)
          │   │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc6480>
          │   │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │   └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          └ <function request_response.<locals>.app.<locals>.app at 0x72aa3afc7920>
  File "/root/.local/lib/python3.11/site-packages/starlette/routing.py", line 75, in app
    await response(scope, receive, send)
          │        │      │        └ <function wrap_app_handling_exceptions.<locals>.wrapped_app.<locals>.sender at 0x72aa3afc6480>
          │        │      └ <bound method RequestResponseCycle.receive of <uvicorn.protocols.http.httptools_impl.RequestResponseCycle object at 0x72aa3c4...
          │        └ {'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.4'}, 'http_version': '1.1', 'server': ('10.11.8.81', 8000), 'c...
          └ <starlette.responses.JSONResponse object at 0x72aa3afb6590>
  File "/root/.local/lib/python3.11/site-packages/starlette/responses.py", line 162, in __call__
    await self.background()
          │    └ <fastapi.background.BackgroundTasks object at 0x72aa3afa3ad0>
          └ <starlette.responses.JSONResponse object at 0x72aa3afb6590>
  File "/root/.local/lib/python3.11/site-packages/starlette/background.py", line 45, in __call__
    await task()
          └ <starlette.background.BackgroundTask object at 0x72aa38683710>
  File "/root/.local/lib/python3.11/site-packages/starlette/background.py", line 28, in __call__
    await self.func(*self.args, **self.kwargs)
          │    │     │    │       │    └ {}
          │    │     │    │       └ <starlette.background.BackgroundTask object at 0x72aa38683710>
          │    │     │    └ ({'key': {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3ABBAFA2BF384251E840', 'senderLid': '1294720240...
          │    │     └ <starlette.background.BackgroundTask object at 0x72aa38683710>
          │    └ <function process_new_message at 0x72aa3b11f420>
          └ <starlette.background.BackgroundTask object at 0x72aa38683710>

  File "/app/app/api/webhooks.py", line 898, in process_new_message
    media_data = await _handle_media_message(message)
                       │                     └ {'key': {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3ABBAFA2BF384251E840', 'senderLid': '12947202407...
                       └ <function _handle_media_message at 0x72aa3b11eb60>

  File "/app/app/api/webhooks.py", line 150, in _handle_media_message
    media_bytes = await evolution_client.download_media(media_payload, media_type)
                        │                │              │              └ 'document'
                        │                │              └ {'url': 'https://mmg.whatsapp.net/v/t62.7119-24/539016214_1077372274591924_4933382134214538917_n.enc?ccb=11-4&oh=01_Q5Aa2QH7d...
                        │                └ <function EvolutionAPIClient.download_media at 0x72aa3b11cb80>
                        └ <app.integrations.evolution.EvolutionAPIClient object at 0x72aa3b10f610>

> File "/app/app/integrations/evolution.py", line 930, in download_media
    emoji_logger.system_info(f"Baixando mídia de: {media_url[:50]}...", f"MediaKey presente: {bool(media_key)}")
    │            └ <classmethod(<function EmojiLogger.system_info at 0x72aa5a49e7a0>)>
    └ <app.utils.logger.EmojiLogger object at 0x72aa5a4c5cd0>

TypeError: EmojiLogger.system_info() takes 2 positional arguments but 3 were given
2025-08-25 20:48:35.647 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Erro no fallback download_media para documentMessage: Erro: EmojiLogger.system_error() missing 1 required positional argument: 'error' | Data: {'component': 'Erro no fallback download_media para documentMessage'}
2025-08-25 20:48:35.647 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em Falha total no download de mídia para documentMessage: Key: {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3ABBAFA2BF384251E840', 'senderLid': '129472024072320@lid'}, Mimetype: application/pdf | Data: {'component': 'Falha total no download de mídia para documentMessage'}
2025-08-25 20:48:35.647 | INFO     | app.utils.logger:log_with_emoji:75 | 📥 Recebido error de 558182986181 | Data: {'preview': '', 'sender': '558182986181', 'type': 'error'}
2025-08-25 20:48:35.649 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 20:48:35.649 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ 🚫 CONTACTS_UPDATE ignorado - Duplicata detectada para 558182986181@s.whatsapp.net (processado há 0.7s)
INFO:     10.11.0.4:56666 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 20:48:35.651 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 0}
2025-08-25 20:48:35.651 | INFO     | app.utils.logger:log_with_emoji:75 | 💬 🚀 INICIANDO PROCESSAMENTO PRINCIPAL - Telefone: 558182986181, Mensagem: '...', ID: 3ABBAFA2BF384251E840
2025-08-25 20:48:37.438 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:56666 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK
2025-08-25 20:48:37.439 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/chats-upsert de evolution-api | Data: {'event': 'CHATS_UPSERT', 'endpoint': '/whatsapp/chats-upsert', 'source': 'evolution-api'}
2025-08-25 20:48:37.439 | WARNING  | app.api.webhooks:whatsapp_dynamic_webhook:765 | Evento não reconhecido: CHATS_UPSERT
INFO:     10.11.0.4:56640 - "POST /webhook/evolution/chats-upsert HTTP/1.1" 200 OK
2025-08-25 20:48:37.440 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead encontrado - ID: 9c2bb788-7efc-408c-859f-07669786b765, Nome: 'Mateus M'
2025-08-25 20:48:37.441 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Conversa encontrada - ID: 25d7c06b-a1b0-4e38-b38c-0ed491591677
2025-08-25 20:48:37.441 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: 25d7c06b-a1b0-4e38-b38c-0ed491591677, Phone: 558182986181
2025-08-25 20:48:39.508 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 20:48:39.508 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 20:48:39.508 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 20:48:40.312 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 20:48:41.011 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 20:48:41.579 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:48:43.034 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 20:48:43.034 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 20:48:43.034 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 20:48:43.044 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 20:48:43.044 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 20:48:43.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 20:48:43.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 20:48:43.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 20:48:43.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 20:48:43.045 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 20:48:43.046 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 20:48:43.048 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 20:48:43.297 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 20:48:43.867 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
⚠️ Rate Limiter: Usando burst para kommo
2025-08-25 20:48:44.437 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
⚠️ Rate Limiter: Usando burst para kommo
INFO:     127.0.0.1:59618 - "GET /health HTTP/1.1" 200 OK
2025-08-25 20:48:46.019 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 20:48:46.056 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 20:48:46.057 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 20:48:46.057 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 19, 'lead_name': 'Mateus M'}
2025-08-25 20:48:46.058 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 20:48:46.058 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: '...'
2025-08-25 20:48:46.060 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 20:48:46.061 | ERROR    | app.utils.logger:log_with_emoji:75 | 💥 Erro em AgenticSDRStateless: ❌ ERRO CRÍTICO NO AGENTE: Não consegui baixar a documento que você enviou. Isso pode ser um problema temporário da Evolution API. Tente enviar novamente em alguns instantes. | Data: {'traceback': 'Traceback (most recent call last):\n  File "/app/app/agents/agentic_sdr_stateless.py", line 128, in process_message\n    conversation_history, lead_info = await self._update_context(message, conversation_history, lead_info, execution_context.get("media"))\n                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/app/app/agents/agentic_sdr_stateless.py", line 196, in _update_context\n    raise ValueError(media_data.get("content", "Erro ao processar mídia."))\nValueError: Não consegui baixar a documento que você enviou. Isso pode ser um problema temporário da Evolution API. Tente enviar novamente em alguns instantes.\n', 'component': 'AgenticSDRStateless'}
2025-08-25 20:48:46.061 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ AGENTIC ERROR: 💥 FALHA NO PROCESSAMENTO - 558182986181: '...' -> ERRO: Não consegui baixar a documento que você enviou. I...