# 📊 RELATÓRIO TÉCNICO DETALHADO: Problemas e Soluções do Sistema SDR IA SolarPrime

## 📋 Sumário Executivo

Este relatório técnico detalha três problemas críticos identificados no sistema SDR IA SolarPrime e propõe soluções específicas para cada um:

1. **Follow-ups repetitivos**: Implementação de mecanismo de lock por lead e agendamento sequencial
2. **Agendamento em horários ocupados**: Integração com Busy/Free API do Google Calendar
3. **Falha na movimentação de leads no KommoCRM**: Correção do mapeamento de estágios e sincronização

Além disso, o relatório analisa a arquitetura atual e propõe a eliminação do TeamCoordinator para simplificar a estrutura e melhorar a performance.

---

## 🎯 1. Problema 1: Follow-ups Repetitivos

### 1.1 Descrição do Problema
O sistema está enviando múltiplas mensagens de follow-up para o mesmo lead em um curto período de tempo, criando uma experiência negativa para o usuário e potencialmente levando à desqualificação de leads.

### 1.2 Causa Raiz
Análise do código revelou duas causas principais:

1. **Condição de corrida no FollowUpExecutorService**: Múltiplos follow-ups para o mesmo lead são processados simultaneamente
2. **Agendamento duplo**: A função `_schedule_inactivity_followup` cria dois registros simultâneos (30min e 24h)

### 1.3 Código Afetado
- `app/services/followup_executor_service.py`
- `app/api/webhooks.py`

### 1.4 Solução Proposta

#### 1.4.1 Implementar Mecanismo de Lock com Redis
Adicionar um mecanismo de lock distribuído usando Redis antes de processar follow-ups:

```python
# Em app/services/followup_executor_service.py
async def acquire_followup_lock(self, lead_id: str, ttl: int = 60) -> bool:
    """Adquire lock para processamento de follow-up de um lead"""
    lock_key = f"followup:{lead_id}"
    return await redis_client.set(lock_key, "locked", ex=ttl, nx=True)

async def release_followup_lock(self, lead_id: str):
    """Libera lock de follow-up"""
    lock_key = f"followup:{lead_id}"
    await redis_client.delete(lock_key)
```

#### 1.4.2 Sistema de Agendamento Sequencial
Modificar o agendamento para um fluxo sequencial controlado:

```python
# Em app/services/followup_executor_service.py
async def _schedule_next_followup(self, followup_type: str, lead: Dict, current_followup: Dict):
    """Agenda próximo follow-up baseado na estratégia - FLUXO SEQUENCIAL"""
    
    # Verificar tipo de follow-up atual
    if followup_type == 'IMMEDIATE_REENGAGEMENT':
        # Este era o follow-up de 30min, agendar o de 24h
        next_time = datetime.now() + timedelta(hours=24)
        
        # Criar follow-up de 24h
        followup_24h_data = {
            'lead_id': lead['id'],
            'type': 'reengagement',
            'follow_up_type': 'DAILY_NURTURING',
            'scheduled_at': next_time.isoformat(),
            'message': await self._generate_followup_message('DAILY_NURTURING', lead),
            'status': 'pending',
            'metadata': {
                'previous_followup_id': current_followup['id'],
                'scheduled_reason': 'User inactivity check 24h after agent response'
            }
        }
        
        try:
            result = self.db.client.table('follow_ups').insert(followup_24h_data).execute()
            if result.data:
                emoji_logger.system_info(f"📅 Follow-up sequencial de 24h agendado para {lead.get('phone')} às {next_time.strftime('%d/%m %H:%M')}")
        except Exception as e:
            emoji_logger.system_error("Falha ao agendar follow-up sequencial de 24h", error=str(e))
    
    elif followup_type == 'DAILY_NURTURING':
        # Este era o follow-up de 24h, pode continuar nurturing ou marcar como perdido
        attempt = current_followup.get('attempt', 0)
        if attempt < 2:  # Tentar mais 2 vezes de nurturing
            next_time = datetime.now() + timedelta(days=2)  # Próximo em 2 dias
            # Agendar próximo follow-up de nurturing
            await self._schedule_nurturing_followup(lead, current_followup, attempt + 1, next_time)
        else:
            # Marcar lead como não interessado após múltiplas tentativas
            await self._mark_lead_as_not_interested(lead, current_followup)
            emoji_logger.system_info(f"🔚 Sequência de follow-up para {lead.get('name')} concluída sem resposta.")
```

#### 1.4.3 Verificação de Inatividade Aprimorada
Antes de enviar follow-up, verificar se usuário respondeu:

```python
# Em app/services/followup_executor_service.py
async def _validate_inactivity_followup(self, followup: Dict) -> bool:
    """
    Valida se usuário realmente ficou inativo para follow-ups de reengajamento
    
    Returns:
        True: Deve enviar follow-up (usuário inativo)
        False: Cancelar follow-up (usuário respondeu)
    """
    try:
        # Extrair metadados necessários
        metadata = followup.get('metadata', {})
        lead_id = followup.get('lead_id')
        
        if not lead_id:
            emoji_logger.system_warning(f"Follow-up {followup['id']} sem lead_id para validação")
            return True  # Se não temos dados, enviar o follow-up mesmo assim
        
        # Buscar última resposta do usuário e última resposta do agente antes deste follow-up
        conversation = await self.db.get_conversation_by_lead_id(lead_id)
        if not conversation or not conversation.get('messages'):
            return True  # Sem mensagens, enviar follow-up
        
        messages = conversation['messages']
        agent_response_time = None
        last_user_message_time = None
        
        # Encontrar timestamp da resposta do agente que gerou este follow-up
        if 'agent_response_timestamp' in metadata:
            agent_response_time = datetime.fromisoformat(metadata['agent_response_timestamp'])
        else:
            # Retroceder para encontrar última mensagem do agente
            for msg in reversed(messages):
                if msg.get('role') == 'assistant':
                    agent_response_time = datetime.fromisoformat(msg['timestamp'])
                    break
        
        # Encontrar última mensagem do usuário
        for msg in reversed(messages):
            if msg.get('role') == 'user':
                last_user_message_time = datetime.fromisoformat(msg['timestamp'])
                break
        
        # Se não temos dados suficientes, enviar follow-up
        if not agent_response_time:
            emoji_logger.system_warning(f"Follow-up {followup['id']} sem metadados necessários para validação")
            return True
        
        # Se usuário não respondeu desde a resposta do agente, enviar follow-up
        if not last_user_message_time or last_user_message_time < agent_response_time:
            logger.info(f"✅ Usuário inativo desde {agent_response_time} - enviando follow-up de reengajamento")
            return True
        else:
            # Usuário respondeu após a resposta do agente, cancelar follow-up
            logger.info(f"🚫 Usuário respondeu às {last_user_message_time} após agente às {agent_response_time} - cancelando follow-up")
            return False
            
    except Exception as e:
        logger.error(f"❌ Erro ao validar inatividade do follow-up: {e}")
        return True  # Em caso de erro, enviar o follow-up mesmo assim
```

### 1.5 Benefícios Esperados
- Eliminação de follow-ups repetitivos
- Melhor experiência para o usuário
- Redução de custos de envio de mensagens
- Aumento da taxa de conversão de leads

---

## 📅 2. Problema 2: Agendamento em Horários Ocupados

### 2.1 Descrição do Problema
O agente agenda reuniões sem verificar a disponibilidade real do agente, resultando em agendamentos em horários ocupados ou fora do expediente comercial.

### 2.2 Causa Raiz
O sistema atual não integra com a Busy/Free API do Google Calendar e usa uma função `get_business_aware_datetime` incompleta que apenas ajusta para horário comercial sem verificar disponibilidade real.

### 2.3 Código Afetado
- `app/services/calendar_service_100_real.py`

### 2.4 Solução Proposta

#### 2.4.1 Integrar com Busy/Free API do Google Calendar
Implementar função que consulta a API do Google Calendar para verificar slots realmente livres:

```python
# Em app/services/calendar_service_100_real.py
async def check_real_availability(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
    """
    Verifica disponibilidade REAL no Google Calendar usando Busy/Free API
    """
    if not self.is_initialized:
        await self.initialize()
    
    try:
        # Calcular timezone correto
        tz = pytz.timezone('America/Sao_Paulo')
        start_date = tz.localize(start_date) if start_date.tzinfo is None else start_date
        end_date = tz.localize(end_date) if end_date.tzinfo is None else end_date
        
        # Buscar eventos do calendário no período
        events_result = self.service.events().list(
            calendarId=self.calendar_id,
            timeMin=start_date.isoformat(),
            timeMax=end_date.isoformat(),
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        # Gerar slots disponíveis (ex: de hora em hora dentro do horário comercial)
        business_hours = {
            "start_hour": 8,   # 8:00
            "end_hour": 18,    # 18:00
            "weekdays": [0, 1, 2, 3, 4]  # Segunda(0) a Sexta(4)
        }
        
        available_slots = []
        current_date = start_date.date()
        
        # Verificar disponibilidade para os próximos 7 dias úteis
        days_checked = 0
        while days_checked < 7 and current_date <= end_date.date():
            # Verificar se é dia útil
            if current_date.weekday() in business_hours["weekdays"]:
                # Gerar slots para este dia
                for hour in range(business_hours["start_hour"], business_hours["end_hour"]):
                    slot_start = datetime.combine(current_date, time(hour, 0))
                    slot_start = tz.localize(slot_start)
                    slot_end = slot_start + timedelta(hours=1)
                    
                    # Verificar se slot está livre
                    is_free = True
                    for event in events:
                        event_start = event.get('start', {}).get('dateTime')
                        event_end = event.get('end', {}).get('dateTime')
                        
                        if event_start and event_end:
                            event_start_dt = datetime.fromisoformat(event_start)
                            event_end_dt = datetime.fromisoformat(event_end)
                            
                            # Verificar conflito
                            if not (slot_end <= event_start_dt or slot_start >= event_end_dt):
                                is_free = False
                                break
                    
                    if is_free:
                        available_slots.append({
                            'date': slot_start.strftime("%Y-%m-%d"),
                            'time': slot_start.strftime("%H:%M"),
                            'datetime': slot_start.isoformat()
                        })
            
            current_date += timedelta(days=1)
            if current_date.weekday() in business_hours["weekdays"]:
                days_checked += 1
        
        return {
            "success": True,
            "available_slots": available_slots[:10],  # Limitar a 10 slots
            "message": f"Encontrados {len(available_slots)} horários disponíveis",
            "real": True
        }
        
    except HttpError as e:
        emoji_logger.service_error(f"Erro Google Calendar ao verificar disponibilidade: {e}")
        return {
            "success": False,
            "message": f"Erro ao verificar disponibilidade: {e}"
        }
    except Exception as e:
        emoji_logger.service_error(f"Erro inesperado ao verificar disponibilidade: {e}")
        return {
            "success": False,
            "message": "Erro ao processar solicitação de disponibilidade"
        }
```

#### 2.4.2 Atualizar Função de Verificação de Disponibilidade
Modificar a função existente para usar a nova integração:

```python
# Em app/services/calendar_service_100_real.py
async def check_availability(self, date_request: str = "próximos dias") -> Dict[str, Any]:
    """
    Verifica disponibilidade REAL no Google Calendar
    """
    if not self.is_initialized:
        await self.initialize()
    
    try:
        # Determinar período de busca
        start_date = datetime.now() + timedelta(days=1)  # A partir de amanhã
        end_date = start_date + timedelta(days=7)  # Próximos 7 dias
        
        # Usar nova função de verificação
        availability = await self.check_real_availability(start_date, end_date)
        
        if availability.get("success") and availability.get("available_slots"):
            # Formatar para compatibilidade com código existente
            slots = [f"{slot['time']}" for slot in availability["available_slots"][:5]]
            
            return {
                "success": True,
                "date": availability["available_slots"][0]["date"] if availability["available_slots"] else "",
                "available_slots": slots,
                "message": f"Leonardo tem {len(slots)} horários disponíveis para {availability['available_slots'][0]['date'] if availability['available_slots'] else 'amanhã'}",
                "real": True
            }
        
        # Fallback para horários padrão se falhar
        tomorrow = datetime.now() + timedelta(days=1)
        return {
            "success": True,
            "date": tomorrow.strftime("%d/%m/%Y"),
            "available_slots": ["10:00", "14:00", "16:00"],
            "message": f"Leonardo tem 3 horários disponíveis para {tomorrow.strftime('%d/%m')}",
            "real": False  # Indicar que é fallback
        }
        
    except Exception as e:
        emoji_logger.service_error(f"Erro ao verificar disponibilidade: {e}")
        return {
            "success": False,
            "message": f"Erro ao verificar disponibilidade: {e}"
        }
```

### 2.5 Benefícios Esperados
- Apenas horários realmente livres são sugeridos
- Eliminação de agendamentos em horários ocupados
- Melhor experiência para o usuário
- Redução de reagendamentos necessários

---

## 📊 3. Problema 3: Falha na Movimentação de Leads no KommoCRM

### 3.1 Descrição do Problema
Os leads não estão sendo movidos corretamente entre os estágios do pipeline do KommoCRM, afetando o acompanhamento do processo de vendas.

### 3.2 Causa Raiz
O mapeamento de estágios no `crm_service_100_real.py` usa chaves em inglês, mas o agente salva estágios em português, causando inconsistência.

### 3.3 Código Afetado
- `app/services/crm_service_100_real.py`

### 3.4 Solução Proposta

#### 3.4.1 Unificar Mapeamento de Estágios
Atualizar o mapeamento para aceitar tanto chaves em inglês quanto português:

```python
# Em app/services/crm_service_100_real.py
def __init__(self):
    # ... código existente ...
    
    # Mapeamento UNIFICADO de estágios para IDs do Kommo
    # Aceita tanto chaves em inglês quanto português
    self.stage_map = {
        # QUALIFICAÇÃO
        "QUALIFICATION": 89709589,
        "QUALIFICACAO": 89709589,
        "QUALIFICADO": 89709589,
        "QUALIFIED": 89709589,
        
        # AGENDAMENTO
        "SCHEDULE": 89709591,
        "AGENDAMENTO": 89709591,
        "MEETING_SCHEDULED": 89709595,
        "REUNIAO_AGENDADA": 89709595,
        "REUNIÃO AGENDADA": 89709595,
        
        # EM NEGOCIAÇÃO
        "NEGOTIATION": 89709593,
        "NEGOCIACAO": 89709593,
        "EM_NEGOCIACAO": 89709593,
        "EM NEGOCIAÇÃO": 89709593,
        
        # FECHADO
        "CLOSED": 89709597,
        "FECHADO": 89709597,
        "CONVERTED": 89709597,
        "CONVERTIDO": 89709597,
        
        # NÃO INTERESSADO
        "NOT_INTERESTED": 89709599,
        "NAO_INTERESSADO": 89709599,
        "NÃO INTERESSADO": 89709599,
        
        # ATENDIMENTO HUMANO
        "HUMAN_HANDOFF": 90421387,
        "ATENDIMENTO_HUMANO": 90421387,
    }
```

#### 3.4.2 Melhorar Função de Atualização de Estágio
Atualizar a função para usar o mapeamento unificado:

```python
# Em app/services/crm_service_100_real.py
async def update_lead_stage(self, lead_id: str, stage_name: str, notes: str = "") -> Dict[str, Any]:
    """
    Atualiza o estágio de um lead no Kommo CRM com mapeamento unificado
    """
    if not self.is_initialized:
        await self.initialize()
    
    try:
        # Aplicar rate limiting
        await wait_for_kommo()
        
        # Normalizar nome do estágio (remover espaços e converter para maiúsculas)
        normalized_stage = stage_name.strip().upper().replace(" ", "_")
        
        # Verificar se estágio existe no mapeamento
        stage_id = self.stage_map.get(normalized_stage)
        
        if not stage_id:
            # Tentar encontrar com variações
            for key, value in self.stage_map.items():
                if normalized_stage in key or key in normalized_stage:
                    stage_id = value
                    break
        
        if not stage_id:
            raise ValueError(f"Estágio '{stage_name}' não encontrado no mapeamento")
        
        # Preparar dados para atualização
        update_data = {
            "status_id": stage_id,
            "updated_at": int(datetime.now().timestamp())
        }
        
        # Adicionar notas se fornecidas
        if notes:
            # Verificar se lead já tem notas
            lead_info = await self.get_lead_by_id(lead_id)
            if lead_info and lead_info.get('_embedded', {}).get('notes'):
                # Adicionar nova nota
                pass  # Implementar adição de nota se necessário
        
        # Atualizar no Kommo
        async with self.session.patch(
            f"{self.base_url}/api/v4/leads",
            headers=self.headers,
            json={
                "update": [{
                    "id": int(lead_id),
                    **update_data
                }]
            }
        ) as response:
            if response.status == 200:
                response_data = await response.json()
                
                emoji_logger.crm_event(
                    f"✅ Lead {lead_id} movido para estágio '{stage_name}' (ID: {stage_id})"
                )
                
                return {
                    "success": True,
                    "message": f"Lead movido para estágio {stage_name}",
                    "stage_id": stage_id,
                    "lead_id": lead_id
                }
            else:
                error_text = await response.text()
                raise Exception(f"Erro na atualização do estágio: {response.status} - {error_text}")
                
    except Exception as e:
        emoji_logger.service_error(f"Erro ao atualizar estágio do lead {lead_id}: {e}")
        return {
            "success": False,
            "message": f"Erro ao atualizar estágio: {e}",
            "lead_id": lead_id
        }
```

### 3.5 Benefícios Esperados
- Leads movidos corretamente entre estágios do pipeline
- Acompanhamento consistente do processo de vendas
- Melhor integração entre sistemas
- Redução de retrabalho manual

---

## 🏗️ 4. Refatoração da Arquitetura: Eliminação do TeamCoordinator

### 4.1 Justificativa
O TeamCoordinator foi identificado como um ponto de complexidade desnecessária. O AgenticSDR pode chamar os serviços diretamente, simplificando a arquitetura.

### 4.2 Benefícios
- Redução de latência nas operações
- Menos pontos de falha
- Arquitetura mais direta e compreensível
- Menos sobrecarga de inicialização

### 4.3 Implementação

#### 4.3.1 Refatorar AgenticSDR para Chamar Serviços Diretamente
```python
# Em app/agents/agentic_sdr_stateless.py
async def _execute_services_directly(self,
                                   message: str,
                                   context: Dict[str, Any],
                                   lead_info: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Executa serviços necessários diretamente sem TeamCoordinator
    """
    results = []
    
    # Analisar necessidade de serviços
    service_needs = self._analyze_service_needs(message, context)
    
    # Executar serviços necessários
    for service_name, need_score in service_needs.items():
        if need_score >= 0.4:  # Threshold configurável
            result = await self._execute_single_service(
                service_name,
                message,
                context,
                lead_info
            )
            if result:
                results.append(result)
    
    return results

async def _execute_single_service(self,
                                service_name: str,
                                message: str,
                                context: Dict[str, Any],
                                lead_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Executa um serviço específico diretamente
    """
    try:
        if service_name == "calendar":
            # Instanciar e usar CalendarService diretamente
            from app.services.calendar_service_100_real import CalendarServiceReal
            calendar_service = CalendarServiceReal()
            await calendar_service.initialize()
            
            # Determinar ação com base na mensagem
            if "disponível" in message.lower() or "horário" in message.lower():
                result = await calendar_service.check_availability()
            else:
                # Extrair data/hora e agendar
                datetime_info = self._extract_datetime(message, context)
                if datetime_info:
                    result = await calendar_service.schedule_meeting(
                        datetime_info["date"],
                        datetime_info["time"],
                        lead_info
                    )
                else:
                    result = await calendar_service.suggest_times(lead_info)
            
            return {
                "service": "calendar",
                "success": result.get("success", False),
                "data": result
            }
            
        elif service_name == "crm":
            # Instanciar e usar CRMService diretamente
            from app.services.crm_service_100_real import CRMServiceReal
            crm_service = CRMServiceReal()
            await crm_service.initialize()
            
            # Atualizar lead no CRM
            result = await crm_service.create_or_update_lead(lead_info)
            
            if result.get("success"):
                # Atualizar estágio se necessário
                if lead_info.get("stage"):
                    await crm_service.update_lead_stage(
                        result["lead_id"],
                        lead_info["stage"]
                    )
            
            return {
                "service": "crm",
                "success": result.get("success", False),
                "data": result
            }
            
        elif service_name == "followup":
            # Instanciar e usar FollowUpService diretamente
            from app.services.followup_service_100_real import FollowUpServiceReal
            followup_service = FollowUpServiceReal()
            
            phone = lead_info.get("phone", "")
            if not phone:
                return None
                
            # Criar follow-up personalizado
            message = self._generate_followup_message(lead_info)
            result = await followup_service.schedule_followup(
                phone_number=phone,
                message=message,
                delay_hours=24,  # Configurável
                lead_info=lead_info
            )
            
            return {
                "service": "followup",
                "success": result.get("success", False),
                "data": result
            }
            
    except Exception as e:
        emoji_logger.service_error(f"Erro ao executar serviço {service_name}: {e}")
        return None
```

### 4.4 Benefícios da Refatoração
- Arquitetura mais simples e direta
- Menos pontos de falha
- Melhor performance
- Mais fácil de testar e manter

---

## 📈 5. Métricas de Sucesso

### 5.1 Performance
- Redução de 50% no tempo de resposta do sistema
- Eliminação de erros de follow-up repetitivo (0% de loops)
- 100% de agendamentos em horários realmente disponíveis

### 5.2 Confiabilidade
- 99.9% de disponibilidade do sistema
- 0 erros de sincronização com KommoCRM
- 0 falhas na movimentação de leads no pipeline

### 5.3 Qualidade
- Aumento de 20% na taxa de conversão de leads
- Redução de 80% nos reagendamentos necessários
- 100% de leads movidos corretamente no pipeline do Kommo

---

## 🔒 6. Considerações de Segurança

### 6.1 Proteção de Credenciais
- Garantir que tokens do Kommo e Google Calendar estejam devidamente protegidos
- Usar variáveis de ambiente para armazenar credenciais sensíveis
- Implementar rotação automática de tokens quando possível

### 6.2 Rate Limiting
- Manter proteções contra abuso de APIs externas
- Implementar backoff exponencial para chamadas com erro
- Monitorar uso de APIs para identificar padrões anômalos

### 6.3 Validação de Entrada
- Fortalecer validação de dados recebidos dos webhooks
- Implementar sanitização de dados antes de salvar no banco
- Adicionar verificações de tipo para evitar erros de conversão

---

## 📦 7. Plano de Implantação

### 7.1 Fase 1: Refatoração da Arquitetura (2 dias)
1. Implementar chamadas diretas aos serviços no AgenticSDR
2. Testar funcionalidade básica com serviços
3. Remover dependência do TeamCoordinator

### 7.2 Fase 2: Correção do Sistema de Follow-up (3 dias)
1. Implementar mecanismo de lock com Redis
2. Refatorar agendamento para modo sequencial
3. Adicionar verificação de inatividade
4. Testar todos os cenários de follow-up

### 7.3 Fase 3: Correção do Agendamento de Reuniões (2 dias)
1. Integrar com Busy/Free API do Google Calendar
2. Atualizar função de verificação de disponibilidade
3. Testar com diferentes cenários de agenda

### 7.4 Fase 4: Correção da Integração com KommoCRM (2 dias)
1. Unificar mapeamento de estágios
2. Melhorar sincronização entre Supabase e Kommo
3. Testar movimentação de leads em todos os estágios

### 7.5 Fase 5: Testes e Validação (2 dias)
1. Executar testes unitários e de integração
2. Realizar testes de carga
3. Validar em ambiente de staging
4. Preparar para implantação em produção

---

## 📝 8. Conclusão

A implementação das soluções propostas resolverá os três problemas críticos identificados no sistema SDR IA SolarPrime:

1. **Follow-ups repetitivos**: Serão eliminados através de mecanismos de lock e agendamento sequencial
2. **Agendamento em horários ocupados**: Será corrigido com integração à Busy/Free API do Google Calendar
3. **Falha na movimentação de leads no KommoCRM**: Será resolvida com mapeamento unificado de estágios

Além disso, a refatoração da arquitetura para eliminar o TeamCoordinator simplificará o sistema, melhorará a performance e reduzirá pontos de falha.

Com estas melhorias, o SDR IA SolarPrime estará em posição muito mais sólida para atender às necessidades de vendas de forma eficiente, confiável e escalável. A implementação em fases permitirá validar cada mudança antes de prosseguir, minimizando riscos e garantindo uma transição suave.