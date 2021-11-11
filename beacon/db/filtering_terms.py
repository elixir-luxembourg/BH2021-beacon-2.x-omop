from beacon.db import client
from beacon.db.filters import apply_filters
from beacon.db.utils import query_id
from beacon.request.model import RequestParams
import asyncio
import asyncpg


async def get_filtering_terms():
    connection = await asyncpg.connect(user='postgres', password='password',
                                 database='postgres', host='127.0.0.1')
    filterList = []
    values = await connection.fetch(
        "select concat(t2.vocabulary_id, ':', concept_code) as id, concept_name as label, t3.vocabulary_name as type from cdm_synthea10.condition_occurrence as t1 join cdm_synthea10.concept as t2 on t2.concept_id = t1.condition_concept_id join cdm_synthea10.vocabulary as t3 on t3.vocabulary_id = t2.vocabulary_id group by condition_concept_id, concept_name, concept_code, t2.vocabulary_id, t3.vocabulary_name;",
    )
    v2 = await connection.fetch(
        "select concat(vocabulary_id, ':', concept_code) as id, concept_name as label, 'numeric' as type from cdm_synthea10.measurement join cdm_synthea10.concept on concept_id = measurement_concept_id group by measurement_concept_id, concept_name, concept_code, vocabulary_id;"
        )
    v3 = await connection.fetch(
        "select concat('CDM:', tf.concept_id) as id, tf.concept_name as label, 'OMOP CDM' as type from cdm_synthea10.concept v join cdm_synthea10.concept_relationship on concept_id_1 = v.concept_id AND relationship_id = 'Version contains'join cdm_synthea10.concept tf on concept_id_2 = tf.concept_id where v.concept_id = 756265  -- OMOP CDM v5.4.0 and tf.concept_class_id = 'Field'order by tf.concept_name;"
        )
    v4 = await connection.fetch(
        "select concat(t2.vocabulary_id, ':', concept_code) as id, concept_name as label, t3.vocabulary_name as type from cdm_synthea10.drug_exposure as t1 join cdm_synthea10.concept as t2 on t2.concept_id = t1.drug_concept_id	join cdm_synthea10.vocabulary as t3 on t3.vocabulary_id = t2.vocabulary_id group by drug_concept_id, concept_name, concept_code, t2.vocabulary_id, t3.vocabulary_name;"
        )
    for filter in values:
        filterList.append(beaconify_filters(filter))
    for filter in v2:
        filterList.append(beaconify_filters(filter))
    for filter in v3:
        filterList.append(beaconify_filters(filter))
    for filter in v4:
        filterList.append(beaconify_filters(filter))
    return filterList



def beaconify_filters(values):
    return {
        "type": values['type'],
        "id": values['id'],
        "label": values['label']
        }


def get_filtering_term_with_id(entry_id: str, qparams: RequestParams):
    return {
        'error': 'not_implemented'
    }  # TODO: fill
    query = apply_filters({}, qparams.query.filters)
    query = query_id(query, entry_id)
    return client.beacon.filtering_terms\
        .find(query)\
        .skip(qparams.query.pagination.skip)\
        .limit(qparams.query.pagination.limit)
