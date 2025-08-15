#  Diagnóstico e Solução da Integração CRM: KommoCRM (Versão 2)

**Data da Análise:** 15/08/2025
**Status:** Crítico - A sincronização de dados e o fluxo do pipeline entre o agente e o Kommo CRM estão incompletos, impedindo a gestão eficaz dos leads.
**Princípio da Solução:** Centralizar e Orquestrar. Implementar um mecanismo de sincronização proativo e orientado por estado que traduza o contexto da conversa e as ações do sistema em atualizações precisas no CRM.

---

## 1. Resumo Executivo

Após uma análise aprofundada e com base nos novos requisitos de pipeline, o diagnóstico inicial foi confirmado e expandido. A integração com o Kommo CRM falha por três motivos principais:

1.  **Atualização de Nome Falha:** Um bug de propagação de dados impede que o nome do lead, mesmo após ser extraído, seja enviado ao Kommo.
2.  **Estagnação no Pipeline:** O sistema carece de uma lógica explícita para mapear o progresso da conversa (ex: início da qualificação, lead qualificado, reunião agendada) para as mudanças de estágio correspondentes no funil do Kommo.
3.  **Sincronização de Dados Incompleta:** Tags contextuais e campos customizados não são atualizados dinamicamente ao longo da conversa.

Este relatório atualizado detalha uma **solução arquitetural completa** que resolve todos os pontos. A solução se baseia em um **orquestrador de sincronização proativo** que, a cada interação, avalia o estado do lead e aciona as atualizações necessárias no Kommo, garantindo que o CRM seja um reflexo fiel e em tempo real do funil de vendas.

---

## 2. Diagnóstico Detalhado e Mapeamento de Estágios

O problema central é a ausência de uma "ponte" entre a lógica interna do agente e as ações no CRM. O agente determina o estágio da conversa, mas não há um processo para converter essa informação em uma chamada de API para o Kommo.

### Mapeamento do Fluxo de Sincronização (Como Deveria Ser):

- **NOVO LEAD:**
  - **Gatilho:** Primeira mensagem do usuário.
  - **Ação:** `crm_service.create_or_update_lead()` é chamado. **(Funcional)**
  - **Falha Atual:** O nome não é atualizado em interações subsequentes devido ao bug de propagação de dados.

- **EM QUALIFICAÇÃO:**
  - **Gatilho:** O agente apresenta as 4 soluções (início dos fluxos A, B, C ou D).
  - **Ação Necessária:** Mover o card para o estágio "EM QUALIFICAÇÃO".
  - **Falha Atual:** Nenhuma ação é acionada.

- **QUALIFICADO:**
  - **Gatilho:** O agente, com base nas respostas do lead, atinge os critérios de qualificação definidos no `prompt-agente.md`.
  - **Ação Necessária:** Mover o card para "QUALIFICADO".
  - **Falha Atual:** A qualificação é um estado interno do agente, mas não há um gatilho para comunicá-la ao CRM.

- **DESQUALIFICADO:**
  - **Gatilho:** O agente determina que o lead não atende aos critérios mínimos (ex: valor da conta baixo).
  - **Ação Necessária:** Mover o card para "DESQUALIFICADO".
  - **Falha Atual:** Lógica de desqualificação não está conectada a uma ação no CRM.

- **REUNIÃO AGENDADA:**
  - **Gatilho:** Sucesso no agendamento via `calendar_service`.
  - **Ação Necessária:** Mover o card para "REUNIÃO AGENDADA".
  - **Falha Atual:** O fluxo pós-agendamento não inclui a mudança de estágio no CRM.

- **ATENDIMENTO HUMANO:**
  - **Gatilho:** Manual, feito por um atendente no Kommo.
  - **Ação Necessária:** O agente deve parar de interagir com o lead.
  - **Status Atual:** **Funcional.** A lógica de handoff em `webhooks.py` já verifica o `kommo_human_handoff_stage_id` e pausa a interação.

- **NÃO INTERESSADO:**
  - **Gatilho:** Lead não responde à sequência de follow-ups de reengajamento (30 min e 24h).
  - **Ação Necessária:** Mover o card para "NÃO INTERESSADO".
  - **Falha Atual:** O `FollowUpExecutorService` não possui a lógica para acionar esta mudança de estágio ao final do ciclo.

---

## 3. A Solução Completa: Arquitetura de Sincronização Proativa

Implementaremos as seguintes modificações para criar um sistema de sincronização robusto e centralizado.

### Passo 1: Corrigir o Bug da Atualização do Nome

Esta correção é fundamental e permanece a mesma do diagnóstico anterior.

**Arquivo:** `app/agents/agentic_sdr_stateless.py`

```python
# Dentro do método _sync_lead_changes
# ...
try:
    sync_data = lead_info.copy()
    sync_data.update(changes)  # ✅ CORREÇÃO: Mescla as alterações (incluindo o nome) nos dados a serem sincronizados.
    result = await self.team_coordinator.sync_lead_to_crm(sync_data)
# ...
```

### Passo 2: Refatorar o `TeamCoordinator` para Orquestração de Estágios

O `TeamCoordinator` será o ponto central para traduzir o contexto da conversa em ações no CRM. Atualizaremos o método `proactive_crm_sync` para ser mais inteligente.

**Arquivo:** `app/core/team_coordinator.py`

```python
# Substitua o método proactive_crm_sync pela versão aprimorada

async def proactive_crm_sync(self, lead_info: Dict[str, Any], context: Dict[str, Any]):
    """
    Sincroniza proativamente o estágio do lead, tags e campos customizados com o CRM,
    baseado no contexto completo da conversa e nas regras de negócio.
    """
    if "crm" not in self.services:
        return

    crm_service = self.services["crm"]
    kommo_lead_id = lead_info.get("kommo_lead_id")

    if not kommo_lead_id:
        emoji_logger.service_warning("Kommo Lead ID não encontrado para sync proativo.")
        return

    # 1. Mapeamento de Estágio Conversacional para Estágio do CRM
    conversation_stage = context.get("conversation_stage")
    lead_score = lead_info.get("qualification_score", 0)
    
    target_stage_name = None
    if conversation_stage == "agendamento":
        target_stage_name = "REUNIÃO AGENDADA"
    elif conversation_stage == "qualificação":
        if lead_score >= settings.min_qualification_score:
            target_stage_name = "QUALIFICADO"
        else:
            target_stage_name = "DESQUALIFICADO" # Se em qualificação, mas score baixo
    elif conversation_stage in ["estágio_1_apresentar_soluções", "estágio_2_aguardando_escolha"]:
        target_stage_name = "EM QUALIFICAÇÃO"
    
    if target_stage_name:
        await crm_service.update_lead_stage(str(kommo_lead_id), target_stage_name)

    # 2. Atualização de Campos Customizados (Lógica mantida)
    fields_to_update = {}
    if lead_info.get("bill_value"):
        fields_to_update["bill_value"] = lead_info["bill_value"]
    if lead_info.get("chosen_flow"):
        fields_to_update["solution_type"] = lead_info["chosen_flow"]
    
    if fields_to_update:
        await crm_service.update_fields(str(kommo_lead_id), fields_to_update)

    # 3. Atualização de Tags Contextuais (Lógica mantida)
    tags_to_add = []
    if lead_info.get("chosen_flow"):
        tags_to_add.append(f"fluxo_{lead_info['chosen_flow'].lower().replace(' ', '_')}")
    if context.get("objections_raised"):
        for objection in context["objections_raised"]:
            tags_to_add.append(f"objecao_{objection}")
    
    if tags_to_add:
        await crm_service.add_tags_to_lead(str(kommo_lead_id), tags_to_add)
```

### Passo 3: Integrar o Gatilho de "Não Interessado" no Serviço de Follow-up

Modificaremos o `FollowUpExecutorService` para que, ao final de uma sequência de follow-ups sem resposta, ele mova o lead para o estágio correto.

**Arquivo:** `app/services/followup_executor_service.py`

```python
# Adicionar esta lógica ao final do método _schedule_next_followup

# ... dentro de _schedule_next_followup, após a lógica de agendamento ...

                elif trigger == "agent_response_24h":
                    # Este era o follow-up de 24h, pode continuar nurturing ou marcar como perdido
                    attempt = current_followup.get('attempt', 0)
                    if attempt >= 2: # Ex: Após 30min + 24h + 48h sem resposta
                        emoji_logger.system_info(f"🔚 Sequência de follow-up para {lead.get('name')} concluída sem resposta.")
                        # ✅ AÇÃO: Mover para o estágio "NÃO INTERESSADO"
                        if 'crm' in self.services:
                            crm_service = self.services["crm"]
                            kommo_lead_id = lead.get("kommo_lead_id")
                            if kommo_lead_id:
                                await crm_service.update_lead_stage(str(kommo_lead_id), "NÃO INTERESSADO")
                                emoji_logger.crm_event(f"Lead {kommo_lead_id} movido para NÃO INTERESSADO.")
                    else:
                        # Agendar próximo nurturing
                        # ... (lógica existente)
```

---

## 4. Conclusão

Com estas três modificações, o sistema de integração com o Kommo CRM se tornará totalmente funcional e alinhado com as regras de negócio especificadas:

1.  **Correção do Bug:** O nome do lead será atualizado corretamente.
2.  **Orquestração Centralizada:** O `TeamCoordinator` passará a gerenciar ativamente o pipeline do CRM, movendo os leads para os estágios de **EM QUALIFICAÇÃO**, **QUALIFICADO**, **DESQUALIFICADO** e **REUNIÃO AGENDADA** com base no contexto real da conversa.
3.  **Automação de Fim de Ciclo:** O `FollowUpExecutorService` irá mover automaticamente os leads para **NÃO INTERESSADO** após o esgotamento das tentativas de reengajamento.
4.  **Sincronização Contínua:** Tags e campos customizados serão atualizados a cada interação, mantendo o CRM como uma fonte de verdade confiável e em tempo real.

Esta solução é robusta, adere ao princípio da simplicidade e fortalece a arquitetura modular do sistema.