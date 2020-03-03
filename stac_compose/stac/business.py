
#!/usr/bin/env python3

from pprint import PrettyPrinter
from werkzeug.exceptions import BadRequest
from copy import deepcopy

from stac_compose.common import MAX_LIMIT, rename_fields_from_feature_collection, destructuring_dict, \
                                get_limit_to_search, add_context_field_in_the_feature_collection_if_it_does_not_exist
from stac_compose.services import StacComposeServices
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.log import logging

from stac_compose.collections.business import CollectionsBusiness


pp = PrettyPrinter(indent=4)


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

        response = StacComposeServices.get_stac_search(url, parameters)

        # post processing to add field and rename other ones if it is necessary
        response = add_context_field_in_the_feature_collection_if_it_does_not_exist(response, page=page, limit=limit)
        response = rename_fields_from_feature_collection(response)

        # logging.info('StacBusiness.get_stac_search() - response: %s', response)

        return response

    @classmethod
    def post_stac_search(cls, providers_json, collections, bbox, time=False, query=None, page=1, limit=MAX_LIMIT):
        """POST /stac/search"""

        logging.info('StacBusiness.post_stac_search()\n')

        logging.info('StacBusiness.post_stac_search() - providers_json: %s', providers_json)
        logging.info('StacBusiness.post_stac_search() - collections: %s', collections)
        logging.info('StacBusiness.post_stac_search() - type(collections): %s', type(collections))
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

        # if `collections` is a list of collection, then I join all collections to send them
        if isinstance(collections, list):
            # `collections` is something like this `[{"name": "CBERS4_AWFI_L4_DN"}, ...]``
            # then the `map` function returns a list of collections (strings), for example: `['CBERS4_AWFI_L4_DN', ...]`
            # thus the `join` function joins the list of strings

            # data["collections"] = ','.join(list(map(lambda c: c['name'], collections)))
            data["collections"] = list(map(lambda c: c['name'], collections))

        # if `collections` is a string, in other words, is just one collection, then I just send it
        elif isinstance(collections, str):

            # if STAC supports just to search collection as property, then add it inside query
            if search_collection_as_property:
                # if `data` does not have `query` field, then initialize it
                if "query" not in data:
                    data["query"] = {}

                data["query"]["collection"] = {
                    "eq": collections
                }
            # else it searchs as STAC standard
            else:
                data["collections"] = [collections]

        else:
            raise BadRequest('`collections` must be instance of `list` or `str`.')

        logging.info('StacBusiness.post_stac_search() - data: %s\n', data)

        response = StacComposeServices.post_stac_search(url, data)

        # logging.debug('StacBusiness.post_stac_search() - \n\n(1) response: %s\n\n', response)

        # post processing to rename fields and add field is it is necessary
        response = add_context_field_in_the_feature_collection_if_it_does_not_exist(response, page=page, limit=limit)
        response = rename_fields_from_feature_collection(response)

        # logging.info('StacBusiness.post_stac_search() - \n\n(2) response: %s\n\n', response)

        return response

    @classmethod
    def stac_search(cls, method, providers_json, collections, bbox, time=False, query=None, page=1, limit=MAX_LIMIT):
        if method == "GET":
            # return cls.get_stac_search(providers_json, collections, bbox, time, query=query, page=1, limit=limit)
            return CollectionsBusiness.stac_get_items(providers_json, collections, bbox, time=time, limit=limit)
        elif method == "POST":
            return cls.post_stac_search(providers_json, collections, bbox, time, query=query, page=1, limit=limit)
        else:
            raise BadRequest('Invalid method: {}'.format(method))

    @classmethod
    def stac_search_by_pagination(cls, result, method, providers_json, collection_name, bbox, time, query, limit, limit_to_search):
        # if there is more results to get, I'm going to search them by pagination
        for page in range(2, int(limit/MAX_LIMIT) + 1):
            logging.info('StacBusiness.stac_search_by_pagination() - page: %s', page)

            __result = cls.stac_search(method, providers_json, collection_name, bbox, time, query, page, limit_to_search)
            # logging.info('StacBusiness.stac_search_by_pagination() - __result: %s', __result)

            # if I'm on other page, then I increase the old result
            result['features'] += __result['features']
            result['context']['returned'] += __result['context']['returned']

            # logging.info('StacBusiness.stac_search_by_pagination() - __result: %s', __result)

        # get matched variable based on 'result['context']['matched']'
        context = result['context']
        matched = int(context['matched'])

        logging.info('StacBusiness.stac_search_by_pagination() - matched: %s', matched)
        logging.info('StacBusiness.stac_search_by_pagination() - returned: %s', context['returned'])

        # if something was found, then fill 'limit' key with the true limit
        if matched:
            context['limit'] = limit

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

            if providers_json['filter_mult_collection']:
                logging.info('StacBusiness.post_search() - filter_mult_collection == True\n')

                limit_to_search = get_limit_to_search(limit)

                feature_collection = cls.stac_search(method, providers_json, collections, bbox, time, query, 1, limit_to_search)
                # logging.info('StacBusiness.post_search() - feature_collection: %s', feature_collection)

                logging.info('StacBusiness.post_search() - matched: %s', feature_collection['context']['matched'])

                metadata_related_to_collections = feature_collection['context'].pop('meta')

                logging.info('StacBusiness.post_search() - metadata_related_to_collections: %s', metadata_related_to_collections)

                features = feature_collection.pop('features')

                logging.info('StacBusiness.post_search() - collections:')
                for collection in collections:
                    collection_name = collection['name']
                    logging.info('StacBusiness.post_search() -     collection_name: %s', collection_name)

                    result = list(filter(lambda f: f['collection'] == collection_name, features))
                    metadata = list(filter(lambda f: f['name'] == collection_name, metadata_related_to_collections))

                    logging.info('StacBusiness.post_search() - metadata: %s', metadata)

                    fc_structure = deepcopy(feature_collection)
                    fc_structure['features'] = result
                    fc_structure['context']['matched'] = metadata[0]['context']['matched']
                    fc_structure['context']['returned'] = metadata[0]['context']['returned']

                    # add the found collection to the result
                    result_dict[provider_name][collection_name] = fc_structure

            else:
                logging.info('StacBusiness.post_search() - filter_mult_collection == False\n')
                logging.info('StacBusiness.post_search() - collections:')
                for collection in collections:
                    collection_name = collection['name']
                    logging.info('StacBusiness.post_search() -     collection_name: %s', collection_name)

                    limit_to_search = get_limit_to_search(limit)

                    # first: I'm searching by the first page
                    result = cls.stac_search(method, providers_json, collection_name, bbox, time, query, 1, limit_to_search)
                    # logging.info('StacBusiness.post_search() - result: %s', result)

                    matched = result['context']['matched']

                    logging.info('StacBusiness.post_search() - matched: %s', matched)

                    # if I've already got all features, then I go out of the loop
                    if limit <= MAX_LIMIT or matched <= MAX_LIMIT:
                        logging.info('StacBusiness.post_search() - just one result was found')
                    # if there is more features to get, then I search by them
                    else:
                        logging.info('StacBusiness.post_search() - more than one result was found')

                        result = cls.stac_search_by_pagination(
                            result, method, providers_json, collection_name, bbox, time, query, limit, limit_to_search
                        )

                    # add the found collection to the result
                    result_dict[provider_name][collection_name] = result

        # logging.debug('StacBusiness.post_search() - result_dict: %s', result_dict)

        return result_dict
