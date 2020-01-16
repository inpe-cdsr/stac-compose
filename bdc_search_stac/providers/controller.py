#!/usr/bin/env python3

import os, json
from flask import request

from bdc_search_stac.providers import ns
from bdc_search_stac.providers.business import ProvidersBusiness
from bdc_search_stac.providers.parsers import validate
from bdc_core.utils.flask import APIResource

api = ns

@api.route('/')
class ProviderController(APIResource):
    """
    Full route: http://localhost:5000/stac-compose/providers/
    """

    providers_business = ProvidersBusiness()

    def get(self):
        """
        List of STAC providers
        """

        providers = {
            "providers": self.providers_business.get_providers()
        }

        return providers
