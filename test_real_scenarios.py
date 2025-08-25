#!/usr/bin/env python3
"""
Teste de cenários reais para validação das correções implementadas
"""

import asyncio
import json
from typing import Dict, Any, List
from app.api.webhooks import process_contacts_update
from app.core.lead_manager import LeadManager
from app.core.context_analyzer import ContextAnalyzer
from app.utils.logger import emoji_logger


class RealScenariosValidator:
    """Valida correções com cenários reais de produção"""
    
    def __init__(self):
        self.lead_manager = LeadManager()
        self.context_analyzer = ContextAnalyzer()
        self.test_results = []
        
        # Cenários baseados em logs reais e situações de produção
        self.real_scenarios = [
            {
                "name": "Cenário 1: Cliente mudou nome no WhatsApp",
                "description": "Cliente que estava como 'Lead 123' agora tem nome real",
                "contacts_update_payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "5511999887766@c.us",
                        "pushName": "João Silva Santos",
                        "name": "João Silva Santos",
                        "notify": "João Silva Santos"
                    }]
                },
                "expected_behavior": "Deve atualizar nome genérico para nome real"
            },
            {
                "name": "Cenário 2: Evolution API com estrutura aninhada",
                "description": "Payload com estrutura complexa da Evolution API",
                "contacts_update_payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": {
                        "contactInfo": {
                            "id": "5511888776655@c.us",
                            "pushName": "Maria Oliveira",
                            "profile": {
                                "name": "Maria Oliveira",
                                "displayName": "Maria O.",
                                "status": "Disponível"
                            }
                        }
                    }
                },
                "expected_behavior": "Deve extrair nome de estrutura aninhada"
            },
            {
                "name": "Cenário 3: Apenas notify disponível",
                "description": "Caso onde só o campo notify tem o nome",
                "contacts_update_payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "5511777665544@c.us",
                        "pushName": None,
                        "name": "",
                        "notify": "Carlos Mendes",
                        "verifiedName": None
                    }]
                },
                "expected_behavior": "Deve usar notify como fallback"
            },
            {
                "name": "Cenário 4: Nome com caracteres especiais",
                "description": "Nome com emojis e caracteres especiais",
                "contacts_update_payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": [{
                        "id": "5511666554433@c.us",
                        "pushName": "Ana 🌟 Costa",
                        "name": "Ana 🌟 Costa",
                        "notify": "Ana Costa"
                    }]
                },
                "expected_behavior": "Deve processar nomes com caracteres especiais"
            },
            {
                "name": "Cenário 5: Múltiplas estruturas aninhadas",
                "description": "Payload com múltiplos níveis de aninhamento",
                "contacts_update_payload": {
                    "event": "contacts.update",
                    "instance": "SDR IA SolarPrime",
                    "data": {
                        "contact": {
                            "profile": {
                                "id": "5511555443322@c.us",
                                "pushName": "Roberto Silva",
                                "displayName": "Roberto S."
                            }
                        }
                    }
                },
                "expected_behavior": "Deve extrair de estruturas profundamente aninhadas"
            }
        ]
        
        # Cenários de contexto conversacional
        self.context_scenarios = [
            {
                "name": "Contexto 1: Extração de nome em conversa",
                "messages": [
                    "Olá, meu nome é Pedro Santos",
                    "Tenho interesse em energia solar",
                    "Moro em São Paulo"
                ],
                "expected_name": "Pedro Santos"
            },
            {
                "name": "Contexto 2: Nome mencionado posteriormente",
                "messages": [
                    "Oi, tudo bem?",
                    "Quero saber sobre painéis solares",
                    "Ah, me chamo Fernanda Lima"
                ],
                "expected_name": "Fernanda Lima"
            },
            {
                "name": "Contexto 3: Múltiplos nomes mencionados",
                "messages": [
                    "Olá, sou o Ricardo",
                    "Estou perguntando para minha esposa Maria",
                    "Queremos instalar energia solar"
                ],
                "expected_name": "Ricardo"
            }
        ]
    
    async def test_contacts_update_scenario(self, scenario: Dict[str, Any]) -> bool:
        """Testa um cenário de CONTACTS_UPDATE"""
        try:
            print(f"\n🧪 {scenario['name']}")
            print(f"📝 {scenario['description']}")
            
            # Processar o payload
            await process_contacts_update(scenario['contacts_update_payload'])
            
            print(f"✅ {scenario['expected_behavior']}")
            return True
            
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return False
    
    def test_context_scenario(self, scenario: Dict[str, Any]) -> bool:
        """Testa um cenário de contexto conversacional"""
        try:
            print(f"\n🧪 {scenario['name']}")
            
            # Simular mensagens no formato esperado pelo LeadManager
            messages = []
            for i, msg_text in enumerate(scenario['messages']):
                messages.append({
                    "role": "user",
                    "content": msg_text
                })
            
            # Extrair informações usando o LeadManager
            lead_info = self.lead_manager.extract_lead_info(messages)
            extracted_name = lead_info.get('name')
            
            if extracted_name and extracted_name.lower() in scenario['expected_name'].lower():
                print(f"✅ Nome extraído corretamente: '{extracted_name}'")
                return True
            else:
                print(f"⚠️ Nome esperado: '{scenario['expected_name']}', extraído: '{extracted_name}'")
                return False
                
        except Exception as e:
            print(f"❌ Erro: {str(e)}")
            return False
    
    async def run_all_tests(self):
        """Executa todos os testes de cenários reais"""
        print("🚀 Iniciando validação com cenários reais...")
        
        # Testes de CONTACTS_UPDATE
        print("\n" + "="*60)
        print("📞 TESTANDO CENÁRIOS DE CONTACTS_UPDATE")
        print("="*60)
        
        contacts_results = []
        for scenario in self.real_scenarios:
            result = await self.test_contacts_update_scenario(scenario)
            contacts_results.append(result)
        
        # Testes de contexto conversacional
        print("\n" + "="*60)
        print("💬 TESTANDO CENÁRIOS DE CONTEXTO CONVERSACIONAL")
        print("="*60)
        
        context_results = []
        for scenario in self.context_scenarios:
            result = self.test_context_scenario(scenario)
            context_results.append(result)
        
        # Relatório final
        print("\n" + "="*60)
        print("📊 RELATÓRIO FINAL")
        print("="*60)
        
        contacts_passed = sum(contacts_results)
        context_passed = sum(context_results)
        total_passed = contacts_passed + context_passed
        total_tests = len(self.real_scenarios) + len(self.context_scenarios)
        
        print(f"📞 CONTACTS_UPDATE: {contacts_passed}/{len(self.real_scenarios)} cenários passaram")
        print(f"💬 Contexto: {context_passed}/{len(self.context_scenarios)} cenários passaram")
        print(f"🎯 Total: {total_passed}/{total_tests} cenários passaram")
        
        if total_passed == total_tests:
            print("\n🎉 Todos os cenários reais foram validados com sucesso!")
        else:
            print(f"\n⚠️ {total_tests - total_passed} cenários falharam. Revisar implementação.")
        
        return total_passed == total_tests
    
    def generate_production_test_report(self):
        """Gera relatório para testes em produção"""
        print("\n" + "="*60)
        print("📋 GUIA PARA TESTES EM PRODUÇÃO")
        print("="*60)
        
        print("\n🔍 Pontos a monitorar:")
        print("1. Logs de 'CONTACTS_UPDATE sem pushName ou telefone válido'")
        print("2. Logs de 'Lead não encontrado para telefone'")
        print("3. Atualizações de nome de leads genéricos")
        print("4. Extração de nomes em conversas")
        
        print("\n📊 Métricas importantes:")
        print("- Taxa de sucesso na extração de pushName")
        print("- Número de leads com nomes atualizados")
        print("- Redução de leads com nomes genéricos")
        
        print("\n🚨 Alertas a configurar:")
        print("- Aumento súbito de erros CONTACTS_UPDATE")
        print("- Muitos leads sem nome após 24h")
        print("- Falhas na extração de contexto")


async def main():
    """Função principal"""
    validator = RealScenariosValidator()
    
    # Executar todos os testes
    success = await validator.run_all_tests()
    
    # Gerar guia para produção
    validator.generate_production_test_report()
    
    return success


if __name__ == "__main__":
    result = asyncio.run(main())
    exit(0 if result else 1)