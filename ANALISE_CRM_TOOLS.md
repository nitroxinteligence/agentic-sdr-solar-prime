# Análise de Viabilidade: Expansão de Ferramentas de CRM via Tool Calls

**Data:** 16 de agosto de 2025
**Autor:** Gemini
**Status:** Análise Concluída

## 1. Diagnóstico e Resumo Executivo (TL;DR)

A análise confirma que a implementação de novas ferramentas de CRM (movimentar cards, atualizar tags, etc.) através do sistema de `tool calls` no `agentic_sdr_stateless.py` é **altamente viável e recomendada**.

A arquitetura atual é ideal para essa expansão. O agente já utiliza um mecanismo de `tool calls` para interagir com serviços, e o `crm_service_100_real.py` já possui as funções necessárias para executar as ações desejadas. A implementação consiste apenas em "conectar" o agente a essas funções já existentes.

**Conclusão:** A implementação é de baixo risco, baixo esforço e trará um ganho significativo de autonomia e eficiência para o agente.

---

## 2. Análise da Arquitetura Atual

Para entender a viabilidade, foram analisados os seguintes componentes chave no diretório `@app/`:

### a. `app/agents/agentic_sdr_stateless.py` (O Agente)

Este é o cérebro da operação. A análise revelou um sistema de `tool calling` já implementado e em uso.

- **Mecanismo de Detecção:** O método `_parse_and_execute_tools` utiliza a expressão regular `\[TOOL: ...\]` para identificar chamadas de ferramentas na resposta do LLM.
- **Mecanismo de Execução:** O método `_execute_single_tool` atua como um roteador, direcionando a chamada para o serviço correto.
- **Ferramentas de CRM Existentes:** O agente já possui ferramentas para interagir com o CRM:
    - `crm.update_stage`: Para mover o lead no funil.
    - `crm.update_field`: Para atualizar um campo customizado.

Isso demonstra que o padrão para adicionar novas ferramentas de CRM já está estabelecido e funcional.

### b. `app/services/crm_service_100_real.py` (O Serviço de CRM)

Este arquivo contém a lógica de negócio para interagir com a API do Kommo (CRM). A análise confirmou que as funções necessárias para as novas ferramentas **já existem e são robustas**:

- `update_lead_stage(lead_id, stage)`: Já utilizada pelo agente.
- `update_fields(lead_id, fields)`: Já utilizada pelo agente.
- `add_tags_to_lead(lead_id, tags)`: **Existe, mas não está exposta como uma ferramenta para o agente.** Esta é a função que usaremos para a nova ferramenta de tags.
- `create_or_update_lead(lead_data, tags)`: Permite criar e atualizar leads, inclusive com tags, o que reforça a capacidade do sistema.

A presença dessas funções no serviço de CRM significa que não precisamos escrever nenhuma lógica nova de integração com a API do Kommo. O trabalho é apenas no nível do agente.

### c. `app/prompts/prompt-agente.md` (O Cérebro do Agente)

Este arquivo é crucial. Ele "ensina" o agente a como e quando usar as ferramentas disponíveis. A seção `<tool_calling_system>` já documenta as ferramentas existentes, fornecendo a sintaxe e exemplos para o LLM.

Para que o agente aprenda a usar as novas ferramentas, este prompt deverá ser atualizado.

---

## 3. Plano de Implementação Detalhado

A implementação é notavelmente simples e envolve a modificação de apenas dois arquivos.

### Passo 1: Expor a Função de Tags no Agente

Precisamos adicionar um novo `elif` no método `_execute_single_tool` do arquivo `app/agents/agentic_sdr_stateless.py` para que ele saiba o que fazer quando o LLM gerar um `[TOOL: crm.add_tags]`.

**Arquivo a ser modificado:** `app/agents/agentic_sdr_stateless.py`

**Código a ser adicionado dentro do método `_execute_single_tool`:**

```python
        # ... (código existente para crm.update_field)

            elif method_name == "add_tags":
                tags_str = params.get("tags", "")
                if tags_str:
                    # Converte string separada por vírgula em lista
                    tags = [tag.strip() for tag in tags_str.split(',')]
                    return await crm_service.add_tags_to_lead(
                        lead_info.get("kommo_lead_id"),
                        tags
                    )
        
        # Follow-up tools
        elif service_name == "followup":
        # ... (restante do código)
```

### Passo 2: Ensinar o Agente a Usar a Nova Ferramenta

Agora, precisamos atualizar o "manual de instruções" do agente para que ele aprenda sobre a nova ferramenta.

**Arquivo a ser modificado:** `app/prompts/prompt-agente.md`

**Adicionar a seguinte definição dentro da seção `<crm_tools>`:**

```xml
      <tool name="crm.add_tags">
        <description>Adicionar uma ou mais tags a um lead no Kommo CRM</description>
        <usage>Usar para categorizar leads, marcar interesses ou registrar status importantes (ex: 'hot_lead', 'contato_futuro')</usage>
        <parameters>
          - tags: uma string com tags separadas por vírgula
        </parameters>
        <example>[TOOL: crm.add_tags | tags=hot_lead, precisa_financiamento]</example>
      </tool>
```

---

## 4. Benefícios e Próximos Passos

### Benefícios Imediatos

- **Maior Autonomia:** O agente poderá gerenciar o ciclo de vida do lead no CRM de forma mais completa, sem intervenção humana.
- **Melhor Organização:** O uso de tags permitirá uma segmentação muito mais rica e contextual dos leads.
- **Eficiência:** Ações que hoje seriam manuais (como adicionar uma tag "contato_futuro") poderão ser executadas instantaneamente pelo agente.

### Próximas Ferramentas Potenciais

Com base neste padrão, podemos facilmente adicionar outras ferramentas no futuro, como:
- `crm.add_note`: Para adicionar notas detalhadas ao histórico do lead.
- `crm.get_lead_info`: Para o agente consultar o estado atual de um lead antes de agir.
- `crm.create_task`: Para agendar tarefas para vendedores humanos no Kommo.

## 5. Conclusão

A arquitetura do projeto é robusta, modular e preparada para a evolução. A implementação das ferramentas de CRM solicitadas é um passo natural e de baixo risco que aumentará significativamente a capacidade do agente. Recomendo a execução do plano de implementação detalhado acima.
