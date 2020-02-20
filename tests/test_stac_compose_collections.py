#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/collections/ endpoint."""

from tests.utils import StacComposeTester

# - http://localhost:8089/stac-compose/collections?providers=INPE-CDSR
# - http://localhost:8089/stac-compose/collections?providers=INPE-CDSR,LANDAST8-SENTINEL2-AWS,CBERS4-AWS

URN = '/stac-compose/collections/'

class TestStacComposeCollections(StacComposeTester):

    def setUp(self):
        self.set_urn(URN)

    def test_get_stac_compose_collections__inpe_cdsr(self):
        expected = {
            "INPE-CDSR": [
                "CBERS4A_MUX_L2_DN",
                "CBERS4A_MUX_L4_DN",
                "CBERS4A_WFI_L2_DN",
                "CBERS4A_WFI_L4_DN",
                "CBERS4A_WPM_L2_DN",
                "CBERS4_AWFI_L4_DN",
                "CBERS4_AWFI_L4_SR",
                "CBERS4_MUX_L2_DN",
                "CBERS4_MUX_L4_DN",
                "CBERS4_MUX_L4_SR",
                "CBERS4_PAN10M_L2_DN",
                "CBERS4_PAN10M_L4_DN",
                "CBERS4_PAN5M_L4_DN",
                "LANDSAT5_TM_L2_DN",
                "LANDSAT5_TM_L4_DN"
            ]
        }

        self.get(expected, query_string={'providers': 'INPE-CDSR'})


class TestStacComposeCollectionsError(StacComposeTester):

    def setUp(self):
        self.set_urn(URN)

    def test_get_stac_compose_collections__400_bad_request__provider_required_field(self):
        expected = {
            'code': 400,
            'message': '{"providers": ["required field"]}'
        }

        self.get(expected, expected_status_code=400)
