from beacon.db import client
from beacon.db.filters import apply_filters
from beacon.db.utils import query_id
from beacon.request.model import RequestParams
from beacon import conf
import asyncio
import asyncpg


async def get_filtering_terms():
    # TODO: pass the connection object through to here to use instead of the below
    connection = await asyncpg.connect(user=conf.database_user, password=conf.database_password,
                                       database=conf.database_name, host=conf.database_url,
                                       port=conf.database_port)
    filterList = []
    values = await connection.fetch(
        "select * from public.get_filtering_terms()"
    )
    for filter in values:
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
