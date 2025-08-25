#!/usr/bin/env python3
"""
Script para testar e debugar o processamento de CONTACTS_UPDATE
"""

import asyncio
import json
from typing import Dict, Any
from app.api.webhooks import process_contacts_update
from app.utils.logger import emoji_logger


class ContactsUpdateTester:
    """Testa diferentes formatos de payload CONTACTS_UPDATE"""
    
    def __init__(self):
        self.test_cases = [
            {
                "name": "Evolution API Standard Format",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "558182986181@c.us",
                        "pushName": "Mateus",
                        "name": "Mateus",
                        "notify": "Mateus",
                        "verifiedName": None,
                        "imgUrl": None,
                        "status": None
                    }]
                }
            },
            {
                "name": "Evolution API Nested Format",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": {
                        "contact": {
                            "id": "558182986181@c.us",
                            "pushName": "João Silva",
                            "name": "João Silva"
                        }
                    }
                }
            },
            {
                "name": "Evolution API Profile Format",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": {
                        "profile": {
                            "id": "558182986181@c.us",
                            "pushName": "Maria Santos",
                            "displayName": "Maria Santos"
                        }
                    }
                }
            },
            {
                "name": "Evolution API Empty pushName",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "558182986181@c.us",
                        "pushName": None,
                        "name": "Pedro Costa",
                        "notify": "Pedro Costa"
                    }]
                }
            },
            {
                "name": "Evolution API No pushName Field",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "558182986181@c.us",
                        "name": "Ana Oliveira",
                        "notify": "Ana Oliveira"
                    }]
                }
            },
            {
                "name": "Evolution API Complex Nested",
                "payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": {
                        "contactInfo": {
                            "id": "558182986181@c.us",
                            "pushName": "Carlos Mendes",
                            "profile": {
                                "name": "Carlos Mendes",
                                "displayName": "Carlos Mendes"
                            }
                        }
                    }
                }
            }
        ]
    
    async def test_payload(self, test_case: Dict[str, Any]):
        """Testa um payload específico"""
        print(f"\n🧪 Testando: {test_case['name']}")
        print(f"📄 Payload: {json.dumps(test_case['payload'], indent=2)}")
        
        try:
            # Simular o processamento
            await process_contacts_update(test_case['payload'])
            print("✅ Processamento concluído sem erros")
        except Exception as e:
            print(f"❌ Erro no processamento: {str(e)}")
    
    async def run_all_tests(self):
        """Executa todos os testes"""
        print("🚀 Iniciando testes de CONTACTS_UPDATE...")
        
        for test_case in self.test_cases:
            await self.test_payload(test_case)
        
        print("\n🎉 Todos os testes concluídos!")
    
    def analyze_payload_structure(self, payload: Dict[str, Any]):
        """Analisa a estrutura de um payload"""
        print(f"\n🔍 Analisando estrutura do payload:")
        print(f"📊 Chaves principais: {list(payload.keys())}")
        
        data = payload.get('data', {})
        if isinstance(data, list) and data:
            print(f"📋 Data é lista com {len(data)} item(s)")
            print(f"📋 Chaves do primeiro item: {list(data[0].keys())}")
        elif isinstance(data, dict):
            print(f"📋 Data é dict com chaves: {list(data.keys())}")
        else:
            print(f"📋 Data: {data}")


async def main():
    """Função principal"""
    tester = ContactsUpdateTester()
    await tester.run_all_tests()
    
    # Análise adicional
    print("\n" + "="*50)
    print("📊 ANÁLISE DE ESTRUTURAS")
    print("="*50)
    
    for i, test_case in enumerate(tester.test_cases):
        print(f"\n{i+1}. {test_case['name']}")
        tester.analyze_payload_structure(test_case['payload'])


if __name__ == "__main__":
    asyncio.run(main())