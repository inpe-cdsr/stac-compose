#!/usr/bin/env python3

from json import dumps

from flask import request
from werkzeug.exceptions import BadRequest
from pprint import PrettyPrinter

from bdc_core.utils.flask import APIResource

from stac_compose.decorator import catch_generic_exceptions
from stac_compose.log import logging
from stac_compose.stac import ns
from stac_compose.stac.business import StacBusiness
from stac_compose.stac.parsers import validate


api = ns

pp = PrettyPrinter(indent=4)


@api.route('/search/')
class StacSearchController(APIResource):
    """StacSearchController"""

    @catch_generic_exceptions
    def post(self):
        logging.info('StacBusiness.post()')

        if request.is_json:
            body = request.get_json()

            logging.info('StacBusiness.post() - body: %s', body)

            data, status = validate(body, 'search_post')

            logging.info('StacBusiness.post() - data: %s', data)
            logging.info('StacBusiness.post() - status: %s', status)

            if status is False:
                raise BadRequest(dumps(data))  # 400 - Bad Request

            features = StacBusiness.post_search(**data)

            # logging.debug('\n\n StacBusiness.post() - features: %s \n\n', features)
            # pp.pprint(features)

            return features
        else:
            raise BadRequest("mimetype must indicate JSON data, in other words, mimetype must be equals to `application/json`")
