#!/usr/bin/env python3

from json import load

from requests import get
from requests.exceptions import ConnectionError
# from pprint import pprint

from stac_compose.config import BASE_DIR
from stac_compose.log import logging


def is_url_valid(url):
    url = url + '/stac'

    try:
        r = get(url, headers={})
    except ConnectionError:
        logging.warning('Failed to establish a new connection with \'GET {}\''.format(url))
        return False

    if r and r.status_code in (200, 201):
        return True

    return False


class ProvidersBusiness():

    def __init__(self):
        data = None

        with open('{}/providers/static/providers.json'.format(BASE_DIR)) as p:
            data = load(p)

        self.__providers__ = {}
        self.__versions__ = {}
        self.__method__ = {}
        self.__require_credentials__ = {}
        self.__downloadable__ = {}
        self.__filter_mult_collection__ = {}

        self.__objs__ = {}

        for key in data.keys():
            url = data[key]['url']
            ignore_provider_validation = data[key]['ignore_provider_validation']

            # 'ignore_provider_validation' flag indicates if this provider can be validated or not,
            # because 'inpe-stac' is slow to run, then it cannot be validated when docker compose is executed
            if ignore_provider_validation:
                logging.info('Ignored validation of provider: \'{}\''.format(url))

            # if STAC URL is not valid, then ignore this provider, it cannot be returned
            elif not is_url_valid(url):
                logging.warning('Invalid provider: \'{}\''.format(url))
                continue

            self.__providers__[key] = url
            self.__versions__[key] = data[key]['version']
            self.__method__[key] = data[key]['method']
            self.__require_credentials__[key] = data[key]['require_credentials']
            self.__downloadable__[key] = data[key]['downloadable']
            self.__filter_mult_collection__[key] = data[key]['filter_mult_collection']

            self.__objs__[key] = {
                "url": url,
                "require_credentials": data[key]['require_credentials'],
                "downloadable": data[key]['downloadable']
            }

    def get_providers(self):
        return self.__objs__

    def get_providers_version(self):
        return self.__versions__

    def get_providers_methods(self):
        return self.__method__

    def get_require_credentials(self):
        return self.__require_credentials__

    def get_downloadable(self):
        return self.__downloadable__

    def get_filter_mult_collection(self):
        return self.__filter_mult_collection__
