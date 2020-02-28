
#!/usr/bin/env python3

from pprint import PrettyPrinter
from werkzeug.exceptions import BadRequest

from stac_compose.stac.services import StacServices
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.log import logging


pp = PrettyPrinter(indent=4)

MAX_LIMIT = 1000


def rename_fields_from_feature_collection(feature_collection):
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


def add_context_field_in_the_feature_collection_if_it_does_not_exist(feature_collection, page=1, limit=MAX_LIMIT):
    """add `context` field in the feature collection if it does not exist"""

    if 'context' not in feature_collection:
        # if there is not a `context` field in the feature collection, then I create a fake one
        context = {
            'matched': 0,
            'returned': 0,
            'page': page,
            'limit': limit
        }

        if 'features' in feature_collection:
            # create a fake `context` using the size of results returned as 'matched' and 'returned' fields
            returned = len(feature_collection['features'])
            context['matched'] = returned
            context['returned'] = returned

            feature_collection['context'] = context
        else:
            # create a fake `context` using the default one
            feature_collection['context'] = context

    return feature_collection


class StacBusiness():
    providers_business = ProvidersBusiness()

    @classmethod
    def get_stac_search(cls, providers_json, collection, bbox, time, query=None, page=1, limit=MAX_LIMIT):
        """GET /stac/search"""

        logging.info('StacBusiness.get_stac_search()\n')

        logging.info('StacBusiness.get_stac_search() - providers_json: %s', providers_json)
        logging.info('StacBusiness.get_stac_search() - collection: %s', collection)
        logging.info('StacBusiness.get_stac_search() - bbox: %s', bbox)
        logging.info('StacBusiness.get_stac_search() - time: %s', time)
        logging.info('StacBusiness.get_stac_search() - query: %s', query)
        logging.info('StacBusiness.post_stac_sget_stac_searchearch() - page: %s', page)
        logging.info('StacBusiness.get_stac_search() - limit: %s', limit)

        url = providers_json['url']
        search_collection_as_property = providers_json['search_collection_as_property']

        logging.info('StacBusiness.get_stac_search() - url: %s', url)
        logging.info('StacBusiness.get_stac_search() - search_collection_as_property: %s\n', search_collection_as_property)

        parameters = []

        if isinstance(bbox, str):
            parameters.append('bbox={}'.format(bbox))
        elif isinstance(bbox, list):
            bbox = ",".join(list(map(str, bbox)))
            parameters.append('bbox={}'.format(bbox))
        else:
            raise BadRequest('`bbox` field is invalid: `{0}`, it should be a string or list, but its type is {1}.'.format(bbox, type(bbox)))

        parameters.append('collections={}'.format(collection))

        parameters.append('time={}'.format(time))

        # if cloud_cover:
        #     query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        parameters.append('page={}'.format(page))
        parameters.append('limit={}'.format(limit))

        parameters = "&".join(parameters)

        logging.info('StacBusiness.get_stac_search() - parameters: %s', parameters)

        response = StacServices.get_stac_search(url, parameters)

        # post processing to add field and rename other ones if it is necessary
        response = add_context_field_in_the_feature_collection_if_it_does_not_exist(response, page=page, limit=limit)
        response = rename_fields_from_feature_collection(response)

        # logging.info('StacBusiness.get_stac_search() - response: %s', response)

        return response

    @classmethod
    def post_stac_search(cls, providers_json, collection, bbox, time=False, query=None, page=1, limit=MAX_LIMIT):
        """POST /stac/search"""

        logging.info('StacBusiness.post_stac_search()\n')

        logging.info('StacBusiness.post_stac_search() - providers_json: %s', providers_json)
        logging.info('StacBusiness.post_stac_search() - collection: %s', collection)
        logging.info('StacBusiness.post_stac_search() - bbox: %s', bbox)
        logging.info('StacBusiness.post_stac_search() - time: %s', time)
        logging.info('StacBusiness.post_stac_search() - query: %s', query)
        logging.info('StacBusiness.post_stac_search() - page: %s', page)
        logging.info('StacBusiness.post_stac_search() - limit: %s', limit)

        url = providers_json['url']
        search_collection_as_property = providers_json['search_collection_as_property']

        logging.info('StacBusiness.post_stac_search() - url: %s', url)
        logging.info('StacBusiness.post_stac_search() - search_collection_as_property: %s\n', search_collection_as_property)

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

        logging.info('StacBusiness.post_stac_search() - data: %s\n', data)

        response = StacServices.post_stac_search(url, data)

        # post processing to rename fields and add field is it is necessary
        response = add_context_field_in_the_feature_collection_if_it_does_not_exist(response, page=page, limit=limit)
        response = rename_fields_from_feature_collection(response)

        # logging.debug('StacBusiness.post_stac_search() - response: %s', response)

        return response

    @classmethod
    def stac_search_by_pagination(cls, result, providers_json, method, collection_name, bbox, time, query, limit, limit_to_search):
        # if there is more results to get, I'm going to search them by pagination
        for page in range(2, int(limit/MAX_LIMIT) + 1):
            logging.info('StacBusiness.search_by_pagination() - page: %s', page)

            if method == "GET":
                __result = cls.get_stac_search(providers_json, collection_name, bbox, time, query, page, limit_to_search)
            elif method == "POST":
                __result = cls.post_stac_search(providers_json, collection_name, bbox, time, query, page, limit_to_search)
            else:
                raise BadRequest('Invalid method: {}'.format(method))
            # logging.debug('StacBusiness.search_by_pagination() - result: %s', result)

            # if I'm on other page, then I increase the old result
            result['features'] += __result['features']
            result['context']['returned'] += __result['context']['returned']

            # logging.debug('StacBusiness.search_by_pagination() - result: %s', result)

        # get matched variable based on 'result['context']['matched']'
        context = result['context']
        matched = int(context['matched'])

        logging.info('StacBusiness.search_by_pagination() - matched: %s', matched)
        logging.info('StacBusiness.search_by_pagination() - returned: %s', context['returned'])

        # if something was found, then fill 'limit' key with the true limit
        if matched:
            context['limit'] = limit

        # logging.debug('StacBusiness.search_by_pagination() - result: %s', result)

        return result

    @classmethod
    def post_search(cls, providers, bbox, time, limit=MAX_LIMIT):
        logging.info('StacBusiness.post_search()\n')

        logging.info('StacBusiness.post_search() - MAX_LIMIT: %s\n', MAX_LIMIT)

        logging.info('StacBusiness.post_search() - providers: %s', providers)
        logging.info('StacBusiness.post_search() - bbox: %s', bbox)
        logging.info('StacBusiness.post_search() - time: %s', time)
        logging.info('StacBusiness.post_search() - limit: %s\n', limit)

        result_dict = {}

        for provider in providers:
            logging.info('StacBusiness.post_search() - provider:')

            # destructuring dictionary contents into variables
            provider_name, method, collections, query = destructuring_dict(provider, 'name', 'method', 'collections', 'query')
            providers_json = cls.providers_business.get_providers_json()[provider_name]

            logging.info('StacBusiness.post_search() -   provider_name: %s', provider_name)
            logging.info('StacBusiness.post_search() -   method: %s', method)
            logging.info('StacBusiness.post_search() -   collections: %s', collections)
            logging.info('StacBusiness.post_search() -   query: %s', query)
            logging.info('StacBusiness.post_search() -   providers_json: %s\n', providers_json)

            # if there is not a provider inside the dict, then initialize it
            if provider_name not in result_dict:
                result_dict[provider_name] = {}

            for collection in collections:
                logging.info('StacBusiness.post_search() - collection:')

                collection_name = collection['name']
                logging.info('StacBusiness.post_search() - collection_name: %s', collection_name)

                limit_to_search = get_limit_to_search(limit)

                # if I'm searching by the first, and only one, page
                if method == "GET":
                    result = cls.get_stac_search(providers_json, collection_name, bbox, time, query, 1, limit_to_search)
                elif method == "POST":
                    result = cls.post_stac_search(providers_json, collection_name, bbox, time, query, 1, limit_to_search)
                else:
                    raise BadRequest('Invalid method: {}'.format(method))

                # logging.debug('StacBusiness.post_search() - result: %s', result)

                matched = result['context']['matched']

                logging.debug('StacBusiness.post_search() - matched: %s', matched)

                # if I've already got all features, then I go out of the loop
                if limit <= MAX_LIMIT or matched <= MAX_LIMIT:
                    logging.debug('StacBusiness.post_search() - just one result was found')
                # if there is more features to get, then I search by them
                else:
                    logging.debug('StacBusiness.post_search() - more than one result was found')

                    result = cls.stac_search_by_pagination(
                        result, providers_json, method, collection_name, bbox, time, query, limit, limit_to_search
                    )

                # add the found collection to the result
                result_dict[provider_name][collection_name] = result

        return result_dict
