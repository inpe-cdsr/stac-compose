import json
import os
from pprint import pprint

from bdc_search_stac.search.services import SearchServices
from bdc_search_stac.config import BASE_DIR

class SearchBusiness():

    @classmethod
    def get_providers(cls):
        with open('{}/search/static/providers.json'.format(BASE_DIR)) as p:
            data = json.load(p)
        
        providers = {}
        for key in data.keys():
            providers[key] = data[key]['url']
        return providers
        
    @classmethod
    def search(cls, providers, bbox, cloud, start_date, last_date, limit_sat=10):
        # range temporal
        query = '&time={}T00:00:00Z/{}T23:59:59Z'.format(start_date, last_date)
        # cloud cover
        query += '&eo:cloud_cover=0/{}'.format(cloud)
        # limit
        query += '&limit={}'.format(limit_sat)
        
        result_by_provider = {}
        result_features = []
        for p in providers.split(','):
            query_full = 'bbox={}{}'.format(bbox if p == 'KEPLER_STAC' else '[{}]'.format(bbox), query)

            response = SearchServices.search_stac(cls.get_providers()[p], query_full)
            if response:
                result_by_provider[p] = json.loads(response.text)
                result_features += json.loads(response.text)['features']
        return result_features