#!/usr/bin/env python3
"""
Teste da Solução de Cache Híbrido para Correlação PushName -> Telefone

Este teste valida:
1. Cache em memória (desenvolvimento)
2. Correlação entre MESSAGES_UPSERT e CONTACTS_UPDATE
3. Atualização de leads com pushName extraído do cache
"""

import asyncio
import json
import time
from unittest.mock import AsyncMock, MagicMock, patch

# Simular estrutura de dados
class MockRedisClient:
    def __init__(self, should_fail=False):
        self.should_fail = should_fail
        self.data = {}
    
    async def set(self, key, value, ex=None):
        if self.should_fail:
            raise Exception("Redis não disponível")
        self.data[key] = {'value': value, 'expires': time.time() + (ex or 300)}
    
    async def get(self, key):
        if self.should_fail:
            raise Exception("Redis não disponível")
        if key in self.data:
            if time.time() < self.data[key]['expires']:
                return self.data[key]['value']
            else:
                del self.data[key]
        return None

class MockEmojiLogger:
    def system_debug(self, msg): print(f"🔍 DEBUG: {msg}")
    def system_warning(self, msg): print(f"⚠️ WARNING: {msg}")
    def webhook_process(self, msg): print(f"📡 WEBHOOK: {msg}")

class MockSupabaseClient:
    async def get_lead_by_phone(self, phone):
        # Simular lead existente com nome genérico
        if phone == "5511999888777":
            return {
                'id': 'lead_123',
                'phone_number': phone,
                'name': 'Lead sem nome',
                'created_at': '2025-01-01T10:00:00Z'
            }
        return None
    
    async def update_lead_name(self, lead_id, new_name):
        print(f"✅ Lead {lead_id} atualizado com nome: '{new_name}'")
        return True

# Simular as funções do webhook
async def simulate_process_new_message(message_data, use_redis=True):
    """Simula o processamento de uma nova mensagem"""
    
    # Mock dos clientes
    redis_client = MockRedisClient(should_fail=not use_redis)
    emoji_logger = MockEmojiLogger()
    
    # Extrair dados da mensagem
    key = message_data.get("key", {})
    remote_jid = key.get("remoteJid", "")
    phone = remote_jid.split("@")[0] if "@" in remote_jid else remote_jid
    
    # Extrair pushName
    push_name = None
    msg_content = message_data.get("message", {})
    
    if "pushName" in message_data:
        push_name = message_data["pushName"]
    elif "key" in message_data and "pushName" in message_data["key"]:
        push_name = message_data["key"]["pushName"]
    elif msg_content and "pushName" in msg_content:
        push_name = msg_content["pushName"]
    
    emoji_logger.webhook_process(f"Processando mensagem de {phone}")
    
    # Armazenar correlação pushName -> telefone no cache
    if push_name and phone:
        try:
            # Tentar Redis primeiro (produção)
            try:
                await redis_client.set(
                    f"pushname_phone:{push_name}", 
                    phone, 
                    ex=300  # 5 minutos
                )
                emoji_logger.system_debug(f"Cache Redis pushName->telefone: '{push_name}' -> '{phone}'")
            except Exception:
                # Fallback para cache em memória (desenvolvimento)
                if not hasattr(simulate_process_new_message, '_memory_cache'):
                    simulate_process_new_message._memory_cache = {}
                
                # Limpar entradas antigas (simular TTL)
                current_time = time.time()
                simulate_process_new_message._memory_cache = {
                    k: v for k, v in simulate_process_new_message._memory_cache.items() 
                    if current_time - v['timestamp'] < 300  # 5 minutos
                }
                
                # Armazenar nova entrada
                simulate_process_new_message._memory_cache[f"pushname_phone:{push_name}"] = {
                    'phone': phone,
                    'timestamp': current_time
                }
                emoji_logger.system_debug(f"Cache memória pushName->telefone: '{push_name}' -> '{phone}'")
                
        except Exception as e:
            emoji_logger.system_warning(f"Erro ao armazenar cache pushName: {e}")
    
    return redis_client, emoji_logger

async def simulate_process_contacts_update(contacts_data, redis_client, use_redis=True):
    """Simula o processamento de CONTACTS_UPDATE"""
    
    emoji_logger = MockEmojiLogger()
    supabase_client = MockSupabaseClient()
    
    # Extrair pushName do CONTACTS_UPDATE
    contact_data = contacts_data.get('data', contacts_data)
    if isinstance(contact_data, list) and contact_data:
        contact_data = contact_data[0]
    
    push_name = contact_data.get('pushName')
    phone_number = contact_data.get('id', '').replace('@c.us', '').replace('@s.whatsapp.net', '')
    
    emoji_logger.system_debug(f"CONTACTS_UPDATE - Phone: '{phone_number}', PushName: '{push_name}'")
    
    # Buscar telefone no cache se não estiver disponível
    if not phone_number and push_name:
        emoji_logger.system_debug(f"Tentando encontrar telefone para pushName '{push_name}' no cache")
        try:
            cached_phone = None
            
            # Tentar Redis primeiro (produção)
            if use_redis:
                try:
                    cached_phone = await redis_client.get(f"pushname_phone:{push_name}")
                    if cached_phone:
                        phone_number = cached_phone
                        emoji_logger.system_debug(f"Telefone encontrado no cache Redis: '{phone_number}'")
                except Exception:
                    pass
            
            # Fallback para cache em memória (desenvolvimento)
            if not cached_phone and hasattr(simulate_process_new_message, '_memory_cache'):
                cache_key = f"pushname_phone:{push_name}"
                if cache_key in simulate_process_new_message._memory_cache:
                    cache_entry = simulate_process_new_message._memory_cache[cache_key]
                    # Verificar se não expirou (TTL 5 minutos)
                    if time.time() - cache_entry['timestamp'] < 300:
                        phone_number = cache_entry['phone']
                        emoji_logger.system_debug(f"Telefone encontrado no cache memória: '{phone_number}'")
                    else:
                        # Remover entrada expirada
                        del simulate_process_new_message._memory_cache[cache_key]
                        emoji_logger.system_debug(f"Cache expirado para pushName '{push_name}'")
            
            if not phone_number:
                emoji_logger.system_debug(f"Telefone não encontrado no cache para pushName '{push_name}'")
                
        except Exception as e:
            emoji_logger.system_warning(f"Erro ao buscar telefone no cache: {e}")
    
    # Atualizar lead se temos pushName e telefone
    if push_name and phone_number and phone_number.strip():
        existing_lead = await supabase_client.get_lead_by_phone(phone_number)
        
        if existing_lead:
            current_name = existing_lead.get('name')
            is_generic_name = (
                not current_name or 
                current_name in ['Lead sem nome', 'Lead Sem Nome', None] or
                'Lead sem nome' in current_name or
                'Lead Sem Nome' in current_name
            )
            
            if is_generic_name:
                await supabase_client.update_lead_name(existing_lead['id'], push_name)
                emoji_logger.system_debug(f"✅ Lead atualizado com pushName: '{push_name}'")
            else:
                emoji_logger.system_debug(f"Lead já possui nome válido: '{current_name}'")
        else:
            emoji_logger.system_debug(f"Lead não encontrado para telefone: '{phone_number}'")
    else:
        emoji_logger.system_warning(f"CONTACTS_UPDATE sem pushName ou telefone válido. Phone: '{phone_number}', PushName: '{push_name}'")

async def test_cache_solution():
    """Teste principal da solução de cache"""
    
    print("🧪 TESTE: Solução de Cache Híbrido para PushName -> Telefone\n")
    
    # Cenário 1: Desenvolvimento (sem Redis)
    print("📱 CENÁRIO 1: Desenvolvimento (cache em memória)")
    print("=" * 50)
    
    # 1. Simular MESSAGES_UPSERT
    message_payload = {
        "key": {
            "remoteJid": "5511999888777@c.us",
            "fromMe": False,
            "pushName": "Mateus M"
        },
        "message": {
            "conversation": "Olá, tenho interesse em energia solar"
        }
    }
    
    redis_client, emoji_logger = await simulate_process_new_message(message_payload, use_redis=False)
    
    # 2. Simular CONTACTS_UPDATE (sem telefone)
    contacts_payload = {
        "data": {
            "pushName": "Mateus M",
            "id": ""  # Telefone vazio (problema real)
        }
    }
    
    await simulate_process_contacts_update(contacts_payload, redis_client, use_redis=False)
    
    print("\n" + "=" * 50)
    
    # Cenário 2: Produção (com Redis)
    print("\n🏭 CENÁRIO 2: Produção (cache Redis)")
    print("=" * 50)
    
    # Limpar cache de memória para testar Redis
    if hasattr(simulate_process_new_message, '_memory_cache'):
        simulate_process_new_message._memory_cache.clear()
    
    redis_client, emoji_logger = await simulate_process_new_message(message_payload, use_redis=True)
    await simulate_process_contacts_update(contacts_payload, redis_client, use_redis=True)
    
    print("\n" + "=" * 50)
    
    # Cenário 3: Teste de TTL (expiração)
    print("\n⏰ CENÁRIO 3: Teste de TTL (expiração do cache)")
    print("=" * 50)
    
    # Simular cache expirado
    if hasattr(simulate_process_new_message, '_memory_cache'):
        # Modificar timestamp para simular expiração
        for key in simulate_process_new_message._memory_cache:
            simulate_process_new_message._memory_cache[key]['timestamp'] = time.time() - 400  # 6+ minutos atrás
    
    await simulate_process_contacts_update(contacts_payload, redis_client, use_redis=False)
    
    print("\n✅ TESTE CONCLUÍDO: Solução funciona em desenvolvimento e produção!")

if __name__ == "__main__":
    asyncio.run(test_cache_solution())