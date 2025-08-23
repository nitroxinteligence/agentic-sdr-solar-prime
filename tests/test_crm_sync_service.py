# tests/test_crm_sync_service.py

import pytest
from app.services.crm_sync_service import crm_sync_service

def test_get_update_payload_with_chosen_flow_and_tag():
    """
    Tests that a chosen flow correctly adds the 'chosen_flow' field
    and the corresponding tag to the payload.
    """
    lead_info = {
        "chosen_flow": "Usina Investimento",
        "phone_number": "5511999998888"
    }
    payload = crm_sync_service.get_update_payload(lead_info, [])
    
    assert payload is not None
    assert payload["chosen_flow"] == "Usina Investimento"
    assert "tags" in payload
    assert "Usina Investimento" in payload["tags"]

def test_get_update_payload_with_bill_value():
    """
    Tests that a bill value is correctly added to the payload.
    """
    lead_info = {
        "bill_value": 550.75,
        "phone_number": "5511999998888"
    }
    payload = crm_sync_service.get_update_payload(lead_info, [])
    
    assert payload is not None
    assert payload["bill_value"] == 550.75

def test_get_update_payload_for_uninterested_lead():
    """
    Tests that a lead with stage 'NAO_INTERESSADO' gets the
    'sem-resposta' tag and the stage update.
    """
    lead_info = {
        "current_stage": "NAO_INTERESSADO",
        "phone_number": "5511999998888"
    }
    payload = crm_sync_service.get_update_payload(lead_info, [])
    
    assert payload is not None
    assert payload["current_stage"] == "NAO_INTERESSADO"
    assert "tags" in payload
    assert "sem-resposta" in payload["tags"]

def test_get_update_payload_all_fields():
    """
    Tests that all fields and tags are correctly combined in the payload.
    """
    lead_info = {
        "chosen_flow": "Aluguel de Lote",
        "bill_value": 1200.00,
        "phone_number": "5511999998888"
    }
    payload = crm_sync_service.get_update_payload(lead_info, [])
    
    assert payload is not None
    assert payload["chosen_flow"] == "Aluguel de Lote"
    assert payload["bill_value"] == 1200.00
    assert payload["phone"] == "5511999998888"
    assert "tags" in payload
    assert "Aluguel de Lote" in payload["tags"]

def test_get_update_payload_only_phone():
    """
    Tests that the payload only contains the phone if no other changes are needed.
    """
    lead_info = {
        "name": "Test Lead",
        "phone_number": "5511999998888"
    }
    payload = crm_sync_service.get_update_payload(lead_info, [])
    
    assert payload is not None
    assert payload == {"phone": "5511999998888"}
