#!/usr/bin/env python
"""
Teste para validar correção do campo 'type' em follow-ups
Verifica se o ConversationMonitor está criando follow-ups corretamente
"""

import asyncio
from datetime import datetime, timedelta
from app.services.conversation_monitor import ConversationMonitor
from app.database.supabase_client import SupabaseClient
from app.utils.logger import emoji_logger
import sys

async def test_followup_creation():
    """
    Testa a criação de follow-ups pelo ConversationMonitor
    """
    emoji_logger.system_info("🧪 TESTE DE CORREÇÃO DE FOLLOW-UPS")
    emoji_logger.system_info("=" * 60)
    
    # Inicializar componentes
    monitor = ConversationMonitor()
    db = SupabaseClient()
    
    # Número de teste
    test_phone = "5511999999999"  # Número de teste
    
    emoji_logger.system_info("📋 Preparando teste...")
    
    # 1. Garantir que existe um lead para teste
    emoji_logger.system_info("1️⃣ Criando/buscando lead de teste...")
    
    # Buscar ou criar lead
    lead_result = db.client.table('leads').select("*").eq('phone_number', test_phone).execute()
    
    if not lead_result.data:
        # Criar lead de teste
        lead_data = {
            'phone_number': test_phone,
            'name': 'Teste Follow-up Fix',
            'current_stage': 'INITIAL_CONTACT',
            'interested': True,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }
        
        create_result = db.client.table('leads').insert(lead_data).execute()
        
        if create_result.data:
            lead_id = create_result.data[0]['id']
            emoji_logger.system_success(f"✅ Lead de teste criado: {lead_id}")
        else:
            emoji_logger.system_error("Test", "❌ Falha ao criar lead de teste")
            return False
    else:
        lead_id = lead_result.data[0]['id']
        emoji_logger.system_info(f"✅ Lead existente encontrado: {lead_id}")
    
    # 2. Simular inatividade e agendar follow-up
    emoji_logger.system_info("2️⃣ Simulando inatividade e agendamento de follow-up...")
    
    # Registrar mensagem antiga (simular inatividade)
    monitor.active_conversations[test_phone] = datetime.now() - timedelta(minutes=31)
    
    # Testar agendamento direto
    try:
        await monitor._schedule_followup(test_phone, 'IMMEDIATE_REENGAGEMENT')
        emoji_logger.system_success("✅ Follow-up agendado via ConversationMonitor")
    except Exception as e:
        emoji_logger.system_error("Schedule", f"❌ Erro ao agendar: {e}")
        return False
    
    # 3. Verificar se o follow-up foi criado corretamente
    emoji_logger.system_info("3️⃣ Verificando follow-up no banco...")
    
    # Buscar follow-ups recentes para este lead
    followup_result = db.client.table('follow_ups')\
        .select("*")\
        .eq('lead_id', lead_id)\
        .order('created_at', desc=True)\
        .limit(1)\
        .execute()
    
    if followup_result.data:
        followup = followup_result.data[0]
        
        # Verificar campos críticos
        validations = []
        
        # Campo 'type' deve existir e não ser null
        if 'type' in followup and followup['type']:
            validations.append(("Campo 'type'", True, f"✅ Preenchido: {followup['type']}"))
        else:
            validations.append(("Campo 'type'", False, "❌ NULL ou ausente"))
        
        # Lead ID deve corresponder
        if followup.get('lead_id') == lead_id:
            validations.append(("Lead ID", True, "✅ Corresponde"))
        else:
            validations.append(("Lead ID", False, "❌ Não corresponde"))
        
        # Status deve ser 'pending'
        if followup.get('status') == 'pending':
            validations.append(("Status", True, "✅ pending"))
        else:
            validations.append(("Status", False, f"❌ {followup.get('status')}"))
        
        # Phone number deve existir
        if followup.get('phone_number'):
            validations.append(("Phone", True, f"✅ {followup['phone_number'][:8]}..."))
        else:
            validations.append(("Phone", False, "❌ Ausente"))
        
        # Mostrar resultados
        emoji_logger.system_info("\n📊 RESULTADOS DA VALIDAÇÃO:")
        emoji_logger.system_info("-" * 40)
        
        all_passed = True
        for name, passed, message in validations:
            emoji_logger.system_info(f"  {name}: {message}")
            if not passed:
                all_passed = False
        
        if all_passed:
            emoji_logger.system_success("\n✅ TESTE APROVADO! Campo 'type' corrigido com sucesso!")
            
            # Limpar follow-up de teste
            db.client.table('follow_ups').delete().eq('id', followup['id']).execute()
            emoji_logger.system_info("🧹 Follow-up de teste removido")
            
            return True
        else:
            emoji_logger.system_error("Validation", "\n❌ TESTE FALHOU! Verifique os erros acima")
            
            # Debug: mostrar estrutura completa
            emoji_logger.system_info("\n🔍 DEBUG - Estrutura do follow-up:")
            import json
            emoji_logger.system_info(json.dumps(followup, indent=2, default=str))
            
            return False
    else:
        emoji_logger.system_error("Database", "❌ Nenhum follow-up encontrado no banco")
        return False

async def main():
    """Executa o teste"""
    emoji_logger.system_info("🚀 INICIANDO TESTE DE CORREÇÃO DE FOLLOW-UPS")
    emoji_logger.system_info(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    emoji_logger.system_info("=" * 60)
    
    success = await test_followup_creation()
    
    emoji_logger.system_info("\n" + "=" * 60)
    if success:
        emoji_logger.system_success("🎉 CORREÇÃO VALIDADA COM SUCESSO!")
        emoji_logger.system_info("O campo 'type' está sendo preenchido corretamente.")
        emoji_logger.system_info("O sistema de follow-ups está funcionando!")
    else:
        emoji_logger.system_error("Test Failed", "💔 CORREÇÃO AINDA NÃO FUNCIONA")
        emoji_logger.system_info("Verifique os logs acima para detalhes.")
    
    return success

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)