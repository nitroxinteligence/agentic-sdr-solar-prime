# Plano de Ação: Sincronização Inteligente de Tags e Campos

*Objetivo: Implementar uma lógica robusta e em tempo real para que o agente atualize tags e campos customizados no Kommo CRM com base no contexto da conversa, garantindo 100% de precisão.*

---

### Fase 1: Análise e Mapeamento

- [x] **1.1. Mapear Campos e Tags:**
  - [x] Analisar o `crm_service_100_real.py` para confirmar como os campos customizados (`WHATSAPP`, `VALOR CONTA DE ENERGIA`, `SOLUÇAO SOLAR`) e as tags são atualmente manipulados.
  - [x] Validar que os nomes dos campos e os valores do select `SOLUÇAO SOLAR` correspondem exatamente ao que a API do Kommo espera. Vou garantir que acentos e variações sejam tratados corretamente.

- [x] **1.2. Identificar Pontos de Extração de Dados:**
  - [x] Revisar `lead_manager.py` e `multimodal_processor.py` para entender como o "VALOR CONTA DE ENERGIA" é extraído de texto e de mídias (PDF/imagem).
  - [x] Revisar `context_analyzer.py` para ver como a intenção "SOLUÇAO SOLAR" é identificada.

---

### Fase 2: Implementação do Sincronizador

- [x] **2.1. Criar um "Módulo de Sincronização" (`CRMDataSync`):**
  - [x] Proponho criar uma nova classe, talvez em `app/services/crm_sync_service.py`, para centralizar toda a lógica de decisão sobre quais campos e tags atualizar. Isso evita espalhar a lógica por vários arquivos.
  - [x] Este módulo receberá o `lead_info` e o histórico da conversa e retornará um payload de atualização para o Kommo.

- [x] **2.2. Implementar a Lógica de Decisão:**
  - [x] **`SOLUÇAO SOLAR` e Tags Associadas:** Implementar a lógica que, baseada na escolha inicial do usuário (Opção 1, 2, 3 ou 4), define o campo `SOLUÇAO SOLAR` e adiciona a tag correspondente (ex: `Usina Investimento`).
  - [x] **`VALOR CONTA DE ENERGIA`:** Garantir que, sempre que este valor for extraído (de texto ou mídia), ele seja preparado para atualização.
  - [x] **`sem-resposta`:** Implementar a regra que aplica esta tag e move o lead para o estágio "NÃO INTERESSADO" quando o contexto indicar.
  - [x] **Atualização Contínua:** A lógica permitirá que, se o usuário mudar de ideia, os campos e tags sejam sobrescritos com a informação mais recente, garantindo que o CRM esteja sempre atualizado.

- [x] **2.3. Integrar o Sincronizador ao Fluxo Principal:**
  - [x] Em `agentic_sdr_stateless.py`, no final do método `process_message`, vou adicionar uma chamada ao novo `CRMDataSync`.
  - [x] Após cada interação do usuário, o agente analisará o estado da conversa e, se houver mudanças, chamará o `crm_service` para aplicar as atualizações de campos e tags imediatamente. Esta abordagem em tempo real é mais simples e confiável que um worker de 30 minutos.

---

### Fase 3: Validação e Testes

- [x] **3.1. Criar Testes de Unidade:**
  - [x] Escrever testes para o `CRMDataSync` que simulem diferentes cenários de conversa e verifiquem se o payload de atualização correto é gerado.
- [ ] **3.2. Adicionar Logs para Validação:**
  - [ ] Adicionar logs detalhados que mostrem: "Decidido atualizar campo X com valor Y" e "Decidido adicionar tag Z". Isso permitirá a validação em tempo real.