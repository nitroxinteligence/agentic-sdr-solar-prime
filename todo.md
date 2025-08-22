# Plano de Ação - Finalização da Capacidade Multimodal

## Tarefa 1: Generalizar a Estrutura de Dados de Mídia

- [x] **Refatorar `agentic_sdr_stateless.py`:** Modificado o método `process_message` para parar de usar a estrutura hardcoded `{"type": "image_url", ...}`. Em vez disso, ele agora cria uma estrutura genérica, `{"type": "media", "media_data": {...}}`, que contém o `mime_type` e o conteúdo base64, independentemente do tipo de arquivo.

## Tarefa 2: Adaptar o Model Manager para a Estrutura Genérica

- [x] **Refatorar `model_manager.py`:** Atualizado o método `Gemini.achat` para que ele reconheça a nova estrutura genérica `{"type": "media", ...}`. A lógica interna extrai o `mime_type` e o conteúdo para criar o `Blob` para a API do Gemini, tornando o `ModelManager` agnóstico ao tipo de mídia.

## Tarefa 3: Validação e Conclusão

- [x] O fluxo de ponta a ponta foi revisado e agora suporta corretamente áudios, PDFs e imagens.
- [x] O `todo.md` foi atualizado para marcar a tarefa como 100% concluída.