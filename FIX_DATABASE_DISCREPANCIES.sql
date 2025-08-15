-- ============================================
-- CORREÇÃO DE DISCREPÂNCIAS SCHEMA-CÓDIGO
-- Data: 15/08/2025
-- Resolve problemas encontrados na análise de conformidade
-- ============================================

-- IMPORTANTE: Execute após SUPABASE_SCHEMA_OPTIMIZATION_V3_FIXED.sql

BEGIN;

-- ============================================
-- CORREÇÃO 1: Remover referências a agent_sessions
-- (Tabela já foi removida, este é apenas para garantir)
-- ============================================

-- A tabela agent_sessions já foi removida no script de otimização
-- Nenhuma ação SQL necessária, mas o código Python precisa ser atualizado

-- ============================================
-- CORREÇÃO 2: Campo meeting_scheduled_at
-- O campo foi movido para leads_qualifications
-- ============================================

-- Campo já existe em leads_qualifications, não precisa criar
-- Verificar se existe para garantir
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_name = 'leads_qualifications' 
        AND column_name = 'meeting_scheduled_at'
    ) THEN
        ALTER TABLE leads_qualifications 
        ADD COLUMN meeting_scheduled_at TIMESTAMP WITH TIME ZONE;
    END IF;
END $$;

-- ============================================
-- CORREÇÃO 3: Campos extraídos pelo LeadManager
-- Adicionar campos faltantes como JSONB em preferences
-- ============================================

-- O campo preferences já existe como JSONB em leads
-- Pode armazenar: location, property_type, has_bill_image, interests, objections

-- Criar função helper para atualizar preferences
CREATE OR REPLACE FUNCTION update_lead_preferences(
    p_lead_id UUID,
    p_location TEXT DEFAULT NULL,
    p_property_type TEXT DEFAULT NULL,
    p_has_bill_image BOOLEAN DEFAULT NULL,
    p_interests TEXT[] DEFAULT NULL,
    p_objections TEXT[] DEFAULT NULL
) RETURNS VOID AS $$
BEGIN
    UPDATE leads
    SET preferences = preferences || 
        jsonb_strip_nulls(jsonb_build_object(
            'location', p_location,
            'property_type', p_property_type,
            'has_bill_image', p_has_bill_image,
            'interests', p_interests,
            'objections', p_objections
        )),
        updated_at = NOW()
    WHERE id = p_lead_id;
END;
$$ LANGUAGE plpgsql;

-- ============================================
-- CORREÇÃO 4: Garantir colunas removidas não causem erro
-- (channel e sentiment foram removidas de conversations)
-- ============================================

-- Estas colunas já foram removidas no script de otimização
-- O código usa IF EXISTS então não causará erro

-- ============================================
-- CORREÇÃO 5: Criar view para compatibilidade
-- View que simula campos antigos para backward compatibility
-- ============================================

-- View para leads com campos de qualificação (compatibilidade)
CREATE OR REPLACE VIEW leads_with_qualification AS
SELECT 
    l.*,
    lq.meeting_scheduled_at,
    lq.google_event_id,
    lq.meeting_link,
    lq.meeting_status,
    lq.is_decision_maker,
    lq.has_solar_system,
    lq.wants_new_solar_system,
    lq.has_active_contract
FROM leads l
LEFT JOIN LATERAL (
    SELECT * FROM leads_qualifications 
    WHERE lead_id = l.id 
    ORDER BY created_at DESC 
    LIMIT 1
) lq ON true;

-- ============================================
-- VALIDAÇÃO
-- ============================================

-- Verificar estrutura final
DO $$
DECLARE
    v_count INTEGER;
BEGIN
    -- Verificar se agent_sessions não existe
    SELECT COUNT(*) INTO v_count
    FROM information_schema.tables
    WHERE table_name = 'agent_sessions';
    
    IF v_count = 0 THEN
        RAISE NOTICE '✅ Tabela agent_sessions removida corretamente';
    ELSE
        RAISE WARNING '⚠️ Tabela agent_sessions ainda existe!';
    END IF;
    
    -- Verificar se meeting_scheduled_at existe em leads_qualifications
    SELECT COUNT(*) INTO v_count
    FROM information_schema.columns
    WHERE table_name = 'leads_qualifications'
    AND column_name = 'meeting_scheduled_at';
    
    IF v_count > 0 THEN
        RAISE NOTICE '✅ Campo meeting_scheduled_at existe em leads_qualifications';
    ELSE
        RAISE WARNING '⚠️ Campo meeting_scheduled_at não existe em leads_qualifications!';
    END IF;
    
    -- Verificar se preferences existe em leads
    SELECT COUNT(*) INTO v_count
    FROM information_schema.columns
    WHERE table_name = 'leads'
    AND column_name = 'preferences'
    AND data_type = 'jsonb';
    
    IF v_count > 0 THEN
        RAISE NOTICE '✅ Campo preferences (JSONB) existe em leads para dados adicionais';
    ELSE
        RAISE WARNING '⚠️ Campo preferences não existe em leads!';
    END IF;
    
    RAISE NOTICE '';
    RAISE NOTICE '📊 Correções aplicadas com sucesso!';
    RAISE NOTICE '⚠️ IMPORTANTE: Atualize o código Python para:';
    RAISE NOTICE '   1. Remover métodos agent_sessions de supabase_client.py';
    RAISE NOTICE '   2. Usar leads_qualifications.meeting_scheduled_at';
    RAISE NOTICE '   3. Mapear phone→phone_number e stage→current_stage no LeadManager';
    RAISE NOTICE '   4. Armazenar dados extras em preferences JSONB';
END $$;

COMMIT;

-- ============================================
-- CÓDIGO PYTHON - CORREÇÕES NECESSÁRIAS
-- ============================================

/*
ARQUIVO: app/integrations/supabase_client.py
- Remover linhas 463-518 (métodos agent_sessions)
- Linha 437: Mudar query para usar leads_qualifications.meeting_scheduled_at

ARQUIVO: app/core/lead_manager.py
- Mudar "phone" para "phone_number"
- Mudar "stage" para "current_stage"
- Armazenar location, property_type, etc em preferences:
  lead_info["preferences"] = {
      "location": location,
      "property_type": property_type,
      "has_bill_image": has_bill_image,
      "interests": interests,
      "objections": objections
  }

ARQUIVO: app/services/followup_executor_service.py
- Remover fallbacks legacy (linha 409 e 405)
- Usar sempre phone_number e scheduled_at
*/