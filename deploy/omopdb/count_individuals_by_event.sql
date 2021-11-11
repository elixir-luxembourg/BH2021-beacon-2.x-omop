DROP FUNCTION IF EXISTS public.count_individuals_by_event;
/*
 Prerequisites: clinical_events view in public schema.
 Based on functions in https://github.com/EGA-archive/beacon-2.x/blob/master/deploy/db/schema.sql
 TODO: descendants
 TODO: age of onset at first occurrence (ordinal=1)
 */
CREATE FUNCTION public.count_individuals_by_event(
    _event_codes text [] default NULL, -- ARRAY['<ontology>:<code>', ... ]
    _min_age_of_onset integer default NULL,
    _max_age_of_onset integer default NULL,
    _include_descendants bool default NULL,  -- TODO
    _gender_code text default NULL,
    _min_value integer default NULL,
    _max_value integer default NULL,
    _unit_code text default NULL,
    _value_code text default NULL
    )
    RETURNS TABLE(_num_total_results bigint)
    LANGUAGE plpgsql
AS $$
-- If _include_descendants is missing, it is treated as FALSE
DECLARE
    _query text;
    _where_clause text;
BEGIN
    _query = 'SELECT COUNT(DISTINCT person_id)
    FROM public.clinical_events';

    -- #1=_event_codes, #2=_min_age_of_onset, #3=_max_age_of_onset
    -- #4=_include_descendants, #5=_gender_concept_id, #6=_min_value, #7=_max_value,
    -- #8=_unit_code, #9=_value_code
    _where_clause = '
    WHERE 1=1';

    IF _event_codes IS NOT NULL THEN
        _where_clause =  _where_clause || '
		AND  event_code = ANY($1)';
    END IF;

    IF _min_age_of_onset IS NOT NULL THEN
        _where_clause =  _where_clause || '
		AND age >= $2';
    END IF;

    IF _max_age_of_onset IS NOT NULL THEN
        _where_clause =  _where_clause || '
		AND age <= $3';
    END IF;

    -- TODO
--     IF _include_descendants IS NULL OR NOT _include_descendants THEN
--         _where_clause =  _where_clause || '
-- 		AND min_levels_of_separation = 0'; -- only match on given code
--     END IF;

    IF _gender_code IS NOT NULL THEN
        _where_clause = _where_clause || 'AND gender_code = $5';
    END IF;

    IF _min_value IS NOT NULL THEN
        _where_clause = _where_clause || 'AND value_as_number >= $6';
    END IF;

    IF _max_value IS NOT NULL THEN
        _where_clause = _where_clause || 'AND value_as_number <= $7';
    END IF;

    IF _unit_code IS NOT NULL THEN
        _where_clause = _where_clause || 'AND unit_code = $8';
    END IF;

    IF _value_code IS NOT NULL THEN
        _where_clause = _where_clause || 'AND value_code = $9';
    END IF;

    _query = _query || _where_clause;

    RAISE NOTICE '_query: %', _query;

    RETURN QUERY EXECUTE _query
        USING _event_codes, _min_age_of_onset, _max_age_of_onset, _include_descendants,
        _gender_code, _min_value, _max_value, _unit_code, _value_code;
END
$$;
