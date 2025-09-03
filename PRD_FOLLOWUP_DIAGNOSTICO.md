# PRD - Diagnóstico Completo do Sistema de Follow-up
## SolarPrime SDR IA - Análise Ultra Detalhada

---

## 📋 RESUMO EXECUTIVO

**Status Atual:** ❌ SISTEMA DE FOLLOW-UP COM FALHAS CRÍTICAS  
**Impacto:** ALTO - Follow-ups não funcionam corretamente em produção  
**Prioridade:** CRÍTICA - Correção imediata necessária  

### Problemas Identificados
- ✅ 9 problemas identificados (1 já resolvido)
- ❌ 0 follow-ups de 48h funcionando
- ❌ Desqualificação automática não funciona
- ❌ Limites de tentativas insuficientes
- ❌ Dependência crítica do Redis sem fallback

---

## 🔍 ANÁLISE DETALHADA DOS PROBLEMAS

### 1. ❌ PROBLEMA CRÍTICO: ConversationMonitor não detecta 48h

**Arquivo:** `app/services/conversation_monitor.py`  
**Linhas:** 147-152  

**Problema:**
```python
# CÓDIGO ATUAL - APENAS VERIFICA ATÉ 24H
if inactive_time > timedelta(minutes=30) and current_status != 'followup_30min_sent':
    # ... agenda 30min
elif inactive_time > timedelta(hours=24) and current_status != 'followup_24h_sent':
    # ... agenda 24h
# ❌ FALTA: elif inactive_time > timedelta(hours=48):
```

**Impacto:**
- Leads nunca são desqualificados automaticamente após 48h
- Sistema não cumpre requisito de "cortar contato após 48h sem resposta"
Obs: Nao precisa ter uma SUPER FUNÇAO para cortar o contato após 48h sem resposta, apenas inserir uma funçao que... sempre que o lead estiver no estágio "Não Interessado" do KommoCRM, o Agente nao responde a nenhuma mensagem do lead e nao entra mais em contato, assim como já está configurado no card "Atendimento Humano", apenas isso.
- Leads ficam indefinidamente no pipeline

**Solução Necessária:**
- Adicionar verificação de 48h no ConversationMonitor
- Implementar chamada para desqualificação automática

---

### 2. ❌ PROBLEMA CRÍTICO: max_follow_up_attempts insuficiente

**Arquivo:** `app/config.py`  
**Linha:** 150  

**Problema:**
```python
max_follow_up_attempts: int = Field(default=3)  # ❌ INSUFICIENTE
```

**Análise:**
- Sequência necessária: 30min → 24h → 48h → desqualificação = 4 tentativas
- Configuração atual permite apenas 3 tentativas
- Sistema bloqueia follow-up de 48h antes mesmo de tentar

**Evidência no Código:**
```python
# followup_manager.py linha 65
if count >= settings.max_follow_up_attempts:
    # ❌ Bloqueia no 3º follow-up, nunca chega ao 4º (48h)
    return
```

**Solução Necessária:**
- Alterar `max_follow_up_attempts` para pelo menos 4
- Ou criar lógica específica para desqualificação

---

### 3. ✅ RESOLVIDO: Sistema de desqualificação adequado

**Arquivos:** `tabelas leads` e `leads_qualifications` no Supabase + Kommo CRM  

**Solução Atual:**
- Leads desqualificados são enviados para o estágio "Não Interessado" no Kommo CRM
- Não é necessário inserir DISQUALIFICATION na tabela follow_ups
- Sistema já funciona corretamente com as tabelas `leads` e `leads_qualifications`

**Status:** ✅ **ADEQUADO** - Não requer alteração

---

### 3. ❌ PROBLEMA CRÍTICO: Timing de desqualificação incorreto

**Arquivo:** `app/services/followup_manager.py`  
**Linha:** 115  

**Problema:**
```python
# CÓDIGO ATUAL
await followup_service.schedule_followup(
    delay_hours=0,  # ❌ EXECUTA IMEDIATAMENTE
    followup_type=FollowUpType.DISQUALIFICATION.value,
    context={
        "inactive_since": inactive_since,
        "reason": "48h_no_response"
    }
)
```

**Análise:**
- `delay_hours=0` agenda para execução imediata
- Deveria calcular 48h desde `inactive_since`
- Lógica de timing está incorreta

**Solução Necessária:**
```python
# CORREÇÃO NECESSÁRIA
inactive_since_dt = datetime.fromisoformat(inactive_since)
delay_needed = 48 - (datetime.now() - inactive_since_dt).total_seconds() / 3600
delay_hours = max(0, delay_needed)
```

---

### 4. ❌ PROBLEMA CRÍTICO: Dependência total do Redis

**Arquivo:** `app/services/conversation_monitor.py`  
**Linhas:** 47-50, 85-88  

**Problema:**
```python
# CÓDIGO ATUAL
if not self.redis.redis_client:
    emoji_logger.system_debug("Redis não disponível, pulando registro")
    return  # ❌ PARA COMPLETAMENTE SE REDIS FALHAR
```

**Impacto:**
- Se Redis falhar, nenhum follow-up é processado
- Sistema não tem fallback para banco de dados
- Perda completa de funcionalidade de follow-up

**Solução Necessária:**
- Implementar fallback para Supabase quando Redis falhar
- Manter registro de atividade no banco como backup

---

### 5. ⚠️ PROBLEMA: Meeting reminders sem validação

**Arquivo:** `app/services/followup_service_100_real.py`  
**Linhas:** 119-150  

**Problema:**
```python
# CÓDIGO ATUAL
scheduled_time = datetime.now(pytz.utc) + timedelta(hours=delay_hours)
# ❌ NÃO VERIFICA SE A REUNIÃO REALMENTE EXISTE NESSE HORÁRIO
```

**Impacto:**
- Lembretes podem ser enviados para reuniões canceladas
OBS: se um usuário/lead cancelar uma reuniao, deve atualizar a tabela "leads_qualifications", pois todos os leads que agendaram uma reuniao com o Agente, vao para esta tabela leads qualifications. Nesta tabela deve atualizar a coluna "meeting_status" para CANCELADO.
- Lembretes podem ter horários incorretos
- Falta integração com Google Calendar para validação

---

### 6. ⚠️ PROBLEMA: Processamento duplicado

**Arquivos:**
- `app/services/followup_worker.py` (linha 107)
- `app/services/followup_executor_service.py` (linha 26)

**Problema:**
```python
# AMBOS OS SERVIÇOS FAZEM A MESMA COISA
await asyncio.sleep(15)  # Verifica a cada 15 segundos
```
Obs: talvez possa aumentar este tempo de verificar os follow-ups para cada 15minutos para nao sobrecarregar o servidor, nao seria melhor? 15s o tempo está MUITO baixo.

**Impacto:**
- Overhead desnecessário no banco de dados
- Possível processamento duplicado de follow-ups
- Ineficiência de recursos

---

### 7. ❌ PROBLEMA: Falta de bloqueio após desqualificação

**Arquivo:** `app/services/followup_worker.py`  
**Linhas:** 179-237  

**Problema:**
```python
# CÓDIGO ATUAL - APENAS ATUALIZA CRM
await crm_service.update_lead_stage(
    stage_name="NAO_INTERESSADO",
    notes="Lead desqualificado automaticamente após 48h sem resposta"
)
# ❌ NÃO BLOQUEIA FUTURAS INTERAÇÕES
```

**Requisito não atendido:**
> "pode bloquear o usuário no redis ou supabase, ou algo do tipo, é realmente ideal que o Agente seja bloqueado quando entrar no estágio 'Não Interessado'"

**Solução Necessária:**
- Adicionar bloqueio no Redis/Supabase
- Implementar verificação de bloqueio antes de processar mensagens

---

### 8. ⚠️ PROBLEMA: Inconsistência de tipos de follow-up

**Arquivos múltiplos:**

**Problema:**
```python
# config.py - Define enum
FOLLOW_UP_TYPES = ["IMMEDIATE_REENGAGEMENT", "DAILY_NURTURING", ...]

# Mas código usa strings diretamente
followup_type = "DISQUALIFICATION"  # ❌ String literal
```

**Impacto:**
- Inconsistência entre definições
- Possíveis erros de digitação
- Dificuldade de manutenção

---

### 9. ⚠️ PROBLEMA: Ignorar horário comercial

**Requisito do prompt:**
> "business hours (8h to 17h, Monday to Friday)"

**Problema:**
- Follow-ups são agendados sem considerar horário comercial
- Mensagens podem ser enviadas fora do horário de atendimento
- Não respeita configuração de `business_hours_start` e `business_hours_end`

---

## 📊 MATRIZ DE IMPACTO

| Problema | Severidade | Impacto | Esforço | Prioridade |
|----------|------------|---------|---------|------------|
| ConversationMonitor 48h | CRÍTICA | ALTO | MÉDIO | P0 |
| max_follow_up_attempts | CRÍTICA | ALTO | BAIXO | P0 |
| ~~SQL constraint DISQUALIFICATION~~ | ~~RESOLVIDO~~ | ~~N/A~~ | ~~N/A~~ | ~~N/A~~ |
| Timing desqualificação | CRÍTICA | ALTO | MÉDIO | P0 |
| Dependência Redis | CRÍTICA | ALTO | ALTO | P1 |
| Meeting reminders | MÉDIA | MÉDIO | MÉDIO | P2 |
| Processamento duplicado | BAIXA | BAIXO | BAIXO | P3 |
| Bloqueio pós-desqualificação | MÉDIA | MÉDIO | MÉDIO | P1 |
| Inconsistência tipos | BAIXA | BAIXO | BAIXO | P3 |
| Horário comercial | MÉDIA | MÉDIO | MÉDIO | P2 |

---

## 🎯 REQUISITOS FUNCIONAIS CORRETOS

### Follow-up de Reengajamento
1. ✅ **30 minutos:** Detectar inatividade e enviar primeiro follow-up
2. ✅ **24 horas:** Se sem resposta, enviar segundo follow-up
3. ❌ **48 horas:** Se sem resposta, desqualificar automaticamente
4. ❌ **Bloqueio:** Bloquear interações futuras após desqualificação

### Follow-up de Reunião
1. ⚠️ **24h antes:** Enviar lembrete com link da reunião
2. ⚠️ **2h antes:** Enviar segundo lembrete
3. ❌ **Validação:** Verificar se reunião existe no Google Calendar

### Requisitos Técnicos
1. ❌ **Horário comercial:** Respeitar 8h-17h, seg-sex
2. ❌ **Fallback Redis:** Funcionar mesmo se Redis falhar
3. ❌ **Limite tentativas:** Permitir sequência completa de follow-ups
4. ❌ **Mensagens humanizadas:** Seguir prompt principal

---

## 🔧 ARQUITETURA ATUAL vs IDEAL

### Arquitetura Atual (Problemática)
```
ConversationMonitor → Redis → FollowUpManager → FollowUpService → Worker
                      ↓ (falha)
                   ❌ Sistema para
```

### Arquitetura Ideal (Robusta)
```
ConversationMonitor → Redis + Supabase → FollowUpManager → FollowUpService → Worker
                      ↓ (fallback)         ↓ (validações)    ↓ (bloqueios)
                   ✅ Continua funcionando
```

---

## 📈 MÉTRICAS DE SUCESSO

### Antes da Correção
- ❌ 0% de follow-ups de 48h executados
- ❌ 0% de desqualificações automáticas
- ❌ 100% dependência do Redis
- ❌ Possível processamento duplicado
- ✅ Sistema de desqualificação via CRM já adequado

### Após Correção (Meta)
- ✅ 100% de follow-ups de 48h executados
- ✅ 100% de desqualificações automáticas funcionando
- ✅ 0% dependência crítica do Redis
- ✅ 0% processamento duplicado
- ✅ 100% respeito ao horário comercial
- ✅ Manter sistema de desqualificação via CRM funcionando

---

## 🚨 RISCOS IDENTIFICADOS

### Riscos de Negócio
1. **Leads perdidos:** Sem desqualificação, leads ficam indefinidamente no pipeline
2. **Ineficiência comercial:** Tempo perdido com leads não interessados
3. **Experiência ruim:** Leads podem receber mensagens desnecessárias

### Riscos Técnicos
1. **Falha do Redis:** Sistema para completamente
2. **Sobrecarga do banco:** Processamento duplicado
3. **Inconsistência de dados:** Tipos de follow-up incorretos

### Riscos Operacionais
1. **Mensagens fora de horário:** Impacto na imagem da empresa
2. **Lembretes incorretos:** Reuniões canceladas/alteradas
3. **Falta de bloqueio:** Leads desqualificados continuam sendo contatados

---

## 📋 CONCLUSÃO

O sistema de follow-up apresenta **9 problemas identificados** (1 já resolvido), sendo **4 críticos** que impedem o funcionamento correto em produção. A correção destes problemas é **URGENTE** para garantir que:

1. ✅ Follow-ups de reengajamento funcionem completamente (30min → 24h → 48h → desqualificação)
2. ✅ Follow-ups de reunião sejam enviados corretamente
3. ✅ Sistema seja robusto e não dependa criticamente do Redis
4. ✅ Leads desqualificados sejam bloqueados adequadamente
5. ✅ Horário comercial seja respeitado

**Próximo passo:** Implementar correções conforme TODO.md detalhado.

---

*Documento gerado em: " + new Date().toISOString() + "*  
*Análise realizada por: Claude 4 Sonnet via Trae AI*  
*Projeto: SolarPrime SDR IA - Sistema de Follow-up*