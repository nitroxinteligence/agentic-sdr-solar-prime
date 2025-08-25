]
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data é lista com 1 itens
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Usando primeiro item da lista: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 19:36:11.627 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 1 - campo 'id' RAW: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 1 - telefone após limpeza: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2a - campo 'phone' RAW: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2a - telefone após limpeza: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2b - campo 'number' RAW: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2b - telefone após limpeza: ''
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Buscando em estruturas aninhadas
2025-08-25 19:36:11.628 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'contact': {}
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contact.id RAW: ''
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contact.phone RAW: ''
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'contactInfo': {}
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contactInfo.id RAW: ''
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contactInfo.phone RAW: ''
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'profile': {}
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - profile.id RAW: ''
2025-08-25 19:36:11.629 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - profile.phone RAW: ''
2025-08-25 19:36:11.630 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando encontrar telefone para pushName 'Mateus M' no cache
2025-08-25 19:36:11.630 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhum lead existente encontrado - será criado novo
2025-08-25 19:36:11.630 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhuma conversa existente - será criada nova
2025-08-25 19:36:11.860 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Nova conversa criada - ID: f63830f3-b91c-4d08-a238-0aed4f830067
2025-08-25 19:36:11.861 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Conversa validada - ID: f63830f3-b91c-4d08-a238-0aed4f830067, Phone: 558182986181
2025-08-25 19:36:11.861 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/contacts-update de evolution-api | Data: {'event': 'CONTACTS_UPDATE', 'endpoint': '/whatsapp/contacts-update', 'source': 'evolution-api'}
2025-08-25 19:36:11.862 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:36:11.862 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Payload RAW completo:
{
  "event": "contacts.update",
  "instance": "SDR IA SolarPrime",
  "data": {
    "remoteJid": "558182986181@s.whatsapp.net",
    "pushName": "Mateus M",
    "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
    "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
  },
  "destination": "https://sdr-api-evolution-api.fzvgou.easypanel.host/webhook/evolution",
  "date_time": "2025-08-25T16:36:10.727Z",
  "sender": "558195554978@s.whatsapp.net",
  "server_url": "https://evoapi-evolution-api.fzvgou.easypanel.host",
  "apikey": "3ECB607589F3-4D35-949F-BA5D2D5892E9"
}
2025-08-25 19:36:11.862 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tipo do payload: <class 'dict'>
2025-08-25 19:36:11.862 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves do payload: ['event', 'instance', 'data', 'destination', 'date_time', 'sender', 'server_url', 'apikey']
2025-08-25 19:36:11.862 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data inicial: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ contact_data final para processamento: {
  "remoteJid": "558182986181@s.whatsapp.net",
  "pushName": "Mateus M",
  "profilePicUrl": "https://pps.whatsapp.net/v/t61.24694-24/521428372_23966156116410343_3058739794538851299_n.jpg?ccb=11-4&oh=01_Q5Aa2QHIi5dnOiDR61SUnKqLCoT1mgqybVjIUUJdRMfeJAX6oQ&oe=68B9D20D&_nc_sid=5e03e0&_nc_cat=104",
  "instanceId": "02f1c146-f8b8-4f19-9e8a-d3517ee84269"
}
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Chaves disponíveis em contact_data: ['remoteJid', 'pushName', 'profilePicUrl', 'instanceId']
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === INÍCIO EXTRAÇÃO DE TELEFONE ===
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 1 - campo 'id' RAW: ''
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 1 - telefone após limpeza: ''
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2a - campo 'phone' RAW: ''
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2a - telefone após limpeza: ''
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2b - campo 'number' RAW: ''
2025-08-25 19:36:11.863 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 2b - telefone após limpeza: ''
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Buscando em estruturas aninhadas
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'contact': {}
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contact.id RAW: ''
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contact.phone RAW: ''
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'contactInfo': {}
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contactInfo.id RAW: ''
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - contactInfo.phone RAW: ''
2025-08-25 19:36:11.864 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - Verificando chave 'profile': {}
2025-08-25 19:36:11.865 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - profile.id RAW: ''
2025-08-25 19:36:11.865 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentativa 3 - profile.phone RAW: ''
2025-08-25 19:36:11.865 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando encontrar telefone para pushName 'Mateus M' no cache
2025-08-25 19:36:12.560 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone não encontrado no cache para pushName 'Mateus M'
2025-08-25 19:36:12.560 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando encontrar telefone para pushName 'Mateus M' em mensagens recentes
2025-08-25 19:36:12.783 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 19:36:12.783 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '' (válido: False)
2025-08-25 19:36:12.783 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 19:36:12.784 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:36:12.784 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === BUSCA REVERSA POR PUSHNAME ===
Tentando encontrar lead existente com nome 'Mateus M'
2025-08-25 19:36:13.023 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhum lead encontrado com nome similar a 'Mateus M'
INFO:     10.11.0.4:58228 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 19:36:13.024 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone não encontrado no cache para pushName 'Mateus M'
2025-08-25 19:36:13.025 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando encontrar telefone para pushName 'Mateus M' em mensagens recentes
2025-08-25 19:36:13.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === RESULTADO FINAL DA EXTRAÇÃO ===
2025-08-25 19:36:13.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Telefone extraído: '' (válido: False)
2025-08-25 19:36:13.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ PushName extraído: 'Mateus M' (válido: True)
2025-08-25 19:36:13.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === FIM ANÁLISE CONTACTS_UPDATE ===
2025-08-25 19:36:13.247 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ === BUSCA REVERSA POR PUSHNAME ===
Tentando encontrar lead existente com nome 'Mateus M'
2025-08-25 19:36:13.465 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Nenhum lead encontrado com nome similar a 'Mateus M'
INFO:     10.11.0.4:58238 - "POST /webhook/evolution/contacts-update HTTP/1.1" 200 OK
2025-08-25 19:36:13.467 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem e cache salvos
2025-08-25 19:36:13.467 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ Criando AGENTIC SDR Stateless...
2025-08-25 19:36:13.467 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ 🏭 Criando agente stateless com contexto...
2025-08-25 19:36:13.930 | INFO     | app.services.knowledge_service:__init__:24 | ✅ KnowledgeService inicializado (versão simplificada)
2025-08-25 19:36:13.931 | INFO     | app.utils.logger:log_with_emoji:75 | 🚀 Iniciando AgenticSDR Stateless
2025-08-25 19:36:13.931 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo primário Gemini configurado pronto | Data: {'model': 'gemini-2.5-pro'}
2025-08-25 19:36:13.939 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo fallback OpenAI configurado pronto | Data: {'model': 'o3-mini'}
2025-08-25 19:36:13.939 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Modelo reasoning configurado pronto | Data: {'model': 'gemini-2.0-flash-thinking'}
2025-08-25 19:36:13.939 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sistema de modelos configurado pronto | Data: {'primary_model': 'gemini-2.5-pro', 'fallback_available': True, 'reasoning_enabled': True}
2025-08-25 19:36:13.940 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🎨 MultimodalProcessor habilitado pronto | Data: {'dependencies': {'ocr': True, 'audio': True, 'pdf': True}}
2025-08-25 19:36:13.940 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 LeadManager inicializado pronto
2025-08-25 19:36:13.940 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 🧠 ContextAnalyzer inicializado pronto
2025-08-25 19:36:13.940 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ 📊 ConversationMonitor inicializado pronto
2025-08-25 19:36:13.940 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ ✅ ConversationMonitor: Loop iniciado
2025-08-25 19:36:13.943 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: ✅ Serviço Google Calendar construído com OAuth
2025-08-25 19:36:14.575 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: Google Calendar conectado via OAuth ao calendário: 'leonardofvieira00@gmail.com' | Data: {'calendar_id': 'leonardofvieira00@gmail.com'}
2025-08-25 19:36:16.221 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Kommo CRM conectado: leonardofvieira00
2025-08-25 19:36:16.747 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 9 campos customizados mapeados
2025-08-25 19:36:17.276 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Service: 📊 30 variações de estágios mapeadas
2025-08-25 19:36:17.310 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Service: ✅ Evolution API conectada: 1 instâncias
2025-08-25 19:36:17.311 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ AgenticSDR Stateless inicializado! pronto | Data: {'modules': ['ModelManager', 'MultimodalProcessor', 'LeadManager', 'ContextAnalyzer', 'CalendarService', 'CRMService', 'FollowUpService']}
2025-08-25 19:36:17.311 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Agente stateless criado com contexto pronto | Data: {'history_count': 1, 'lead_name': 'Não identificado'}
2025-08-25 19:36:17.311 | INFO     | app.utils.logger:log_with_emoji:75 | ⚙️ AGENTIC SDR Stateless pronto para uso
2025-08-25 19:36:17.311 | INFO     | app.utils.logger:log_with_emoji:75 | 🤖 AGENTIC SDR: 🤖 AGENTE STATELESS INICIADO - Mensagem: 'oi...'
2025-08-25 19:36:17.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem do usuário registrada
2025-08-25 19:36:17.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Mensagem adicionada ao histórico. Total: 2 mensagens
2025-08-25 19:36:17.313 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto analisado - Sentimento: {'enabled': True, 'sentiment': 'neutro', 'score': 0.0, 'confidence': 0.7}, Urgência: normal
2025-08-25 19:36:17.314 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 19:36:17.315 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Nenhum nome foi extraído do texto
2025-08-25 19:36:17.316 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado - Nome: 'None', Valor: None
2025-08-25 19:36:17.316 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ CONTEXTO ATUALIZADO - Histórico e lead_info finalizados
2025-08-25 19:36:17.316 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Contexto atualizado - Lead: None, Histórico: 2 msgs
2025-08-25 19:36:17.317 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Iniciando criação de novo lead para 558182986181 com nome 'None'.
2025-08-25 19:36:17.551 | INFO     | app.utils.logger:log_with_emoji:75 | 📝 1 registro(s) inserido(s) em leads | Data: {'phone': '558182986181', 'name': None, 'lead_id': '31e81ed1-6812-4929-9e27-10271a06fb24', 'table': 'leads', 'count': 1}
2025-08-25 19:36:17.551 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ Tentando criar lead no Kommo para o lead_id 31e81ed1-6812-4929-9e27-10271a06fb24.
INFO:     10.11.0.4:58238 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 19:36:18.395 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Sincronização externa concluída
2025-08-25 19:36:18.395 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Payload de atualização gerado. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
INFO:     10.11.0.4:58238 - "POST /webhook/kommo/events HTTP/1.1" 200 OK
2025-08-25 19:36:19.048 | INFO     | app.utils.logger:log_with_emoji:75 | ℹ️ CRM Sync: Dados do lead atualizados no Kommo. | Data: {'payload': {'phone': '558182986181', 'qualification_score': 0}}
2025-08-25 19:36:19.048 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Dados CRM sincronizados
INFO:     127.0.0.1:60278 - "GET /health HTTP/1.1" 200 OK
2025-08-25 19:36:22.888 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta LLM gerada: '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o se...'
2025-08-25 19:36:22.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente registrada
2025-08-25 19:36:22.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ AGENTIC SUCCESS: ✅ AGENTE STATELESS CONCLUÍDO - 558182986181: 'oi...' -> '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira,...'
2025-08-25 19:36:22.889 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada pelo agente: '<RESPOSTA_FINAL>Boa tarde!! Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o se...'
2025-08-25 19:36:23.935 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta do assistente salva
2025-08-25 19:36:24.169 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Lead atualizado
2025-08-25 19:36:32.500 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 2.92, 'message_length': 141, 'recipient': '558182986181', 'type': 'typing'}
2025-08-25 19:36:37.500 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando text para 558182986181 | Data: {'message_length': 141, 'delay_used': 5.0, 'recipient': '558182986181', 'type': 'text'}
2025-08-25 19:36:37.500 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta enviada via WhatsApp
2025-08-25 19:36:37.500 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ PROCESSAMENTO PRINCIPAL CONCLUÍDO - 558182986181: 'oi...' -> 'Boa tarde!! Me chamo Helen Vieira, sou consultora ...'
2025-08-25 19:36:38.324 | INFO     | app.utils.logger:log_with_emoji:75 | 📞 Webhook recebido: /whatsapp/messages-update de evolution-api | Data: {'event': 'MESSAGES_UPDATE', 'endpoint': '/whatsapp/messages-update', 'source': 'evolution-api'}
INFO:     10.11.0.4:34502 - "POST /webhook/evolution/messages-update HTTP/1.1" 200 OK