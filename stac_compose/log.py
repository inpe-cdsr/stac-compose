#!/usr/bin/env python3

import logging

from stac_compose.environment import LOGGING_LEVEL


logging.basicConfig(format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s', level=LOGGING_LEVEL)
