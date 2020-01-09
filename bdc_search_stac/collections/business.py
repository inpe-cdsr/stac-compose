
from pprint import pprint

from werkzeug.exceptions import BadRequest

from bdc_search_stac.collections.services import CollectionsServices
from bdc_search_stac.providers.business import ProvidersBusiness


providers_business = ProvidersBusiness()


class CollectionsBusiness():

    @classmethod
    def get_collections_by_providers(cls, providers):
        result_by_provider = {}

        for p in providers.split(','):
            response = CollectionsServices.search_collections(providers_business.get_providers()[p]['url'])

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
    def search_post(cls, url, collections, bbox, time=False, cloud_cover=False, limit=100):
        result_features = []
        for collection in collections:
            data = {
                'bbox': bbox.split(','),
                'query': {
                    'collections': { 'eq': collection }
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
            
            try:
                response = CollectionsServices.search_post(url, data)
                if not response:
                    continue

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

            except Exception as e:
                continue
        return result_features

    @classmethod
    def search_get(cls, url, collections, bbox, time=None, cloud_cover=None, limit=300):
        query = 'bbox={}'.format(bbox)
        query += '&limit={}'.format(limit)
        query += '&collections={}'.format(','.join(collections))

        if time:
            # range temporal
            query += '&time={}'.format(time)
        if cloud_cover:
            # cloud cover
            query += '&eo:cloud_cover=0/{}'.format(cloud_cover)

        try:
            response = CollectionsServices.search_get(url, query)
            if not response:
                return []

            return response['features'] if response.get('features') else [response]
        except Exception as e:
            return []

    @classmethod
    def search(cls, collections, bbox, cloud_cover=False, time=False, limit=100):
        result_features = []

        providers = list(set([p.split(':')[0] for p in collections.split(',')]))
        for p in providers:
            cs = [c.split(':')[1] for c in collections.split(',') if c.split(':')[0] == p]
            method = providers_business.get_providers_methods()[p]

            if method == 'POST':
                result_features += cls.search_post(providers_business.get_providers()[p]['url'],
                                                               cs, bbox, time, cloud_cover, limit)
            elif method == 'GET':
                result_features += cls.search_get(providers_business.get_providers()[p]['url'],
                                                   cs, bbox, time=time, limit=limit)
            else:
                raise BadRequest('Unexpected provider: {}'.format(p))

        return result_features
