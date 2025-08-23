# tests/test_model_manager.py

import pytest
from unittest.mock import patch, AsyncMock
from app.core.model_manager import ModelManager, Gemini, OpenAI
from google.api_core.exceptions import ResourceExhausted

@pytest.mark.asyncio
@patch('app.core.model_manager.settings')
@patch.object(OpenAI, 'achat', new_callable=AsyncMock)
@patch.object(Gemini, 'achat', new_callable=AsyncMock)
async def test_get_response_fallback_on_gemini_quota_error(mock_gemini_achat, mock_openai_achat, mock_settings):
    """
    Tests if the ModelManager correctly falls back to OpenAI
    when the primary Gemini model fails with a ResourceExhausted (quota) error.
    """
    # 1. Arrange: Configure mocks
    mock_settings.primary_ai_model = "gemini-1.5-pro"
    mock_settings.fallback_ai_model = "o3-mini"
    mock_settings.openai_api_key = "fake-key"
    mock_settings.google_api_key = "fake-key"
    mock_settings.agno_reasoning_enabled = False

    mock_gemini_achat.side_effect = ResourceExhausted("Quota exceeded")
    
    # Mock the response object from OpenAI.achat
    mock_openai_response = AsyncMock()
    mock_openai_response.content = "Fallback successful"
    mock_openai_achat.return_value = mock_openai_response

    # 2. Act: Initialize the manager and call the method
    manager = ModelManager()
    manager.initialize()
    
    result = await manager.get_response(messages=[{"role": "user", "content": "Hello"}])

    # 3. Assert: Verify the fallback was used
    assert mock_gemini_achat.called
    mock_openai_achat.assert_called_once()
    assert result == "Fallback successful"
