2025-08-15 18:12:31.393 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:34212 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-15 18:12:33.350 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/chats-update de evolution-api | Data: {'event': 'CHATS_UPDATE', 'endpoint': '/whatsapp/chats-update', 'source': 'evolution-api'}
2025-08-15 18:12:33.351 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:376 | Chat update recebido: {'event': 'chats.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, {'remoteJid': '558195554978@s.whatsapp.net', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:12:33.336Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:34212 - "POST /webhook/whatsapp/chats-update HTTP/1.1" 200 OK
2025-08-15 18:12:33.456 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/messages-upsert de evolution-api | Data: {'event': 'MESSAGES_UPSERT', 'endpoint': '/whatsapp/messages-upsert', 'source': 'evolution-api'}
INFO:     10.11.0.4:34212 - "POST /webhook/whatsapp/messages-upsert HTTP/1.1" 200 OK
2025-08-15 18:12:33.457 | INFO     | app.utils.logger:log_with_emoji:140 | 📥 Recebido text de 558182986181 | Data: {'preview': 'oi, boa tarde', 'sender': '558182986181', 'type': 'text'}
2025-08-15 18:12:33.677 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:12:33.678 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': [{'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}], 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:12:33.669Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:34212 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
2025-08-15 18:12:33.834 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-15 18:12:33.835 | INFO     | app.api.webhooks:whatsapp_dynamic_webhook:381 | Contacts update recebido: {'event': 'contacts.update', 'instance': 'SDR IA SolarPrime', 'data': {'remoteJid': '558182986181@s.whatsapp.net', 'pushName': 'Mateus M', 'profilePicUrl': 'https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHetiTNOyZCXsjDMgsMpMzUzypO7U4l_EpUwEcpr5xRCw&oe=68ACA30D&_nc_sid=5e03e0&_nc_cat=104', 'instanceId': '02f1c146-f8b8-4f19-9e8a-d3517ee84269'}, 'destination': 'https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/whatsapp', 'date_time': '2025-08-15T15:12:33.827Z', 'sender': '558195554978@s.whatsapp.net', 'server_url': 'https://evoapi-evolution-api.fzvgou.easypanel.host', 'apikey': '3ECB607589F3-4D35-949F-BA5D2D5892E9'}
INFO:     10.11.0.4:34212 - "POST /webhook/whatsapp/contacts-update HTTP/1.1" 200 OK
INFO:     127.0.0.1:40654 - "GET /health HTTP/1.1" 200 OK
2025-08-15 18:12:43.712 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Processando 1 mensagens combinadas | Data: {'phone': '558182986181', 'total_chars': 13}
2025-08-15 18:12:44.978 | INFO     | app.utils.logger:log_with_emoji:140 | ℹ️ Conversa validada - ID: 66827ec0-03d6-4506-ae4a-576cf092498a, Phone: 558182986181
2025-08-15 18:12:44.979 | INFO     | app.utils.logger:log_with_emoji:140 | 📞 Webhook recebido: /whatsapp/presence-update de evolution-api | Data: {'event': 'PRESENCE_UPDATE', 'endpoint': '/whatsapp/presence-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:35930 - "POST /webhook/whatsapp/presence-update HTTP/1.1" 200 OK
2025-08-15 18:12:46.444 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em Webhook: Erro ao criar agente com contexto: name 'create_stateless_agent' is not defined | Data: {'component': 'Webhook'}
2025-08-15 18:12:46.445 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em Agent Creation: Erro ao criar agente: name 'create_stateless_agent' is not defined | Data: {'component': 'Agent Creation'}
2025-08-15 18:12:46.445 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em Agent Message Processing: 503: Agente temporariamente indisponível | Data: {'component': 'Agent Message Processing'}
2025-08-15 18:12:46.445 | ERROR    | app.api.webhooks:process_message_with_agent:1394 | Erro detalhado no processamento com agente:
Traceback (most recent call last):

  File "/app/app/api/webhooks.py", line 639, in process_message_with_agent
    agentic, execution_context = await create_agent_with_context(
                                       └ <function create_agent_with_context at 0x741bef879760>

  File "/app/app/api/webhooks.py", line 285, in create_agent_with_context
    agent = await create_stateless_agent()  # Singleton

NameError: name 'create_stateless_agent' is not defined


During handling of the above exception, another exception occurred:


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
           │    └ <function Command.main at 0x741c0a70e480>
           └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1363, in main
    rv = self.invoke(ctx)
         │    │      └ <click.core.Context object at 0x741c0b378a90>
         │    └ <function Command.invoke at 0x741c0a70e160>
         └ <Command main>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 1226, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           │   │      │    │           │   └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │   │      │    │           └ <click.core.Context object at 0x741c0b378a90>
           │   │      │    └ <function main at 0x741c0a33a660>
           │   │      └ <Command main>
           │   └ <function Context.invoke at 0x741c0a70d3a0>
           └ <click.core.Context object at 0x741c0b378a90>
  File "/root/.local/lib/python3.11/site-packages/click/core.py", line 794, in invoke
    return callback(*args, **kwargs)
           │         │       └ {'host': '0.0.0.0', 'port': 8000, 'workers': 1, 'app': 'main:app', 'uds': None, 'fd': None, 'reload': False, 'reload_dirs': (...
           │         └ ()
           └ <function main at 0x741c0a33a660>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 410, in main
    run(
    └ <function run at 0x741c0a72b880>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/main.py", line 577, in run
    server.run()
    │      └ <function Server.run at 0x741c0a600cc0>
    └ <uvicorn.server.Server object at 0x741c0a76b290>
  File "/root/.local/lib/python3.11/site-packages/uvicorn/server.py", line 65, in run
    return asyncio.run(self.serve(sockets=sockets))
           │       │   │    │             └ None
           │       │   │    └ <function Server.serve at 0x741c0a600d60>
           │       │   └ <uvicorn.server.Server object at 0x741c0a76b290>
           │       └ <function run at 0x741c0b374ea0>
           └ <module 'asyncio' from '/usr/local/lib/python3.11/asyncio/__init__.py'>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           │      │   └ <coroutine object Server.serve at 0x741c0a51b5b0>
           │      └ <function Runner.run at 0x741c0a8c8cc0>
           └ <asyncio.runners.Runner object at 0x741c0a34b8d0>
  File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           │    │     │                  └ <Task pending name='Task-1' coro=<Server.serve() running at /root/.local/lib/python3.11/site-packages/uvicorn/server.py:69> w...
           │    │     └ <cyfunction Loop.run_until_complete at 0x741c0a376260>
           │    └ <uvloop.Loop running=True closed=False debug=False>
           └ <asyncio.runners.Runner object at 0x741c0a34b8d0>

  File "/app/app/services/message_buffer.py", line 112, in _process_queue
    await self._process_messages(phone, messages)
          │    │                 │      └ [{'content': 'oi, boa tarde', 'data': {'key': {'remoteJid': '558182986181@s.whatsapp.net', 'fromMe': False, 'id': '3A14083484...
          │    │                 └ '558182986181'
          │    └ <function MessageBuffer._process_messages at 0x741c076dd940>
          └ <app.services.message_buffer.MessageBuffer object at 0x741beec95910>

  File "/app/app/services/message_buffer.py", line 161, in _process_messages
    await process_message_with_agent(
          └ <function process_message_with_agent at 0x741bef87a200>

> File "/app/app/api/webhooks.py", line 646, in process_message_with_agent
    raise HTTPException(status_code=503, detail="Agente temporariamente indisponível")
          └ <class 'fastapi.exceptions.HTTPException'>

fastapi.exceptions.HTTPException: 503: Agente temporariamente indisponível
2025-08-15 18:12:46.459 | ERROR    | app.utils.logger:log_with_emoji:140 | 💥 Erro em Recovery failed: name 'create_agentic_sdr' is not defined | Data: {'component': 'Recovery failed'}
INFO:     127.0.0.1:55246 - "GET /health HTTP/1.1" 200 OK