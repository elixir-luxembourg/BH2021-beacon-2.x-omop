DROP FUNCTION IF EXISTS public.count_individuals;

CREATE FUNCTION public.count_individuals(
    _disease_code text,
    _disease_code_vocabulary text,
    _min_age_of_onset integer default NULL,
    _max_age_of_onset integer default NULL,
    _include_descendants bool default NULL,
    _gender_concept_id integer default NULL  -- 8507 for male, 8532 for female
    )
    RETURNS TABLE(_num_total_results bigint)
    LANGUAGE plpgsql
AS $$
-- _disease_code and _disease_code_vocabulary are required.
-- If _include_descendants is missing, it is treated as FALSE
DECLARE
    _query text;
    _where_clause text;
BEGIN
    -- TODO: only add joins if needed.
    -- Note: every concept has itself as descendant with distance 0.
    _query = '
		SELECT COUNT(DISTINCT person_id)
		FROM cdm_syntheav.condition_occurrence
        JOIN cdm_syntheav.person USING (person_id)
        JOIN vocab.concept AS concept ON condition_concept_id = concept_id
        JOIN vocab.concept_ancestor on condition_concept_id = descendant_concept_id
        JOIN vocab.concept AS ancestor on ancestor_concept_id = ancestor.concept_id';

    -- Require disease code
    IF _disease_code IS NULL OR _disease_code_vocabulary IS NULL THEN
        RETURN QUERY EXECUTE NULL;
    END IF;

    -- #1=_disease_code, #2=_disease_vocabulary, #3=_min_age_of_onset, #4=_max_age_of_onset
    -- #5=_gender_concept_id
    _where_clause = '
	WHERE ancestor.concept_code = $1 AND ancestor.vocabulary_id = $2';

    IF _min_age_of_onset IS NOT NULL THEN
        _where_clause =  _where_clause || '
		AND EXTRACT(YEAR FROM condition_start_date) - person.year_of_birth >= $3';
    END IF;

    IF _max_age_of_onset IS NOT NULL THEN
        _where_clause =  _where_clause || '
		AND EXTRACT(YEAR FROM condition_start_date) - person.year_of_birth <= $4';
    END IF;

    IF _include_descendants IS NULL OR NOT _include_descendants THEN
        _where_clause =  _where_clause || '
		AND min_levels_of_separation = 0'; -- only match on given code
    END IF;

    IF _gender_concept_id IS NOT NULL THEN
        _where_clause = _where_clause || 'AND gender_concept_id = $5';
    END IF;

    _query = _query || _where_clause;

    RAISE NOTICE '_query: %', _query;

    RETURN QUERY EXECUTE _query
        USING _disease_code, _disease_code_vocabulary, _min_age_of_onset, _max_age_of_onset, _gender_concept_id;
END
$$;

-- IDEAs:
-- * ~Build query in sqlalchemy (orm)~
-- * Make a generic count_individuals, independent of domain
-- * Accept multiple disease codes.
-- * age of onset: for the first time in someones history. => solved with era
-- * write out doc which describes how beacon request is translated into OMOP query. e.g. diseases from era