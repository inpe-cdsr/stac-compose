#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/status/ endpoint."""

from tests.utils import StacComposeTester


class TestStacComposeStatus(StacComposeTester):

    def setUp(self):
        self.set_urn('/stac-compose/status/')

    def test__get__stac_compose_status(self):
        """http://localhost:8089/stac-compose/status/"""

        expected = {
            "status": "Running"
        }

        self.get(expected)
