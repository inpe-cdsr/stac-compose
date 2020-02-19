#!/usr/bin/env python3

import os, json

from flask import request
from werkzeug.exceptions import InternalServerError, BadRequest
from werkzeug.datastructures import ImmutableMultiDict
from pprint import PrettyPrinter

from bdc_search_stac.collections import ns
from bdc_search_stac.collections.business import CollectionsBusiness
from bdc_search_stac.collections.parsers import validate
from bdc_core.utils.flask import APIResource
from bdc_search_stac.log import logging


api = ns

pp = PrettyPrinter(indent=4)


@api.route('/')
class ItemsController(APIResource):
    """
    Examples of full route:
        - http://localhost:8089/stac-compose/collections?providers=INPE-CDSR
        - http://localhost:8089/stac-compose/collections?providers=INPE-CDSR,LANDAST8-SENTINEL2-AWS,CBERS4-AWS,BRAZILDATACUBE
    """

    def get(self):
        args = request.args.to_dict(flat=True)

        # logging.debug('logging debug: args: %s', args)

        data, status = validate(args, 'providers')

        if status is False:
            raise BadRequest(json.dumps(data))  # 400 - Bad Request

        # List of STAC collections by providers
        return CollectionsBusiness.get_collections_by_providers(data['providers'])


@api.route('/items')
class CollectionsController(APIResource):
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
