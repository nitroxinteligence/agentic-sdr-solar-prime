# Relatório de Diagnóstico: Agendamento Sobreposto no Google Calendar

**Data:** 23 de Agosto de 2025
**Autor:** Agente Gemini
**Status:** Análise Concluída

---

## 1. Resumo do Problema (Sintoma)

O sistema está permitindo que o agente de IA agende ou reagende reuniões em horários que já estão ocupados no Google Calendar, resultando em "double booking" (agendamentos sobrepostos), como evidenciado pela captura de tela fornecida.

-   **Observação 1:** O agente confirma o agendamento para o usuário.
-   **Observação 2:** O evento é de fato criado no calendário, mas sobrepõe um evento existente.
-   **Impacto:** Esta falha compromete a confiabilidade do sistema, gera conflitos de agenda para a equipe de vendas e prejudica a experiência do cliente.

## 2. Análise da Causa Raiz

A investigação do código-fonte, focada em `app/services/calendar_service_100_real.py` e `app/agents/agentic_sdr_stateless.py`, revelou uma **falha arquitetural crítica**: a responsabilidade de verificar conflitos de horário não está sendo devidamente aplicada na camada de serviço.

### Falha Principal: Ausência de Verificação Proativa de Conflitos

1.  **`schedule_meeting` (Agendar Nova Reunião):**
    -   **Problema:** Esta função **não realiza nenhuma verificação proativa** para saber se o horário solicitado já está ocupado. Ela tenta criar o evento diretamente.
    -   **Lógica Atual:** A função apenas *reage* a um erro `HttpError 409 (Conflict)` retornado pela API do Google. Se a API, por qualquer motivo, não retornar este erro específico, o evento é criado, causando a sobreposição.
    -   **Risco:** Confiar apenas na detecção de conflito da API do Google é frágil. A responsabilidade de garantir um horário vago deve ser do nosso próprio sistema, *antes* de tentar a escrita no calendário.

2.  **`reschedule_meeting` (Reagendar Reunião):**
    -   **Problema:** Embora esta função contenha uma lógica para verificar conflitos, ela não é suficientemente robusta e pode ser contornada. A falha principal é a mesma: o sistema não garante a verificação de disponibilidade como um passo obrigatório e inviolável.
    -   **Risco:** A lógica de verificação está acoplada ao fluxo de reagendamento e não é reutilizada de forma consistente, abrindo margem para cenários onde a verificação pode falhar ou ser pulada.

### Falha Arquitetural Subjacente

A responsabilidade de garantir que um horário esteja livre não deveria ser do agente de IA ou do orquestrador (`AgenticSDRStateless`). Deixar essa decisão a cargo do LLM (que precisa "lembrar" de chamar `check_availability` antes de `schedule_meeting`) é inerentemente instável.

**A camada de serviço (`CalendarServiceReal`) deve ser a guardiã do estado do calendário.** Qualquer chamada para `schedule_meeting` ou `reschedule_meeting` deve, como primeira e obrigatória ação, validar a disponibilidade do horário solicitado.

## 3. Solução Estratégica Proposta

A solução definitiva é refatorar o `CalendarServiceReal` para internalizar e tornar a verificação de conflitos um passo **obrigatório e não negociável** em todas as operações de escrita (criação e atualização de eventos).

### Pilares da Solução:

1.  **Centralizar a Lógica de Verificação:** Criar uma função interna e robusta, `_is_slot_available(start_time, end_time)`, dentro do `CalendarServiceReal`. Esta função será a única fonte da verdade sobre a disponibilidade de um horário.

2.  **Tornar a Verificação Mandatória:**
    -   No início da função `schedule_meeting`, chamar `_is_slot_available`. Se o horário estiver ocupado, a função deve retornar um erro de conflito imediatamente, sem sequer tentar chamar a API do Google para criar o evento.
    -   No início da função `reschedule_meeting`, usar a mesma função `_is_slot_available` para validar o novo horário.

3.  **Melhorar a Resposta de Erro:** Quando um conflito for detectado proativamente, a função deve retornar uma resposta estruturada, informando o erro e, se possível, sugerindo os próximos horários livres (reutilizando a lógica já existente em `check_availability`).

Esta abordagem move a responsabilidade para a camada correta, desacopla a lógica de negócio da orquestração do LLM e torna o sistema de agendamento fundamentalmente mais robusto e confiável.
