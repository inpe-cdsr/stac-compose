
from json import load
# from pprint import pprint

from bdc_search_stac.config import BASE_DIR


class ProvidersBusiness():

    def __init__(self):
        data = None

        with open('{}/providers/static/providers.json'.format(BASE_DIR)) as p:
            data = load(p)

        self.__providers__ = {}

        for key in data.keys():
            self.__providers__[key] = data[key]['url']

    def get_providers(self):
        return self.__providers__
