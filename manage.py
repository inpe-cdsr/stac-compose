#!/usr/bin/env python3

from flask_script import Manager

from bdc_search_stac import app
from bdc_search_stac.environment import SERVER_HOST, SERVER_PORT, DEBUG_MODE

manager = Manager(app)

@manager.command
def run():
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE)

if __name__ == '__main__':
    manager.run()