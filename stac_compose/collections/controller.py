#!/usr/bin/env python3

from json import dumps

from flask import request
from werkzeug.exceptions import BadRequest
from pprint import PrettyPrinter

from bdc_core.utils.flask import APIResource

from stac_compose.decorator import catch_generic_exceptions
from stac_compose.log import logging
from stac_compose.collections import ns
from stac_compose.collections.business import CollectionsBusiness
from stac_compose.collections.parsers import validate


api = ns

pp = PrettyPrinter(indent=4)


@api.route('/')
class CollectionsController(APIResource):
    """CollectionsController"""

    @catch_generic_exceptions
    def get(self):
        logging.info('CollectionsController.get()')

        args = request.args.to_dict(flat=True)

        logging.info('CollectionsController.get() - args: %s', args)

        data, status = validate(args, 'controller_validation')

        logging.info('CollectionsController.get() - data: %s', data)
        logging.info('CollectionsController.get() - status: %s', status)

        if status is False:
            raise BadRequest(dumps(data))  # 400 - Bad Request

        # List of STAC collections by providers
        return CollectionsBusiness.get_collections_by_providers(args['providers'].split(','))


@api.route('/items/')
class CollectionsItemsController(APIResource):
    """CollectionsItemsController"""

    @catch_generic_exceptions
    def get(self):
        args = request.args.to_dict(flat=True)

        logging.info('CollectionsItemsController.get() - args: %s', args)

        data, status = validate(args, 'search_get')

        logging.info('CollectionsItemsController.get() - data: %s', data)
        logging.info('CollectionsItemsController.get() - status: %s', status)

        if status is False:
            raise BadRequest(dumps(data))  # 400 - Bad Request

        features = CollectionsBusiness.search_get(**request.args)

        # logging.debug('\n\nCollectionsItemsController.get() - features: %s \n\n', features)
        # pp.pprint(features)

        return features
