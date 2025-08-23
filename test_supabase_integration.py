
import asyncio
import pytest
from datetime import datetime, timedelta
from uuid import uuid4
from app.integrations.supabase_client import SupabaseClient

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
async def supabase_client():
    client = SupabaseClient()
    # Forçar a inicialização se necessário (opcional, dependendo da implementação)
    # await client.initialize() 
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_full_lead_lifecycle(supabase_client: SupabaseClient):
    """
    Testa o ciclo de vida completo de um lead:
    Criação -> Leitura -> Atualização -> Criação de Entidades Relacionadas -> Limpeza
    """
    # --- DADOS DE TESTE ---
    test_phone = f"551199999{datetime.now().strftime('%f')[-4:]}"
    lead_data = {
        "phone_number": test_phone,
        "name": "Lead de Teste Automatizado",
        "email": f"teste.{uuid4().hex[:6]}@example.com",
        "bill_value": 500.50,
        "current_stage": "INITIAL_CONTACT",
        "qualification_status": "PENDING"
    }
    lead_id = None
    conversation_id = None

    try:
        # 1. CRIAÇÃO DO LEAD
        print(f"\n[TESTE] Criando lead para {test_phone}...")
        created_lead = await supabase_client.create_lead(lead_data)
        assert created_lead is not None
        assert "id" in created_lead
        lead_id = created_lead["id"]
        print(f"✅ Lead criado com sucesso. ID: {lead_id}")

        # 2. LEITURA DO LEAD
        print(f"\n[TESTE] Buscando lead pelo telefone {test_phone}...")
        fetched_lead = await supabase_client.get_lead_by_phone(test_phone)
        assert fetched_lead is not None
        assert fetched_lead["id"] == lead_id
        assert fetched_lead["name"] == "Lead de Teste Automatizado"
        print("✅ Lead encontrado com sucesso.")

        # 3. ATUALIZAÇÃO DO LEAD
        print(f"\n[TESTE] Atualizando lead ID: {lead_id}...")
        update_data = {"current_stage": "QUALIFYING", "qualification_score": 75}
        updated_lead = await supabase_client.update_lead(lead_id, update_data)
        assert updated_lead is not None
        assert updated_lead["current_stage"] == "QUALIFYING"
        assert updated_lead["qualification_score"] == 75
        print("✅ Lead atualizado com sucesso.")

        # 4. CRIAÇÃO DE CONVERSA
        print(f"\n[TESTE] Criando conversa para o lead...")
        conversation = await supabase_client.get_or_create_conversation(test_phone, lead_id)
        assert conversation is not None
        assert "id" in conversation
        conversation_id = conversation["id"]
        print(f"✅ Conversa criada com sucesso. ID: {conversation_id}")

        # 5. SALVANDO MENSAGEM
        print(f"\n[TESTE] Salvando mensagem na conversa...")
        message_data = {
            "conversation_id": conversation_id,
            "role": "user",
            "content": "Olá, gostaria de um orçamento."
        }
        saved_message = await supabase_client.save_message(message_data)
        assert saved_message is not None
        assert saved_message["role"] == "user"
        print("✅ Mensagem salva com sucesso.")

        # 6. CRIAÇÃO DE FOLLOW-UP
        print(f"\n[TESTE] Criando follow-up para o lead...")
        follow_up_data = {
            "lead_id": lead_id,
            "scheduled_at": (datetime.now() + timedelta(days=1)).isoformat(),
            "type": "check_in",
            "message": "Olá, tudo bem? Alguma novidade sobre o orçamento?",
            "status": "pending"
        }
        created_follow_up = await supabase_client.create_follow_up(follow_up_data)
        assert created_follow_up is not None
        assert created_follow_up["status"] == "pending"
        print("✅ Follow-up criado com sucesso.")

        # 7. CRIAÇÃO DE QUALIFICAÇÃO
        print(f"\n[TESTE] Criando qualificação para o lead...")
        qualification_data = {
            "lead_id": lead_id,
            "qualification_status": "QUALIFIED",
            "score": 90,
            "notes": "Lead muito interessado, agendou reunião."
        }
        created_qualification = await supabase_client.create_lead_qualification(qualification_data)
        assert created_qualification is not None
        assert created_qualification["score"] == 90
        print("✅ Qualificação criada com sucesso.")

        # 8. LOG DE EVENTO DE ANALYTICS
        print(f"\n[TESTE] Registrando evento de analytics...")
        event_data = {
            "lead_id": lead_id,
            "event_type": "MEETING_SCHEDULED",
            "event_category": "MEETING",
            "event_data": {"calendar_event_id": "12345"}
        }
        logged_event = await supabase_client.log_event(event_data)
        assert logged_event is not None
        assert logged_event["event_type"] == "MEETING_SCHEDULED"
        print("✅ Evento de analytics registrado com sucesso.")

    finally:
        # --- LIMPEZA ---
        if lead_id:
            print(f"\n[LIMPEZA] Deletando lead de teste ID: {lead_id} e dados relacionados...")
            # A deleção do lead deve cascatear para as outras tabelas
            # devido às constraints 'on delete CASCADE'
            try:
                # A API do Supabase Python não tem um método 'delete' direto que retorna dados.
                # Executamos e verificamos se não há erro.
                response = supabase_client.client.table('leads').delete().eq('id', lead_id).execute()
                # A resposta de delete bem-sucedido geralmente tem dados vazios e nenhum erro
                assert response.data is not None
                
                # Verificação extra para garantir que foi deletado
                deleted_lead = await supabase_client.get_lead_by_phone(test_phone)
                assert deleted_lead is None
                
                print(f"✅ Lead {lead_id} e dados associados deletados com sucesso.")
            except Exception as e:
                print(f"⚠️ Erro durante a limpeza do lead {lead_id}: {e}")

