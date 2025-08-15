#!/usr/bin/env python
"""
Teste completo da implementação Stateless
Valida arquitetura sem singleton, contexto temporal e histórico expandido
"""

import asyncio
import json
from datetime import datetime
import pytz
from app.agents.agentic_sdr_stateless import create_stateless_agent
from app.utils.logger import emoji_logger

async def test_stateless_architecture():
    """
    Testa a arquitetura stateless completa
    """
    emoji_logger.system_info("🧪 TESTE DA ARQUITETURA STATELESS")
    emoji_logger.system_info("=" * 60)
    
    test_results = []
    
    # Teste 1: Criação de múltiplas instâncias isoladas
    emoji_logger.system_info("\n🔬 Teste 1: Isolamento de instâncias")
    
    try:
        # Criar 3 instâncias diferentes
        agent1 = await create_stateless_agent()
        agent2 = await create_stateless_agent()
        agent3 = await create_stateless_agent()
        
        # Verificar que são instâncias diferentes
        if agent1 is not agent2 and agent2 is not agent3:
            emoji_logger.system_success("✅ Instâncias são isoladas (sem singleton)")
            test_results.append({"test": "isolamento", "status": "passed"})
        else:
            emoji_logger.system_error("Test", "❌ Instâncias compartilhadas (singleton detectado)")
            test_results.append({"test": "isolamento", "status": "failed"})
            
    except Exception as e:
        emoji_logger.system_error("Test", f"Erro no teste de isolamento: {e}")
        test_results.append({"test": "isolamento", "status": "error", "error": str(e)})
    
    # Teste 2: Contexto temporal no prompt
    emoji_logger.system_info("\n⏰ Teste 2: Contexto temporal")
    
    try:
        agent = await create_stateless_agent()
        
        # Criar contexto de execução com histórico vazio
        execution_context = {
            "phone": "5511999999999",
            "lead_info": {"name": "Teste Silva"},
            "conversation_history": [],
            "conversation_id": "test-123",
            "timestamp": datetime.now().isoformat()
        }
        
        # Construir prompt para verificar contexto temporal
        prompt = agent._build_prompt_with_history(
            message="Olá!",
            context={"conversation_stage": "início"},
            lead_info={"name": "Teste"},
            service_results=[],
            media_context="",
            conversation_history=[],
            execution_context=execution_context
        )
        
        # Verificar se contém data/hora
        brasil_tz = pytz.timezone('America/Recife')
        now = datetime.now(brasil_tz)
        expected_date = now.strftime('%d/%m/%Y')
        
        if expected_date in prompt:
            emoji_logger.system_success(f"✅ Contexto temporal presente: {expected_date}")
            test_results.append({"test": "contexto_temporal", "status": "passed"})
        else:
            emoji_logger.system_error("Test", "❌ Contexto temporal ausente")
            test_results.append({"test": "contexto_temporal", "status": "failed"})
            
    except Exception as e:
        emoji_logger.system_error("Test", f"Erro no teste temporal: {e}")
        test_results.append({"test": "contexto_temporal", "status": "error", "error": str(e)})
    
    # Teste 3: Histórico expandido
    emoji_logger.system_info("\n📜 Teste 3: Histórico expandido")
    
    try:
        agent = await create_stateless_agent()
        
        # Criar histórico com 60 mensagens
        conversation_history = []
        for i in range(60):
            conversation_history.append({
                "role": "user" if i % 2 == 0 else "assistant",
                "content": f"Mensagem de teste {i}",
                "timestamp": datetime.now().isoformat()
            })
        
        execution_context = {
            "phone": "5511999999999",
            "lead_info": {"name": "Teste Silva"},
            "conversation_history": conversation_history,
            "conversation_id": "test-123",
            "timestamp": datetime.now().isoformat()
        }
        
        # Construir prompt
        prompt = agent._build_prompt_with_history(
            message="Nova mensagem",
            context={"conversation_stage": "qualificação"},
            lead_info={"name": "Teste", "bill_value": 500},
            service_results=[],
            media_context="",
            conversation_history=conversation_history,
            execution_context=execution_context
        )
        
        # Verificar se inclui mensagens do histórico
        messages_included = sum(1 for i in range(10, 50) if f"Mensagem de teste {i}" in prompt)
        
        if messages_included >= 30:  # Pelo menos 30 das últimas 50 mensagens
            emoji_logger.system_success(f"✅ Histórico expandido: {messages_included} mensagens incluídas")
            test_results.append({"test": "historico_expandido", "status": "passed", "messages": messages_included})
        else:
            emoji_logger.system_error("Test", f"❌ Histórico limitado: apenas {messages_included} mensagens")
            test_results.append({"test": "historico_expandido", "status": "failed", "messages": messages_included})
            
    except Exception as e:
        emoji_logger.system_error("Test", f"Erro no teste de histórico: {e}")
        test_results.append({"test": "historico_expandido", "status": "error", "error": str(e)})
    
    # Teste 4: Processamento de mensagem completo
    emoji_logger.system_info("\n📨 Teste 4: Processamento completo")
    
    try:
        agent = await create_stateless_agent()
        
        execution_context = {
            "phone": "5511999999999",
            "lead_info": {
                "name": "João Silva",
                "bill_value": 450
            },
            "conversation_history": [
                {"role": "user", "content": "Oi", "timestamp": datetime.now().isoformat()},
                {"role": "assistant", "content": "Olá! Sou a Helen da SolarPrime", "timestamp": datetime.now().isoformat()}
            ],
            "conversation_id": "test-123",
            "timestamp": datetime.now().isoformat()
        }
        
        # Processar mensagem
        response = await agent.process_message(
            message="Quero agendar uma reunião com o Leonardo amanhã às 14h",
            execution_context=execution_context
        )
        
        # Verificar resposta
        if response and "<RESPOSTA_FINAL>" in response:
            emoji_logger.system_success("✅ Processamento completo funcionando")
            emoji_logger.system_info(f"Resposta: {response[:100]}...")
            test_results.append({"test": "processamento", "status": "passed"})
        else:
            emoji_logger.system_error("Test", "❌ Processamento falhou")
            test_results.append({"test": "processamento", "status": "failed"})
            
    except Exception as e:
        emoji_logger.system_error("Test", f"Erro no processamento: {e}")
        test_results.append({"test": "processamento", "status": "error", "error": str(e)})
    
    # Resultado final
    emoji_logger.system_info("\n" + "=" * 60)
    emoji_logger.system_info("📊 RESULTADO DOS TESTES")
    
    passed = sum(1 for r in test_results if r["status"] == "passed")
    failed = sum(1 for r in test_results if r["status"] == "failed")
    errors = sum(1 for r in test_results if r["status"] == "error")
    
    emoji_logger.system_info(f"✅ Passou: {passed}")
    emoji_logger.system_info(f"❌ Falhou: {failed}")
    emoji_logger.system_info(f"⚠️ Erros: {errors}")
    
    # Salvar relatório
    with open("stateless_test_report.json", "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "passed": passed,
                "failed": failed,
                "errors": errors,
                "total": len(test_results)
            },
            "tests": test_results
        }, f, indent=2)
    
    if failed == 0 and errors == 0:
        emoji_logger.system_success("\n🎉 TODOS OS TESTES PASSARAM!")
        emoji_logger.system_success("✅ Arquitetura Stateless implementada com sucesso")
        emoji_logger.system_success("✅ Contexto temporal funcionando")
        emoji_logger.system_success("✅ Histórico expandido ativo")
        emoji_logger.system_success("✅ Sistema pronto para produção")
        return True
    else:
        emoji_logger.system_error("Test", f"\n❌ {failed + errors} testes falharam - verificar implementação")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_stateless_architecture())
    exit(0 if success else 1)