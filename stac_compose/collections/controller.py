#!/usr/bin/env python3

from json import dumps

from flask import request
from werkzeug.exceptions import BadRequest
from pprint import PrettyPrinter

from bdc_core.utils.flask import APIResource

from stac_compose.collections import ns
from stac_compose.collections.business import CollectionsBusiness
from stac_compose.collections.parsers import validate
from stac_compose.log import logging


api = ns

pp = PrettyPrinter(indent=4)


@api.route('/')
class CollectionsController(APIResource):
    """CollectionsController"""

    def get(self):
        args = request.args.to_dict(flat=True)

        logging.info('CollectionsController.get() - args: %s', args)

        data, status = validate(args, 'providers')

        logging.info('CollectionsController.get() - data: %s', data)
        logging.info('CollectionsController.get() - status: %s', status)

        if status is False:
            raise BadRequest(dumps(data))  # 400 - Bad Request

        # List of STAC collections by providers
        return CollectionsBusiness.get_collections_by_providers(args['providers'])


@api.route('/items/')
class CollectionsItemsController(APIResource):
    """CollectionsItemsController"""

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

    def post(self):
        logging.info('CollectionsItemsController.post()\n')

        if request.is_json:
            body = request.get_json()

            logging.info('CollectionsItemsController.post() - body: %s', body)

            data, status = validate(body, 'search_post')

            logging.info('CollectionsItemsController.post() - data: %s', data)
            logging.info('CollectionsItemsController.post() - status: %s', status)

            if status is False:
                raise BadRequest(dumps(data))  # 400 - Bad Request

            features = CollectionsBusiness.search_post(**data)

            # logging.debug('\n\n CollectionsItemsController.post() - features: %s \n\n', features)
            # pp.pprint(features)

            return features
        else:
            raise BadRequest("POST Request must be an application/json")
