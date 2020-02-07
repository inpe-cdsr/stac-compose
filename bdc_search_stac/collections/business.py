
#!/usr/bin/env python3

from pprint import PrettyPrinter

from werkzeug.exceptions import BadRequest

from bdc_search_stac.collections.services import CollectionsServices
from bdc_search_stac.providers.business import ProvidersBusiness
from bdc_search_stac.log import logging


pp = PrettyPrinter(indent=4)


class CollectionsBusiness():
    providers_business = ProvidersBusiness()

    @classmethod
    def get_collections_by_providers(cls, providers):
        result_by_provider = {}

        for p in providers.split(','):
            response = CollectionsServices.search_collections(cls.providers_business.get_providers()[p]['url'])

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
    def search_post(cls, url, collection, bbox, time=False, cloud_cover=False, limit=100):
        logging.info('CollectionsBusiness.search_post()')

        logging.info('CollectionsBusiness.search_post() - url: %s', url)
        logging.info('CollectionsBusiness.search_post() - collection: %s', collection)

        data = {
            'bbox': bbox.split(','),
            'query': {
                'collection': { 'eq': collection }
            },
            'limit': limit if int(limit) <= 1000 else 1000
        }

        if cloud_cover:
            data['query']['eo:cloud_cover'] = { "lt": cloud_cover }
        if time:
            data['time'] = time

        logging.info('CollectionsBusiness.search_post() - data: %s', data)

        try:
            response = CollectionsServices.search_post(url, data)

            # logging.debug('CollectionsBusiness.search_post() - response: %s', response)

            return CollectionsServices.search_post(url, data)
        except Exception as e:
            return None

    @classmethod
    def search_get(cls, url, collections, bbox, time=None, cloud_cover=None, limit=300):
        logging.info('CollectionsBusiness.search_get()')

        logging.info('CollectionsBusiness.search_get() - url: %s', url)
        logging.info('CollectionsBusiness.search_get() - collections: %s', collections)

        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)
        query += '&collections={}'.format(','.join(collections))

        if time:
            query += '&time={}'.format(time)
        if cloud_cover:
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        logging.info('CollectionsBusiness.search_get() - query: %s', query)

        try:
            response = CollectionsServices.search_get(url, query)

            logging.info('CollectionsBusiness.search_get() - response: %s', response)

            if not response:
                return []

            return response['features'] if response.get('features') else [response]
        except Exception as e:
            return []

    @classmethod
    def search_get_items(cls, url, collection, bbox, time=None, cloud_cover=None, limit=300):
        logging.info('CollectionsBusiness.search_get_items()')

        logging.info('CollectionsBusiness.search_get_items() - url: %s', url)
        logging.info('CollectionsBusiness.search_get_items() - collection: %s', collection)

        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)

        if time:
            query += '&time={}'.format(time)
        if cloud_cover:
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        logging.info('CollectionsBusiness.search_get_items() - query: %s', query)

        try:
            response = CollectionsServices.search_items(url, collection, query)

            # logging.debug('CollectionsBusiness.search_get_items() - response: %s', response)

            return response
        except Exception as e:
            return None

    @classmethod
    def search(cls, collections, bbox, cloud_cover=False, time=False, limit=100):
        logging.info('CollectionsBusiness.search()')

        result_dict = {}
        providers = list(set([p.split(':')[0] for p in collections.split(',')]))

        logging.info('CollectionsBusiness.search() - providers: %s', providers)

        for provider in providers:
            logging.info('CollectionsBusiness.search() - provider: %s', provider)

            url = cls.providers_business.get_providers()[provider]['url']
            cs = [c.split(':')[1] for c in collections.split(',') if c.split(':')[0] == provider]
            method = cls.providers_business.get_providers_methods()[provider]
            filter_mult = cls.providers_business.get_filter_mult_collection()[provider]

            logging.info('CollectionsBusiness.search() - url: %s', url)
            logging.info('CollectionsBusiness.search() - cs: %s', cs)
            logging.info('CollectionsBusiness.search() - method: %s', method)
            logging.info('CollectionsBusiness.search() - filter_mult: %s', filter_mult)

            # if there is not a provider inside the dict, then initialize it
            if provider not in result_dict:
                result_dict[provider] = {}

            if method == 'POST':
                for collection in cs:
                    result = cls.search_post(url, collection, bbox, time, cloud_cover, limit)

                    # add the result to the corresponding collection
                    result_dict[provider][collection] = result

            elif method == 'GET':
                if filter_mult:
                    # TODO: fixing this line to return separate by collection and not just by provider (like the other ones)
                    result = cls.search_get(url, cs, bbox, time=time, limit=limit)

                    result_dict[provider] = result
                else:
                    for collection in cs:
                        result = cls.search_get_items(url, collection, bbox, time=time, limit=limit)

                        # add the result to the corresponding collection
                        result_dict[provider][collection] = result
            else:
                raise BadRequest('Unexpected provider: {}'.format(provider))

        return result_dict
