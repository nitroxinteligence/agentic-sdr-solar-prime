#!/usr/bin/env python3
"""
EXEMPLO PRÁTICO: Como o Sistema de Tool Calling funciona na Helen v0.3

Este arquivo demonstra o fluxo completo de qualificação e agendamento
usando o novo sistema de tool calling implementado.
"""

def exemplo_fluxo_completo():
    """Demonstra um fluxo completo de qualificação com tool calling"""
    
    print("🎯 EXEMPLO PRÁTICO: FLUXO COMPLETO COM TOOL CALLING")
    print("=" * 60)
    
    print("\n📱 CENÁRIO: Cliente interessado em energia solar")
    print("-" * 50)
    
    # Etapa 1: Qualificação inicial
    print("👤 Cliente: Oi, quero saber sobre energia solar")
    print("🤖 Helen: Oi! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime...")
    print("         Como posso te chamar?")
    
    print("\n👤 Cliente: João Silva")
    print("🤖 Helen: Perfeito, João! Hoje na Solarprime nós temos quatro modelos:")
    print("         1) Instalação de usina própria")
    print("         2) Aluguel de lote para instalação")
    print("         3) Compra de energia com desconto")
    print("         4) Usina de investimento")
    print("         Qual desses modelos seria do seu interesse?")
    
    # Etapa 2: Escolha do fluxo
    print("\n👤 Cliente: Quero a opção 1, instalar minha própria usina")
    print("🤖 Helen: [FLUXO A ATIVADO] Perfeito! A instalação da própria usina...")
    print("         Qual o valor médio da sua conta de energia mensal?")
    
    # Etapa 3: Análise de conta
    print("\n👤 Cliente: [Envia foto da conta de R$ 850,00]")
    print("🤖 Helen: [ANÁLISE MULTIMODAL] Recebi sua conta de R$ 850,00!")
    print("         Com esse valor você pode economizar cerca de R$ 765 por mês...")
    
    # Etapa 4: Qualificação aprovada
    print("\n🤖 Helen: Pelo que você me contou, seu perfil se encaixa perfeitamente!")
    print("         [TOOL: crm.update_stage | stage=qualificado]")
    print("         [TOOL: crm.update_field | field=energy_value | value=850.00]")
    print("         [TOOL: crm.update_field | field=solution_type | value=instalacao_propria]")
    
    # Etapa 5: Agendamento
    print("\n🤖 Helen: Quando podemos marcar a reunião com o Leonardo?")
    print("👤 Cliente: Pode ser essa semana")
    print("🤖 Helen: Perfeito! O decisor principal poderá participar da reunião?")
    print("👤 Cliente: Sim, sou eu mesmo o decisor")
    
    print("\n🤖 Helen: [TOOL: calendar.check_availability]")
    print("🔧 Sistema: Horários disponíveis: Segunda 14h, Terça 10h, Quinta 15h")
    print("🤖 Helen: O Leonardo tem estes horários disponíveis:")
    print("         Segunda às 14h, Terça às 10h ou Quinta às 15h.")
    print("         Qual fica melhor para você?")
    
    # Etapa 6: Confirmação do agendamento
    print("\n👤 Cliente: Prefiro terça às 10h")
    print("🤖 Helen: Perfeito! Preciso do seu melhor email para enviar o convite.")
    print("👤 Cliente: joao.silva@email.com")
    
    print("\n🤖 Helen: [TOOL: calendar.schedule_meeting | date=2024-08-20 | time=10:00 | email=joao.silva@email.com]")
    print("🔧 Sistema: Reunião agendada! Link: https://meet.google.com/abc-def-ghi")
    print("🤖 Helen: Prontinho João! Reunião confirmada para terça-feira dia 20/08")
    print("         às 10h com o Leonardo Ferraz.")
    print("         Aqui está o link: https://meet.google.com/abc-def-ghi")
    
    # Etapa 7: Lembretes automáticos
    print("\n🤖 Helen: [TOOL: followup.schedule | hours=24 | message=Oi João! Passando para confirmar sua reunião de amanhã às 10h]")
    print("🤖 Helen: [TOOL: followup.schedule | hours=2 | message=João, sua reunião é daqui a 2 horas!]")
    print("🤖 Helen: Perfeito! Configurei lembretes automáticos para você não esquecer.")
    
    print("\n" + "=" * 60)
    print("✅ FLUXO COMPLETO FINALIZADO COM SUCESSO!")
    print("🎯 Lead qualificado, reunião agendada, lembretes configurados")

def exemplo_tratamento_erro():
    """Demonstra como Helen trata erros de tools"""
    
    print("\n\n🚨 EXEMPLO: TRATAMENTO DE ERRO")
    print("=" * 40)
    
    print("🤖 Helen: [TOOL: calendar.check_availability]")
    print("❌ Sistema: ERRO - Falha na conexão com Google Calendar")
    print("🤖 Helen: Opa, tô com uma dificuldade técnica aqui para acessar")
    print("         a agenda do Leonardo. Deixa eu te passar o WhatsApp")
    print("         dele direto: (81) 99999-9999")
    print("         Ou se preferir, posso tentar novamente em alguns minutos?")

def exemplo_transparencia():
    """Demonstra a transparência do sistema"""
    
    print("\n\n🔍 EXEMPLO: TRANSPARÊNCIA NO USO DE TOOLS")
    print("=" * 50)
    
    print("🤖 Helen: Oxente, deixa eu dar uma olhadinha na agenda do Leonardo aqui...")
    print("         [TOOL: calendar.check_availability]")
    print("         Pronto! Ele tá com umas opções bem bacanas para vocês!")
    
    print("\n💡 OBSERVAÇÃO: Helen mantém sua personalidade nordestina")
    print("   mesmo usando o sistema de tools técnico!")

def main():
    """Função principal dos exemplos"""
    
    exemplo_fluxo_completo()
    exemplo_tratamento_erro()
    exemplo_transparencia()
    
    print("\n" + "=" * 60)
    print("📚 BENEFÍCIOS DO SISTEMA TOOL CALLING:")
    print("✅ Nunca mais inventar horários disponíveis")
    print("✅ Confirmações reais de agendamento")
    print("✅ Integração automática com CRM")
    print("✅ Lembretes automáticos configurados")
    print("✅ Transparência em caso de erros")
    print("✅ Personalidade Helen preservada")
    print("✅ Fluxo robusto e confiável")

if __name__ == "__main__":
    main()