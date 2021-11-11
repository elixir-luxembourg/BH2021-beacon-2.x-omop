import json
from aiohttp import web
from aiohttp.web_request import Request
from bson import json_util

from beacon.request import get_parameters
from beacon.response.info_response_schema import build_beacon_resultset_response
import logging

LOG = logging.getLogger(__name__)


def generic_mongo_handler(db_fn, request=None):
    async def wrapper(request: Request):
        # Get params
        LOG.debug(type(request))
        qparams = await get_parameters(request)
        entry_id = request.match_info["id"] if "id" in request.match_info else None

        # Get response
        response_converted = [ json.loads(json_util.dumps(r)) for r in db_fn(entry_id, qparams)]
        response = build_beacon_resultset_response(response_converted, len(response_converted), qparams, lambda x, y: x)
        return web.json_response(response)

    return wrapper


def print_qparams(qparams_db, proxy, logger):
    logger.debug('{:-^50}'.format(" Query Parameters for DB "))
    for key in proxy.__keys__:
        val = getattr(qparams_db, key)
        t = ' ' if val is None else str(type(val))
        name = getattr(proxy.__names__, key)
        logger.debug(f"{key:>20} | {name:<20} : {str(val):<8} {t}")


def dummy_pg_handler(log_name, db_fn):
    async def wrapper(request):
        LOG.info('Running a request for %s', log_name)

        qparams = {}
        # qparams = get_qparams_from_request(request)  # TODO
        # LOG.debug('requested datasets:  %s', qparams.datasetIds)

        # TODO: Pick access_token
        # TODO: Filter out datasets

        # TODO: Get values from the database
        response = db_fn(qparams)
        # response_total_results = count_results_func(qparams_db, datasets, authenticated)
        
        # rows = [row async for row in response]
        # num_total_results = await response_total_results

        # build_beacon_response knows how to loop through it
        # response_converted = build_beacon_response(proxy, rows, num_total_results, qparams_db, by_entity_type, non_accessible_datasets, build_response_func)

        LOG.info('Formatting the response for %s', log_name)
        return await web.Response(body=str(response))
    return wrapper
