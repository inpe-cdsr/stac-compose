
#!/usr/bin/env python3

from pprint import PrettyPrinter
from werkzeug.exceptions import BadRequest

from stac_compose.collections.services import CollectionsServices
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.log import logging


pp = PrettyPrinter(indent=4)

MAX_LIMIT = 1000


def rename_feature_collection(feature_collection):
    """This function renames feature collection keys to leave it according to STAC 9.0 and it is returned"""

    if 'meta' in feature_collection:
        # rename 'meta' key to 'context'
        feature_collection['context'] = feature_collection.pop('meta')

    if 'found' in feature_collection['context']:
        # rename 'found' key to 'matched'
        feature_collection['context']['matched'] = feature_collection['context'].pop('found')

    return feature_collection


def destructuring_dict(d, *args):
    """
    Destructuring a dictionary (i.e. d) into variables

    d (dict): dictionary to destructure
    *args (list): list of arguments to remove from d
    """
    result = [d[arg] if arg in d else None for arg in args]
    if len(result) == 1:
        return result[0]
    else:
        return result


def get_limit_to_search(limit):
    # if 'limit' is less than the maximum I can search, then I can use 'limit' to search my features just one time
    if limit <= MAX_LIMIT:
        return limit
    # if 'limit' is greater than the maximum I can search, then I use the maximum number and I search by pages
    else:
        return MAX_LIMIT


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
            response = CollectionsServices.post_stac_search(url, data)

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
            response = CollectionsServices.search_get(url, query)

            # logging.info('CollectionsBusiness.stac_get() - response: %s', response)

            if not response:
                return []

            return response['features'] if response.get('features') else [response]
        except Exception as e:
            return []

    @classmethod
    def stac_get_items(cls, url, collection, bbox, time=None, cloud_cover=None, limit=300):
        logging.info('CollectionsBusiness.stac_get_items()')

        logging.info('CollectionsBusiness.stac_get_items() - url: %s', url)
        logging.info('CollectionsBusiness.stac_get_items() - collection: %s', collection)

        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)

        if time:
            query += '&time={}'.format(time)
        if cloud_cover:
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        logging.info('CollectionsBusiness.stac_get_items() - query: %s', query)

        try:
            response = CollectionsServices.search_items(url, collection, query)

            # logging.debug('CollectionsBusiness.stac_get_items() - response: %s', response)

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

                    result = rename_feature_collection(result)

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

                            result = rename_feature_collection(result)

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
                        result = cls.stac_get_items(url, collection, bbox, time=time, limit=limit)

                        # add the result to the corresponding collection
                        result_dict[provider][collection] = result
            else:
                raise BadRequest('Unexpected provider: {}'.format(provider))

        return result_dict

    # POST method

    @classmethod
    def post_stac_search(cls, providers_json, collection, bbox, time=False, query=None, page=1, limit=MAX_LIMIT):
        """POST /stac/search"""

        logging.info('CollectionsBusiness.post_stac_search()\n')

        logging.info('CollectionsBusiness.post_stac_search() - providers_json: %s', providers_json)
        logging.info('CollectionsBusiness.post_stac_search() - collection: %s', collection)
        logging.info('CollectionsBusiness.post_stac_search() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.post_stac_search() - time: %s', time)
        logging.info('CollectionsBusiness.post_stac_search() - query: %s', query)
        logging.info('CollectionsBusiness.post_stac_search() - page: %s', page)
        logging.info('CollectionsBusiness.post_stac_search() - limit: %s', limit)

        url = providers_json['url']
        search_collection_as_property = providers_json['search_collection_as_property']

        logging.info('CollectionsBusiness.post_stac_search() - url: %s', url)
        logging.info('CollectionsBusiness.post_stac_search() - search_collection_as_property: %s\n', search_collection_as_property)

        data = {
            "bbox": bbox,
            "time": time,
            "page": page,
            "limit": limit
        }

        if query is not None:
            data["query"] = query

        # if STAC supports just to search collection as property, then add it inside query
        if search_collection_as_property:
            data["query"]["collection"] = {
                "eq": collection
            }
        # else it searchs as STAC standard
        else:
            data["collections"] = [collection]

        logging.info('CollectionsBusiness.post_stac_search() - data: %s\n', data)

        response = CollectionsServices.post_stac_search(url, data)

        # if there is fields to rename, then this function does it
        response = rename_feature_collection(response)

        # logging.debug('CollectionsBusiness.post_stac_search() - response: %s', response)

        return response

    @classmethod
    def post_stac_search_by_pagination(cls, result_by_collection, providers_json, method, collection_name, bbox, time, query, limit, limit_to_search):
        # if there is more results to get, I'm going to search them by pagination
        for page in range(2, int(limit/MAX_LIMIT) + 1):
            logging.info('CollectionsBusiness.search_by_pagination() - page: %s', page)

            if method == "POST":
                __result = cls.post_stac_search(providers_json, collection_name, bbox, time, query, page, limit_to_search)
            else:
                raise BadRequest('Invalid method: {}'.format(method))
            # logging.debug('CollectionsBusiness.search_by_pagination() - result: %s', result)

            # if I'm on other page, then I increase the old result
            result_by_collection['features'] += __result['features']
            result_by_collection['context']['returned'] += __result['context']['returned']

            # logging.debug('CollectionsBusiness.search_by_pagination() - result_by_collection: %s', result_by_collection)

        # get matched variable based on 'result_by_collection['context']['matched']'
        context = result_by_collection['context']
        matched = int(context['matched'])

        logging.info('CollectionsBusiness.search_by_pagination() - matched: %s', matched)
        logging.info('CollectionsBusiness.search_by_pagination() - returned: %s', context['returned'])

        # if something was found, then fill 'limit' key with the true limit
        if matched:
            context['limit'] = limit

        # logging.debug('CollectionsBusiness.search_by_pagination() - result_by_collection: %s', result_by_collection)

        return result_by_collection

    @classmethod
    def post_search(cls, providers, bbox, time, limit=MAX_LIMIT):
        logging.info('CollectionsBusiness.post_search()\n')

        logging.info('CollectionsBusiness.post_search() - MAX_LIMIT: %s\n', MAX_LIMIT)

        logging.info('CollectionsBusiness.post_search() - providers: %s', providers)
        logging.info('CollectionsBusiness.post_search() - bbox: %s', bbox)
        logging.info('CollectionsBusiness.post_search() - time: %s', time)
        logging.info('CollectionsBusiness.post_search() - limit: %s\n', limit)

        result_dict = {}

        for provider in providers:
            logging.info('CollectionsBusiness.post_search() - provider:')

            # destructuring dictionary contents into variables
            provider_name, method, collections, query = destructuring_dict(provider, 'name', 'method', 'collections', 'query')
            providers_json = cls.providers_business.get_providers_json()[provider_name]

            logging.info('CollectionsBusiness.post_search() -   provider_name: %s', provider_name)
            logging.info('CollectionsBusiness.post_search() -   method: %s', method)
            logging.info('CollectionsBusiness.post_search() -   collections: %s', collections)
            logging.info('CollectionsBusiness.post_search() -   query: %s', query)
            logging.info('CollectionsBusiness.post_search() -   providers_json: %s\n', providers_json)

            # if there is not a provider inside the dict, then initialize it
            if provider_name not in result_dict:
                result_dict[provider_name] = {}

            for collection in collections:
                logging.info('CollectionsBusiness.post_search() - collection:')

                collection_name = collection['name']
                logging.info('CollectionsBusiness.post_search() - collection_name: %s', collection_name)

                # initialize collection
                result_by_collection = None

                limit_to_search = get_limit_to_search(limit)

                # if I'm searching by the first, and only one, page [...]
                if method == "POST":
                    result = cls.post_stac_search(providers_json, collection_name, bbox, time, query, 1, limit_to_search)
                else:
                    raise BadRequest('Invalid method: {}'.format(method))

                logging.debug('CollectionsBusiness.post_search() - result: %s', result)

                # [...] then I add it to the dict directly
                result_by_collection = result

                matched = int(result['context']['matched'])
                logging.debug('CollectionsBusiness.post_search() - matched: %s', matched)

                # if I've already got all features, then I go out of the loop
                if limit <= MAX_LIMIT or matched <= MAX_LIMIT:
                    logging.debug('CollectionsBusiness.post_search() - just one result was found')
                # if there is more features to get, then I search by them
                else:
                    logging.debug('CollectionsBusiness.post_search() - more than one result was found')

                    result_by_collection = cls.post_stac_search_by_pagination(
                        result_by_collection, providers_json, method, collection_name, bbox, time, query, limit, limit_to_search
                    )

                # add the found collection to the result
                result_dict[provider_name][collection_name] = result_by_collection

        return result_dict
