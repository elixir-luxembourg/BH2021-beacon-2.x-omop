"""
Filtering terms Endpoint.

Querying the filtering terms endpoint reveals information about existing ontology filters in this beacon.
These are stored in the DB inside the table named 'ontology_terms'.

"""

from beacon import conf
from beacon.db.filtering_terms import get_filtering_terms
from beacon.utils.stream import json_stream


async def handler(request):


    ontology_terms = await get_filtering_terms()
    # response = {
    #     'beaconId': conf.beacon_id,
    #     'apiVersion': conf.api_version,
    #     'filteringTerms': ontology_terms,
    # }
    response = {
        "meta": {
            "beaconId": "org.example.beacon.v2",
            "apiVersion": "2.0.0-draft.4",
            "returnedSchemas": {
                "entityType": "filteringTerm",
                "schema": "ga4gh-beacon-filteringTerm-v2.0.0-draft.4"
            }
        },
        "response": {
            "resources": [
                {
                    "id": "SNOMED",
                    "name": "Systematic Nomenclature of Medicine - Clinical Terms (IHTSDO)",
                    "url": "https://www.snomed.org/",
                    "version": "2020-07-31 SNOMED CT International Edition; 2020-09-01 SNOMED CT US Edition; 2020-10-28 SNOMED CT UK Edition",
                    "namespacePrefix": "SNOMED",
                    "iriPrefix": "https://bioportal.bioontology.org/ontologies/SNOMEDCT?p=classes&conceptid="
                },
                {
                    "id": "LOINC",
                    "name": "Logical Observation Identifiers Names and Codes (Regenstrief Institute)",
                    "url": "https://loinc.org/file-access/download-id/431672/",
                    "version": "2.69",
                    "namespacePrefix": "LOINC",
                    "iriPrefix": "https://bioportal.bioontology.org/ontologies/LOINC?p=classes&conceptid="
                },
                {
                    "id": "OMOP CDM",
                    "name": "OMOP Common DataModel",
                    "url": "https://github.com/OHDSI/CommonDataModel/blob/v5.4/inst/csv/OMOP_CDMv5.4_Field_Level.csv",
                    "version": "V5.4.0",
                    "namespacePrefix": "CDM",
                    "iriPrefix": "https://athena.ohdsi.org/search-terms/terms/"
                },
                {
                    "id": "RxNorm",
                    "iriPrefix": "http://purl.bioontology.org/ontology/RXNORM/",
                    "name": "RxNorm",
                    "namespacePrefix": "RxNorm",
                    "url": "https://www.nlm.nih.gov/research/umls/rxnorm/index.html",
                    "version": "20210802"
                }
            ],
            "filterTerms": ontology_terms
        }
    }

    return response
