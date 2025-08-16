# Relatório de Diagnóstico de Alucinação do Agente v3

## 1. Visão Geral do Incidente

Em 16/08/2025, aproximadamente à 01:01, o agente SDR apresentou uma alucinação crítica. Após receber a mensagem "oi, boa noite", o agente respondeu como se uma reunião tivesse sido agendada com sucesso, o que não ocorreu. Este comportamento foi causado por uma falha em cascata, iniciada por uma detecção de intenção incorreta no código e agravada por uma ambiguidade no novo `prompt-agente.md`.

## 2. Análise da Causa Raiz (Efeito Cascata)

A investigação do código em `@app/**` e dos logs do servidor revelou uma cadeia de eventos precisa que levou à falha:

### Etapa 1: Detecção de Intenção Incorreta (Gatilho no Código)

- **Componente:** `app/core/team_coordinator.py`
- **Função:** `_analyze_calendar_intent`
- **Problema:** A função que decide se o serviço de calendário deve ser ativado contém uma lista de palavras-chave (`time_patterns`) excessivamente ampla. A lista inclui termos como `"manhã"`, `"tarde"` e `"noite"`.
- **Falha:** A mensagem do usuário, `"oi, boa noite"`, continha a palavra-chave `"noite"`. Isso atribuiu um score de `0.5` para a intenção de agendamento, superando o threshold de `0.35` e ativando o `calendar_service` por engano.

```python
# Trecho problemático em app/core/team_coordinator.py

# 4. INDICADORES DE TEMPO ESPECÍFICO (peso 0.5)
time_patterns = [
    r"\d{1,2}h\d{0,2}", r"\d{1,2}:\d{2}", r"\d{1,2}/\d{1,2}",
    "manhã", "tarde", "noite", "segunda", "terça", "quarta", 
    "quinta", "sexta", "sábado", "domingo"
]
```

### Etapa 2: Execução Desnecessária do Serviço

- **Componente:** `app/services/calendar_service_100_real.py`
- **Ação:** Uma vez que a intenção de agendamento foi detectada (incorretamente), o `TeamCoordinator` executou a função `suggest_times` do serviço de calendário.
- **Resultado:** O serviço consultou o Google Calendar e retornou uma lista de horários disponíveis para o dia seguinte (ex: `['09:00', '10:00', '11:00']`).

### Etapa 3: Alucinação Induzida pelo Prompt

- **Componente:** `app/prompts/prompt-agente.md` (a sua nova versão)
- **Problema:** O resultado da Etapa 2 (`available_slots: ['09:00', ...]`) foi injetado no contexto do agente. O novo prompt, ao que tudo indica, carece de instruções explícitas sobre como lidar com uma **lista de sugestões de horários**. Ele não instrui o agente a **apresentar** esses horários ao usuário.
- **Falha:** Sem uma diretriz clara, o modelo de IA (Gemini) interpretou a presença de dados do serviço de calendário como uma confirmação de que a ação (agendamento) foi concluída com sucesso. Ele "alucinou" o resultado final, em vez de seguir o próximo passo lógico (oferecer os horários).
- **Agravante:** A resposta alucinada incluiu a expressão regional `"Ôxe, que coisa boa!"`, indicando que o modelo tentou seguir as novas diretrizes de personalidade do prompt, mas com base em uma premissa completamente errada.

## 3. Conclusão Final

O incidente não foi causado por uma única falha, mas por uma combinação de um **código com lógica de detecção de intenção frágil** e um **prompt que, embora mais sofisticado em personalidade, tornou-se menos robusto no tratamento de resultados de ferramentas**. A mudança no prompt expôs a fragilidade da lógica de ativação de serviços.

### Recomendações (Para Ação Futura)

1.  **Correção Imediata (Código):** Refinar a função `_analyze_calendar_intent` em `app/core/team_coordinator.py` para remover palavras ambíguas como "manhã", "tarde" e "noite" da detecção de intenção de agendamento. A detecção deve focar em palavras-chave explícitas como "agendar", "marcar", "horário", "reunião", etc.

2.  **Melhora de Robustez (Prompt):** Adicionar uma seção ao `prompt-agente.md` que instrua o agente sobre como agir com base nos resultados das ferramentas. Por exemplo:
    - `SE o calendar_service retornar uma lista de horários, SUA TAREFA é apresentar esses horários ao cliente e perguntar qual ele prefere.`
    - `NUNCA assuma que uma ação foi concluída apenas porque um serviço retornou dados. Apresente os dados ao cliente.`
