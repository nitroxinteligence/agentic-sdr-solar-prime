# PRD - Diagnóstico e Solução: Problema de Criação de Leads no Supabase

## 🚨 Problema Identificado

### Descrição
O sistema não está criando leads no Supabase para mensagens iniciais simples como "oi?", resultando em perda de oportunidades de captura de leads.

### Log de Erro Analisado
```
2025-01-27 14:32:47,987 - INFO - Processando mensagem do número: 558182986181
2025-01-27 14:32:47,987 - INFO - Mensagem: oi?
2025-01-27 14:32:48,123 - INFO - Lead não encontrado para o telefone 558182986181
2025-01-27 14:32:48,124 - INFO - Criando nova conversa para o telefone 558182986181
2025-01-27 14:32:48,124 - INFO - Conversa criada com ID: 123e4567-e89b-12d3-a456-426614174000
2025-01-27 14:32:48,125 - INFO - Aguardando criação do lead no DB...
```

## 🔍 Análise Técnica Detalhada

### Fluxo Atual do Sistema
1. **Webhook recebe mensagem** → `webhooks.py`
2. **Busca lead existente** → `supabase_client.get_lead_by_phone(phone)` retorna `None`
3. **Cria conversa sem lead_id** → Conversa órfã criada
4. **Carrega contexto** → `execution_context` com `lead_info = {}`
5. **Processa mensagem** → `AgenticSDR.process_message()`
6. **Extrai informações** → `LeadManager.extract_lead_info()` não encontra nome em "oi?"
7. **Falha na criação** → Condição restritiva impede criação do lead

### Ponto de Falha Identificado
**Arquivo:** `agentic_sdr_stateless.py`  
**Linha:** 213  
**Código Problemático:**
```python
if lead_info.get('name') and not lead_info.get('id'):
    # Criação do lead só acontece se houver nome
```

### Impacto do Problema
- ❌ **Perda de Leads:** Conversas iniciais não geram leads
- ❌ **Dados Fragmentados:** Conversas órfãs sem vinculação
- ❌ **Oportunidades Perdidas:** Contatos não capturados no CRM
- ❌ **Inconsistência:** Sistema espera leads mas não os cria

## 💡 Solução Proposta

### Mudança Técnica
**Alterar condição na linha 213 de `agentic_sdr_stateless.py`:**

```python
# ANTES (Problemático)
if lead_info.get('name') and not lead_info.get('id'):

# DEPOIS (Solução)
if not lead_info.get('id'):
```

### Justificativa da Solução
1. **Sistema Já Preparado:** 
   - `SupabaseClient.create_lead()` aceita leads sem nome
   - `CRMService.create_lead()` usa "Lead sem nome" como padrão
   - Tabela `leads` permite `name` NULL

2. **Baixo Risco:**
   - Mantém arquitetura stateless intacta
   - Não quebra funcionalidades existentes
   - Apenas relaxa condição restritiva

3. **Alto Benefício:**
   - Captura todos os contatos desde primeira interação
   - `LeadManager` continua extraindo informações progressivamente
   - Leads são atualizados conforme conversa evolui

## 🎯 Implementação

### Passo 1: Aplicar Correção
```bash
# Editar arquivo
vim /Users/mateusmpz/Documents/Projetos\ Clientes\ -\ Code/agent-sdr-ia-solarprime/agentic_sdr_stateless.py

# Localizar linha 213 e alterar condição
```

### Passo 2: Teste de Validação
```python
# Cenário de teste
phone = "558182986181"
message = "oi?"

# Resultado esperado após correção:
# 1. Lead criado no Supabase com phone_number
# 2. Nome padrão "Lead sem nome"
# 3. Conversa vinculada ao lead_id
# 4. Sistema funciona normalmente
```

### Passo 3: Monitoramento
- Verificar logs de criação de leads
- Confirmar vinculação conversa-lead
- Validar sincronização com Kommo CRM

## 📊 Resultados Esperados

### Antes da Correção
- ❌ Mensagem "oi?" → Nenhum lead criado
- ❌ Conversa órfã no sistema
- ❌ Oportunidade perdida

### Após a Correção
- ✅ Mensagem "oi?" → Lead básico criado
- ✅ Conversa vinculada ao lead
- ✅ Captura garantida desde primeira interação
- ✅ Sistema atualiza lead conforme conversa evolui

## 🔧 Alternativas Consideradas

### Opção 1: Criação no Webhook (Descartada)
- **Prós:** Garantia de lead antes do processamento
- **Contras:** Quebra arquitetura stateless, maior complexidade

### Opção 2: Fallback Separado (Descartada)
- **Prós:** Mantém lógica atual
- **Contras:** Adiciona complexidade desnecessária

### Opção 3: Relaxar Condição (ESCOLHIDA)
- **Prós:** Simples, segura, efetiva
- **Contras:** Nenhum significativo

## 🚀 Próximos Passos

1. **Implementar correção** na linha 213
2. **Testar** com mensagem "oi?" do número 558182986181
3. **Validar** criação do lead no Supabase
4. **Monitorar** comportamento em produção
5. **Documentar** mudança no changelog

## 📝 Conclusão

O problema é causado por uma condição muito restritiva que impede a criação de leads básicos. A solução proposta é simples, segura e efetiva, garantindo que todos os contatos sejam capturados desde a primeira interação, mantendo a integridade do sistema e melhorando significativamente a taxa de captura de leads.

**Status:** 🔴 Crítico - Implementação Imediata Recomendada  
**Complexidade:** 🟢 Baixa - Uma linha de código  
**Risco:** 🟢 Baixo - Sistema já preparado  
**Impacto:** 🟢 Alto - Melhoria significativa na captura de leads