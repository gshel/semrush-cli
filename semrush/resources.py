import os

import semrush.resources

SEMRUSH_API_KEY = os.environ['SEMRUSH_API_KEY']

def assemble_query_string(**kwargs):
    query_string = list()

    if not 'key' in kwargs:
        kwargs['key'] = semrush.resources.SEMRUSH_API_KEY

    for k,v in kwargs.items():
        if v is None:
            continue
        elif type(v) is bool:
            v = str(v).lower()
        query_string.append(f'{k}={v}')
    output_query_string = '&'.join(query_string)
    return output_query_string