CREATE OR REPLACE FUNCTION public.get_filtering_terms()
 RETURNS TABLE(id text, label character varying, type character varying)
 LANGUAGE plpgsql
AS $function$

BEGIN
RETURN QUERY
        select concat(t2.vocabulary_id, ':', concept_code) as id, concept_name as label, t3.vocabulary_name as type from cdm_synthea10.condition_occurrence as t1 join cdm_synthea10.concept as t2 on t2.concept_id = t1.condition_concept_id join cdm_synthea10.vocabulary as t3 on t3.vocabulary_id = t2.vocabulary_id group by condition_concept_id, concept_name, concept_code, t2.vocabulary_id, t3.vocabulary_name
        UNION
        select concat(vocabulary_id, ':', concept_code) as id, concept_name as label, 'numeric' as type from cdm_synthea10.measurement join cdm_synthea10.concept on concept_id = measurement_concept_id group by measurement_concept_id, concept_name, concept_code, vocabulary_id
        UNION
        select concat('CDM:', tf.concept_id) as id, tf.concept_name as label, 'OMOP CDM' as type from cdm_synthea10.concept v join cdm_synthea10.concept_relationship on concept_id_1 = v.concept_id AND relationship_id = 'Version contains'join cdm_synthea10.concept tf on concept_id_2 = tf.concept_id where v.concept_id = 75626 and tf.concept_class_id = 'Field' --order by tf.concept_name
        UNION
        select concat(t2.vocabulary_id, ':', concept_code) as id, concept_name as label, t3.vocabulary_name as type from cdm_synthea10.drug_exposure as t1 join cdm_synthea10.concept as t2 on t2.concept_id = t1.drug_concept_id       join cdm_synthea10.vocabulary as t3 on t3.vocabulary_id = t2.vocabulary_id group by drug_concept_id, concept_name, concept_code, t2.vocabulary_id, t3.vocabulary_name;
END;$function$
