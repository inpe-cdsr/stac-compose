#!/usr/bin/env python3

from cerberus import Validator
from datetime import datetime

from bdc_search_stac.providers.parsers import validate_providers, providers
from bdc_search_stac.log import logging


def validate_date(s):
    dates = s.split("/")
    for date in dates:
        if date.split('T')[0] and not datetime.strptime(date.split('T')[0], '%Y-%m-%d'):
            return None
    return s


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


def validate_cloud(cloud):
    cloud = float(cloud)
    return cloud if cloud >= 0 and cloud <= 100 else None


def validate_limit(limit):
    limit = int(limit)
    return limit if limit > 0 else None


def search():
    base = {
        'collections': {"type": "string", "coerce": validate_collections, "empty": False, "required": True},
        'bbox': {"type": "list", "coerce": validate_bbox, "empty": False, "required": True},
        'cloud_cover': {"type": "number", "coerce": validate_cloud, "empty": True, "required": False},
        'time': {"type": "string", "coerce": validate_date, "empty": True, "required": False},
        'limit': {"type": "number", "coerce": validate_limit, "empty": True, "required": False},
        'query': {"type": "dict", "required": False}
    }
    return base


def validate(data, type_schema):
    schema = eval('{}()'.format(type_schema))

    v = Validator(schema)

    if not v.validate(data):
        return v.errors, False

    return data, True
