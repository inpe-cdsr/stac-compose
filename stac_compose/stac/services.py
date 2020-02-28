#!/usr/bin/env python3

from json import dumps, loads
from requests import get, post

from stac_compose.log import logging


class StacServices():

    @classmethod
    def get_stac_search(cls, url, query):
        """GEt /stac/search"""

        base_url = '{}/stac/search?{}'.format(url, query)

        logging.warning('StacServices.get_stac_search() - base_url: \'GET {}\''.format(base_url))

        r = get(base_url, headers={})

        if r and r.status_code in (200, 201):
            return loads(r.text)

        return None

    @classmethod
    def post_stac_search(cls, url, data):
        """POST /stac/search"""

        base_url = '{}/stac/search'.format(url)

        logging.warning('StacServices.search_post() - base_url: \'POST {}\''.format(base_url))

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
