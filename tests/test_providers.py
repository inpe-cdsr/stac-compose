#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/providers/ endpoint."""

from tests.utils import StacComposeTester


class TestStacComposeProviders(StacComposeTester):

    def setUp(self):
        self.set_urn('/stac-compose/providers/')

    def test__get__stac_compose_providers(self):
        """http://localhost:8089/stac-compose/providers/"""

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

        self.get(expected)
