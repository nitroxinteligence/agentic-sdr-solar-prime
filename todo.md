# TODO - Correção de Tipo de Dado em qualification_score

## Tarefa 1: Análise e Diagnóstico

- [x] **Analisar `logs-console.md`**: Identificar o erro `invalid input syntax for type integer: "30.0"`.
- [x] **Diagnosticar Causa Raiz**: Concluir que a função `calculate_qualification_score` em `lead_manager.py` retorna um `float`, enquanto a coluna `qualification_score` na tabela `leads` espera um `integer`.

## Tarefa 2: Implementar a Correção

- [x] **Modificar `app/core/lead_manager.py`**:
    - [x] Alterar a função `calculate_qualification_score` para que ela retorne um `int` em vez de um `float`. A conversão pode ser feita de forma segura envolvendo o cálculo final com `int()`.

## Tarefa 3: Publicar Correção

- [ ] **Executar `git add .`**: Adicionar o arquivo modificado.
- [ ] **Executar `git commit`**: Criar um commit com uma mensagem clara sobre a correção do tipo de dado.
- [ ] **Executar `git push`**: Enviar a correção para o repositório remoto.
