import json
import os
from pprint import pprint

from werkzeug.exceptions import BadRequest

from bdc_search_stac.collections.services import CollectionsServices
from bdc_search_stac.providers.business import ProvidersBusiness


class CollectionsBusiness():

    @classmethod
    def get_collections_by_providers(cls, providers):
        result_by_provider = {}

        for p in providers.split(','):
            response = CollectionsServices.search_collections(ProvidersBusiness.get_providers()[p])

            if response.get('collections'):
                result_by_provider[p] = [c['id'] for c in response['collections']]
            else:
                if p == 'BDC_STAC':
                    result_by_provider[p] = ["{}:SCENE".format(c['title']) for c in response['links'] if c['rel'] == 'child']
                    result_by_provider[p] += ["{}:MERGED".format(c['title']) for c in response['links'] if c['rel'] == 'child']
                else:
                    result_by_provider[p] = [c['title'] for c in response['links'] if c['rel'] == 'child']

        return result_by_provider

    @classmethod
    def search_development_seed(cls, url, collection, bbox, time=False, cloud_cover=False, limit=100):
        data = {
            'bbox': bbox.split(','),
            'query': {
                'collection': { 'eq': collection }
            }
        }

        if cloud_cover:
            # cloud cover
            data['query']['eo:cloud_cover'] = { "lt": cloud_cover }
        if time:
            # range temporal
            data['time'] = time
        if limit:
            # limit
            data['limit'] = limit if int(limit) <= 1000 else 1000

        response = CollectionsServices.search_post(url, data)

        if not response:
            return []

        result_features = []
        # get all features
        if int(limit) <= 1000 or int(response['meta']['found']) <= 1000:
            result_features += response['features']

        # get 1000 features at a time
        else:
            qnt_all_features = response['meta']['found']
            for x in range(0, int(qnt_all_features/1000)+1):
                data['page'] = x+1
                response_by_page = CollectionsServices.search_post(url, data)
                if response_by_page:
                    result_features += response_by_page['features']

        return result_features

    # @classmethod
    # def search_bdc_stac(cls, url, collection, composite, bbox, time=False, cloud_cover=False, limit=100):
    #     query = 'bbox={}&type={}'.format(bbox, composite)

    #     if time:
    #         # range temporal
    #         query += '&time={}'.format(time)
    #     if cloud_cover:
    #         # cloud cover
    #         query += '&eo:cloud_cover=0/{}'.format(cloud_cover)
    #     if limit:
    #         # limit
    #         query += '&limit={}'.format(limit)

    #     response = CollectionsServices.search_items(url, collection, query)

    #     if not response:
    #         return []

    #     return response['features'] if response.get('features') else [response]

    # @classmethod
    # def search_kepler_stac(cls, url, collection, bbox, time=False):
    #     query = 'bbox={}'.format(bbox)
    #     query += '&limit={}'.format(300)

    #     if time:
    #         # range temporal
    #         query += '&time={}'.format(time)

    #     response = CollectionsServices.search_items(url, collection.upper(), query)

    #     if not response:
    #         return []

    #     return response['features'] if response.get('features') else [response]

    @classmethod
    def search_stac(cls, url, collection, bbox, time=None, cloud_cover=None, limit=300):
        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)

        if time:
            # range temporal
            query += '&time={}'.format(time)
        if cloud_cover:
            # cloud cover
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)
        # if limit:
        #     # limit
        #     query += '&limit={}'.format(limit)

        response = CollectionsServices.search_items(url, collection.upper(), query)

        if not response:
            return []

        return response['features'] if response.get('features') else [response]

    @classmethod
    def search(cls, collections, bbox, cloud_cover=False, time=False, limit=100):
        result_features = []

        for cp in collections.split(','):
            cp = cp.split(':')
            provider = cp[0].upper()
            collection = cp[1]

            if provider == 'DEVELOPMENT_SEED_STAC':
                result_features += cls.search_development_seed(ProvidersBusiness.get_providers()[provider],
                                                               collection, bbox, time, cloud_cover, limit)

            # elif provider == 'BDC_STAC':
            #     result_features += cls.search_bdc_stac(ProvidersBusiness.get_providers()[provider],
            #                                    collection, cp[2], bbox, time, cloud_cover, limit)

            elif provider == 'KEPLER_STAC':
                result_features += cls.search_stac(ProvidersBusiness.get_providers()[provider],
                                                   collection, bbox, time)

            else:
                raise BadRequest('Unexpected provider: {}'.format(provider))

        return result_features
