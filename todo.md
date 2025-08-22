# Histórico de Correções Críticas - 22/08/2025

## ✅ **CLOSED** - Falha no Cancelamento de Reuniões e Erro de Redis

-   **[DONE]** Corrigido `TypeError` na chamada `eval` do Redis em `calendar_service_100_real.py` para usar a sintaxe posicional correta.
-   **[DONE]** Refatorado o fluxo de agendamento para salvar o `google_event_id` na tabela `leads_qualifications` após uma reunião ser criada com sucesso.
-   **[DONE]** Refatorado o fluxo de cancelamento e reagendamento para buscar o `meeting_id` da qualificação mais recente do lead, garantindo a manutenção do estado.

## ✅ **CLOSED** - Cascata de Erros no Workflow Pós-Agendamento

-   **[DONE]** Corrigida a inconsistência de `case` e acentuação no nome do estágio `em_qualificação` para o Kommo CRM.
-   **[DONE]** Corrigido `AttributeError` no agente ao chamar `crm_service.update_lead` (anteriormente chamava `update_fields` de forma incorreta).
-   **[DONE]** Resolvido `TypeError` de fuso horário ao agendar follow-ups, padronizando o uso de datetimes "cientes" (com fuso horário).

## ✅ **CLOSED** - Agente Ignorando Análise de Mídia (Imagens/Documentos)

-   **[DONE]** **Causa Raiz Identificada:** A ordem das operações no `agentic_sdr_stateless.py` estava incorreta. As análises de contexto e de lead eram executadas *antes* do processamento da mídia, resultando em decisões baseadas em estado desatualizado.
-   **[DONE]** **Solução Implementada:** O método `process_message` foi refatorado para garantir que o processamento de mídia ocorra **primeiro**. A informação extraída (ex: valor da conta) é imediatamente injetada no `lead_info` e no conteúdo da mensagem do usuário.
-   **[DONE]** As análises de `LeadManager` e `ContextAnalyzer` agora rodam **após** a atualização do contexto com os dados da mídia, garantindo que o agente tenha a informação mais recente para tomar decisões e evitando o loop de perguntas.

## ✅ **CLOSED** - Refinamentos de Comportamento

-   **[DONE]** Adicionada regra `ABSOLUTA` e `INVIOLÁVEL` ao prompt do agente para proibir o uso de emojis nas respostas, garantindo um tom mais profissional.
