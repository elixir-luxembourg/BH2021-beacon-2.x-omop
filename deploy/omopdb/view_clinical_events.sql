/**
  Union of all clinical events from the clinical OMOP domains condition, drug, procedure, measurement,
  observation, device and specimen.
 */
CREATE OR REPLACE VIEW public.clinical_events AS
with clinical_events AS (
    SELECT
        'Visit' AS domain_name,
        person_id,
        visit_start_date AS start_date,
        visit_concept_id AS event_concept_id,
        NULL::float AS value_as_number,
        NULL::int AS unit_concept_id,
        NULL::int AS value_as_concept_id
    FROM @cdm.visit_occurrence

    UNION

    SELECT
        'Condition' AS domain_name,
        person_id,
        condition_start_date AS start_date,
        condition_concept_id AS event_concept_id,
        NULL AS value_as_number,
        NULL AS unit_concept_id,
        NULL AS value_as_concept_id
    FROM @cdm.condition_occurrence

    UNION

    SELECT
        'Drug' AS domain_name, person_id,
        drug_exposure_start_date AS start_date,
        drug_concept_id AS event_concept_id,
        NULL AS value_as_number,
        NULL AS unit_concept_id,
        NULL AS value_as_concept_id
    FROM @cdm.drug_exposure

    UNION

    SELECT
        'Procedure' AS domain_name,
        person_id,
        procedure_date AS start_date,
        procedure_concept_id AS event_concept_id,
        NULL AS value_as_number,
        NULL AS unit_concept_id,
        NULL AS value_as_concept_id
    FROM @cdm.procedure_occurrence

    UNION

    SELECT
        'Observation' AS domain_name,
        person_id,
        observation_date AS start_date,
        observation_concept_id AS event_concept_id,
        value_as_number AS value_as_number,
        unit_concept_id AS unit_concept_id,
        value_as_concept_id AS value_as_concept_id
    FROM @cdm.observation

    UNION

    SELECT
        'Measurement' AS domain_name,
        person_id,
        measurement_date AS start_date,
        measurement_concept_id AS event_concept_id,
        value_as_number AS value,
        unit_concept_id AS unit_concept_id,
        value_as_concept_id AS value_as_concept_id
    FROM @cdm.measurement

    UNION

    SELECT
        'Device' AS domain_name,
        person_id,
        device_exposure_start_date AS start_date,
        device_concept_id AS event_concept_id,
        NULL AS value_as_number,
        NULL AS unit_concept_id,
        NULL AS value_as_concept_id
    FROM @cdm.device_exposure
    UNION

    SELECT
        'Specimen' AS domain_name,
        person_id,
        specimen_date AS start_date,
        specimen_concept_id AS event_concept_id,
        NULL AS value_as_number,
        NULL AS unit_concept_id,
        NULL AS value_as_concept_id
    FROM @cdm.specimen
)
SELECT
    clinical_events.person_id,
    EXTRACT(YEAR FROM start_date) - person.year_of_birth AS age,
    gender.vocabulary_id || ':' || gender.concept_code AS gender_code,
    gender.concept_name AS gender_label,
    domain_name,
    start_date,
    event.vocabulary_id || ':' || event.concept_code AS event_code,
    event.concept_name AS event_label,
    value_as_number,
    unit.vocabulary_id || ':' || unit.concept_code AS unit_code,
    unit.concept_name AS unit_label,
    value.vocabulary_id || ':' || value.concept_code AS value_code,
    value.concept_name AS value_label,
    row_number() OVER (PARTITION BY person.person_id, event.concept_id ORDER BY start_date) AS ordinal
FROM clinical_events
    JOIN @cdm.person AS person ON person.person_id = clinical_events.person_id
    JOIN @vocab.concept AS event ON event.concept_id = event_concept_id
    LEFT JOIN @vocab.concept AS unit ON unit.concept_id = unit_concept_id
    LEFT JOIN @vocab.concept AS value ON value.concept_id = value_as_concept_id
    JOIN @vocab.concept AS gender ON gender.concept_id = gender_concept_id
where person.person_id = 4666
order by domain_name, event_code
;