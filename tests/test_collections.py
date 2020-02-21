#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/collections/ endpoint."""

from json import load

from tests.utils import StacComposeTester


URN_collections = '/stac-compose/collections/'
URN_collections_items = '/stac-compose/collections/items/'


class TestStacComposeCollections(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections)

    def test_get_stac_compose_collections__inpe_cdsr(self):
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

    def test_get_stac_compose_collections__landsat8_sentinel2_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=LANDAST8-SENTINEL2-AWS"""

        expected = {
            "LANDAST8-SENTINEL2-AWS": [
                "landsat-8-l1",
                "sentinel-2-l1c"
            ]
        }

        self.get(expected, query_string={'providers': 'LANDAST8-SENTINEL2-AWS'})

    def test_get_stac_compose_collections__cbers4_aws(self):
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

    def test_get_stac_compose_collections__inpe_cdsr_and_landsat8_sentinel2_aws_and_cbers4_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=INPE-CDSR,LANDAST8-SENTINEL2-AWS,CBERS4-AWS"""

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
            "LANDAST8-SENTINEL2-AWS": [
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

        self.get(expected, query_string={'providers': 'INPE-CDSR,LANDAST8-SENTINEL2-AWS,CBERS4-AWS'})


class TestStacComposeCollectionsError(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections)

    def test_get_stac_compose_collections__400_bad_request__provider_required_field(self):
        """http://localhost:8089/stac-compose/collections/"""

        expected = {
            'code': 400,
            'message': '{"providers": ["required field"]}'
        }

        self.get(expected, expected_status_code=400)


class TestStacComposeCollectionsItems(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections_items)

    def test_get_stac_compose_collections_items__landsat8_sentinel2_aws_sentinel_2_l1c_limit_2(self):
        """
        http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=2
        """

        expected = {
            "LANDAST8-SENTINEL2-AWS": {
                "sentinel-2-l1c": {
                    "type": "FeatureCollection",
                    "meta": {
                        "page": 1,
                        "limit": 2,
                        "found": 10675,
                        "returned": 2
                    },
                    "features": [
                        {
                            "type": "Feature",
                            "id": "S2A_19JEN_20200213_0",
                            "bbox": [
                                -69.00018891115606,
                                -25.405044731652644,
                                -67.9085796253574,
                                -24.40956510234512
                            ],
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -69.00018891115606,
                                            -25.405044731652644
                                        ],
                                        [
                                            -69.00018740722889,
                                            -24.413436938906102
                                        ],
                                        [
                                            -67.91726637780653,
                                            -24.40956510234512
                                        ],
                                        [
                                            -67.9085796253574,
                                            -25.400994146447758
                                        ],
                                        [
                                            -69.00018891115606,
                                            -25.405044731652644
                                        ]
                                    ]
                                ]
                            },
                            "properties": {
                                "collection": "sentinel-2-l1c",
                                "eo:gsd": 10,
                                "eo:instrument": "MSI",
                                "eo:off_nadir": 0,
                                "eo:bands": [
                                    {
                                        "full_width_half_max": 0.027,
                                        "center_wavelength": 0.4439,
                                        "name": "B01",
                                        "gsd": 60,
                                        "common_name": "coastal"
                                    },
                                    {
                                        "full_width_half_max": 0.098,
                                        "center_wavelength": 0.4966,
                                        "name": "B02",
                                        "gsd": 10,
                                        "common_name": "blue"
                                    },
                                    {
                                        "full_width_half_max": 0.045,
                                        "center_wavelength": 0.56,
                                        "name": "B03",
                                        "gsd": 10,
                                        "common_name": "green"
                                    },
                                    {
                                        "full_width_half_max": 0.038,
                                        "center_wavelength": 0.6645,
                                        "name": "B04",
                                        "gsd": 10,
                                        "common_name": "red"
                                    },
                                    {
                                        "full_width_half_max": 0.019,
                                        "center_wavelength": 0.7039,
                                        "name": "B05",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.018,
                                        "center_wavelength": 0.7402,
                                        "name": "B06",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.028,
                                        "center_wavelength": 0.7825,
                                        "name": "B07",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.145,
                                        "center_wavelength": 0.8351,
                                        "name": "B08",
                                        "gsd": 10,
                                        "common_name": "nir"
                                    },
                                    {
                                        "full_width_half_max": 0.033,
                                        "center_wavelength": 0.8648,
                                        "name": "B8A",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.026,
                                        "center_wavelength": 0.945,
                                        "name": "B09",
                                        "gsd": 60
                                    },
                                    {
                                        "full_width_half_max": 0.075,
                                        "center_wavelength": 1.3735,
                                        "name": "B10",
                                        "gsd": 60,
                                        "common_name": "cirrus"
                                    },
                                    {
                                        "full_width_half_max": 0.143,
                                        "center_wavelength": 1.6137,
                                        "name": "B11",
                                        "gsd": 20,
                                        "common_name": "swir16"
                                    },
                                    {
                                        "full_width_half_max": 0.242,
                                        "center_wavelength": 2.22024,
                                        "name": "B12",
                                        "gsd": 20,
                                        "common_name": "swir22"
                                    }
                                ],
                                "datetime": "2020-02-13T14:49:40.049000+00:00",
                                "eo:platform": "sentinel-2a",
                                "eo:cloud_cover": 28.13,
                                "sentinel:utm_zone": 19,
                                "sentinel:latitude_band": "J",
                                "sentinel:grid_square": "EN",
                                "sentinel:sequence": "0",
                                "sentinel:product_id": "S2A_MSIL1C_20200213T143721_N0209_R096_T19JEN_20200213T180805"
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/EN/2020/2/13/0/preview.jpg"
                                },
                                "info": {
                                    "title": "Basic JSON metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/EN/2020/2/13/0/tileInfo.json"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/EN/2020/2/13/0/metadata.xml"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/TKI.jp2"
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B01.jp2"
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B02.jp2"
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B03.jp2"
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B04.jp2"
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B05.jp2"
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B06.jp2"
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B07.jp2"
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B08.jp2"
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B08.jp2"
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B09.jp2"
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B10.jp2"
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B11.jp2"
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/EN/2020/2/13/0/B11.jp2"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items/S2A_19JEN_20200213_0"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "collection",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                }
                            ]
                        },
                        {
                            "type": "Feature",
                            "id": "S2A_19JFN_20200213_0",
                            "bbox": [
                                -68.01369356393954,
                                -25.401683501450417,
                                -67.28980250350575,
                                -24.403777159128175
                            ],
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -68.00578012056987,
                                            -25.401683501450417
                                        ],
                                        [
                                            -68.01369356393954,
                                            -24.41022403751015
                                        ],
                                        [
                                            -67.28980250350575,
                                            -24.403777159128175
                                        ],
                                        [
                                            -67.44916956613386,
                                            -25.074618981435503
                                        ],
                                        [
                                            -67.48916902620348,
                                            -25.23965943697605
                                        ],
                                        [
                                            -67.5280060914807,
                                            -25.397676775149883
                                        ],
                                        [
                                            -68.00578012056987,
                                            -25.401683501450417
                                        ]
                                    ]
                                ]
                            },
                            "properties": {
                                "collection": "sentinel-2-l1c",
                                "eo:gsd": 10,
                                "eo:instrument": "MSI",
                                "eo:off_nadir": 0,
                                "eo:bands": [
                                    {
                                        "full_width_half_max": 0.027,
                                        "center_wavelength": 0.4439,
                                        "name": "B01",
                                        "gsd": 60,
                                        "common_name": "coastal"
                                    },
                                    {
                                        "full_width_half_max": 0.098,
                                        "center_wavelength": 0.4966,
                                        "name": "B02",
                                        "gsd": 10,
                                        "common_name": "blue"
                                    },
                                    {
                                        "full_width_half_max": 0.045,
                                        "center_wavelength": 0.56,
                                        "name": "B03",
                                        "gsd": 10,
                                        "common_name": "green"
                                    },
                                    {
                                        "full_width_half_max": 0.038,
                                        "center_wavelength": 0.6645,
                                        "name": "B04",
                                        "gsd": 10,
                                        "common_name": "red"
                                    },
                                    {
                                        "full_width_half_max": 0.019,
                                        "center_wavelength": 0.7039,
                                        "name": "B05",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.018,
                                        "center_wavelength": 0.7402,
                                        "name": "B06",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.028,
                                        "center_wavelength": 0.7825,
                                        "name": "B07",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.145,
                                        "center_wavelength": 0.8351,
                                        "name": "B08",
                                        "gsd": 10,
                                        "common_name": "nir"
                                    },
                                    {
                                        "full_width_half_max": 0.033,
                                        "center_wavelength": 0.8648,
                                        "name": "B8A",
                                        "gsd": 20
                                    },
                                    {
                                        "full_width_half_max": 0.026,
                                        "center_wavelength": 0.945,
                                        "name": "B09",
                                        "gsd": 60
                                    },
                                    {
                                        "full_width_half_max": 0.075,
                                        "center_wavelength": 1.3735,
                                        "name": "B10",
                                        "gsd": 60,
                                        "common_name": "cirrus"
                                    },
                                    {
                                        "full_width_half_max": 0.143,
                                        "center_wavelength": 1.6137,
                                        "name": "B11",
                                        "gsd": 20,
                                        "common_name": "swir16"
                                    },
                                    {
                                        "full_width_half_max": 0.242,
                                        "center_wavelength": 2.22024,
                                        "name": "B12",
                                        "gsd": 20,
                                        "common_name": "swir22"
                                    }
                                ],
                                "datetime": "2020-02-13T14:49:36.500000+00:00",
                                "eo:platform": "sentinel-2a",
                                "eo:cloud_cover": 27.66,
                                "sentinel:utm_zone": 19,
                                "sentinel:latitude_band": "J",
                                "sentinel:grid_square": "FN",
                                "sentinel:sequence": "0",
                                "sentinel:product_id": "S2A_MSIL1C_20200213T143721_N0209_R096_T19JFN_20200213T180805"
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/FN/2020/2/13/0/preview.jpg"
                                },
                                "info": {
                                    "title": "Basic JSON metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/FN/2020/2/13/0/tileInfo.json"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/J/FN/2020/2/13/0/metadata.xml"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/TKI.jp2"
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B01.jp2"
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B02.jp2"
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B03.jp2"
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B04.jp2"
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B05.jp2"
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B06.jp2"
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B07.jp2"
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B08.jp2"
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B08.jp2"
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B09.jp2"
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B10.jp2"
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B11.jp2"
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/J/FN/2020/2/13/0/B11.jp2"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items/S2A_19JFN_20200213_0"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "collection",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                }
                            ]
                        }
                    ],
                    "links": [
                        {
                            "rel": "next",
                            "title": "Next page of results",
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2020-01-13T00%3A00%3A00%2F2020-02-13T23%3A59%3A00&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=2"
                        }
                    ]
                }
            }
        }

        query_string = {
            'collections': 'LANDAST8-SENTINEL2-AWS:sentinel-2-l1c',
            'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
            'time': '2020-01-13T00:00:00/2020-02-13T23:59:00',
            'limit': 2
        }

        self.get(expected, query_string=query_string)

    '''
    # this test is commented, because it is slow
    def test_get_stac_compose_collections_items__landsat8_sentinel2_aws_sentinel_2_l1c_limit_2000(self):
        """
        http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=2000
        """

        with open('tests/json/collections_items_landsat8_sentinel2_aws_sentinel_2_l1c_limit_2000.json') as json_file:
            # this is a big 'expected', then I load it from a file
            expected = load(json_file)

            query_string = {
                'collections': 'LANDAST8-SENTINEL2-AWS:sentinel-2-l1c',
                'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
                'time': '2020-01-13T00:00:00/2020-02-13T23:59:00',
                'limit': 2000
            }

            data = self.get(expected, query_string=query_string)

            self.assertIn('LANDAST8-SENTINEL2-AWS', data)
            self.assertIn('sentinel-2-l1c', data['LANDAST8-SENTINEL2-AWS'])
            self.assertIn('meta', data['LANDAST8-SENTINEL2-AWS']['sentinel-2-l1c'])

            context = data['LANDAST8-SENTINEL2-AWS']['sentinel-2-l1c']['meta']

            self.assertEqual(1, context['page'])
            self.assertEqual(2000, context['limit'])
            self.assertEqual(2000, context['returned'])
    '''

    # def test_get_stac_compose_collections_items__landsat8_sentinel2_aws_sentinel_2_l1c_limit_2(self):
    #     """
    #     - collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c and limit=10:
    #         http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=10
    #     """

    #     expected = {}

    #     query_string = {
    #         'collections': 'LANDAST8-SENTINEL2-AWS:sentinel-2-l1c',
    #         'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
    #         'time': '2020-01-13T00:00:00/2020-02-13T23:59:00',
    #         'limit': 2
    #     }

    #     self.get(expected, query_string=query_string)
