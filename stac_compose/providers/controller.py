#!/usr/bin/env python3

from bdc_core.utils.flask import APIResource

from stac_compose.providers import ns
from stac_compose.providers.business import ProvidersBusiness
# from stac_compose.providers.parsers import validate


api = ns


@api.route('/')
class ProviderController(APIResource):
    """ProviderController"""

    providers_business = ProvidersBusiness()

    def get(self):
        """List of STAC providers"""

        return {
            "providers": self.providers_business.get_providers()
        }
