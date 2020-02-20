#!/usr/bin/env python3

import os
from flask import Flask
from flask_cors import CORS

from stac_compose.blueprint import blueprint
from stac_compose.config import get_settings

def create_app(config):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)
        app.register_blueprint(blueprint)

    return app

app = create_app(get_settings(os.environ.get('ENVIRONMENT', 'DevelopmentConfig')))

CORS(app, resources={r'/d/*': {"origins": '*'}})
