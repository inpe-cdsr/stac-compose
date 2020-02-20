#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/providers/ endpoint."""

from unittest import TestCase
from json import loads

from stac_compose import app as stac_compose_app


class StacComposeTester(TestCase):

    def setUp(self):
        self.app = stac_compose_app.test_client()

    def get_stac_compose_providers(self):
        return self.app.get('/stac-compose/providers/')

    def test_get_stac_compose_providers(self, expected):
        result = self.get_stac_compose_providers()

        self.assertEqual(200, result.status_code)
        self.assertIn('application/json', result.content_type)
        self.assertEqual(expected, loads(result.data))
