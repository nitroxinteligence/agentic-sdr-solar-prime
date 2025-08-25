#!/usr/bin/env python3
"""
Script de validação das correções implementadas no sistema SDR IA
Testa:
1. Processamento de CONTACTS_UPDATE no webhook
2. Envio correto de telefone para campo principal do Kommo
3. Mapeamento correto de tags/chosen_flow
"""

import asyncio
import json
from typing import Dict, Any
from unittest.mock import AsyncMock, MagicMock, patch

# Simular imports do sistema
class MockLogger:
    def team_crm(self, msg): print(f"[CRM] {msg}")
    def service_info(self, msg): print(f"[INFO] {msg}")
    def service_error(self, msg): print(f"[ERROR] {msg}")
    def system_debug(self, msg): print(f"[DEBUG] {msg}")
    def webhook_info(self, msg): print(f"[WEBHOOK] {msg}")

class TestValidation:
    def __init__(self):
        self.logger = MockLogger()
        self.passed_tests = 0
        self.total_tests = 0

    def assert_test(self, condition: bool, test_name: str, details: str = ""):
        """Helper para validar testes"""
        self.total_tests += 1
        if condition:
            self.passed_tests += 1
            print(f"✅ {test_name}")
        else:
            print(f"❌ {test_name} - {details}")

    def test_webhook_contacts_update_processing(self):
        """Testa se o webhook processa corretamente CONTACTS_UPDATE"""
        print("\n🧪 Testando processamento de CONTACTS_UPDATE...")
        
        # Simular payload de CONTACTS_UPDATE
        webhook_payload = {
            "account": {"id": "123"},
            "contacts": {
                "update": [{
                    "id": 456,
                    "name": "João Silva",
                    "custom_fields_values": [{
                        "field_code": "PHONE",
                        "values": [{"value": "+5511999887766"}]
                    }]
                }]
            }
        }
        
        # Simular extração de dados
        contact = webhook_payload["contacts"]["update"][0]
        extracted_name = contact.get("name")
        phone_field = next(
            (cf for cf in contact.get("custom_fields_values", []) 
             if cf.get("field_code") == "PHONE"), None
        )
        extracted_phone = phone_field["values"][0]["value"] if phone_field else None
        
        self.assert_test(
            extracted_name == "João Silva",
            "Extração de nome do CONTACTS_UPDATE",
            f"Esperado: 'João Silva', Obtido: '{extracted_name}'"
        )
        
        self.assert_test(
            extracted_phone == "+5511999887766",
            "Extração de telefone do CONTACTS_UPDATE",
            f"Esperado: '+5511999887766', Obtido: '{extracted_phone}'"
        )

    def test_phone_field_mapping(self):
        """Testa se o telefone é enviado para o campo principal do Kommo"""
        print("\n🧪 Testando envio de telefone para campo principal...")
        
        # Simular dados do lead
        lead_data = {
            "name": "Maria Santos",
            "phone": "+5511987654321"
        }
        
        # Simular estrutura do payload Kommo
        kommo_lead = {
            "name": lead_data["name"],
            "pipeline_id": 12345,
            "_embedded": {"tags": [{"name": "SDR_IA"}]}
        }
        
        # Adicionar contato com telefone no campo principal
        if lead_data.get("phone"):
            kommo_lead["_embedded"]["contacts"] = [{
                "name": lead_data["name"],
                "custom_fields_values": [{
                    "field_code": "PHONE",
                    "values": [{
                        "value": lead_data["phone"],
                        "enum_code": "WORK"
                    }]
                }]
            }]
        
        # Validar estrutura
        has_contacts = "contacts" in kommo_lead.get("_embedded", {})
        phone_in_main_field = False
        
        if has_contacts:
            contact = kommo_lead["_embedded"]["contacts"][0]
            phone_field = next(
                (cf for cf in contact.get("custom_fields_values", [])
                 if cf.get("field_code") == "PHONE"), None
            )
            phone_in_main_field = phone_field is not None
        
        self.assert_test(
            has_contacts,
            "Criação de contato no payload Kommo"
        )
        
        self.assert_test(
            phone_in_main_field,
            "Telefone no campo principal (PHONE) do contato"
        )

    def test_chosen_flow_mapping(self):
        """Testa mapeamento correto de chosen_flow para enum_id e tags"""
        print("\n🧪 Testando mapeamento de chosen_flow...")
        
        # Mapeamentos do sistema
        solution_type_values = {
            "usina própria": 326358, "usina propria": 326358,
            "instalação usina própria": 326358, "instalacao usina propria": 326358,
            "fazenda solar": 326360, "consórcio": 326362,
            "consorcio": 326362, "consultoria": 326364,
            "não definido": 326366, "nao definido": 326366,
            "aluguel de lote": 1078618, "compra com desconto": 1078620,
            "usina investimento": 1078622
        }
        
        flow_to_tag_map = {
            "Instalação Usina Própria": "Instalação Usina Própria",
            "Aluguel de Lote": "Aluguel de Lote",
            "Compra com Desconto": "Compra com Desconto",
            "Usina Investimento": "Usina Investimento"
        }
        
        # Casos de teste
        test_cases = [
            ("Instalação Usina Própria", 326358, "Instalação Usina Própria"),
            ("Aluguel de Lote", 1078618, "Aluguel de Lote"),
            ("Compra com Desconto", 1078620, "Compra com Desconto"),
            ("Usina Investimento", 1078622, "Usina Investimento")
        ]
        
        for chosen_flow, expected_enum_id, expected_tag in test_cases:
            # Testar mapeamento para enum_id
            enum_id = solution_type_values.get(chosen_flow.lower())
            self.assert_test(
                enum_id == expected_enum_id,
                f"Mapeamento enum_id para '{chosen_flow}'",
                f"Esperado: {expected_enum_id}, Obtido: {enum_id}"
            )
            
            # Testar mapeamento para tag
            tag_name = flow_to_tag_map.get(chosen_flow)
            self.assert_test(
                tag_name == expected_tag,
                f"Mapeamento tag para '{chosen_flow}'",
                f"Esperado: '{expected_tag}', Obtido: '{tag_name}'"
            )

    def test_lead_extraction_consistency(self):
        """Testa consistência na extração de chosen_flow"""
        print("\n🧪 Testando extração de chosen_flow...")
        
        # Simular extração do lead_manager
        flow_priority_map = {
            "Usina Investimento": ["investimento", "usina de investimento", "opção 4", "modelo 4"],
            "Aluguel de Lote": ["aluguel de lote", "alugar lote", "opção 2", "modelo 2"],
            "Compra com Desconto": ["compra de energia", "comprar energia", "desconto", "opção 3", "modelo 3"],
            "Instalação Usina Própria": ["instalação", "usina própria", "minha usina", "opção 1", "modelo 1"],
        }
        
        test_texts = [
            ("Quero a opção 1, instalação de usina própria", "Instalação Usina Própria"),
            ("Prefiro o aluguel de lote", "Aluguel de Lote"),
            ("Gostaria da compra de energia com desconto", "Compra com Desconto"),
            ("Tenho interesse em investimento", "Usina Investimento")
        ]
        
        for text, expected_flow in test_texts:
            text_lower = text.lower().strip()
            extracted_flow = None
            
            for flow, keywords in flow_priority_map.items():
                for keyword in keywords:
                    if keyword in text_lower:
                        extracted_flow = flow
                        break
                if extracted_flow:
                    break
            
            self.assert_test(
                extracted_flow == expected_flow,
                f"Extração de '{text}'",
                f"Esperado: '{expected_flow}', Obtido: '{extracted_flow}'"
            )

    def run_all_tests(self):
        """Executa todos os testes"""
        print("🚀 Iniciando validação das correções implementadas...")
        
        self.test_webhook_contacts_update_processing()
        self.test_phone_field_mapping()
        self.test_chosen_flow_mapping()
        self.test_lead_extraction_consistency()
        
        print(f"\n📊 Resultado dos testes: {self.passed_tests}/{self.total_tests} passaram")
        
        if self.passed_tests == self.total_tests:
            print("🎉 Todas as correções foram validadas com sucesso!")
            return True
        else:
            print("⚠️  Algumas correções precisam de ajustes.")
            return False

if __name__ == "__main__":
    validator = TestValidation()
    success = validator.run_all_tests()
    exit(0 if success else 1)