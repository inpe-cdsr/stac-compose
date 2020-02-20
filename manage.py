#!/usr/bin/env python3

from flask_script import Manager

from stac_compose import app
from stac_compose.environment import SERVER_HOST, SERVER_PORT, DEBUG_MODE

manager = Manager(app)

@manager.command
def run():
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG_MODE)

if __name__ == '__main__':
    manager.run()