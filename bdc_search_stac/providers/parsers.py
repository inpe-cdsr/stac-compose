#!/usr/bin/env python3

from cerberus import Validator
from datetime import datetime

from bdc_search_stac.providers.business import ProvidersBusiness


providers_business = ProvidersBusiness()


def validate_providers(providers):
    bdc_providers = providers_business.get_providers().keys()

    for p in providers.split(','):
        if p not in bdc_providers:
            return None

    return providers.split(',')


def providers():
    return {
        'providers': {"type": "list", "coerce": validate_providers, "empty": False, "required": True}
    }


def validate(data, type_schema):
    schema = eval('{}()'.format(type_schema))

    v = Validator(schema)

    if not v.validate(data):
        return v.errors, False

    return data, True
