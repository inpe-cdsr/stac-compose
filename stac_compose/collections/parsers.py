#!/usr/bin/env python3

from cerberus import Validator
from datetime import datetime
from werkzeug.exceptions import BadRequest

from stac_compose.providers.parsers import validate_providers, providers
from stac_compose.log import logging


def validate_time(__time):
    times = __time.split('/')

    for time in times:
        if time and not datetime.strptime(time, '%Y-%m-%dT%H:%M:%S'):
            # returning None means that '__time' was not coerced, then the following message will be raised, for example:
            # "field 'time' cannot be coerced: time data '2019-12-01' does not match format '%Y-%m-%dT%H:%M:%S'"
            return None

    # returning the original '__time' field means it was coerced (or, in this case, it is still a string)
    return __time


def validate_collections(collections):
    ps = [p.split(':')[0] for p in collections.split(',')]
    if not validate_providers(','.join(ps)):
        return None
    return collections


def validate_bbox(box):
    # GET method
    if isinstance(box, str):
        list_bbox = box.split(',')
        coordinates = [float(b) for b in list_bbox]
        return coordinates if len(coordinates) == 4 else None

    # POST method
    if isinstance(box, list):
        coordinates = box
        return coordinates if len(coordinates) == 4 else None

    return None


# convert_string_to_datetime = lambda date: datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')


convert_string_to_int = lambda string: int(string)


def controller_validation():
    return {
        'providers': {
            'type': 'string', 'empty': False, 'required': True
        }
    }


def search_get():
    return {
        'collections': {
            'type': 'string', 'empty': False, 'required': True,
            'coerce': validate_collections
        },
        'bbox': {
            'type': 'list', 'empty': False, 'required': True,
            'coerce': validate_bbox
        },
        'time': {
            'type': 'string', 'empty': False, 'required': True,
            'coerce': validate_time
        },
        'limit': {
            'type': 'integer', 'empty': False, 'required': True,
            'minlength': 1, 'maxlength': 1000,
            'coerce': convert_string_to_int
        },
        'cloud_cover': {
            'type': 'number', 'empty': False, 'required': False,
            'min': 0, 'max': 100
        },
        'query': {
            'type': 'dict', 'required': False
        }
    }


def search_post():
    return {
        'providers': {
            'type': 'list', 'empty': False, 'required': True,
            'schema': {
                'type': 'dict', 'empty': False, 'required': True,
                'schema': {
                    'name': {'type': 'string', 'empty': False, 'required': True},
                    'method': {'type': 'string', 'empty': False, 'required': True},
                    'collections': {'type': 'list', 'empty': False, 'required': True},
                    'query': {'type': 'dict', 'required': False}
                }
            }
        },
        'bbox': {
            'type': 'list', 'empty': False, 'required': True,
            'minlength': 4, 'maxlength': 4,
            'schema': {
                'type': 'float',
                'empty': False,
                'required': True
            }
        },
        'time': {
            'type': 'string', 'empty': False, 'required': True,
            'coerce': validate_time
        },
        'limit': {
            'type': 'number', 'empty': False, 'required': True,
            'minlength': 1, 'maxlength': 1000
        }
    }


def validate(data, type_schema):
    schema = eval('{}()'.format(type_schema))

    v = Validator(schema)

    if not v.validate(data):
        return v.errors, False

    return v.document, True
