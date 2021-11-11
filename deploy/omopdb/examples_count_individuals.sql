
-- Heart disease. Has four descendants at various levels, and concept itself also occurs.
select * from public.count_individuals('56265001', 'SNOMED', 24, 42, TRUE); -- 116
select public.count_individuals('56265001', 'SNOMED', 24, 42, FALSE); -- 17
select public.count_individuals('56265001', 'SNOMED', NULL, NULL, NULL); -- 34
select public.count_individuals('56265001', 'SNOMED', NULL, NULL, TRUE); -- 504

-- Non-small cell lung cancer. Does not have descendants.
select public.count_individuals('254637007', 'SNOMED', NULL, NULL, NULL); -- 12, with or without descendants
select public.count_individuals('254637007', 'SNOMED', 0, 99, NULL); -- 12, with or without descendants

-- Non-existing (measurement) code
select public.count_individuals('1751-7', 'SNOMED', 0, 99, NULL); -- 0

-- Error
select public.count_individuals(NULL, NULL, NULL, NULL, NULL); -- disease code is required

-- With gender
select public.count_individuals('254637007', 'SNOMED', NULL, NULL, NULL, 8532);

-- The basic count query
SELECT COUNT(DISTINCT person_id) --, COUNT(*), string_agg(DISTINCT concept.concept_name, '|')
FROM cdm_syntheav.condition_occurrence
         JOIN cdm_syntheav.person USING (person_id)
         JOIN vocab.concept AS concept ON condition_concept_id = concept_id
         JOIN vocab.concept_ancestor on condition_concept_id = descendant_concept_id
         JOIN vocab.concept AS ancestor on ancestor_concept_id = ancestor.concept_id
WHERE
        ancestor.concept_code = '56265001'
  AND ancestor.vocabulary_id = 'SNOMED'
  AND EXTRACT(YEAR FROM condition_start_date) - person.year_of_birth >= 24 -- if _min_age_onset
  AND EXTRACT(YEAR FROM condition_start_date) - person.year_of_birth <= 42 -- if _max_age_onset
  AND min_levels_of_separation = 0 -- if not _include_descendants
  AND gender_concept_id = 8531 -- if _gender_concept_id
;