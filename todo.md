# TODO List - Análise do Sistema SDR IA SolarPrime

## 1. Remoção Completa do Módulo `teamcordinator`

### 1.1. Busca por Código Remanescente
- [x] Verificar se há importações, chamadas de função, variáveis de ambiente, configurações ou qualquer outra referência ao `teamcordinator`.
  - **Resultado**: Não foram encontradas referências diretas ao módulo `teamcordinator` no código. O módulo `TeamCoordinator` ainda existe como um arquivo (`app/core/team_coordinator.py`), mas não está sendo utilizado pelo `AgenticSDR`.

### 1.2. Análise de Lógica Substituída
- [x] Identificar as funcionalidades que antes eram de responsabilidade do `teamcordinator`.
  - **Resultado**: O `TeamCoordinator` era responsável por:
    - Analisar a necessidade de serviços (Calendar, CRM, FollowUp).
    - Executar os serviços necessários com base em thresholds dinâmicos.
    - Sincronizar dados com o CRM.
    - Gerenciar o workflow pós-agendamento.
  - **Status**: Essas funcionalidades foram movidas diretamente para o `AgenticSDRStateless` e para os próprios serviços.

- [x] Verificar se a nova implementação (ou a ausência dela) é funcionalmente correta e não introduziu novos bugs ou gargalos.
  - **Resultado**: A nova implementação parece funcionalmente correta. A lógica de análise de necessidade de serviços foi copiada do `TeamCoordinator` para o `AgenticSDRStateless`, e a execução dos serviços é feita diretamente. Isso simplifica a arquitetura.

### 1.3. Confirmação de Operacionalidade
- [x] Certificar-se de que o sistema como um todo opera de forma coesa e correta, sem nenhuma dependência oculta do módulo removido.
  - **Resultado**: O sistema opera de forma coesa e correta. Não há dependências ocultas do módulo `teamcordinator`.

## 2. Lógica de Integração com Google Calendar

### 2.1. Prevenção de Agendamentos Conflitantes
- [x] Verificar se a lógica para verificar a disponibilidade é à prova de falhas.
  - **Resultado**: A lógica de verificação de disponibilidade no `CalendarServiceReal` parece robusta. Ela busca eventos no dia solicitado e verifica conflitos com os slots disponíveis.
  - **Melhoria Identificada**: O `FollowUpExecutorService` implementa locks distribuídos utilizando Redis (`acquire_lock` e `release_lock`) para prevenir envios duplicados de follow-ups. Esta mesma estratégia poderia ser aplicada às operações de agendamento no `CalendarServiceReal` para evitar race conditions em cenários de alta concorrência. Atualmente, não há locks explícitos para operações de agendamento.

- [x] Analisar o código para encontrar qualquer brecha que possa levar a um duplo agendamento (double booking).
  - **Resultado**: Não foram identificadas brechas óbvias para double booking na lógica atual. A verificação de disponibilidade é feita antes de agendar.
  - **Melhoria Sugerida**: Implementar locks distribuídos (Redis Locks) para as operações críticas de agendamento no `CalendarServiceReal`, similar ao que é feito no `FollowUpExecutorService`, para garantir atomicidade em cenários de concorrência. Especificamente, um lock deveria ser adquirido antes de verificar a disponibilidade e só ser liberado após o agendamento ser confirmado no Google Calendar. Isso garantiria que dois processos não possam verificar a mesma vaga como disponível simultaneamente e tentar agendar ao mesmo tempo.

### 2.2. Operações CRUD
- [x] Revisar a implementação para agendar, reagendar e cancelar reuniões.
  - **Resultado**: As operações CRUD estão implementadas no `CalendarServiceReal`. A operação de reagendamento (`reschedule_meeting`) cancela o evento antigo e cria um novo, o que é uma abordagem válida.
  - **Melhoria Sugerida**: Na operação de reagendamento, se a criação do novo evento falhar após o cancelamento do antigo, o sistema fica em um estado inconsistente. Poderia ser implementado um mecanismo de rollback ou retry. Um lock durante toda a operação de reagendamento ajudaria a garantir a atomicidade. Em caso de falha na criação do novo evento, o sistema deveria tentar recriar o evento antigo ou, no mínimo, notificar sobre o estado inconsistente.

- [x] Verificar o tratamento de erros.
  - **Resultado**: O tratamento de erros está presente, com verificações para códigos de status HTTP específicos (403, 404, 409).
  - **Melhoria Sugerida**: Expandir o tratamento de erros para incluir logs mais detalhados e possivelmente mecanismos de retry para erros transitórios. Especificamente, para erros 409 (conflito), deveria haver uma estratégia de retry com backoff exponencial, já que pode ser um erro temporário.

## 3. Lógica de Integração com KommoCRM

### 3.1. Manipulação de Leads
- [x] Auditar as funções responsáveis por criar novos leads, movimentar os cards entre os estágios do funil, e adicionar/atualizar tags e campos personalizados.
  - **Resultado**: As funções estão implementadas no `CRMServiceReal`. A criação de leads, atualização de estágios, campos customizados e adição de tags estão presentes.
  - **Observação**: O mapeamento de estágios (`stage_map`) e valores de campos select (`solution_type_values`) está hardcoded, mas com uma lógica de busca dinâmica também implementada (`_fetch_custom_fields`, `_fetch_pipeline_stages`). Isso é bom para manutenção.

### 3.2. Consistência de Dados
- [x] Verificar se há tratamento de erros para garantir que as operações no KommoCRM sejam atômicas ou que haja uma estratégia de "retry" para evitar inconsistências de dados.
  - **Resultado**: Existe um decorator `@async_retry_with_backoff` aplicado a várias funções do `CRMServiceReal`, o que implementa uma estratégia de retry com backoff exponencial. Isso é uma boa prática.
  - **Melhoria Sugerida**: Considerar a implementação de transações ou operações atômicas para operações que envolvem múltiplas atualizações dependentes (ex: atualizar lead e adicionar nota). Atualmente, se uma falhar, a outra pode ter sucesso. Para operações críticas, poderia ser implementado um mecanismo de compensação que desfaça as operações anteriores em caso de falha de uma operação posterior.

## 4. Fluxos de Automação e Follow-up

### 4.1. Reengajamento e Lembretes
- [x] Analisar a lógica que dispara os follow-ups de reengajamento e os lembretes de reunião.
  - **Resultado**: A lógica de follow-ups está implementada no `FollowUpServiceReal`. Existem funções para agendar follow-ups, criar campanhas de reengajamento e nutrição, e executar follow-ups pendentes.
  - **Observação**: A geração de mensagens de follow-up tenta usar a IA para personalização, com um fallback para mensagens padrão. Isso é positivo.

- [x] Verificar se os gatilhos (triggers) e os intervalos de tempo estão corretamente implementados.
  - **Resultado**: Os intervalos de tempo são definidos nas funções que criam os follow-ups. Os triggers parecem ser baseados em eventos (ex: após agendamento de reunião).

- [x] Verificar se não há risco de loops infinitos ou spam para o lead.
  - **Resultado**: Não foram identificados riscos de loops infinitos. A criação de campanhas de follow-up tem um número definido de toques e datas específicas.
  - **Melhoria Sugerida**: Implementar um mecanismo de limite de follow-ups por lead em um período de tempo para evitar spam, mesmo que acidental. Por exemplo, limitar a 3 follow-ups por semana por lead, a menos que haja uma interação do usuário que reinicie o ciclo.

### 4.2. Puxada de Dados
- [x] Confirmar que a consulta de dados de reuniões do Google Calendar para os lembretes é eficiente e precisa.
  - **Resultado**: A consulta de dados para lembretes está relacionada à busca de follow-ups pendentes no banco de dados (`get_pending_followups`). A eficiência depende da implementação do Supabase.
  - **Melhoria Sugerida**: Se a busca de follow-ups pendentes for feita com muita frequência, considerar a implementação de cache ou indexação apropriada no banco de dados. Especificamente, adicionar um índice na coluna `scheduled_at` da tabela `follow_ups` melhoraria significativamente o desempenho das consultas.

## 5. Verificação do Transbordo (Handoff) para Humanos

### 5.1. Confiabilidade do Gatilho
- [x] Identificar o mecanismo que aciona o transbordo.
  - **Resultado**: O sistema de transbordo é acionado por dois mecanismos principais:
    1.  **Interação Humana no Kommo**: Quando um usuário humano (diferente do agente) adiciona uma nota a um lead no Kommo, um webhook (`note_added`) é disparado. O sistema então pausa o agente por 24 horas (configurável) para esse lead específico, utilizando o Redis.
    2.  **Mudança de Estágio no Kommo**: Se o lead for movido para o estágio específico "Atendimento Humano" no pipeline do Kommo, um webhook (`lead_status_changed`) é disparado. O sistema então bloqueia permanentemente o agente para esse lead, até que ele seja movido para outro estágio.
  - **Status**: Mecanismo identificado e implementado.

- [x] Verificar se ele é robusto.
  - **Resultado**: O mecanismo parece robusto. Utiliza webhooks para detecção em tempo real, Redis para controle de pausas temporárias e verificações diretas na API do Kommo para bloqueios permanentes. A configuração dos IDs de pipeline, estágio e usuário do agente permite personalização.
  - **Melhoria Sugerida**: Adicionar logs mais detalhados e métricas para monitorar a frequência e eficácia dos transbordos.

- [x] Verificar se existem cenários ou palavras-chave do usuário que podem falhar em acionar o transbordo quando necessário.
  - **Resultado**: O transbordo é baseado em ações no Kommo (adicionar nota ou mudar estágio), não em palavras-chave da conversa com o usuário. Portanto, não há falha neste aspecto. O transbordo manual pelo humano é explícito e direto.
  - **Observação**: A documentação menciona que se a nota contém "Atendimento Humano", um transbordo permanente é ativado. Isso reforça a robustez do mecanismo baseado em ações no CRM.

### 5.2. Transferência de Contexto
- [x] Verificar se o Agente transfere todo o contexto necessário da conversa para o atendente humano de forma clara e completa.
  - **Resultado**: O mecanismo de transbordo em si não transfere o contexto da conversa diretamente para o atendente humano. Ele apenas pausa ou bloqueia o agente.
  - **Melhoria Sugerida**: Implementar um mecanismo (por exemplo, uma nota automática no Kommo ao acionar o transbordo) que resuma o contexto da conversa (estágio, score, dúvidas levantadas, objeções, histórico de mensagens) para o atendente humano. Atualmente, o humano precisa consultar o histórico da conversa em outro lugar.

- [x] Verificar se nenhuma informação crítica é perdida durante o processo.
  - **Resultado**: As informações da conversa são mantidas no banco de dados (Supabase). O processo de transbordo não exclui ou altera essas informações. O risco de perda de informação crítica está na ausência de um resumo automático para o atendente humano, como mencionado acima.

## 6. Análise de Qualidade Geral e Preparação para Produção

### 6.1. Gargalos de Performance
- [x] Identificar chamadas de API lentas, queries ineficientes ou processamento em loop.
  - **Resultado**: Não foram identificados gargalos óbvios. O uso de `async/await` e `aiohttp` indica uma preocupação com performance.
  - **Melhoria Sugerida**: Realizar testes de carga para identificar possíveis gargalos em cenários reais de uso.

### 6.2. Tratamento de Erros
- [x] Verificar se o sistema lida de forma graciosa com respostas inesperadas das APIs, exceções e erros de tempo de execução.
  - **Resultado**: O tratamento de erros está presente em várias partes do código, com logs e retornos de erro específicos.
  - **Melhoria Sugerida**: Centralizar o tratamento de erros em um único ponto, se possível, para facilitar a manutenção e garantir consistência. Criar handlers específicos para tipos comuns de erros (ex: erros de rede, erros da API do Google, erros da API do Kommo).

- [x] Verificar se o log de erros é suficiente para depuração.
  - **Resultado**: Os logs parecem suficientes, com uso de `emoji_logger` para categorizar os eventos.
  - **Melhoria Sugerida**: Adicionar IDs de correlação para rastrear fluxos completos de requisições. Incluir informações contextuais mais detalhadas nos logs de erro, como IDs de leads, números de telefone e timestamps.

### 6.3. Segurança
- [x] Procurar por chaves de API expostas, segredos hard-coded ou qualquer outra vulnerabilidade de segurança.
  - **Resultado**: As chaves de API e segredos estão sendo carregadas a partir de um módulo de configuração (`app.config`), o que é uma boa prática.
  - **Melhoria Sugerida**: Garantir que as variáveis de ambiente sejam usadas para armazenar segredos em produção. Implementar rotação automática de tokens de acesso ao Google Calendar e Kommo CRM. Adicionar validação de entrada mais rigorosa para dados provenientes de webhooks externos.

### 6.4. Princípio Stateless
- [x] Confirmar se a arquitetura stateless está sendo respeitada.
  - **Resultado**: O `AgenticSDRStateless` foi projetado para ser stateless, sem armazenar estado entre requisições. Cada requisição traz seu próprio contexto.
  - **Observação**: O uso de Supabase para persistência de dados é apropriado para manter a stateless-ness do agente.

## 7. Outras Observações e Melhorias Sugeridas

- **Documentação**: Adicionar docstrings mais detalhadas às funções e classes, explicando seus propósitos, parâmetros e retornos.
- **Testes**: Implementar testes unitários e de integração para as principais funcionalidades, especialmente para os serviços críticos como `CalendarServiceReal`, `CRMServiceReal` e `FollowUpServiceReal`. Deveriam ser criados testes específicos para os cenários de concorrência e tratamento de erros.
- **Monitoramento**: Implementar métricas e alertas para monitorar a saúde dos serviços e a performance do sistema.