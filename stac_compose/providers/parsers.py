#!/usr/bin/env python3

from cerberus import Validator
from datetime import datetime

from stac_compose.providers.business import ProvidersBusiness


def validate_providers(providers):
    providers_business = ProvidersBusiness()

    providers_keys = providers_business.get_providers().keys()

    for p in providers.split(','):
        if p not in providers_keys:
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
