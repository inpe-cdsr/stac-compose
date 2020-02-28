
#!/usr/bin/env python3

from pprint import PrettyPrinter
from werkzeug.exceptions import BadRequest

from stac_compose.common import MAX_LIMIT, rename_fields_from_feature_collection, \
                                add_context_field_in_the_feature_collection_if_it_does_not_exist
from stac_compose.services import StacComposeServices
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.log import logging


pp = PrettyPrinter(indent=4)


class CollectionsBusiness():
    providers_business = ProvidersBusiness()

    @classmethod
    def get_collections_by_providers(cls, providers):
        result_by_provider = {}

        for p in providers.split(','):
            response = StacComposeServices.search_collections(cls.providers_business.get_providers()[p]['url'])

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
    def stac_post(cls, url, collection, bbox, time=False, cloud_cover=None, page=1, limit=100):
        logging.info('CollectionsBusiness.stac_post()')

        logging.info('CollectionsBusiness.stac_post() - url: %s', url)
        logging.info('CollectionsBusiness.stac_post() - collection: %s', collection)
        logging.info('CollectionsBusiness.stac_post() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.stac_post() - time: %s', time)
        logging.info('CollectionsBusiness.stac_post() - cloud_cover: %s', cloud_cover)
        logging.info('CollectionsBusiness.stac_post() - page: %s', page)
        logging.info('CollectionsBusiness.stac_post() - limit: %s', limit)

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

        logging.info('CollectionsBusiness.stac_post() - data: %s', data)

        try:
            response = StacComposeServices.post_stac_search(url, data)

            # logging.debug('CollectionsBusiness.sta_post() - response: %s', response)

            return response
        except Exception as e:
            return None

    @classmethod
    def stac_get(cls, url, collections, bbox, time=None, cloud_cover=None, limit=300):
        logging.info('CollectionsBusiness.stac_get()')

        logging.info('CollectionsBusiness.stac_get() - url: %s', url)
        logging.info('CollectionsBusiness.stac_get() - collections: %s', collections)

        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)
        query += '&collections={}'.format(','.join(collections))

        if time:
            query += '&time={}'.format(time)
        if cloud_cover:
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        logging.info('CollectionsBusiness.stac_get() - query: %s', query)

        try:
            response = StacComposeServices.get_stac_search(url, query)

            # logging.info('CollectionsBusiness.stac_get() - response: %s', response)

            if not response:
                return []

            return response['features'] if response.get('features') else [response]
        except Exception as e:
            return []

    @classmethod
    def stac_get_items(cls, providers_json, collection, bbox, time=None, cloud_cover=None, limit=300):
        logging.info('CollectionsBusiness.stac_get_items()\n')

        logging.info('CollectionsBusiness.stac_get_items() - providers_json: %s', providers_json)
        logging.info('CollectionsBusiness.stac_get_items() - collection: %s', collection)
        logging.info('CollectionsBusiness.stac_get_items() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.stac_get_items() - time: %s', time)
        logging.info('CollectionsBusiness.stac_get_items() - cloud_cover: %s', cloud_cover)
        logging.info('CollectionsBusiness.stac_get_items() - limit: %s', limit)

        url = providers_json['url']

        logging.info('CollectionsBusiness.stac_get_items() - url: %s', url)

        if isinstance(bbox, str):
            query = 'bbox={}'.format(bbox)
        elif isinstance(bbox, list):
            bbox = ",".join(list(map(str, bbox)))
            query = 'bbox={}'.format(bbox)
        else:
            raise BadRequest('`bbox` field is invalid: `{0}`, it should be a string or list, but its type is {1}.'.format(bbox, type(bbox)))

        if time:
            query += '&time={}'.format(time)
        if cloud_cover:
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        query += '&limit={}'.format(limit)

        logging.info('CollectionsBusiness.stac_get_items() - query: %s', query)

        try:
            response = StacComposeServices.search_items(url, collection, query)

            # logging.debug('CollectionsBusiness.stac_get_items() - before post processing -  response: %s', response)

            # post processing to rename fields and add field is it is necessary
            response = add_context_field_in_the_feature_collection_if_it_does_not_exist(response, page=1, limit=limit)
            response = rename_fields_from_feature_collection(response)

            # logging.debug('CollectionsBusiness.stac_get_items() - after post processing - response: %s', response)

            return response
        except Exception as e:
            return None

    @classmethod
    def search_get(cls, collections, bbox, cloud_cover=False, time=False, limit=300, query=None):
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

            providers_json = cls.providers_business.get_providers_json()[provider]

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
                    logging.info('CollectionsBusiness.search() - MAX_LIMIT: %s', MAX_LIMIT)

                    # initialize collection
                    result_dict[provider][collection] = None

                    # if 'limit' is less than the maximum I can search, then I can use 'limit' to search my features just one time
                    if limit <= MAX_LIMIT:
                        limit_to_search = limit
                    # if 'limit' is greater than the maximum I can search, then I use the maximum number and I search by pages
                    else:
                        limit_to_search = MAX_LIMIT

                    # if I'm searching by the first, and only one, page [...]
                    result = cls.stac_post(url, collection, bbox, time, cloud_cover, 1, limit_to_search)

                    # logging.debug('CollectionsBusiness.search() - result: %s', result)

                    # [...] then I add it to the dict directly
                    result_dict[provider][collection] = result

                    result = add_context_field_in_the_feature_collection_if_it_does_not_exist(result, page=1, limit=limit_to_search)
                    result = rename_fields_from_feature_collection(result)

                    found = int(result['context']['matched'])

                    logging.debug('CollectionsBusiness.search() - matched: %s', found)

                    # if I've already got all features, then I go out of the loop
                    if limit <= MAX_LIMIT or found <= MAX_LIMIT:
                        logging.debug('CollectionsBusiness.search() - just one result was found')
                        continue
                    else:
                        logging.debug('CollectionsBusiness.search() - more than one result was found')

                        # if there is more results to get, I'm going to search them by pagination
                        for page in range(2, int(limit/MAX_LIMIT) + 1):
                            logging.info('CollectionsBusiness.search() - page: %s', page)

                            result = cls.stac_post(url, collection, bbox, time, cloud_cover, page, limit_to_search)

                            # logging.debug('CollectionsBusiness.search() - result: %s', result)

                            result = add_context_field_in_the_feature_collection_if_it_does_not_exist(result, page=page, limit=limit_to_search)
                            result = rename_fields_from_feature_collection(result)

                            # if I'm on other page, then I increase the old result
                            result_dict[provider][collection]['features'] += result['features']
                            result_dict[provider][collection]['context']['returned'] += result['context']['returned']

                            # logging.debug('CollectionsBusiness.search() - result_dict[provider][collection]: %s', result_dict[provider][collection])

                        # get matched variable based on 'result_dict[provider][collection]['context']['matched']'
                        context = result_dict[provider][collection]['context']
                        matched = int(context['matched'])

                        logging.info('CollectionsBusiness.search() - matched: %s', matched)
                        logging.info('CollectionsBusiness.search() - returned: %s', context['returned'])

                        # if something was found, then fill 'limit' key with the true limit
                        if matched:
                            context['limit'] = limit

                        # logging.debug('CollectionsBusiness.search() - 2 result_dict[provider][collection]: %s', result_dict[provider][collection])
                        logging.debug('\n\nCollectionsBusiness.search() - the end\n\n')

            elif method == 'GET':
                if filter_mult:
                    # TODO: fixing this line to return separate by collection and not just by provider (like the other ones)
                    result = cls.stac_get(url, cs, bbox, time=time, limit=limit)

                    result_dict[provider] = result
                else:
                    for collection in cs:
                        result = cls.stac_get_items(providers_json, collection, bbox, time=time, limit=limit)

                        # add the result to the corresponding collection
                        result_dict[provider][collection] = result
            else:
                raise BadRequest('Unexpected provider: {}'.format(provider))

        return result_dict
