# Relatório de Diagnóstico e Plano de Ação: Repetição e Falha de Agendamento

## 1. Resumo dos Problemas Identificados

A análise da conversa em `@dialogos-chat.md` e dos logs em `@logs-console.md` revelou duas falhas críticas no comportamento do agente:

1.  **Repetição Excessiva de Saudações:** O agente inicia a maioria das suas respostas com saudações genéricas (ex: "Massa, Mateus!", "Show de bola, Mateus!"), o que torna a interação robótica e pouco natural.
2.  **Falha Completa no Agendamento de Reuniões:** O agente entra em loop ao tentar agendar uma reunião. Ele sugere o agendamento, mas nunca aciona o `calendar_service` para verificar a disponibilidade ou criar o evento, mesmo quando o usuário expressa claramente a intenção de agendar (ex: "amanha pode ser?").

## 2. Análise da Causa Raiz

### 2.1. Causa da Repetição de Saudações

- **Componente:** `app/prompts/prompt-agente.md`
- **Análise:** O prompt atual, embora incentive a variação linguística através de um banco de sinônimos, carece de uma **regra negativa forte**. Não há uma instrução clara para **evitar** o uso de saudações em todas as mensagens. O modelo de IA, ao tentar ser cordial, acaba por superutilizar este padrão, resultando em um comportamento repetitivo.

### 2.2. Causa da Falha no Agendamento

- **Componente:** `app/core/team_coordinator.py`
- **Análise:** A lógica de acionamento de serviços é baseada em uma análise de intenção por palavras-chave (`analyze_service_need`). O sistema busca termos exatos como "agendar", "marcar", "reunião", "horário".
- **Falha:** No diálogo fornecido, o usuário responde "amanha pode ser?" e depois "pode ser as 09h?". Nenhuma dessas frases contém as palavras-chave que o `TeamCoordinator` está programado para detectar. Consequentemente, o `score` para a ativação do `calendar_service` permanece em `0.000`, e a ferramenta nunca é chamada. O agente fica preso, pois o prompt o instrui a agendar, mas a lógica do código não lhe dá a capacidade de fazê-lo sem as palavras-chave exatas.

## 3. Solução Proposta: Orquestração Guiada por IA com Chamada de Ferramentas (Tools)

A abordagem atual de tentar adivinhar a intenção do usuário com palavras-chave é inerentemente frágil. A solução mais robusta e eficiente é delegar a decisão de usar ferramentas ao próprio agente de IA, que possui um entendimento muito superior do contexto conversacional.

Esta nova arquitetura, conhecida como **Agent-Led Orchestration with Tool-Calling**, consiste em três etapas principais:

### Etapa 1: Modificar o Prompt para Definir Ferramentas

Vamos alterar o `prompt-agente.md` para ensinar o agente a "chamar ferramentas". Em vez de apenas seguir um fluxo, ele será instruído a gerar uma tag especial `<tool_call>` quando precisar de uma informação externa (como a disponibilidade da agenda).

**Exemplo de nova regra no prompt:**

```xml
<!-- SEÇÃO 15: FLUXOS CONVERSACIONAIS COMPLETOS -->
<agendamento_processo>
  <step_1>Lead confirma interesse em agendar.</step_1>
  <step_2>Confirmar se o decisor estará presente.</step_2>
  <step_3>
    SE decisor confirmado, SUA AÇÃO É:
    <tool_call>calendar_service.check_availability</tool_call>
  </step_3>
  <step_4>SE calendar_service retornar horários, APRESENTE-OS e pergunte qual o lead prefere.</step_4>
  <step_5>SE lead escolher horário, SUA AÇÃO É:
    <tool_call>calendar_service.schedule_meeting(date="{data}", time="{hora}", lead_info={lead_info})</tool_call>
  </step_5>
</agendamento_processo>
```

### Etapa 2: Modificar o Código para Executar as Ferramentas

Vamos adaptar o `AgenticSDRStateless` em `app/agents/agentic_sdr_stateless.py` para se tornar um executor de ferramentas.

1.  **Gerar Resposta Inicial:** O agente gera uma resposta normalmente.
2.  **Detectar Chamada de Ferramenta:** O código irá verificar se a resposta contém a tag `<tool_call>`.
3.  **Executar Ferramenta:** Se a tag for encontrada, o código irá:
    a.  Extrair o nome da ferramenta (ex: `calendar_service.check_availability`).
    b.  Chamar a função correspondente no `TeamCoordinator`.
    c.  Capturar o resultado (ex: a lista de horários disponíveis).
4.  **Gerar Resposta Final:** O código irá fazer uma **segunda chamada** ao modelo de IA, injetando o resultado da ferramenta no contexto. O prompt será algo como:

    > "Contexto: O usuário quer agendar para amanhã. Você usou a ferramenta `check_availability` e o resultado foi: `['09:00', '10:00', '11:00']`. Agora, formule a resposta para o usuário."

    O agente então gerará a resposta final e natural: "Perfeito, Mateus! O Leonardo tem estes horários disponíveis amanhã: 09:00, 10:00 e 11:00. Qual fica melhor para você?"

### Etapa 3: Refinar o Prompt Contra Repetições

Para resolver o problema das saudações repetitivas, vamos adicionar uma regra mais explícita e com maior prioridade no `prompt-agente.md`:

```xml
<rule priority="CRÍTICA" id="direct_communication">
  - NUNCA inicie uma mensagem com saudações genéricas ("Olá", "Opa", "Show de bola") se uma conversa já estiver em andamento.
  - Vá direto ao ponto. A saudação só é permitida na PRIMEIRA mensagem da conversa.
  - Use o nome do lead com extrema moderação (apenas em momentos chave, como no fechamento).
</rule>
```

## 4. Vantagens da Nova Abordagem

- **Robustez:** A decisão de agendar é baseada no fluxo contextual da conversa, não em palavras-chave frágeis.
- **Inteligência:** Permite que o agente lide com variações da linguagem natural (como "amanhã de manhã" ou "pode ser às 9h?") de forma muito mais eficaz.
- **Manutenibilidade:** A lógica de quando chamar uma ferramenta fica centralizada no prompt, tornando-a mais fácil de entender e modificar, sem a necessidade de alterar o código Python para cada novo cenário.
- **Eficiência:** O agente se torna mais autônomo e proativo, seguindo o fluxo de qualificação e agendamento de forma mais direta e com menos erros.
