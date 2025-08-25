#!/usr/bin/env python3
"""
Interceptador de webhook para capturar payloads reais do CONTACTS_UPDATE
"""

import json
from datetime import datetime
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/webhook/evolution/contacts-update")
async def intercept_contacts_update(request: Request):
    """Intercepta e registra payloads reais de CONTACTS_UPDATE"""
    try:
        # Capturar payload completo
        payload = await request.json()
        
        # Timestamp para identificar
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n{'='*60}")
        print(f"🕐 CONTACTS_UPDATE INTERCEPTADO - {timestamp}")
        print(f"{'='*60}")
        
        # Log do payload completo
        print(f"📦 PAYLOAD COMPLETO:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        
        # Análise específica dos campos
        print(f"\n🔍 ANÁLISE DETALHADA:")
        
        # Verificar estrutura de data
        data = payload.get('data', {})
        print(f"📊 Tipo de 'data': {type(data)}")
        print(f"📊 Conteúdo de 'data': {data}")
        
        if isinstance(data, list) and data:
            contact = data[0]
            print(f"\n👤 PRIMEIRO CONTATO:")
            print(f"   📱 ID: '{contact.get('id', 'AUSENTE')}'")
            print(f"   👤 pushName: '{contact.get('pushName', 'AUSENTE')}'")
            print(f"   📝 name: '{contact.get('name', 'AUSENTE')}'")
            print(f"   🔔 notify: '{contact.get('notify', 'AUSENTE')}'")
            
        elif isinstance(data, dict):
            print(f"\n📋 ESTRUTURA DICT:")
            for key, value in data.items():
                print(f"   🔑 {key}: {type(value)} = {value}")
                
                # Se for um dict aninhado, explorar mais
                if isinstance(value, dict):
                    print(f"      📱 ID: '{value.get('id', 'AUSENTE')}'")
                    print(f"      👤 pushName: '{value.get('pushName', 'AUSENTE')}'")
        
        # Salvar em arquivo para análise posterior
        filename = f"contacts_update_payload_{timestamp.replace(' ', '_').replace(':', '-')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Payload salvo em: {filename}")
        print(f"{'='*60}\n")
        
        return {"status": "intercepted", "timestamp": timestamp}
        
    except Exception as e:
        print(f"❌ Erro ao interceptar: {e}")
        return {"status": "error", "message": str(e)}

@app.post("/webhook/evolution/{event_type}")
async def intercept_all_webhooks(event_type: str, request: Request):
    """Intercepta todos os webhooks para análise"""
    if event_type == "contacts-update":
        return await intercept_contacts_update(request)
    
    payload = await request.json()
    print(f"📡 Webhook {event_type}: {json.dumps(payload, indent=2)}")
    return {"status": "ok", "event": event_type}

if __name__ == "__main__":
    print("🚀 Iniciando interceptador de webhook...")
    print("📡 Escutando em: http://localhost:8001")
    print("🎯 Endpoint: /webhook/evolution/contacts-update")
    print("\n⚠️  Configure a Evolution API para enviar webhooks para:")
    print("   http://localhost:8001/webhook/evolution/contacts-update")
    print("\n🔍 Aguardando webhooks...\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8001)
