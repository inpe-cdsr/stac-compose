#!/usr/bin/env python3

from flask import Blueprint
from flask_restplus import Api

from stac_compose.collections.controller import api as collections_ns
from stac_compose.stac.controller import api as stac_ns
from stac_compose.providers.controller import api as providers_ns
from stac_compose.status.controller import api as status_ns

blueprint = Blueprint('stac-compose', __name__, url_prefix='/stac-compose')

api = Api(blueprint, doc=False)

api.add_namespace(collections_ns)
api.add_namespace(stac_ns)
api.add_namespace(providers_ns)
api.add_namespace(status_ns)
