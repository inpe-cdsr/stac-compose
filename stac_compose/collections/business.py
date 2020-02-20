
#!/usr/bin/env python3

from pprint import PrettyPrinter

from werkzeug.exceptions import BadRequest

from stac_compose.collections.services import CollectionsServices
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.log import logging


pp = PrettyPrinter(indent=4)

MAX_LIMIT_DEV_SEED = 1000


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
    def search_post(cls, url, collection, bbox, time=False, cloud_cover=None, page=1, limit=100):
        logging.info('CollectionsBusiness.search_post()')

        logging.info('CollectionsBusiness.search_post() - url: %s', url)
        logging.info('CollectionsBusiness.search_post() - collection: %s', collection)
        logging.info('CollectionsBusiness.search_post() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.search_post() - time: %s', time)
        logging.info('CollectionsBusiness.search_post() - cloud_cover: %s', cloud_cover)
        logging.info('CollectionsBusiness.search_post() - page: %s', page)
        logging.info('CollectionsBusiness.search_post() - limit: %s', limit)

        data = {
            'bbox': bbox.split(','),
            'query': {
                'collection': {
                    'eq': collection
                }
            },
            'page': page,
            'limit': limit
        }

        # if cloud_cover is a number and not a boolean
        if isinstance(cloud_cover, (int, float)) and not isinstance(cloud_cover, bool):
            data['query']['eo:cloud_cover'] = { 'lte': cloud_cover }
        if time:
            data['time'] = time

        logging.info('CollectionsBusiness.search_post() - data: %s', data)

        try:
            response = CollectionsServices.search_post(url, data)

            # logging.debug('CollectionsBusiness.search_post() - response: %s', response)

            return response
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
    def search(cls, collections, bbox, cloud_cover=False, time=False, limit=100, query=None):
        logging.info('CollectionsBusiness.search()')

        # limit is a string, then I need to convert it
        limit = int(limit)

        # if cloud_cover is not False, in other words, it is a string, then I need to convert it
        if cloud_cover:
            cloud_cover = float(cloud_cover)

        logging.info('CollectionsBusiness.search() - collections: %s', collections)
        logging.info('CollectionsBusiness.search() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.search() - cloud_cover: %s', cloud_cover)
        logging.info('CollectionsBusiness.search() - time: %s', time)
        logging.info('CollectionsBusiness.search() - limit: %s', limit)
        logging.info('CollectionsBusiness.search() - query: %s', query)

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
                    logging.info('CollectionsBusiness.search() - collection: %s', collection)
                    logging.info('CollectionsBusiness.search() - MAX_LIMIT_DEV_SEED: %s', MAX_LIMIT_DEV_SEED)

                    # initialize collection
                    result_dict[provider][collection] = None

                    # if 'limit' is less than the maximum I can search, then I can use 'limit' to search my features just one time
                    if limit <= MAX_LIMIT_DEV_SEED:
                        limit_to_search = limit
                    # if 'limit' is greater than the maximum I can search, then I use the maximum number and I search by pages
                    else:
                        limit_to_search = MAX_LIMIT_DEV_SEED

                    # if I'm searching by the first, and only one, page [...]
                    result = cls.search_post(url, collection, bbox, time, cloud_cover, 1, limit_to_search)

                    # logging.debug('CollectionsBusiness.search() - result: %s', result)

                    # [...] then I add it to the dict directly
                    result_dict[provider][collection] = result

                    found = int(result['meta']['found'])

                    logging.debug('CollectionsBusiness.search() - found: %s', found)

                    # if I've already got all features, then I go out of the loop
                    if limit <= MAX_LIMIT_DEV_SEED or found <= MAX_LIMIT_DEV_SEED:
                        logging.debug('CollectionsBusiness.search() - just one result was found')
                        continue
                    else:
                        logging.debug('CollectionsBusiness.search() - more than one result was found')

                        # if there is more results to get, I'm going to search them by pagination
                        for page in range(2, int(limit/MAX_LIMIT_DEV_SEED) + 1):
                            logging.info('CollectionsBusiness.search() - page: %s', page)

                            result = cls.search_post(url, collection, bbox, time, cloud_cover, page, limit_to_search)

                            # logging.debug('CollectionsBusiness.search() - result: %s', result)

                            # if I'm on other page, then I increase the old result
                            result_dict[provider][collection]['features'] += result['features']
                            result_dict[provider][collection]['meta']['returned'] += result['meta']['returned']

                            # logging.debug('CollectionsBusiness.search() - result_dict[provider][collection]: %s', result_dict[provider][collection])

                        # get found variable based on 'result_dict[provider][collection]['meta']['found']'
                        result = result_dict[provider][collection]
                        # if there is not a '['meta']['found']' key inside 'result_dict[provider][collection]',
                        # then return 0, in other words, nothing was found
                        found = int(result['meta']['found']) if 'meta' in result and 'found' in result['meta'] else 0

                        logging.info('CollectionsBusiness.search() - found: %s', found)
                        logging.info('CollectionsBusiness.search() - returned: %s', result_dict[provider][collection]['meta']['returned'])

                        # if something was found, then fill 'limit' key with the true limit
                        if found:
                            result_dict[provider][collection]['meta']['limit'] = limit

                        # logging.debug('CollectionsBusiness.search() - 2 result_dict[provider][collection]: %s', result_dict[provider][collection])
                        logging.debug('\n\nCollectionsBusiness.search() - the end\n\n')

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
