#!/usr/bin/env python3

from json import dumps, loads
from datetime import date, datetime
from requests import get, post
from requests.auth import HTTPBasicAuth
from werkzeug.exceptions import NotFound

from stac_compose.log import logging


class CollectionsServices():

    @classmethod
    def search_items(cls, url, collection_id, query):
        base_url = '{}/collections/{}/items?{}'.format(url, collection_id, query)

        logging.warning('CollectionsServices.search_items() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def search_items_post(cls, url, collection_id, data):
        base_url = '{}/collections/{}/items'.format(url, collection_id)

        logging.warning('CollectionsServices.search_items_post() - base_url: \'POST {}\''.format(base_url))

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
    def search_get(cls, url, query):
        base_url = '{}/stac/search?{}'.format(url, query)

        logging.warning('CollectionsServices.search_get() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def post_stac_search(cls, url, data):
        base_url = '{}/stac/search'.format(url)

        logging.warning('CollectionsServices.search_post() - base_url: \'POST {}\''.format(base_url))

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

        logging.warning('CollectionsServices.search_collections() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        raise NotFound("URL was not found. [ url: {0}, status_code: {1} ]".format(base_url, r.status_code))
