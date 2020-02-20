#!/usr/bin/env python3

import os, json
from flask import request

from bdc_core.utils.flask import APIResource

from stac_compose.providers import ns
from stac_compose.providers.business import ProvidersBusiness
from stac_compose.providers.parsers import validate


api = ns


@api.route('/')
class ProviderController(APIResource):
    """
    Full route: http://localhost:8089/stac-compose/providers/
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
