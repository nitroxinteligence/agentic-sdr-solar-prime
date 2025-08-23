# tests/test_followup_system.py

import pytest
import asyncio
from unittest.mock import AsyncMock, patch, MagicMock
from datetime import datetime, timedelta

from app.services.followup_manager import FollowUpManagerService
from app.services.followup_worker import FollowUpWorker
from app.integrations.supabase_client import SupabaseClient
from app.config import settings

@pytest.fixture
def mock_supabase_client():
    """Mock SupabaseClient para testes."""
    mock_db = AsyncMock(spec=SupabaseClient)
    return mock_db

@pytest.fixture
def mock_redis_client():
    """Mock RedisClient para testes."""
    mock_redis = AsyncMock()
    mock_redis.acquire_lock.return_value = True
    mock_redis.release_lock.return_value = True
    return mock_redis

@pytest.fixture
def mock_agent():
    """Mock AgenticSDRStateless para testes."""
    mock_agent_instance = AsyncMock()
    mock_agent_instance._generate_response.return_value = "Generated followup message."
    return mock_agent_instance

@pytest.fixture(autouse=True)
def mock_settings():
    """Mock settings para testes."""
    with patch('app.config.settings') as mock_s:
        mock_s.max_follow_up_attempts = 3
        yield mock_s

@pytest.mark.asyncio
async def test_followup_manager_schedules_within_limit(mock_supabase_client, mock_settings):
    """
    Testa se o FollowUpManagerService agenda follow-ups quando dentro do limite.
    """
    mock_supabase_client.get_recent_followup_count.return_value = 0
    mock_supabase_client.create_follow_up.return_value = {"id": "new_followup_id"}

    manager = FollowUpManagerService()
    manager.db = mock_supabase_client

    lead_id = "test_lead_id"
    phone_number = "5511999999999"
    inactive_since = datetime.now() - timedelta(minutes=35)
    current_status = "active"

    await manager.handle_conversation_inactivity(lead_id, phone_number, inactive_since, current_status)

    mock_supabase_client.get_recent_followup_count.assert_called_once_with(lead_id, inactive_since.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=7))
    mock_supabase_client.create_follow_up.assert_called_once()
    assert mock_supabase_client.create_follow_up.call_args[0][0]['follow_up_type'] == 'IMMEDIATE_REENGAGEMENT'

@pytest.mark.asyncio
async def test_followup_manager_does_not_schedule_if_limit_reached(mock_supabase_client, mock_settings):
    """
    Testa se o FollowUpManagerService não agenda follow-ups se o limite for atingido.
    """
    mock_supabase_client.get_recent_followup_count.return_value = mock_settings.max_follow_up_attempts
    mock_supabase_client.create_follow_up.reset_mock()

    manager = FollowUpManagerService()
    manager.db = mock_supabase_client

    lead_id = "test_lead_id"
    phone_number = "5511999999999"
    inactive_since = datetime.now() - timedelta(minutes=35)
    current_status = "active"

    await manager.handle_conversation_inactivity(lead_id, phone_number, inactive_since, current_status)

    mock_supabase_client.get_recent_followup_count.assert_called_once()
    mock_supabase_client.create_follow_up.assert_not_called()

@pytest.mark.asyncio
async def test_followup_worker_generates_intelligent_message(mock_supabase_client, mock_agent, mock_redis_client):
    """
    Testa se o FollowUpWorker gera uma mensagem inteligente e contextualizada.
    """
    worker = FollowUpWorker()
    worker.db = mock_supabase_client
    worker.agent = mock_agent
    worker.redis = mock_redis_client

    # Mock data
    lead_info = {
        "id": "lead_123",
        "name": "João",
        "phone_number": "5511987654321",
        "bill_value": 750.0,
        "chosen_flow": "Instalação Usina Própria"
    }
    conversation_history = [
        {"role": "user", "content": "Olá, gostaria de saber sobre energia solar.", "timestamp": (datetime.now() - timedelta(hours=1)).isoformat()},
        {"role": "assistant", "content": "Perfeito, João! Qual o valor da sua conta de luz?", "timestamp": (datetime.now() - timedelta(minutes=59)).isoformat()}
    ]
    task_payload = {
        "followup_id": "task_456",
        "lead_id": "lead_123",
        "phone_number": "5511987654321",
        "followup_type": "IMMEDIATE_REENGAGEMENT",
        "message": ""
    }

    mock_supabase_client.get_lead_by_id.return_value = lead_info
    mock_supabase_client.get_conversation_by_phone.return_value = {"id": "conv_789"}
    mock_supabase_client.get_conversation_messages.return_value = conversation_history

    # Mock extract_final_response from app.api.webhooks
    with patch('app.api.webhooks.extract_final_response', return_value="Generated message from LLM") as mock_extract_final_response:
        message_content = await worker._generate_intelligent_followup_message(task_payload)

        mock_supabase_client.get_lead_by_id.assert_called_once_with("lead_123")
        mock_supabase_client.get_conversation_messages.assert_called_once_with("conv_789")
        mock_agent._generate_response.assert_called_once()
        
        # Verify the prompt content
        llm_prompt = mock_agent._generate_response.call_args[0][0] # The 'message' argument to _generate_response
        assert "Você é a Helen Vieira" in llm_prompt
        assert "Nome: João" in llm_prompt
        assert "Valor da Conta de Energia: R$750.0" in llm_prompt
        assert "Fluxo Escolhido: Instalação Usina Própria" in llm_prompt
        assert "O Lead: Olá, gostaria de saber sobre energia solar." in llm_prompt
        assert "Você: Perfeito, João! Qual o valor da sua conta de luz?" in llm_prompt
        assert "IMMEDIATE_REENGAGEMENT" in llm_prompt
        assert "reabrir a conversa de forma natural, referenciando o último ponto" in llm_prompt

        assert message_content == "Generated message from LLM"
        mock_extract_final_response.assert_called_once_with("Generated followup message.")

@pytest.mark.asyncio
async def test_followup_worker_uses_predefined_message_for_meeting_reminder(mock_supabase_client, mock_agent, mock_redis_client):
    """
    Testa se o FollowUpWorker usa a mensagem pré-definida para lembretes de reunião.
    """
    worker = FollowUpWorker()
    worker.db = mock_supabase_client
    worker.agent = mock_agent
    worker.redis = mock_redis_client

    task_payload = {
        "followup_id": "task_meeting",
        "lead_id": "lead_456",
        "phone_number": "5511987654321",
        "followup_type": "MEETING_REMINDER",
        "message": "Sua reunião é amanhã às 10h. Link: meet.google.com/abc"
    }

    message_content = await worker._generate_intelligent_followup_message(task_payload)

    mock_agent._generate_response.assert_not_called() # LLM não deve ser chamado
    assert message_content == "Sua reunião é amanhã às 10h. Link: meet.google.com/abc"
