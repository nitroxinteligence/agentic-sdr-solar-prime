# Diagnóstico e Plano de Ação: Integração Google Calendar v2

## 1. Diagnóstico Geral

Após uma análise completa do código-fonte, a causa principal para o serviço do Google Calendar não ser ativado de forma consistente foi identificada. O problema não é uma falha única, mas uma combinação de **inconsistência na autenticação** e uma **lógica de acionamento (trigger) reativa**.

- **Problema Central:** O sistema possui um moderno handler de autenticação **OAuth 2.0** (`google_oauth_handler.py`), que é o método correto e necessário para criar eventos com Google Meet e convidar participantes. No entanto, o serviço que o agente efetivamente utiliza (`calendar_service_100_real.py`) está implementado para usar o método legado e mais limitado de **Service Account**. Isso cria um conflito fundamental: o sistema está preparado para o melhor, mas executa o pior.

- **Problema Secundário:** A decisão do agente de agendar uma reunião é **reativa**, dependendo de palavras-chave específicas do usuário (ex: "agendar", "marcar", "horário"). Isso faz com que o agente perca oportunidades de agendamento quando o usuário demonstra claro interesse, mas não usa os termos exatos, exatamente como você descreveu.

## 2. Pontos Críticos Encontrados

| ID | Ponto Crítico | Arquivo(s) Afetado(s) | Impacto |
| :-- | :--- | :--- | :--- |
| **P1** | **Inconsistência na Autenticação** | `calendar_service_100_real.py`, `google_oauth_handler.py` | **Crítico**. Impede a criação de Google Meets e o convite de participantes, que são funcionalidades essenciais. Causa confusão no fluxo de autenticação. |
| **P2** | **Lógica de Acionamento Frágil** | `team_coordinator.py`, `prompt-agente.md` | **Alto**. Causa principal da "não ativação" do serviço. O agente não é proativo e perde chances de agendamento, dependendo da sorte do usuário usar as palavras certas. |
| **P3** | **Complexidade e Redundância** | `google_calendar.py`, `calendar_service_100_real.py` | **Médio**. Existem múltiplos clientes de calendário, violando o princípio de "zero complexidade". Isso aumenta a dificuldade de manutenção e a chance de bugs. |
| **P4** | **Falta de Sincronização Pós-Agendamento** | `agentic_sdr_stateless.py`, `supabase_client.py` | **Médio**. Após agendar, o sistema não armazena de forma robusta o `google_event_id` no lead correspondente no Supabase, dificultando o gerenciamento futuro (cancelar/reagendar). |

## 3. Estratégia de Interação com Ferramentas (A Prova de Alucinações)

Para resolver a questão fundamental de "qual a melhor forma para o agente não alucinar?", é crucial definir a arquitetura correta para a interação entre o LLM e as ferramentas.

### 3.1. Análise de Abordagens: Prompt vs. Orquestrador

Uma abordagem intuitiva seria instruir o LLM diretamente no prompt para gerar o código exato da ferramenta a ser executada (ex: `calendar_service.check_availability()`).

- **Vantagens:**
    - **Simplicidade Aparente:** Parece uma forma direta de comandar o agente.
    - **Flexibilidade:** O comportamento pode ser alterado rapidamente editando o texto do prompt.

- **Desvantagens (Riscos Críticos):**
    - **Risco de Alucinação de Código:** O LLM pode gerar chamadas de função com parâmetros errados, métodos inexistentes ou sintaxe inválida, quebrando o sistema.
    - **Falta de Lógica Estruturada:** O prompt não consegue lidar com lógica complexa (condicionais, loops, tratamento de erros) de forma confiável.
    - **Segurança:** Um input malicioso do usuário poderia enganar o LLM para gerar uma chamada de ferramenta perigosa.
    - **Manutenção Difícil:** O prompt se tornaria um "código spaguetti" de instruções, difícil de depurar e escalar.

### 3.2. A Melhor Estratégia (2025): O Modelo Híbrido - Orquestrador Inteligente

A abordagem mais robusta, segura e que estamos implementando, trata o LLM como um **motor de raciocínio** e o código Python como um **executor de ações**.

**Como Funciona:**

1.  **O Prompt (Define o "Quê" e o "Porquê"):** Define os objetivos e a estratégia do agente. Ex: *"Seu objetivo após qualificar um lead é agendar uma reunião. Seja proativo e sugira isso."*
2.  **O Agente/LLM (Faz a "Análise"):** Analisa a conversa e entende a **intenção**. A saída é uma resposta em linguagem natural que reflete essa intenção, não um código.
3.  **O Orquestrador - `TeamCoordinator` (Decide o "Como" e o "Quando"):** Nosso código Python recebe a intenção do agente, e usa lógica estruturada (`if/else`) para decidir qual ferramenta chamar de forma segura e determinística.

**Diagrama do Fluxo:**
`Usuário -> Agente (LLM + Prompt) -> [Análise/Intenção] -> Orquestrador (TeamCoordinator) -> [Execução Segura da Ferramenta]`

Esta abordagem híbrida nos dá o melhor dos dois mundos: a flexibilidade do LLM e a confiabilidade do código Python.

## 4. Lógica de Acionamento Detalhada

Com o modelo híbrido, o "momento ideal" para cada ação do calendário é determinado pelo estágio da conversa e pela intenção detectada.

#### **Ação: Verificar Disponibilidade (`check_availability`)**
- **Momento Ideal:** Quando o lead demonstra interesse em agendar, mas está incerto sobre o horário, ou pergunta abertamente sobre a agenda.
- **Gatilho:** O `TeamCoordinator` detecta palavras-chave como "horários", "quando", "disponível", ou dias da semana na resposta do usuário ou do próprio agente.

#### **Ação: Agendar Reunião (`schedule_meeting`)**
- **Momento Ideal:** Assim que o lead atende aos critérios de qualificação. O agente deve ser **proativo**.
- **Gatilho:**
    1.  **Contexto:** O agente finaliza as perguntas de qualificação.
    2.  **Lógica do Prompt:** O prompt instrui o agente a focar 100% em agendar a reunião.
    3.  **Ação do Agente:** O agente proativamente oferece o agendamento.
    4.  **Lógica do Orquestrador:** A resposta positiva do usuário, somada ao contexto de "agendamento", atinge o score necessário no `TeamCoordinator` para acionar o serviço.

#### **Ação: Cancelar Reunião (`cancel_meeting`)**
- **Momento Ideal:** Quando o usuário solicita explicitamente o cancelamento.
- **Gatilho:**
    1.  **Usuário:** "Preciso cancelar nossa reunião."
    2.  **Lógica:** O agente primeiro consulta a tabela `leads_qualifications` para encontrar o `google_event_id` associado ao lead.
    3.  **Ação do Agente:** Com o ID, aciona `calendar_service.cancel_meeting(event_id)`.

#### **Ação: Reagendar Reunião (`reschedule_meeting`)**
- **Momento Ideal:** Quando o usuário solicita uma mudança de horário.
- **Gatilho:** É um processo de duas etapas:
    1.  **Cancelar:** O agente executa a lógica de cancelamento para remover o evento antigo.
    2.  **Agendar Novo:** Imediatamente inicia a lógica de "Verificar Disponibilidade" e "Agendar Reunião" para o novo horário.

## 5. Plano de Ação e Solução Proposta

A solução proposta é uma refatoração focada em **unificar, simplificar e tornar a lógica proativa**, seguindo seus princípios de arquitetura.

### Fase 1: Unificação da Autenticação (A Base)

O objetivo é fazer com que todo o sistema utilize o fluxo **OAuth 2.0**, que é mais moderno e funcional.

1.  **Refatorar `calendar_service_100_real.py`:**
    *   Modificar o construtor (`__init__`) e o método `initialize` para obter o serviço de calendário autenticado a partir do `google_oauth_handler.get_oauth_handler().build_calendar_service()`.
    *   Remover completamente a lógica de autenticação via Service Account de dentro deste arquivo.
    *   Ajustar os métodos `schedule_meeting`, `check_availability`, etc., para usar o serviço obtido via OAuth, garantindo que a criação de Google Meet e o convite de participantes funcionem nativamente.

### Fase 2: Fortalecimento do Gatilho de Agendamento (A Inteligência)

Tornaremos o agente **proativo**, transformando o agendamento em uma consequência natural da qualificação.

1.  **Atualizar `prompt-agente.md`:**
    *   Adicionar uma regra explícita na `SEÇÃO 6: FLUXO CONVERSACIONAL COMPLETO`. Após a conclusão das perguntas de qualificação de qualquer fluxo (A, B, C, ou D), a **próxima ação prioritária e obrigatória do agente é tentar o agendamento**.
    *   **Exemplo de nova regra:** `<closing_rule priority="MÁXIMA">Após a última pergunta de qualificação, sua única missão é levar o lead para o agendamento. Use frases como: "Perfeito, {nome}! Com base no que me disse, conseguimos te ajudar. O próximo passo é uma breve reunião com o Leonardo para ele te apresentar os números. Que tal?"</closing_rule>`

2.  **Refinar `team_coordinator.py`:**
    *   Ajustar a função `_analyze_calendar_intent` para dar um peso maior (boost) quando o estágio da conversa for `closing` ou `agendamento_processo`, mesmo que as palavras-chave exatas não estejam na mensagem. Isso fará com que o `TeamCoordinator` reforce a decisão do prompt.

### Fase 3: Robustez e Sincronização (O Polimento)

Garantiremos que o sistema se lembre do que fez e lide com erros de forma graciosa.

1.  **Melhorar `team_coordinator.py`:**
    *   No método `_execute_post_scheduling_workflow`, garantir que o `google_event_id` e o `meet_link` retornados pelo `calendar_service` sejam salvos de volta na tabela `leads_qualifications` do Supabase. Isso associa o evento diretamente ao registro de qualificação, o que é arquiteturalmente mais correto.

2.  **Aprimorar `calendar_service_100_real.py`:**
    *   Envolver as chamadas de API em blocos `try...except` mais específicos para `HttpError`, tratando diferentes códigos de status (403 para permissão, 404 para não encontrado, etc.) e fornecendo logs mais claros.

### Fase 4: Limpeza e Simplificação (O Refinamento)

1.  **Remover Código Obsoleto:**
    *   O arquivo `app/integrations/google_calendar.py` se tornará obsoleto após a Fase 1. Ele deverá ser removido do projeto para eliminar a redundância e simplificar a base de código.

## 6. Benefícios Esperados

- **Funcionalidade Completa:** Agendamentos criarão Google Meets e enviarão convites para os participantes de forma nativa e automática.
- **Redução de "Alucinações":** Com um gatilho proativo e regras claras no prompt, o agente não deixará de agendar reuniões por falta de palavras-chave.
- **Código Simplificado:** A remoção de código redundante e a unificação da autenticação tornarão o sistema mais fácil de manter e depurar.
- **Maior Robustez:** Melhor tratamento de erros e sincronização de estado tornarão a integração mais confiável.

## 7. Próximos Passos

Aguardo sua aprovação para iniciar a implementação deste plano de ação. Podemos começar pela **Fase 1**, que é a mais crítica e trará os maiores benefícios imediatos.