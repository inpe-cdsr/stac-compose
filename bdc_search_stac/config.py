#!/usr/bin/env python3

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def get_settings(env):
    return eval(env)


class Config():
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False


class ProductionConfig(Config):
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    # DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True

