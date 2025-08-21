# TODO - Correção de Alucinação de Ferramenta (image_processing)

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o erro `Erro no tool image_processing: Formato inválido: image_processing`.
- [x] **Diagnosticar Causa Raiz**: Concluir que o modelo de linguagem está alucinando a existência de uma ferramenta `image_processing` due to the structure of the prompt, specifically the rule with `id="image_processing"`.

## Tarefa 2: Implementar a Correção no Prompt

- [x] **Modificar `app/prompts/prompt-agente.md`**:
    - [x] Renomear o ID da regra de `image_processing` para `media_processing_protocol` para evitar a semelhança com um nome de ferramenta.
    - [x] Adicionar uma instrução explícita e em destaque na seção de regras operacionais para instruir o modelo a **NUNCA** chamar uma ferramenta para processar mídias e a **SEMPRE** usar os dados já processados fornecidos na seção `=== ANÁLISE DE MÍDIA RECEBIDA ===` do contexto.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo de prompt modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção da alucinação da ferramenta.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
