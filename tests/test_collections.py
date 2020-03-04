#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/collections/ endpoint."""

from json import load

from tests.utils import StacComposeTester


URN_collections = '/stac-compose/collections/'


class TestStacComposeCollections(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections)

    def test__get__stac_compose_collections__inpe_cdsr(self):
        """http://localhost:8089/stac-compose/collections/?providers=INPE-CDSR"""

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

    def test__get__stac_compose_collections__landsat8_sentinel2_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=LANDSAT8-SENTINEL2-AWS"""

        expected = {
            "LANDSAT8-SENTINEL2-AWS": [
                "landsat-8-l1",
                "sentinel-2-l1c"
            ]
        }

        self.get(expected, query_string={'providers': 'LANDSAT8-SENTINEL2-AWS'})

    def test__get__stac_compose_collections__cbers4_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=CBERS4-AWS"""

        expected = {
            "CBERS4-AWS": [
                "CBERS4MUX",
                "CBERS4AWFI",
                "CBERS4PAN10M",
                "CBERS4PAN5M"
            ]
        }

        self.get(expected, query_string={'providers': 'CBERS4-AWS'})

    def test__get__stac_compose_collections__inpe_cdsr_and_landsat8_sentinel2_aws_and_cbers4_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=INPE-CDSR,LANDSAT8-SENTINEL2-AWS,CBERS4-AWS"""

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
            ],
            "LANDSAT8-SENTINEL2-AWS": [
                "landsat-8-l1",
                "sentinel-2-l1c"
            ],
            "CBERS4-AWS": [
                "CBERS4MUX",
                "CBERS4AWFI",
                "CBERS4PAN10M",
                "CBERS4PAN5M"
            ]
        }

        self.get(expected, query_string={'providers': 'INPE-CDSR,LANDSAT8-SENTINEL2-AWS,CBERS4-AWS'})


class TestStacComposeCollectionsError(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections)

    def test__get__stac_compose_collections__400_bad_request__provider_required_field(self):
        """http://localhost:8089/stac-compose/collections/"""

        expected = {
            'code': 400,
            'description': '{"providers": ["required field"]}',
            'name': 'Bad Request'
        }

        self.get(expected, expected_status_code=400)
