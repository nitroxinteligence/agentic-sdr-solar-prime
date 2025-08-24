# Plano de Ação para Correção de Tag de Transbordo

**Diagnóstico:** O agente está movendo corretamente os leads interessados em "Usina de Investimento" para o estágio de "Atendimento Humano", mas está aplicando a tag errada ("Instalação Usina Própria") no Kommo CRM. A causa raiz foi identificada na lógica de extração de `chosen_flow` no `LeadManager`, que não priorizava corretamente a detecção do fluxo de investimento.

## Fase 1: Correção da Lógica de Extração

- [x] **Tarefa 1.1: Refatorar a Extração de Fluxo no `LeadManager`**
    - **Arquivo:** `app/core/lead_manager.py`
    - **Ação:** O método `_extract_chosen_flow` foi completamente reescrito. A lógica anterior, baseada em um dicionário simples e ordenação por comprimento de chave, foi substituída por uma busca priorizada e explícita.
    - **Melhoria:** A nova implementação verifica palavras-chave específicas para cada fluxo em uma ordem de prioridade (começando por "Usina Investimento"), garantindo que o fluxo correto seja identificado mesmo que o usuário mencione múltiplos termos. Isso resolve a ambiguidade e garante que a tag correta seja aplicada pelo `crm_sync_service`.

## Fase 2: Validação

- [ ] **Tarefa 2.1: Teste de Cenário de Transbordo**
    - **Ação:** Realizar um teste de conversação onde o usuário expressa interesse em "Usina de Investimento".
    - **Verificação:** Confirmar no Kommo CRM que o lead foi movido para "Atendimento Humano" E que a tag aplicada é exatamente "Usina Investimento".

**Conclusão Esperada:** A refatoração da lógica de extração de fluxo garantirá que o `lead_info` contenha o `chosen_flow` correto, o que, por sua vez, fará com que o `crm_sync_service` aplique a tag correta durante o processo de transbordo.
