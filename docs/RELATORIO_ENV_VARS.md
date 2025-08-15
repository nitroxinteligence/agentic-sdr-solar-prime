# Análise e Otimização do Arquivo de Configuração (.env)

## 1. Visão Geral

Após uma análise detalhada do arquivo `.env` e do seu uso real em todo o código da aplicação (`@app/**`), identificamos uma oportunidade significativa de simplificação. Muitas variáveis são legadas de uma arquitetura anterior (possivelmente o framework AGnO), se referem a funcionalidades não implementadas (como relatórios), ou são redundantes.

A limpeza deste arquivo é essencial para reduzir a complexidade, eliminar a confusão e garantir que a configuração reflita o estado atual e funcional do sistema.

## 2. Análise Detalhada das Variáveis

### 2.1. Variáveis Essenciais (MANTER)

Estas variáveis são **cruciais** para o funcionamento do agente e suas integrações principais. Elas são ativamente lidas e utilizadas pelo código em `app/config.py` e pelos respectivos serviços.

| Variável | Justificativa de Uso |
| :--- | :--- |
| `ENVIRONMENT`, `DEBUG` | Controlam o modo de execução e o nível de log. |
| `API_HOST`, `API_PORT`, `UVICORN_WORKERS` | Essenciais para a execução do servidor FastAPI. |
| `USE_STATELESS_MODE` | Controla a arquitetura do agente (Singleton vs. Stateless) em `app/api/webhooks.py`. |
| `OPENAI_API_KEY`, `GOOGLE_API_KEY` | Chaves para os modelos de linguagem primário e de fallback em `app/core/model_manager.py`. |
| `EVOLUTION_API_URL`, `EVOLUTION_API_KEY`, `EVOLUTION_INSTANCE_NAME` | Essenciais para a integração com o WhatsApp via `app/integrations/evolution.py`. |
| `SUPABASE_URL`, `SUPABASE_SERVICE_KEY` | Essenciais para a conexão com o banco de dados via `app/integrations/supabase_client.py`. |
| `REDIS_URL`, `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD`, `REDIS_USERNAME` | Essenciais para o cache e a gestão de locks/filas via `app/integrations/redis_client.py`. |
| `GOOGLE_AUTH_METHOD` | Define o método de autenticação do Google (OAuth ou Service Account). |
| `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, `GOOGLE_OAUTH_REDIRECT_URI`, `GOOGLE_OAUTH_REFRESH_TOKEN` | Essenciais para o fluxo de autenticação do Google Calendar via OAuth 2.0. |
| `GOOGLE_CALENDAR_ID` | ID do calendário a ser utilizado. |
| `KOMMO_BASE_URL`, `KOMMO_LONG_LIVED_TOKEN`, `KOMMO_PIPELINE_ID`, `KOMMO_HUMAN_HANDOFF_STAGE_ID`, `KOMMO_NOT_INTERESTED_STAGE_ID`, `KOMMO_MEETING_SCHEDULED_STAGE_ID`, `KOMMO_AGENT_USER_ID` | Essenciais para a integração com o CRM Kommo e para a lógica de transbordo. |
| `WEBHOOK_BASE_URL` | Utilizada para configurar o webhook da Evolution API. |
| `TIMEZONE`, `BUSINESS_HOURS_START`, `BUSINESS_HOURS_END` | Utilizadas em `app/utils/time_utils.py` para lógicas de horário comercial. |
| `ENABLE_*` (Toggles de Features) | Todas as variáveis `ENABLE_...` são usadas em `app/config.py` para controlar dinamicamente a inicialização e o comportamento de diferentes módulos e serviços. São essenciais para a modularidade do sistema. |
| `TYPING_DURATION_*`, `RESPONSE_DELAY_*`, etc. | Todas as variáveis de timing e humanização são utilizadas para controlar o comportamento do agente, tornando-o mais natural. |

### 2.2. Variáveis Desnecessárias (REMOVER)

Estas variáveis não são utilizadas em nenhum lugar no código da aplicação, são de frameworks antigos ou se referem a funcionalidades inexistentes.

| Variável | Justificativa para Remoção |
| :--- | :--- |
| `AGENTIC_SDR_MODE`, `CONTEXT_ANALYSIS_ENABLED`, `REASONING_ENABLED`, `MULTIMODAL_ENABLED`, `KNOWLEDGE_SEARCH_ENABLED`, `MEMORY_ENABLED` | **Legado do AGnO.** Nenhuma dessas variáveis é referenciada no código atual. As funcionalidades são controladas pelos toggles `ENABLE_*`. |
| `CONTEXT_ANALYSIS_BATCH_SIZE`, `REASONING_TIMEOUT_SECONDS`, `MULTIMODAL_MAX_FILE_SIZE`, `MEMORY_RETENTION_DAYS` | **Legado do AGnO.** Configurações de performance de um framework não mais utilizado. |
| `SUPABASE_ANON_KEY`, `SUPABASE_DB_URL` | **Redundante/Inutilizado.** O cliente Supabase usa apenas a `SERVICE_KEY` para autenticação no backend. A `ANON_KEY` é para o frontend. A `DB_URL` não é usada, pois a conexão é feita via API. |
| `GOOGLE_USE_SERVICE_ACCOUNT`, `GOOGLE_SERVICE_ACCOUNT_EMAIL`, `GOOGLE_PRIVATE_KEY`, `GOOGLE_PROJECT_ID`, `GOOGLE_PRIVATE_KEY_ID`, `GOOGLE_CLIENT_ID` | **Legado.** O sistema foi migrado para o fluxo **OAuth 2.0** (`google_oauth_handler.py`), que é mais robusto e seguro. Manter essas chaves de Service Account é um risco de segurança e causa confusão. |
| `GOOGLE_WORKSPACE_USER_EMAIL` | **Legado.** Relacionado ao antigo método de delegação de domínio do Service Account. O fluxo OAuth atual não necessita desta variável. |
| `KOMMO_CLIENT_ID`, `KOMMO_CLIENT_SECRET`, `KOMMO_SUBDOMAIN`, `KOMMO_REDIRECT_URI`, `KOMMO_ACCESS_TOKEN` | **Legado.** Estas variáveis são para um fluxo de autenticação OAuth com o Kommo. O sistema atual utiliza um `KOMMO_LONG_LIVED_TOKEN`, que simplifica a autenticação. |
| `API_BASE_URL` | **Redundante.** A variável `WEBHOOK_BASE_URL` já cumpre a função de definir a URL base da aplicação para os webhooks. |
| `AGENTE_RESPONSE_DELAY_SECONDS` | **Legado.** Substituída por um conjunto mais granular de variáveis de timing (`RESPONSE_DELAY_MIN`, `RESPONSE_DELAY_MAX`, etc.). |
| `REPORT_DAY_OF_WEEK`, `REPORT_TIME`, `WHATSAPP_GROUP_ID` | **Funcionalidade Inexistente.** Não há no código atual nenhuma lógica para geração ou envio de relatórios. |
| `AGNO_*` (todas as variáveis) | **Legado do AGnO.** Nenhuma destas configurações de modelo é utilizada pelo `ModelManager` atual. |

## 3. Plano de Ação Recomendado

1.  **Backup:** Faça uma cópia do arquivo `.env` atual para `.env.backup` como medida de segurança.
2.  **Limpeza:** Crie um novo arquivo `.env` contendo **apenas** as variáveis listadas na seção **2.1. Variáveis Essenciais (MANTER)**.
3.  **Remoção de Código Morto:** Após a limpeza do `.env`, podemos, em uma próxima etapa, remover as referências a essas variáveis do código em `app/config.py` para uma limpeza completa.

## 4. Benefícios

- **Redução da Complexidade:** Um arquivo `.env` limpo e conciso torna a configuração do ambiente muito mais clara e menos propensa a erros.
- **Segurança Aprimorada:** Remove chaves e segredos não utilizados (como as credenciais de Service Account do Google e as de OAuth do Kommo), diminuindo a superfície de ataque.
- **Clareza Operacional:** Fica evidente quais serviços e funcionalidades estão de fato ativos e configurados no sistema.