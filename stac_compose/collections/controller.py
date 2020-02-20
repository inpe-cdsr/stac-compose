#!/usr/bin/env python3

import os, json

from flask import request
from werkzeug.exceptions import InternalServerError, BadRequest
from werkzeug.datastructures import ImmutableMultiDict
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
            raise BadRequest(json.dumps(data))  # 400 - Bad Request

        # List of STAC collections by providers
        return CollectionsBusiness.get_collections_by_providers(args['providers'])


@api.route('/items')
class CollectionsItemsController(APIResource):
    """
    Example of full route:
        - collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c and limit=10:
            http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=10

        - collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1 and limit=10:
            http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=10

        - collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1 and limit=2000
            http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=2000
    """

    def get(self):
        logging.info('CollectionsController.get() - request.args: %s', request.args)

        data, status = validate(request.args.to_dict(flat=True), 'search')

        logging.info('CollectionsController.get() - data: %s', data)
        logging.info('CollectionsController.get() - status: %s', status)

        if status is False:
            raise BadRequest(json.dumps(data))  # 400 - Bad Request

        features = CollectionsBusiness.search(**request.args)

        # logging.debug('\nCollectionsController.get() - features: %s \n\n', features)
        # pp.pprint(features)

        return features

    # def post(self):
    # {
    #     "collections": "INPE-CDSR:CBERS4_AWFI_L4_DN",
    #     "bbox": [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
    #     "time": "2019-12-22T00:00:00/2020-01-22T23:59:00",
    #     "limit": 2,
    #     "query": {
    #         "cloud_cover": {
    #             "gte": 30,
    #             "lte": 60
    #         }
    #     }
    # }
    #     if request.is_json:
    #         request_json = request.get_json()

    #         logging.info('CollectionsController.post() - request_json: %s', request_json)

    #         data, status = validate(request_json, 'search')

    #         logging.info('CollectionsController.post() - data: %s', data)
    #         logging.info('CollectionsController.post() - status: %s', status)

    #         if status is False:
    #             raise BadRequest(json.dumps(data))  # 400 - Bad Request

    #         features = CollectionsBusiness.search(**request_json)

    #         # logging.debug('\nCollectionsController.post() - features: %s \n\n', features)
    #         # pp.pprint(features)

    #         return features
    #     else:
    #         raise BadRequest("POST Request must be an application/json")
