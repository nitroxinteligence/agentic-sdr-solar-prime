# Diagnóstico e Solução para Falha no Sistema Multimodal

## 1. Visão Geral do Problema

O agente de IA (Helen Vieira) não está interpretando corretamente o conteúdo de documentos, especificamente arquivos PDF enviados pelos usuários. Conforme observado nos logs, um usuário enviou um boleto em PDF no valor de R$ 359,10, mas o agente respondeu com um valor alucinado de R$ 6.850,32.

Este comportamento indica uma falha crítica no pipeline de processamento multimodal, onde o conteúdo do documento não é extraído e disponibilizado para o raciocínio do agente.

## 2. Análise e Diagnóstico da Causa Raiz

Após uma análise profunda do código-fonte nos diretórios `app/core`, `app/api` e dos logs de console, a causa raiz foi identificada com alta confiança.

### Causa Principal: Ausência de OCR para PDFs

O problema central reside no arquivo `app/core/multimodal_processor.py`, na função `process_document`.

1.  **Método de Extração Limitado:** A função utiliza a biblioteca `PyPDF2` para extrair texto de documentos PDF. O método `page.extract_text()` desta biblioteca **só funciona para PDFs baseados em texto** (onde o texto pode ser selecionado e copiado).
2.  **Falha com PDFs de Imagem:** Contas de luz e boletos são frequentemente enviados como "PDFs de imagem" (ou seja, uma imagem escaneada salva dentro de um arquivo PDF). Nestes casos, `PyPDF2` não consegue ler o conteúdo visual e retorna uma string de texto vazia.
3.  **Contexto Incompleto para o Agente:** Como resultado, o `MultimodalProcessor` informa ao agente que um "Documento pdf recebido", mas não fornece nenhum conteúdo textual. O agente, portanto, não tem acesso ao valor real da conta (R$ 359,10).
4.  **Alucinação como Consequência:** Sem os dados essenciais do documento, o agente é forçado a "adivinhar" ou "alucinar" um valor com base no seu treinamento e no contexto da conversa, levando a erros graves como o observado.

### Análise de Componentes Adicionais

-   **Processamento de Imagens:** O sistema **já possui capacidade de OCR** para arquivos de imagem diretos (JPG, PNG) através da biblioteca `pytesseract` na função `process_image`. A falha é que essa capacidade não está sendo aproveitada para os PDFs.
-   **Processamento de Áudio:** A implementação para transcrição de áudio (`process_audio`) parece teoricamente correta, utilizando `speech_recognition`. A sua eficácia prática depende da qualidade do áudio e da disponibilidade da API do Google, mas a lógica no código está presente.
-   **Arquitetura Geral:** O fluxo de dados do webhook para o agente e deste para os processadores é modular e está bem estruturado. O problema não é um erro de arquitetura, mas uma limitação de funcionalidade em um módulo específico.

## 3. Plano de Ação e Solução Inteligente

Para resolver esta falha de forma definitiva e tornar o sistema robusto para todos os tipos de PDF, a seguinte estratégia de correção será implementada:

### Passo 1: Aprimorar o Processamento de Documentos com OCR

A função `process_document` em `app/core/multimodal_processor.py` será modificada para incluir um fluxo de OCR.

**Novo Fluxo Lógico:**

1.  **Tentativa de Extração Direta:** O sistema continuará a usar `PyPDF2` como o primeiro método, por ser rápido e eficiente para PDFs textuais.
2.  **Validação de Conteúdo:** Após a tentativa, o sistema verificará se o texto extraído é útil (ou seja, não é vazio ou insignificante).
3.  **Fallback Inteligente para OCR:** Se nenhum texto for extraído, o sistema automaticamente tratará o PDF como um documento de imagem.
    -   Ele utilizará a biblioteca `pdf2image` para converter cada página do PDF em um objeto de imagem em memória.
    -   Cada uma dessas imagens será então passada para a função de OCR `pytesseract.image_to_string`, que já é utilizada com sucesso no processamento de imagens.
4.  **Consolidação do Contexto:** O texto extraído via OCR de todas as páginas será combinado em uma única string.
5.  **Entrega ao Agente:** Este texto completo e preciso será enviado ao agente, fornecendo o contexto necessário para uma resposta correta e eliminando a causa da alucinação.

### Passo 2: Instalação de Dependências

Para implementar a solução, as seguintes dependências precisam ser adicionadas ao ambiente:

-   `python-pdf2image`: Biblioteca Python para converter PDFs em imagens.
-   `poppler-utils`: Dependência de sistema operacional para a biblioteca `pdf2image` funcionar corretamente.

### Passo 3: Validação e Testes

Após a implementação, o cenário exato do log (envio de um boleto em PDF) será replicado para garantir que o valor correto (R$ 359,10) seja extraído e utilizado pelo agente na sua resposta.

## 4. Conclusão

A falha de interpretação de documentos não é um erro de raciocínio do agente, mas sim uma falha na camada de percepção (processamento de mídia). Ao adicionar a capacidade de OCR para PDFs, garantimos que o agente receba os dados corretos para trabalhar, eliminando a causa raiz do problema e tornando o sistema multimodal verdadeiramente funcional e confiável.
