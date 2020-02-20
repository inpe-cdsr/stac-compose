#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/providers/ endpoint."""

from unittest import TestCase
from json import loads

from stac_compose import app as stac_compose_app


class TestStacComposeProviders(TestCase):

    def setUp(self):
        self.app = stac_compose_app.test_client()

    def test_get_stac_compose_providers(self):
        expected = {
            "providers": {
                "INPE-CDSR": {
                    "url": "http://localhost:8089/inpe-stac",
                    "require_credentials": 1,
                    "downloadable": 1
                },
                "LANDAST8-SENTINEL2-AWS": {
                    "url": "https://sat-api.developmentseed.org",
                    "require_credentials": 0,
                    "downloadable": 0
                },
                "CBERS4-AWS": {
                    "url": "https://stac.amskepler.com/v07",
                    "require_credentials": 0,
                    "downloadable": 0
                }
            }
        }
        result = self.app.get('/stac-compose/providers/')

        self.assertEqual(200, result.status_code)
        self.assertIn('application/json', result.content_type)
        self.assertEqual(expected, loads(result.data))
