
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
        self.__require_credentials__ = {}
        self.__downloadable__ = {}

        self.__objs__ = {}

        for key in data.keys():
            self.__providers__[key] = data[key]['url']
            self.__versions__[key] = data[key]['version']
            self.__method__[key] = data[key]['method']
            self.__require_credentials__[key] = data[key]['require_credentials']
            self.__downloadable__[key] = data[key]['downloadable']

            self.__objs__[key] = {
                "url": data[key]['url'],
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
