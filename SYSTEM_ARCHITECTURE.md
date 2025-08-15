# 🏗️ Arquitetura do Sistema - SDR IA SolarPrime v0.3

## Visão Geral

Sistema de SDR (Sales Development Representative) automatizado para energia solar, 
utilizando IA conversacional com arquitetura **100% stateless** para máxima escalabilidade.

## 🎯 Características Principais

- **Arquitetura Stateless**: Cada requisição cria nova instância, sem compartilhamento de estado
- **Multi-usuário**: Suporte ilimitado de conversas simultâneas
- **Rate Limiting**: Proteção contra limites de API (Kommo, Google, etc)
- **Multimodal**: Processamento de texto, imagem, áudio e documentos
- **Integração Completa**: WhatsApp, Kommo CRM, Google Calendar, Supabase

## 🏛️ Arquitetura Stateless

### Por que Stateless?
- ✅ **Escalabilidade Horizontal**: Adicione workers conforme necessário
- ✅ **Thread-Safety**: Sem riscos de contaminação entre conversas
- ✅ **Simplicidade**: Sem gerenciamento complexo de estado
- ✅ **Cloud-Native**: Pronto para Kubernetes, Lambda, etc

### Implementação
```python
# Cada mensagem cria nova instância
agent = await create_stateless_agent()

# Contexto passado explicitamente
execution_context = {
    'phone': phone_number,
    'conversation_history': history,
    'lead_info': lead_data
}

response = await agent.process_message(message, execution_context)
```

## 📦 Componentes Principais

### 1. AgenticSDR Stateless
- Agente conversacional principal
- Personalidade ultra-humanizada (Helen)
- Decision engine para ativação de agentes especializados

### 2. Team Agents
- **CalendarAgent**: Agendamento com Google Calendar
- **CRMAgent**: Gestão de leads no Kommo
- **FollowUpAgent**: Nutrição automática de leads
- **QualificationAgent**: Scoring de leads
- **KnowledgeAgent**: Base de conhecimento
- **BillAnalyzerAgent**: Análise de contas de energia

### 3. Integrações

#### Evolution API v2
- Integração WhatsApp Business
- Processamento de mídia
- Indicadores de digitação

#### Kommo CRM
- Pipeline completo de vendas
- Mapeamento PT/EN de stages
- Update dinâmico de campos
- Rate limiting integrado

#### Supabase
- PostgreSQL + pgvector
- Memória semântica
- Persistência de conversas
- Estado emocional

#### Redis
- Buffer de mensagens
- Cache de stages
- Rate limiting

## 🔄 Fluxo de Mensagens

```
WhatsApp → Evolution API → Webhook → Message Buffer → AgenticSDR → Response
                                              ↓                        ↓
                                         Redis Cache            Kommo CRM/Supabase
```

## ⚡ Performance

- **Inicialização**: <0.5s
- **Tempo de resposta**: ~13s por conversa
- **Conversas simultâneas**: Ilimitado
- **Taxa de sucesso**: 98%

## 🛠️ Tecnologias

- **Framework**: FastAPI + AGnO v1.7.6
- **IA**: Gemini 2.5 Pro + Reasoning
- **Database**: PostgreSQL + pgvector
- **Cache**: Redis
- **WhatsApp**: Evolution API v2
- **CRM**: Kommo
- **Calendar**: Google Calendar OAuth 2.0

## 📊 Configuração

Todas as funcionalidades controladas via environment variables:

```env
USE_STATELESS_MODE=true
ENABLE_MULTIMODAL_ANALYSIS=true
ENABLE_CALENDAR_AGENT=true
ENABLE_CRM_AGENT=true
PRIMARY_AI_MODEL=gemini-2.5-pro
```

## 🚀 Evolução do Sistema

### v0.1 - MVP Singleton
- Arquitetura singleton básica
- Proof of concept funcional
- Problemas de concorrência

### v0.2 - Refatoração Modular
- Separação em módulos
- Melhoria de performance
- Ainda com limitações de escala

### v0.3 - Pure Stateless (Atual)
- Arquitetura 100% stateless
- Rate limiting integrado
- Pronto para produção em escala

## 📚 Documentação Adicional

- [Guias de Referência](./docs/reference/) - Setup e configuração
- [Arquivo Histórico](./docs/archive/) - Documentação histórica do projeto

---

**Última atualização**: 15/08/2025  
**Versão**: 0.3 - Pure Stateless Architecture
