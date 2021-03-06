from aiohttp import web

from beacon.db import analyses, biosamples, cohorts, datasets, g_variants, individuals, runs
from beacon.db.backends.postgres import get_dummy_value, count_individuals
from beacon.request.handlers import dummy_pg_handler
from beacon.response import framework, filtering_terms, info

routes = [

    # DB Test  TODO: Remove
    web.get('/db_test/', dummy_pg_handler('db test', db_fn=get_dummy_value)),

    ########################################
    # CONFIG
    ########################################

    web.get('/api', info.handler),
    web.get('/api/info', info.handler),
    web.get('/api/filtering_terms', dummy_pg_handler(log_name='filtering terms', db_fn=filtering_terms.handler)),

    web.get('/api/configuration', framework.configuration),
    web.get('/api/entry_types', framework.entry_types),
    web.get('/api/map', framework.beacon_map),

    ########################################
    # GET
    ########################################
    # TODO: Uncomment 
    # web.get('/api/analyses/', generic_handler(db_fn=analyses.get_analyses)),
    # web.get('/api/analyses/{id}/', generic_handler(db_fn=analyses.get_analysis_with_id)),
    # web.get('/api/analyses/{id}/g_variants/', generic_handler(db_fn=analyses.get_variants_of_analysis)),

    # web.get('/api/biosamples/', generic_handler(db_fn=biosamples.get_biosamples)),
    # web.get('/api/biosamples/{id}/', generic_handler(db_fn=biosamples.get_biosample_with_id)),
    # web.get('/api/biosamples/{id}/g_variants/', generic_handler(db_fn=biosamples.get_variants_of_biosample)),
    # web.get('/api/biosamples/{id}/analyses/', generic_handler(db_fn=biosamples.get_analyses_of_biosample)),
    # web.get('/api/biosamples/{id}/runs/', generic_handler(db_fn=biosamples.get_runs_of_biosample)),

    # web.get('/api/cohorts/', generic_handler(db_fn=cohorts.get_cohorts)),
    # web.get('/api/cohorts/{id}/', generic_handler(db_fn=cohorts.get_cohort_with_id)),
    # web.get('/api/cohorts/{id}/individuals/', generic_handler(db_fn=cohorts.get_individuals_of_cohort)),
    # web.get('/api/cohorts/{id}/filtering_terms/', generic_handler(db_fn=cohorts.get_filtering_terms_of_cohort)),
    # web.get('/api/cohorts/{id}/g_variants/', generic_handler(db_fn=cohorts.get_variants_of_cohort)),
    # web.get('/api/cohorts/{id}/biosamples/', generic_handler(db_fn=cohorts.get_biosamples_of_cohort)),
    # web.get('/api/cohorts/{id}/runs/', generic_handler(db_fn=cohorts.get_runs_of_cohort)),
    # web.get('/api/cohorts/{id}/analyses/', generic_handler(db_fn=cohorts.get_analyses_of_cohort)),

    # web.get('/api/datasets/', generic_handler(db_fn=datasets.get_datasets)),
    # web.get('/api/datasets/{id}/', generic_handler(db_fn=datasets.get_dataset_with_id)),
    # web.get('/api/datasets/{id}/g_variants/', generic_handler(db_fn=datasets.get_variants_of_dataset)),
    # web.get('/api/datasets/{id}/biosamples/', generic_handler(db_fn=datasets.get_biosamples_of_dataset)),
    # web.get('/api/datasets/{id}/individuals/', generic_handler(db_fn=datasets.get_individuals_of_dataset)),
    # web.get('/api/datasets/{id}/filtering_terms/', generic_handler(db_fn=datasets.get_filtering_terms_of_dataset)),
    # web.get('/api/datasets/{id}/runs/', generic_handler(db_fn=datasets.get_runs_of_dataset)),
    # web.get('/api/datasets/{id}/analyses/', generic_handler(db_fn=datasets.get_analyses_of_dataset)),

    # web.get('/api/g_variants/', generic_handler(db_fn=g_variants.get_variants)),
    # web.get('/api/g_variants/{id}/', generic_handler(db_fn=g_variants.get_variant_with_id)),
    # web.get('/api/g_variants/{id}/biosamples/', generic_handler(db_fn=g_variants.get_biosamples_of_variant)),
    # web.get('/api/g_variants/{id}/individuals/', generic_handler(db_fn=g_variants.get_individuals_of_variant)),
    # web.get('/api/g_variants/{id}/runs/', generic_handler(db_fn=g_variants.get_runs_of_variant)),
    # web.get('/api/g_variants/{id}/analyses/', generic_handler(db_fn=g_variants.get_analyses_of_variant)),

    # web.get('/api/individuals/', dummy_pg_handler(log_name='GET /api/individuals', db_fn=individuals.get_individuals)),
    # web.get('/api/individuals/{id}/', generic_handler(db_fn=individuals.get_individual_with_id)),
    # web.get('/api/individuals/{id}/g_variants/', generic_handler(db_fn=individuals.get_variants_of_individual)),
    # web.get('/api/individuals/{id}/biosamples/', generic_handler(db_fn=individuals.get_biosamples_of_individual)),
    # web.get('/api/individuals/{id}/filtering_terms/', generic_handler(db_fn=individuals.get_filtering_terms_of_individual)),
    # web.get('/api/individuals/{id}/runs/', generic_handler(db_fn=individuals.get_runs_of_individual)),
    # web.get('/api/individuals/{id}/analyses/', generic_handler(db_fn=individuals.get_analyses_of_individual)),

    # web.get('/api/runs/', generic_handler(db_fn=runs.get_runs)),
    # web.get('/api/runs/{id}/', generic_handler(db_fn=runs.get_run_with_id)),
    # web.get('/api/runs/{id}/g_variants/', generic_handler(db_fn=runs.get_variants_of_run)),
    # web.get('/api/runs/{id}/analyses/', generic_handler(db_fn=runs.get_analyses_of_run)),

    ########################################
    # POST
    ########################################

    # web.post('/api/analyses/', generic_handler(db_fn=analyses.get_analyses)),
    # web.post('/api/analyses/{id}/', generic_handler(db_fn=analyses.get_analysis_with_id)),
    # web.post('/api/analyses/{id}/g_variants/', generic_handler(db_fn=analyses.get_variants_of_analysis)),

    # web.post('/api/biosamples/', generic_handler(db_fn=biosamples.get_biosamples)),
    # web.post('/api/biosamples/{id}/', generic_handler(db_fn=biosamples.get_biosample_with_id)),
    # web.post('/api/biosamples/{id}/g_variants/', generic_handler(db_fn=biosamples.get_variants_of_biosample)),
    # web.post('/api/biosamples/{id}/analyses/', generic_handler(db_fn=biosamples.get_analyses_of_biosample)),
    # web.post('/api/biosamples/{id}/runs/', generic_handler(db_fn=biosamples.get_runs_of_biosample)),

    # web.post('/api/cohorts/', generic_handler(db_fn=cohorts.get_cohorts)),
    # web.post('/api/cohorts/{id}/', generic_handler(db_fn=cohorts.get_cohort_with_id)),
    # web.post('/api/cohorts/{id}/individuals/', generic_handler(db_fn=cohorts.get_individuals_of_cohort)),
    # web.post('/api/cohorts/{id}/filtering_terms/', generic_handler(db_fn=cohorts.get_filtering_terms_of_cohort)),
    # web.post('/api/cohorts/{id}/g_variants/', generic_handler(db_fn=cohorts.get_variants_of_cohort)),
    # web.post('/api/cohorts/{id}/biosamples/', generic_handler(db_fn=cohorts.get_biosamples_of_cohort)),
    # web.post('/api/cohorts/{id}/runs/', generic_handler(db_fn=cohorts.get_runs_of_cohort)),
    # web.post('/api/cohorts/{id}/analyses/', generic_handler(db_fn=cohorts.get_analyses_of_cohort)),

    # web.post('/api/datasets/', generic_handler(db_fn=datasets.get_datasets)),
    # web.post('/api/datasets/{id}/', generic_handler(db_fn=datasets.get_dataset_with_id)),
    # web.post('/api/datasets/{id}/g_variants/', generic_handler(db_fn=datasets.get_variants_of_dataset)),
    # web.post('/api/datasets/{id}/biosamples/', generic_handler(db_fn=datasets.get_biosamples_of_dataset)),
    # web.post('/api/datasets/{id}/individuals/', generic_handler(db_fn=datasets.get_individuals_of_dataset)),
    # web.post('/api/datasets/{id}/filtering_terms/', generic_handler(db_fn=datasets.get_filtering_terms_of_dataset)),
    # web.post('/api/datasets/{id}/runs/', generic_handler(db_fn=datasets.get_runs_of_dataset)),
    # web.post('/api/datasets/{id}/analyses/', generic_handler(db_fn=datasets.get_analyses_of_dataset)),

    # web.post('/api/g_variants/', generic_handler(db_fn=g_variants.get_variants)),
    # web.post('/api/g_variants/{id}/', generic_handler(db_fn=g_variants.get_variant_with_id)),
    # web.post('/api/g_variants/{id}/biosamples/', generic_handler(db_fn=g_variants.get_biosamples_of_variant)),
    # web.post('/api/g_variants/{id}/individuals/', generic_handler(db_fn=g_variants.get_individuals_of_variant)),
    # web.post('/api/g_variants/{id}/runs/', generic_handler(db_fn=g_variants.get_runs_of_variant)),
    # web.post('/api/g_variants/{id}/analyses/', generic_handler(db_fn=g_variants.get_analyses_of_variant)),

    web.post('/api/individuals/', dummy_pg_handler(log_name='/api/individuals/', db_fn=count_individuals)),
    # web.post('/api/individuals/', dummy_pg_handler(log_name='post /api/individuals', db_fn=individuals.get_individuals)),
    # web.post('/api/individuals/{id}/', generic_handler(db_fn=individuals.get_individual_with_id)),
    # web.post('/api/individuals/{id}/g_variants/', generic_handler(db_fn=individuals.get_variants_of_individual)),
    # web.post('/api/individuals/{id}/biosamples/', generic_handler(db_fn=individuals.get_biosamples_of_individual)),
    # web.post('/api/individuals/{id}/filtering_terms/', generic_handler(db_fn=individuals.get_filtering_terms_of_individual)),
    # web.post('/api/individuals/{id}/runs/', generic_handler(db_fn=individuals.get_runs_of_individual)),
    # web.post('/api/individuals/{id}/analyses/', generic_handler(db_fn=individuals.get_analyses_of_individual)),

    # web.post('/api/runs/', generic_handler(db_fn=runs.get_runs)),
    # web.post('/api/runs/{id}/', generic_handler(db_fn=runs.get_run_with_id)),
    # web.post('/api/runs/{id}/g_variants/', generic_handler(db_fn=runs.get_variants_of_run)),
    # web.post('/api/runs/{id}/analyses/', generic_handler(db_fn=runs.get_analyses_of_run)),
]
