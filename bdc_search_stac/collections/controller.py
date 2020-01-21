#!/usr/bin/env python3

import os, json
from flask import request
from werkzeug.exceptions import InternalServerError, BadRequest
from werkzeug.datastructures import ImmutableMultiDict

from bdc_search_stac.collections import ns
from bdc_search_stac.collections.business import CollectionsBusiness
from bdc_search_stac.collections.parsers import validate
from bdc_core.utils.flask import APIResource

from bdc_search_stac.log import logging


api = ns


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
        - http://localhost:8089/stac-compose/collections/items?collections=INPE-CDSR:CB4A_MUX_L2_DN,INPE-CDSR:CB4A_WFI_L2_DN,LANDAST8-SENTINEL2-AWS:landsat-8-l1,CBERS4-AWS:CBERS4AWFI,BRAZILDATACUBE:C64mMEDIAN&bbox=-72.1114203679271,-28.76765910569124,-37.911404889445116,0.6591651462894632&time=2019-09-07T00:00:00/2020-01-21T23:59:00&limit=10000
        - http://localhost:8089/stac-compose/collections/items?collections=CBERS4-AWS:CBERS4AWFI,BRAZILDATACUBE:C64mMEDIAN&bbox=-72.1114203679271,-28.76765910569124,-37.911404889445116,0.6591651462894632&time=2019-09-07T00:00:00/2020-01-21T23:59:00&limit=10000
    """

    def get(self):
        data, status = validate(request.args.to_dict(flat=True), 'search')

        if status is False:
            raise BadRequest(json.dumps(data))  # 400 - Bad Request

        # Search RF in STAC's
        features = CollectionsBusiness.search(**request.args)

        return {
            "meta": {
                "found": len(features)
            },
            "features": features
        }
