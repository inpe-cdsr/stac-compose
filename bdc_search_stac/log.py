#!/usr/bin/env python3

import logging

from bdc_search_stac.environment import LOGGING_LEVEL


logging.basicConfig(format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s', level=LOGGING_LEVEL)
