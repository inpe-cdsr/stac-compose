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
            "providers": [
                {
                    "title": "INPE-CDSR",
                    "collections": [
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_MUX_L2_DN",
                            "title": "CBERS4A_MUX_L2_DN",
                            "description": "CBERS4A MUX Level2 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -66.4038,
                                    -79.9447,
                                    68.6192,
                                    22.637
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-24"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_MUX_L4_DN",
                            "title": "CBERS4A_MUX_L4_DN",
                            "description": "CBERS4A MUX Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -36.1653,
                                    -71.7135,
                                    -12.1405,
                                    -41.6252
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-19"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WFI_L2_DN",
                            "title": "CBERS4A_WFI_L2_DN",
                            "description": "CBERS4A WFI Level2 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -68.6431,
                                    -85.8382,
                                    71.2034,
                                    179.939
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-24"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WFI_L4_DN",
                            "title": "CBERS4A_WFI_L4_DN",
                            "description": "CBERS4A WFI Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -38.1472,
                                    -80.0226,
                                    8.24979,
                                    -32.8996
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-19"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WPM_L2_DN",
                            "title": "CBERS4A_WPM_L2_DN",
                            "description": "CBERS4A WPM Level2 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -66.4318,
                                    -179.957,
                                    68.5559,
                                    179.905
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-03-03"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L2_DN",
                            "title": "CBERS4_AWFI_L2_DN",
                            "description": "CBERS4 AWFI Level2 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -24.4895,
                                    -43.7924,
                                    -16.3034,
                                    -33.683
                                ],
                                "temporal": [
                                    "2018-10-15",
                                    "2018-10-15"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L4_DN",
                            "title": "CBERS4_AWFI_L4_DN",
                            "description": "CBERS4 AWFI Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -45.485,
                                    -82.6242,
                                    21.3355,
                                    55.6045
                                ],
                                "temporal": [
                                    "2016-06-25",
                                    "2020-02-28"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L4_SR",
                            "title": "CBERS4_AWFI_L4_SR",
                            "description": "CBERS4 AWFI Level4 SR dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -46.6432,
                                    -84.468,
                                    37.194,
                                    57.5331
                                ],
                                "temporal": [
                                    "2016-05-01",
                                    "2020-02-29"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L2_DN",
                            "title": "CBERS4_MUX_L2_DN",
                            "description": "CBERS4 MUX Level2 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -70.1442,
                                    -78.5953,
                                    19.4539,
                                    44.9192
                                ],
                                "temporal": [
                                    "2019-12-03",
                                    "2019-12-31"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L4_DN",
                            "title": "CBERS4_MUX_L4_DN",
                            "description": "CBERS4 MUX Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -39.0394,
                                    -78.3893,
                                    19.4595,
                                    45.551
                                ],
                                "temporal": [
                                    "2017-11-09",
                                    "2019-12-31"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L4_SR",
                            "title": "CBERS4_MUX_L4_SR",
                            "description": "CBERS4 MUX Level4 SR dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -39.0349,
                                    -79.3662,
                                    19.4346,
                                    43.8284
                                ],
                                "temporal": [
                                    "2017-01-26",
                                    "2019-12-03"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_PAN10M_L4_DN",
                            "title": "CBERS4_PAN10M_L4_DN",
                            "description": "CBERS4 PAN10M Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -38.9142,
                                    -78.3449,
                                    7.80108,
                                    -34.4983
                                ],
                                "temporal": [
                                    "2017-07-11",
                                    "2019-12-31"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_PAN5M_L4_DN",
                            "title": "CBERS4_PAN5M_L4_DN",
                            "description": "CBERS4 PAN5M Level4 DN dataset",
                            "license": None,
                            "properties": {},
                            "extent": {
                                "spatial": [
                                    -6.7861,
                                    -50.4667,
                                    -5.63506,
                                    -49.6963
                                ],
                                "temporal": [
                                    "2017-07-11",
                                    "2017-07-11"
                                ]
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        self.get(expected, query_string={'providers': 'INPE-CDSR'})

    def test__get__stac_compose_collections__landsat8_sentinel2_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=LANDSAT8-SENTINEL2-AWS"""

        expected = {
            "providers": [
                {
                    "title": "LANDSAT8-SENTINEL2-AWS",
                    "collections": [
                        {
                            "id": "landsat-8-l1",
                            "title": "Landsat 8 L1",
                            "description": "Landat 8 imagery radiometrically calibrated and orthorectified using gound points and Digital Elevation Model (DEM) data to correct relief displacement.",
                            "keywords": [
                                "landsat",
                                "earth observation",
                                "usgs"
                            ],
                            "version": "0.1.0",
                            "stac_version": "0.6.0",
                            "extent": {
                                "spatial": [
                                    -180,
                                    -90,
                                    180,
                                    90
                                ],
                                "temporal": [
                                    "2013-06-01",
                                    None
                                ]
                            },
                            "providers": [
                                {
                                    "name": "USGS",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "https://landsat.usgs.gov/"
                                },
                                {
                                    "name": "Planet Labs",
                                    "roles": [
                                        "processor"
                                    ],
                                    "url": "https://github.com/landsat-pds/landsat_ingestor"
                                },
                                {
                                    "name": "AWS",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://landsatonaws.com/"
                                },
                                {
                                    "name": "Development Seed",
                                    "roles": [
                                        "processor"
                                    ],
                                    "url": "https://github.com/sat-utils/sat-api"
                                }
                            ],
                            "license": "PDDL-1.0",
                            "properties": {
                                "collection": "landsat-8-l1",
                                "eo:gsd": 15,
                                "eo:platform": "landsat-8",
                                "eo:instrument": "OLI_TIRS",
                                "eo:off_nadir": 0,
                                "eo:bands": [
                                    {
                                        "name": "B1",
                                        "common_name": "coastal",
                                        "gsd": 30,
                                        "center_wavelength": 0.44,
                                        "full_width_half_max": 0.02
                                    },
                                    {
                                        "name": "B2",
                                        "common_name": "blue",
                                        "gsd": 30,
                                        "center_wavelength": 0.48,
                                        "full_width_half_max": 0.06
                                    },
                                    {
                                        "name": "B3",
                                        "common_name": "green",
                                        "gsd": 30,
                                        "center_wavelength": 0.56,
                                        "full_width_half_max": 0.06
                                    },
                                    {
                                        "name": "B4",
                                        "common_name": "red",
                                        "gsd": 30,
                                        "center_wavelength": 0.65,
                                        "full_width_half_max": 0.04
                                    },
                                    {
                                        "name": "B5",
                                        "common_name": "nir",
                                        "gsd": 30,
                                        "center_wavelength": 0.86,
                                        "full_width_half_max": 0.03
                                    },
                                    {
                                        "name": "B6",
                                        "common_name": "swir16",
                                        "gsd": 30,
                                        "center_wavelength": 1.6,
                                        "full_width_half_max": 0.08
                                    },
                                    {
                                        "name": "B7",
                                        "common_name": "swir22",
                                        "gsd": 30,
                                        "center_wavelength": 2.2,
                                        "full_width_half_max": 0.2
                                    },
                                    {
                                        "name": "B8",
                                        "common_name": "pan",
                                        "gsd": 15,
                                        "center_wavelength": 0.59,
                                        "full_width_half_max": 0.18
                                    },
                                    {
                                        "name": "B9",
                                        "common_name": "cirrus",
                                        "gsd": 30,
                                        "center_wavelength": 1.37,
                                        "full_width_half_max": 0.02
                                    },
                                    {
                                        "name": "B10",
                                        "common_name": "lwir11",
                                        "gsd": 100,
                                        "center_wavelength": 10.9,
                                        "full_width_half_max": 0.8
                                    },
                                    {
                                        "name": "B11",
                                        "common_name": "lwir12",
                                        "gsd": 100,
                                        "center_wavelength": 12,
                                        "full_width_half_max": 1
                                    }
                                ]
                            },
                            "assets": {
                                "index": {
                                    "type": "text/html",
                                    "title": "HTML index page"
                                },
                                "thumbnail": {
                                    "title": "Thumbnail image",
                                    "type": "image/jpeg"
                                },
                                "B1": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        0
                                    ],
                                    "title": "Band 1 (coastal)"
                                },
                                "B2": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        1
                                    ],
                                    "title": "Band 2 (blue)"
                                },
                                "B3": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        2
                                    ],
                                    "title": "Band 3 (green)"
                                },
                                "B4": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        3
                                    ],
                                    "title": "Band 4 (red)"
                                },
                                "B5": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        4
                                    ],
                                    "title": "Band 5 (nir)"
                                },
                                "B6": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        5
                                    ],
                                    "title": "Band 6 (swir16)"
                                },
                                "B7": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        6
                                    ],
                                    "title": "Band 7 (swir22)"
                                },
                                "B8": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        7
                                    ],
                                    "title": "Band 8 (pan)"
                                },
                                "B9": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        8
                                    ],
                                    "title": "Band 9 (cirrus)"
                                },
                                "B10": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        9
                                    ],
                                    "title": "Band 10 (lwir)"
                                },
                                "B11": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        10
                                    ],
                                    "title": "Band 11 (lwir)"
                                },
                                "ANG": {
                                    "title": "Angle coefficients file",
                                    "type": "text/plain"
                                },
                                "MTL": {
                                    "title": "original metadata file",
                                    "type": "text/plain"
                                },
                                "BQA": {
                                    "title": "Band quality data",
                                    "type": "image/x.geotiff"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1/items"
                                }
                            ]
                        },
                        {
                            "id": "sentinel-2-l1c",
                            "title": "Sentinel 2 L1C",
                            "description": "Sentinel-2a and Sentinel-2b imagery",
                            "keywords": [
                                "sentinel",
                                "earth observation",
                                "esa"
                            ],
                            "version": "0.1.0",
                            "stac_version": "0.6.0",
                            "extent": {
                                "spatial": [
                                    -180,
                                    -90,
                                    180,
                                    90
                                ],
                                "temporal": [
                                    "2013-06-01",
                                    None
                                ]
                            },
                            "providers": [
                                {
                                    "roles": [
                                        "producer"
                                    ],
                                    "name": "ESA",
                                    "url": "https://earth.esa.int/web/guest/home"
                                },
                                {
                                    "roles": [
                                        "processor"
                                    ],
                                    "name": "Sinergise",
                                    "url": "https://registry.opendata.aws/sentinel-2/"
                                },
                                {
                                    "roles": [
                                        "host"
                                    ],
                                    "name": "AWS",
                                    "url": "http://sentinel-pds.s3-website.eu-central-1.amazonaws.com/"
                                },
                                {
                                    "roles": [
                                        "processor"
                                    ],
                                    "name": "Development Seed",
                                    "url": "https://github.com/sat-utils/sat-stac-sentinel"
                                }
                            ],
                            "license": "proprietary",
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
                                ]
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail"
                                },
                                "info": {
                                    "title": "Basic JSON metadata"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ]
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ]
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ]
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ]
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ]
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ]
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ]
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ]
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ]
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ]
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ]
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ]
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items"
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        self.get(expected, query_string={'providers': 'LANDSAT8-SENTINEL2-AWS'})

    def test__get__stac_compose_collections__cbers4_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=CBERS4-AWS"""

        expected = {
            "providers": [
                {
                    "title": "CBERS4-AWS",
                    "collections": [
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4MUX",
                            "description": "CBERS4 MUX camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4MUX"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4MUX/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 20,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "MUX",
                                "eo:bands": [
                                    {
                                        "name": "B5",
                                        "common_name": "blue"
                                    },
                                    {
                                        "name": "B6",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B7",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B8",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4AWFI",
                            "description": "CBERS4 AWFI camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4AWFI"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4AWFI/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 64,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "AWFI",
                                "eo:bands": [
                                    {
                                        "name": "B13",
                                        "common_name": "blue"
                                    },
                                    {
                                        "name": "B14",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B15",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B16",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4PAN10M",
                            "description": "CBERS4 PAN10M camera catalog",
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN10M"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN10M/items"
                                }
                            ],
                            "properties": {
                                "eo:gsd": 10,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "PAN10M",
                                "eo:bands": [
                                    {
                                        "name": "B2",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B3",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B4",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4PAN5M",
                            "description": "CBERS4 PAN5M camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN5M"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN5M/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 5,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "PAN5M",
                                "eo:bands": [
                                    {
                                        "name": "B1",
                                        "common_name": "pan"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }

        self.get(expected, query_string={'providers': 'CBERS4-AWS'})

    def test__get__stac_compose_collections__inpe_cdsr_and_landsat8_sentinel2_aws_and_cbers4_aws(self):
        """http://localhost:8089/stac-compose/collections/?providers=INPE-CDSR,LANDSAT8-SENTINEL2-AWS,CBERS4-AWS"""

        expected = {
            "providers": [
                {
                    "title": "INPE-CDSR",
                    "collections": [
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_MUX_L2_DN",
                            "title": "CBERS4A_MUX_L2_DN",
                            "description": "CBERS4A MUX Level2 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -66.4038,
                                    -79.9447,
                                    68.6192,
                                    22.637
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-24"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_MUX_L4_DN",
                            "title": "CBERS4A_MUX_L4_DN",
                            "description": "CBERS4A MUX Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -36.1653,
                                    -71.7135,
                                    -12.1405,
                                    -41.6252
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-19"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_MUX_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WFI_L2_DN",
                            "title": "CBERS4A_WFI_L2_DN",
                            "description": "CBERS4A WFI Level2 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -68.6431,
                                    -85.8382,
                                    71.2034,
                                    179.939
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-24"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WFI_L4_DN",
                            "title": "CBERS4A_WFI_L4_DN",
                            "description": "CBERS4A WFI Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -38.1472,
                                    -80.0226,
                                    8.24979,
                                    -32.8996
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-02-19"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4A_WPM_L2_DN",
                            "title": "CBERS4A_WPM_L2_DN",
                            "description": "CBERS4A WPM Level2 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -66.4318,
                                    -179.957,
                                    68.5559,
                                    179.905
                                ],
                                "temporal": [
                                    "2019-12-27",
                                    "2020-03-03"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L2_DN",
                            "title": "CBERS4_AWFI_L2_DN",
                            "description": "CBERS4 AWFI Level2 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -24.4895,
                                    -43.7924,
                                    -16.3034,
                                    -33.683
                                ],
                                "temporal": [
                                    "2018-10-15",
                                    "2018-10-15"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L4_DN",
                            "title": "CBERS4_AWFI_L4_DN",
                            "description": "CBERS4 AWFI Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -45.485,
                                    -82.6242,
                                    21.3355,
                                    55.6045
                                ],
                                "temporal": [
                                    "2016-06-25",
                                    "2020-02-28"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_AWFI_L4_SR",
                            "title": "CBERS4_AWFI_L4_SR",
                            "description": "CBERS4 AWFI Level4 SR dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -46.6432,
                                    -84.468,
                                    37.194,
                                    57.5331
                                ],
                                "temporal": [
                                    "2016-05-01",
                                    "2020-02-29"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_SR/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L2_DN",
                            "title": "CBERS4_MUX_L2_DN",
                            "description": "CBERS4 MUX Level2 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -70.1442,
                                    -78.5953,
                                    19.4539,
                                    44.9192
                                ],
                                "temporal": [
                                    "2019-12-03",
                                    "2019-12-31"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L2_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L4_DN",
                            "title": "CBERS4_MUX_L4_DN",
                            "description": "CBERS4 MUX Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -39.0394,
                                    -78.3893,
                                    19.4595,
                                    45.551
                                ],
                                "temporal": [
                                    "2017-11-09",
                                    "2019-12-31"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_MUX_L4_SR",
                            "title": "CBERS4_MUX_L4_SR",
                            "description": "CBERS4 MUX Level4 SR dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -39.0349,
                                    -79.3662,
                                    19.4346,
                                    43.8284
                                ],
                                "temporal": [
                                    "2017-01-26",
                                    "2019-12-03"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_MUX_L4_SR/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_PAN10M_L4_DN",
                            "title": "CBERS4_PAN10M_L4_DN",
                            "description": "CBERS4 PAN10M Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -38.9142,
                                    -78.3449,
                                    7.80108,
                                    -34.4983
                                ],
                                "temporal": [
                                    "2017-07-11",
                                    "2019-12-31"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        },
                        {
                            "stac_version": "0.7",
                            "id": "CBERS4_PAN5M_L4_DN",
                            "title": "CBERS4_PAN5M_L4_DN",
                            "description": "CBERS4 PAN5M Level4 DN dataset",
                            "license": None,
                            "extent": {
                                "spatial": [
                                    -6.7861,
                                    -50.4667,
                                    -5.63506,
                                    -49.6963
                                ],
                                "temporal": [
                                    "2017-07-11",
                                    "2017-07-11"
                                ]
                            },
                            "properties": {},
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN5M_L4_DN/items",
                                    "rel": "items"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections",
                                    "rel": "root"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "LANDSAT8-SENTINEL2-AWS",
                    "collections": [
                        {
                            "id": "landsat-8-l1",
                            "title": "Landsat 8 L1",
                            "description": "Landat 8 imagery radiometrically calibrated and orthorectified using gound points and Digital Elevation Model (DEM) data to correct relief displacement.",
                            "keywords": [
                                "landsat",
                                "earth observation",
                                "usgs"
                            ],
                            "version": "0.1.0",
                            "stac_version": "0.6.0",
                            "extent": {
                                "spatial": [
                                    -180,
                                    -90,
                                    180,
                                    90
                                ],
                                "temporal": [
                                    "2013-06-01",
                                    None
                                ]
                            },
                            "providers": [
                                {
                                    "name": "USGS",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "https://landsat.usgs.gov/"
                                },
                                {
                                    "name": "Planet Labs",
                                    "roles": [
                                        "processor"
                                    ],
                                    "url": "https://github.com/landsat-pds/landsat_ingestor"
                                },
                                {
                                    "name": "AWS",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://landsatonaws.com/"
                                },
                                {
                                    "name": "Development Seed",
                                    "roles": [
                                        "processor"
                                    ],
                                    "url": "https://github.com/sat-utils/sat-api"
                                }
                            ],
                            "license": "PDDL-1.0",
                            "properties": {
                                "collection": "landsat-8-l1",
                                "eo:gsd": 15,
                                "eo:platform": "landsat-8",
                                "eo:instrument": "OLI_TIRS",
                                "eo:off_nadir": 0,
                                "eo:bands": [
                                    {
                                        "name": "B1",
                                        "common_name": "coastal",
                                        "gsd": 30,
                                        "center_wavelength": 0.44,
                                        "full_width_half_max": 0.02
                                    },
                                    {
                                        "name": "B2",
                                        "common_name": "blue",
                                        "gsd": 30,
                                        "center_wavelength": 0.48,
                                        "full_width_half_max": 0.06
                                    },
                                    {
                                        "name": "B3",
                                        "common_name": "green",
                                        "gsd": 30,
                                        "center_wavelength": 0.56,
                                        "full_width_half_max": 0.06
                                    },
                                    {
                                        "name": "B4",
                                        "common_name": "red",
                                        "gsd": 30,
                                        "center_wavelength": 0.65,
                                        "full_width_half_max": 0.04
                                    },
                                    {
                                        "name": "B5",
                                        "common_name": "nir",
                                        "gsd": 30,
                                        "center_wavelength": 0.86,
                                        "full_width_half_max": 0.03
                                    },
                                    {
                                        "name": "B6",
                                        "common_name": "swir16",
                                        "gsd": 30,
                                        "center_wavelength": 1.6,
                                        "full_width_half_max": 0.08
                                    },
                                    {
                                        "name": "B7",
                                        "common_name": "swir22",
                                        "gsd": 30,
                                        "center_wavelength": 2.2,
                                        "full_width_half_max": 0.2
                                    },
                                    {
                                        "name": "B8",
                                        "common_name": "pan",
                                        "gsd": 15,
                                        "center_wavelength": 0.59,
                                        "full_width_half_max": 0.18
                                    },
                                    {
                                        "name": "B9",
                                        "common_name": "cirrus",
                                        "gsd": 30,
                                        "center_wavelength": 1.37,
                                        "full_width_half_max": 0.02
                                    },
                                    {
                                        "name": "B10",
                                        "common_name": "lwir11",
                                        "gsd": 100,
                                        "center_wavelength": 10.9,
                                        "full_width_half_max": 0.8
                                    },
                                    {
                                        "name": "B11",
                                        "common_name": "lwir12",
                                        "gsd": 100,
                                        "center_wavelength": 12,
                                        "full_width_half_max": 1
                                    }
                                ]
                            },
                            "assets": {
                                "index": {
                                    "type": "text/html",
                                    "title": "HTML index page"
                                },
                                "thumbnail": {
                                    "title": "Thumbnail image",
                                    "type": "image/jpeg"
                                },
                                "B1": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        0
                                    ],
                                    "title": "Band 1 (coastal)"
                                },
                                "B2": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        1
                                    ],
                                    "title": "Band 2 (blue)"
                                },
                                "B3": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        2
                                    ],
                                    "title": "Band 3 (green)"
                                },
                                "B4": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        3
                                    ],
                                    "title": "Band 4 (red)"
                                },
                                "B5": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        4
                                    ],
                                    "title": "Band 5 (nir)"
                                },
                                "B6": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        5
                                    ],
                                    "title": "Band 6 (swir16)"
                                },
                                "B7": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        6
                                    ],
                                    "title": "Band 7 (swir22)"
                                },
                                "B8": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        7
                                    ],
                                    "title": "Band 8 (pan)"
                                },
                                "B9": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        8
                                    ],
                                    "title": "Band 9 (cirrus)"
                                },
                                "B10": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        9
                                    ],
                                    "title": "Band 10 (lwir)"
                                },
                                "B11": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        10
                                    ],
                                    "title": "Band 11 (lwir)"
                                },
                                "ANG": {
                                    "title": "Angle coefficients file",
                                    "type": "text/plain"
                                },
                                "MTL": {
                                    "title": "original metadata file",
                                    "type": "text/plain"
                                },
                                "BQA": {
                                    "title": "Band quality data",
                                    "type": "image/x.geotiff"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1/items"
                                }
                            ]
                        },
                        {
                            "id": "sentinel-2-l1c",
                            "title": "Sentinel 2 L1C",
                            "description": "Sentinel-2a and Sentinel-2b imagery",
                            "keywords": [
                                "sentinel",
                                "earth observation",
                                "esa"
                            ],
                            "version": "0.1.0",
                            "stac_version": "0.6.0",
                            "extent": {
                                "spatial": [
                                    -180,
                                    -90,
                                    180,
                                    90
                                ],
                                "temporal": [
                                    "2013-06-01",
                                    None
                                ]
                            },
                            "providers": [
                                {
                                    "roles": [
                                        "producer"
                                    ],
                                    "name": "ESA",
                                    "url": "https://earth.esa.int/web/guest/home"
                                },
                                {
                                    "roles": [
                                        "processor"
                                    ],
                                    "name": "Sinergise",
                                    "url": "https://registry.opendata.aws/sentinel-2/"
                                },
                                {
                                    "roles": [
                                        "host"
                                    ],
                                    "name": "AWS",
                                    "url": "http://sentinel-pds.s3-website.eu-central-1.amazonaws.com/"
                                },
                                {
                                    "roles": [
                                        "processor"
                                    ],
                                    "name": "Development Seed",
                                    "url": "https://github.com/sat-utils/sat-stac-sentinel"
                                }
                            ],
                            "license": "proprietary",
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
                                ]
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail"
                                },
                                "info": {
                                    "title": "Basic JSON metadata"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ]
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ]
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ]
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ]
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ]
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ]
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ]
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ]
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ]
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ]
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ]
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ]
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://sat-api.developmentseed.org/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items"
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "CBERS4-AWS",
                    "collections": [
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4MUX",
                            "description": "CBERS4 MUX camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4MUX"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4MUX/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 20,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "MUX",
                                "eo:bands": [
                                    {
                                        "name": "B5",
                                        "common_name": "blue"
                                    },
                                    {
                                        "name": "B6",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B7",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B8",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4AWFI",
                            "description": "CBERS4 AWFI camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4AWFI"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4AWFI/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 64,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "AWFI",
                                "eo:bands": [
                                    {
                                        "name": "B13",
                                        "common_name": "blue"
                                    },
                                    {
                                        "name": "B14",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B15",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B16",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4PAN10M",
                            "description": "CBERS4 PAN10M camera catalog",
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN10M"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN10M/items"
                                }
                            ],
                            "properties": {
                                "eo:gsd": 10,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "PAN10M",
                                "eo:bands": [
                                    {
                                        "name": "B2",
                                        "common_name": "green"
                                    },
                                    {
                                        "name": "B3",
                                        "common_name": "red"
                                    },
                                    {
                                        "name": "B4",
                                        "common_name": "nir"
                                    }
                                ]
                            }
                        },
                        {
                            "stac_version": "0.7.0",
                            "id": "CBERS4PAN5M",
                            "description": "CBERS4 PAN5M camera catalog",
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN5M"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "root",
                                    "href": "https://stac.amskepler.com/v07/stac"
                                },
                                {
                                    "rel": "items",
                                    "href": "https://stac.amskepler.com/v07/collections/CBERS4PAN5M/items"
                                }
                            ],
                            "license": "CC-BY-SA-3.0",
                            "providers": [
                                {
                                    "name": "Instituto Nacional de Pesquisas Espaciais, INPE",
                                    "roles": [
                                        "producer"
                                    ],
                                    "url": "http://www.cbers.inpe.br"
                                },
                                {
                                    "name": "AMS Kepler",
                                    "roles": [
                                        "processor"
                                    ],
                                    "description": "Convert INPE's original TIFF to COG and copy to Amazon Web Services",
                                    "url": "https://github.com/fredliporace/cbers-on-aws"
                                },
                                {
                                    "name": "Amazon Web Services",
                                    "roles": [
                                        "host"
                                    ],
                                    "url": "https://registry.opendata.aws/cbers/"
                                }
                            ],
                            "extent": {
                                "spatial": [
                                    -180,
                                    -83,
                                    180,
                                    83
                                ],
                                "temporal": [
                                    "2014-12-08T00:00:00Z",
                                    None
                                ]
                            },
                            "properties": {
                                "eo:gsd": 5,
                                "eo:platform": "CBERS-4",
                                "eo:instrument": "PAN5M",
                                "eo:bands": [
                                    {
                                        "name": "B1",
                                        "common_name": "pan"
                                    }
                                ]
                            }
                        }
                    ]
                }
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

    def test__get__stac_compose_collections__400_bad_request__invalid_provider_is_not_available(self):
        """http://localhost:8089/stac-compose/collections/?providers=INVALID-PROVIDER"""

        expected = {
            'code': 400,
            'description': 'Provider `INVALID-PROVIDER` is not available.',
            'name': 'Bad Request'
        }

        self.get(expected, query_string={'providers': 'INVALID-PROVIDER'}, expected_status_code=400)
