#!/usr/bin/env python3

from json import dumps, loads
from requests import get, post
from werkzeug.exceptions import NotFound

from stac_compose.log import logging


class StacComposeServices():

    @classmethod
    def get_collections_collection_id_items(cls, url, collection_id, query):
        """GET /collections/{collection_id}/items"""

        logging.warning('StacComposeServices.get_collections_collection_id_items()\n')

        base_url = '{}/collections/{}/items?{}'.format(url, collection_id, query)

        logging.warning('StacComposeServices.get_collections_collection_id_items() - base_url: \'GET {}\'\n'.format(base_url))

        response = get(base_url, headers={})

        logging.warning('StacComposeServices.get_collections_collection_id_items() - response.status_code: {}'.format(response.status_code))
        # logging.warning('StacComposeServices.get_collections_collection_id_items() - response.text: {}'.format(response.text))
        # logging.warning('StacComposeServices.get_collections_collection_id_items() - loads(response.text): {}\n'.format(loads(response.text)))

        if response and response.status_code in (200, 201):
            return loads(response.text)

        return None

    @classmethod
    def post_collections_collection_id_items(cls, url, collection_id, data):
        """POST /collections/{collection_id}/items"""

        logging.warning('StacComposeServices.post_collections_collection_id_items()\n')

        base_url = '{}/collections/{}/items'.format(url, collection_id)

        logging.warning('StacComposeServices.post_collections_collection_id_items() - base_url: \'POST {}\''.format(base_url))

        r = post(
            base_url,
            headers={
                'Content-Type': 'application/json'
            },
            data=dumps(data)
        )

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def get_stac_search(cls, url, query):
        base_url = '{}/stac/search?{}'.format(url, query)

        logging.warning('StacComposeServices.get_stac_search() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def post_stac_search(cls, url, data):
        """POST /stac/search"""

        base_url = '{}/stac/search'.format(url)

        logging.warning('StacComposeServices.search_post() - base_url: \'POST {}\''.format(base_url))

        r = post(
            base_url,
            headers={
                'Content-Type': 'application/json'
            },
            data=dumps(data)
        )

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def search_collections(cls, url):
        base_url = '{}/collections?limit=1000'.format(url)

        logging.warning('StacComposeServices.search_collections() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        raise NotFound("URL was not found. [ url: {0}, status_code: {1} ]".format(base_url, r.status_code))
