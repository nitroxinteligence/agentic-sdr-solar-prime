# Plano de Correção Definitiva: Erro de Mapeamento de Estágio no Kommo

## Visão Geral

O sistema está falhando ao tentar atualizar o estágio de um lead para "reuniao_agendada" devido a uma falha no mapeamento de nomes de estágio. A causa raiz é uma inconsistência na normalização de caracteres especiais (acentos) entre a chamada da função e as chaves armazenadas no `stage_map`.

## Tarefas

1.  **[CONCLUÍDO] Análise da Causa Raiz:** O erro `Estágio 'reuniao_agendada' não encontrado no mapa` confirma que a normalização atual em `_fetch_pipeline_stages` (`crm_service_100_real.py`) é insuficiente. Ela não lida com variações de acentuação.

2.  **[EM ANDAMENTO] Tornar o Mapeamento Resiliente:** Refatorar a função `_fetch_pipeline_stages` para criar um mapa de estágios mais robusto. Para cada estágio, serão geradas e armazenadas múltiplas chaves:
    *   A original em minúsculas e com `_`.
    *   Uma versão totalmente normalizada (sem acentos).
    *   A versão em maiúsculas.
    *   Outras variações relevantes.

3.  **[PENDENTE] Implementar a Correção:** Aplicar a lógica de mapeamento aprimorada no arquivo `app/services/crm_service_100_real.py`.

4.  **[PENDENTE] Publicar a Correção:** Comitar e enviar a solução definitiva para o repositório.
