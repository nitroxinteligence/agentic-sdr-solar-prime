# Relatório Detalhado de Diagnóstico e Soluções

**Data:** 22 de Agosto de 2025
**Autor:** Agente de Análise de Sistemas Gemini

## 1. Sumário Executivo

O sistema apresenta uma falha crítica onde o agente de IA, Helen Vieira, não está respondendo adequadamente às mensagens do usuário. A análise revelou que o problema não é uma falha de conexão ou um erro de sistema que causa uma parada (crash), mas sim uma **falha de lógica interna na geração de resposta da IA**. O agente processa a mensagem, mas o modelo de linguagem (LLM) falha em gerar uma resposta coerente e alinhada à sua persona, retornando um texto genérico de erro que é então enviado ao usuário.

Este relatório detalha a causa raiz do problema e identifica várias questões estruturais e de lógica subjacentes que contribuem para a instabilidade e a falta de robustez do sistema. As soluções propostas visam não apenas corrigir o problema imediato, mas também fortalecer la arquitetura do agente para torná-lo mais confiável, inteligente e fácil de manter.

## 2. Causa Raiz Imediata: Falha na Geração de Resposta do LLM

A análise do arquivo `logs-console.md` foi conclusiva.

- **Evento:** Uma mensagem "oi" é recebida do número `558182986181`.
- **Processamento:** O webhook (`app/api/webhooks.py`) recebe a mensagem, o `MessageBuffer` a agrupa e a função `process_message_with_agent` é chamada.
- **Contexto:** O agente é instanciado com um histórico de conversa de 73 mensagens (`history_count: 73`).
- **Ponto da Falha:** A função `_generate_response` em `app/agents/agentic_sdr_stateless.py` é chamada. A chamada ao `model_manager.get_response` retorna a seguinte resposta, como visto no log: `"Desculpe, não consegui processar sua solicitação. Poderia tentar novamente?"`.
- **Consequência:** Esta resposta genérica, que não segue a persona e as regras do prompt, é formatada e enviada ao usuário, resultando na percepção de que "o agente não está respondendo".

**Hipóteses para a falha do LLM:**

1.  **Sobrecarga de Contexto:** O histórico de 73 mensagens, somado ao prompt extremamente detalhado, provavelmente excede a janela de contexto ideal do modelo ou o confunde, impedindo-o de seguir as instruções para uma simples saudação.
2.  **Complexidade do Prompt:** O prompt em `app/prompts/prompt-agente.md` é excessivamente longo e complexo. Embora detalhado, ele pode ser contraproducente, criando regras conflitantes ou sobrecarregando a capacidade do modelo de seguir a diretiva principal em um cenário com histórico longo.
3.  **Falta de Instrução para "Reengajamento":** O prompt detalha os fluxos de qualificação, mas pode não ter uma instrução clara sobre como agir quando um usuário antigo com um longo histórico simplesmente diz "oi".

## 3. Problemas Estruturais e de Lógica Encontrados

A análise profunda do código em `app/**` revelou várias vulnerabilidades que precisam ser corrigidas para garantir a estabilidade do sistema.

### 3.1. Lógica Frágil Baseada em Regex e Palavras-chave

- **Arquivos:** `app/core/context_analyzer.py`, `app/core/lead_manager.py`, `app/agents/agentic_sdr_stateless.py`
- **Problema:** Funções críticas como `_extract_intent`, `_extract_name`, e `_extract_bill_value` dependem de expressões regulares e listas de palavras-chave. Isso é extremamente frágil. Por exemplo, se um usuário disser "Gostaria de remarcar nossa conversa", a intenção `reagendamento` pode ser capturada corretamente, mas a lógica de bypass do LLM é muito simplista e pode falhar em extrair os parâmetros necessários, levando a erros.
- **Solução Inteligente:** Substituir a extração baseada em regex por chamadas ao LLM com diretivas para retornar dados estruturados (JSON). Isso torna a extração de intenção e entidades (nome, valor, data) muito mais robusta e flexível.

### 3.2. Falta de Observabilidade e Logging Crítico

- **Arquivos:** `app/core/model_manager.py`, `app/agents/agentic_sdr_stateless.py`
- **Problema:** O log atual não registra a entrada (prompt + histórico) enviada ao LLM nem a saída bruta recebida dele. Isso tornou o diagnóstico da falha atual um processo de inferência. Sem esses logs, é impossível depurar por que o modelo está se comportando de maneira inesperada.
- **Solução Inteligente:** Implementar logging detalhado para todas as interações com o `ModelManager`. Registrar o `system_prompt`, o número de mensagens no histórico e a resposta bruta do modelo antes de qualquer formatação. Isso é vital para a manutenção e o ajuste fino do agente.

### 3.3. Função `process_message` Monolítica (God Method)

- **Arquivo:** `app/agents/agentic_sdr_stateless.py`
- **Problema:** A função `process_message` é excessivamente longa e com múltiplas responsabilidades: processamento de mídia, gerenciamento de histórico, extração de dados do lead, sincronização com CRM, análise de intenção e geração de resposta. Isso viola o Princípio da Responsabilidade Única, tornando o código difícil de ler, testar e depurar.
- **Solução Inteligente:** Refatorar `process_message` em um pipeline de processamento mais claro, com funções menores e bem definidas para cada etapa (ex: `_process_media`, `_update_lead_context`, `_determine_response_strategy`, `_generate_final_response`).

### 3.4. Tratamento de Erros Genérico

- **Arquivos:** `app/agents/agentic_sdr_stateless.py`, `app/api/webhooks.py`
- **Problema:** O bloco `try...except Exception` principal no agente captura qualquer erro e retorna uma mensagem genérica. Isso esconde a causa raiz do problema e impede a recuperação granular de falhas.
- **Solução Inteligente:** Implementar exceções customizadas (ex: `LLMGenerationError`, `ToolExecutionError`) e ter blocos `except` específicos para cada tipo de falha, permitindo que o sistema tente se recuperar de formas diferentes (ex: tentar o modelo de fallback, informar ao usuário que uma ferramenta específica está indisponível) em vez de simplesmente desistir.

## 4. Análise do Prompt (`prompt-agente.md`)

- **Problema 1: Complexidade Excessiva:** O prompt é um documento de engenharia de software, não um conjunto de diretrizes para um LLM. A quantidade de regras, condicionais e a estrutura XML podem confundir o modelo.
- **Problema 2: Regra de Saída Exclusiva:** A regra `<rule id="output_exclusivity" priority="BLOCKER">` é crítica e uma fonte comum de falhas. Ela exige que a saída seja *apenas* um `[TOOL: ...]` ou *apenas* uma `<RESPOSTA_FINAL>`. O código em `_generate_response` que chama o LLM, depois executa a ferramenta e depois chama o LLM novamente é a implementação correta para essa abordagem (padrão ReAct), mas a primeira chamada pode falhar em seguir o formato.
- **Solução Inteligente:**
    1.  **Simplificar o Prompt:** Refatorar o prompt para ser mais conciso. Agrupar regras em seções mais claras e usar linguagem natural em vez de sintaxe XML. Focar nos princípios da persona e nos fluxos principais.
    2.  **Adotar um Prompt de "Roteador" (Router):** Em vez de um único prompt monolítico, usar um primeiro prompt mais simples que decide a intenção principal do usuário (ex: `saudacao`, `qualificacao_fluxo_a`, `agendamento`, `consulta_kb`). Com base na saída do roteador, o sistema então seleciona um prompt secundário, muito mais focado e simples, para gerar a resposta final. Isso reduz drasticamente a carga cognitiva do LLM em cada turno.

## 5. Conclusão e Próximos Passos

A falha atual é um sintoma de problemas mais profundos na arquitetura de lógica e na estratégia de prompt do agente. A correção imediata envolve melhorar o logging e gerenciar o contexto do histórico. A solução de longo prazo requer uma refatoração significativa para tornar o agente menos dependente de lógica frágil (regex) e mais dependente da capacidade de raciocínio do LLM, com melhor observabilidade e uma arquitetura de prompt mais modular.

O plano de ação detalhado para resolver esses problemas está delineado no arquivo `todo.md`.
