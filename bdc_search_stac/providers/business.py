
from json import load
# from pprint import pprint

from bdc_search_stac.config import BASE_DIR


class ProvidersBusiness():

    def __init__(self):
        data = None

        with open('{}/providers/static/providers.json'.format(BASE_DIR)) as p:
            data = load(p)

        self.__providers__ = {}
        self.__versions__ = {}
        self.__method__ = {}

        for key in data.keys():
            self.__providers__[key] = data[key]['url']
            self.__versions__[key] = data[key]['version']
            self.__method__[key] = data[key]['method']

    def get_providers(self):
        return self.__providers__

    def get_providers_version(self):
        return self.__versions__
    
    def get_providers_methods(self):
        return self.__method__
