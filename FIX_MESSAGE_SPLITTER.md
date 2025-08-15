# CORREÇÃO URGENTE: Message Splitter

## Problema Identificado
As 4 opções de soluções energéticas estão sendo enviadas em uma linha contínua no WhatsApp, sem quebras de linha entre as opções, dificultando a leitura.

## Causa Raiz
O Message Splitter só é ativado quando a mensagem tem MAIS de 200 caracteres (configurável via `MESSAGE_MAX_LENGTH`).
Porém, no arquivo `.env`, este valor estava configurado como 4000, fazendo com que a maioria das mensagens NÃO passasse pelo splitter.

## Solução Aplicada

### 1. Ajustar configuração no `.env`
```bash
# ANTES (incorreto):
MESSAGE_MAX_LENGTH=4000  # Limite muito alto, splitter não ativa

# DEPOIS (correto):
MESSAGE_MAX_LENGTH=200  # Limite padrão para ativar o splitter
```

### 2. Como o Message Splitter funciona
- Quando uma mensagem tem MAIS de 200 caracteres, o splitter é ativado
- O splitter detecta automaticamente a mensagem das 4 opções
- Aplica formatação especial com quebras de linha entre as opções
- Retorna a mensagem formatada corretamente

### 3. Código relevante
- `app/services/message_splitter.py`: 
  - Linhas 350-422: Detecção e formatação das 4 opções
  - Método `_is_four_solutions_message()`: Detecta a mensagem
  - Método `_format_four_solutions_message()`: Aplica quebras de linha

- `app/api/webhooks.py`:
  - Linha 1269: Condição que ativa o splitter baseada em `MESSAGE_MAX_LENGTH`

## Ação Necessária
⚠️ **IMPORTANTE**: Alterar no arquivo `.env`:
```bash
MESSAGE_MAX_LENGTH=200
```

## Resultado Esperado
As 4 opções serão apresentadas assim no WhatsApp:
```
Perfeito, [Nome]! Hoje na Solarprime nós temos quatro modelos de soluções energéticas:

1) Instalação de usina própria - você fica dono da usina ao final
2) Aluguel de lote para instalação de usina própria - sua usina em nosso terreno
3) Compra de energia com desconto - economia imediata de 20%
4) Usina de investimento - renda passiva com energia solar

Qual desses modelos seria do seu interesse?
```

## Status
✅ Código do Message Splitter está correto e funcional
✅ Prompt do agente configurado para usar quebras de linha
⚠️ **PENDENTE**: Ajustar `MESSAGE_MAX_LENGTH=200` no `.env` em produção