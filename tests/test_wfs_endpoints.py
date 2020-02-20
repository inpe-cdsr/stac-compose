#!/usr/bin/env python3

#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Unit-test for STAC operations."""

from os import getenv

from stac import STAC

url = getenv('STAC_SERVER_URL', 'http://localhost:8089/inpe-stac')

# ASSETS_URL = 'http://localhost:8089'
ASSETS_URL = 'http://cdsr.dpi.inpe.br'


'''
def test_capabilities():
    # TODO
    """/capabilities"""

    service = STAC(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result


def test_conformance():
    # TODO
    """/conformance"""

    service = STAC(url)

    expected = {}

    result = service.catalog()

    # print('\n expected: ', expected)
    # print('\n result: ', result)

    assert expected == result
'''

def test_collections():
    """/collections"""

    service = STAC(url)

    expected = {
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
                    -37.8691,
                    -55.2729,
                    3.03714,
                    -40.9072
                    ],
                    "time": [
                    "2019-12-30",
                    "2020-01-10"
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
                    -31.529,
                    -53.5023,
                    -17.6994,
                    -44.5841
                    ],
                    "time": [
                    "2019-12-30",
                    "2020-01-10"
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
                    -40.5504,
                    -59.7516,
                    5.85588,
                    -38.0763
                    ],
                    "time": [
                    "2019-12-30",
                    "2020-01-10"
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
                    -35.4051,
                    -56.2641,
                    0.759925,
                    -40.0351
                    ],
                    "time": [
                    "2019-12-30",
                    "2020-01-10"
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
                    -36.9715,
                    -53.4136,
                    3.67659,
                    -43.2105
                    ],
                    "time": [
                    "2019-12-31",
                    "2020-01-10"
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
                "id": "CBERS4_AWFI_L4_DN",
                "title": "CBERS4_AWFI_L4_DN",
                "description": "CBERS4 AWFI Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                    -40.7818,
                    -83.5022,
                    21.3449,
                    55.6045
                    ],
                    "time": [
                    "2019-11-01",
                    "2020-01-20"
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
                    -40.6714,
                    -83.5022,
                    21.3449,
                    53.6684
                    ],
                    "time": [
                    "2019-11-01",
                    "2019-12-03"
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
                    -39.8958,
                    -58.2673,
                    18.5552,
                    45.4624
                    ],
                    "time": [
                    "2020-01-06",
                    "2020-01-18"
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
                    -79.1374,
                    19.4644,
                    48.7398
                    ],
                    "time": [
                    "2019-11-01",
                    "2020-01-20"
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
                    -39.0381,
                    -79.1374,
                    19.4576,
                    48.7398
                    ],
                    "time": [
                    "2019-11-01",
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
                "id": "CBERS4_PAN10M_L2_DN",
                "title": "CBERS4_PAN10M_L2_DN",
                "description": "CBERS4 PAN10M Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                    -11.2928,
                    -35.2598,
                    -6.52036,
                    -32.4047
                    ],
                    "time": [
                    "2019-11-03",
                    "2019-11-09"
                    ]
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L2_DN",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_PAN10M_L2_DN/items",
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
                    -38.9157,
                    -78.3449,
                    7.80108,
                    -34.4983
                    ],
                    "time": [
                    "2019-11-01",
                    "2020-01-20"
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
                    -38.0158,
                    -77.3287,
                    6.01375,
                    -34.4899
                    ],
                    "time": [
                    "2019-11-01",
                    "2020-01-20"
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
            },
            {
                "stac_version": "0.7",
                "id": "LANDSAT5_TM_L2_DN",
                "title": "LANDSAT5_TM_L2_DN",
                "description": "LANDSAT5 TM Level2 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                    -39.8723,
                    -56.6952,
                    2.36172,
                    -44.9312
                    ],
                    "time": [
                    "2008-01-10",
                    "2008-01-12"
                    ]
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L2_DN",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L2_DN/items",
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
                "id": "LANDSAT5_TM_L4_DN",
                "title": "LANDSAT5_TM_L4_DN",
                "description": "LANDSAT5 TM Level4 DN dataset",
                "license": None,
                "properties": {},
                "extent": {
                    "spatial": [
                    -35.4858,
                    -57.6134,
                    0.895265,
                    -46.1207
                    ],
                    "time": [
                    "2008-01-10",
                    "2008-01-12"
                    ]
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L4_DN",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/LANDSAT5_TM_L4_DN/items",
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

    result = service.collections()

    assert expected == result


def test_collections_collection_id():
    """/collections/<collection_id>"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'

    expected = {
        "stac_version": "0.7",
        "id": "CBERS4A_MUX_L2_DN",
        "title": "CBERS4A_MUX_L2_DN",
        "description": "CBERS4A MUX Level2 DN dataset",
        "license": None,
        "properties": {},
        "extent": {
            "spatial": [
                -37.8691,
                -55.2729,
                3.03714,
                -40.9072
            ],
            "time": [
                "2019-12-30",
                "2020-01-10"
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
    }

    result = service.collections(collection_id=collection_id)

    assert expected == result


def test_collections_collection_id__not_found_collection():
    """/collections/<collection_id>"""

    service = STAC(url)

    collection_id = 'CB4A_MUX_L2_DN'

    expected = {}

    result = service.collections(collection_id=collection_id)

    assert expected == result


def test_collections_collection_id_items():
    """/collections/<collection_id>/items"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "context": {
            "page": 1,
            "limit": 2,
            "matched": 8,
            "returned": 2
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4A_MUX15911220200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.7393,
                        1.3427
                        ],
                        [
                        -44.7394,
                        0.269309
                        ],
                        [
                        -43.7009,
                        0.269242
                        ],
                        [
                        -43.7006,
                        1.34236
                        ],
                        [
                        -44.7393,
                        1.3427
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.7394,
                    0.269242,
                    -43.7006,
                    1.3427
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '159',
                    'row': '112',
                    'satellite': 'CBERS4A',
                    'sensor': 'MUX',
                    'cloud_cover': 0,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND5.tif".format(ASSETS_URL)
                    },
                    "green": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND6.tif".format(ASSETS_URL)
                    },
                    "nir": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND8.tif".format(ASSETS_URL)
                    },
                    "red": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND7.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                    "href": "{}/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911220200110".format(url),
                    "rel": "self"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "parent"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "collection"
                    },
                    {
                    "href": "{}/stac".format(url),
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4A_MUX15911320200110",
                "collection": "CBERS4A_MUX_L2_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -44.9039,
                        0.548619
                        ],
                        [
                        -44.9039,
                        -0.524779
                        ],
                        [
                        -43.8651,
                        -0.524677
                        ],
                        [
                        -43.8651,
                        0.548512
                        ],
                        [
                        -44.9039,
                        0.548619
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -44.9039,
                    -0.524779,
                    -43.8651,
                    0.548619
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '159',
                    'row': '113',
                    'satellite': 'CBERS4A',
                    'sensor': 'MUX',
                    'cloud_cover': 0,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND5.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND6.tif".format(ASSETS_URL)
                    },
                    "nir": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND8.tif".format(ASSETS_URL)
                    },
                    "red": {
                    "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113_L2_BAND7.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                    "href": "{}/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_113_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_113.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911320200110".format(url),
                    "rel": "self"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "parent"
                    },
                    {
                    "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
                    "rel": "collection"
                    },
                    {
                    "href": "{}/stac".format(url),
                    "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.collections_items(collection_id=collection_id, params=params)

    assert expected == result


def test_collections_collection_id_items_item_id():
    """/collections/<collection_id>/items/<item_id>"""

    service = STAC(url)

    collection_id = 'CBERS4A_MUX_L2_DN'
    item_id = 'CBERS4A_MUX15911220200110'
    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "type": "Feature",
        "id": "CBERS4A_MUX15911220200110",
        "collection": "CBERS4A_MUX_L2_DN",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
            [
                [
                -44.7393,
                1.3427
                ],
                [
                -44.7394,
                0.269309
                ],
                [
                -43.7009,
                0.269242
                ],
                [
                -43.7006,
                1.34236
                ],
                [
                -44.7393,
                1.3427
                ]
            ]
            ]
        },
        "bbox": [
            -44.7394,
            0.269242,
            -43.7006,
            1.3427
        ],
        "properties": {
            "datetime": "2020-01-21T12:16:23",
            'path': '159',
            'row': '112',
            'satellite': 'CBERS4A',
            'sensor': 'MUX',
            'cloud_cover': 0,
            'sync_loss': 0.0
        },
        "assets": {
            "blue": {
            "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND5.tif".format(ASSETS_URL)
            },
            "green": {
            "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND6.tif".format(ASSETS_URL)
            },
            "nir": {
            "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND8.tif".format(ASSETS_URL)
            },
            "red": {
            "href": "{}/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112_L2_BAND7.tif".format(ASSETS_URL)
            },
            "thumbnail": {
            "href": "{}/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_MUX_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_MUX_20200110_159_112.png".format(ASSETS_URL)
            }
        },
        "links": [
            {
            "href": "{}/collections/CBERS4A_MUX_L2_DN/items/CBERS4A_MUX15911220200110".format(url),
            "rel": "self"
            },
            {
            "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
            "rel": "parent"
            },
            {
            "href": "{}/collections/CBERS4A_MUX_L2_DN".format(url),
            "rel": "collection"
            },
            {
            "href": "{}/stac".format(url),
            "rel": "root"
            }
        ]
    }

    result = service.collections_items(
        collection_id=collection_id, item_id=item_id, params=params
    )

    assert expected == result


def test_stac():
    """/stac"""

    service = STAC(url)

    expected = {
        "stac_version": "0.7",
        "id": "inpe-stac",
        "description": "INPE STAC Catalog",
        "links": [
            {
                "href": "{}/stac".format(service.url),
                "rel": "self"
            },
            {
                "href": "{}/collections/CBERS4A_MUX_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_MUX_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4A_MUX_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_MUX_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WFI_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WFI_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WFI_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WFI_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4A_WPM_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4A_WPM_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_AWFI_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_AWFI_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_AWFI_L4_SR".format(service.url),
                "rel": "child",
                "title": "CBERS4_AWFI_L4_SR"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_MUX_L4_SR".format(service.url),
                "rel": "child",
                "title": "CBERS4_MUX_L4_SR"
            },
            {
                "href": "{}/collections/CBERS4_PAN10M_L2_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN10M_L2_DN"
            },
            {
                "href": "{}/collections/CBERS4_PAN10M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN10M_L4_DN"
            },
            {
                "href": "{}/collections/CBERS4_PAN5M_L4_DN".format(service.url),
                "rel": "child",
                "title": "CBERS4_PAN5M_L4_DN"
            },
            {
                "href": "{}/collections/LANDSAT5_TM_L2_DN".format(service.url),
                "rel": "child",
                "title": "LANDSAT5_TM_L2_DN"
            },
            {
                "href": "{}/collections/LANDSAT5_TM_L4_DN".format(service.url),
                "rel": "child",
                "title": "LANDSAT5_TM_L4_DN"
            }
        ]
    }

    catalog = service.catalog()

    # check all dict/json
    assert expected == catalog

    # check specifics keys
    assert expected['stac_version'] == catalog.stac_version
    assert None == catalog.stac_extensions
    assert expected['id'] == catalog.id
    assert None == catalog.title
    assert expected['description'] == catalog.description
    assert None == catalog.summaries
    assert expected['links'] == catalog.links


def test_stac_search_get():
    """GET /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "meta": {
            "page": 1,
            "limit": 2,
            'matched': 1933,
            "returned": 2
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15010520200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -42.6153,
                        -0.285467
                        ],
                        [
                        -42.6546,
                        -8.42863
                        ],
                        [
                        -33.1365,
                        -8.40183
                        ],
                        [
                        -33.1992,
                        -0.284565
                        ],
                        [
                        -42.6153,
                        -0.285467
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -42.6546,
                    -8.42863,
                    -33.1365,
                    -0.284565
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '105',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 0,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011120200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -43.8293,
                        -5.63972
                        ],
                        [
                        -43.9475,
                        -13.7608
                        ],
                        [
                        -34.2661,
                        -13.765
                        ],
                        [
                        -34.3792,
                        -5.64142
                        ],
                        [
                        -43.8293,
                        -5.63972
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -43.9475,
                    -13.765,
                    -34.2661,
                    -5.63972
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '111',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 50,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011120200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.search(params=params)

    assert expected == result


def test_stac_search_post__without_query_parameter():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2
    }

    expected = {
        "meta": {
            "page": 1,
            "limit": 2,
            'matched': 1933,
            "returned": 2
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15010520200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -42.6153,
                        -0.285467
                        ],
                        [
                        -42.6546,
                        -8.42863
                        ],
                        [
                        -33.1365,
                        -8.40183
                        ],
                        [
                        -33.1992,
                        -0.284565
                        ],
                        [
                        -42.6153,
                        -0.285467
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -42.6546,
                    -8.42863,
                    -33.1365,
                    -0.284565
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '105',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 0,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011120200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -43.8293,
                        -5.63972
                        ],
                        [
                        -43.9475,
                        -13.7608
                        ],
                        [
                        -34.2661,
                        -13.765
                        ],
                        [
                        -34.3792,
                        -5.64142
                        ],
                        [
                        -43.8293,
                        -5.63972
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -43.9475,
                    -13.765,
                    -34.2661,
                    -5.63972
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '111',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 50,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011120200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_lte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'lte': 0
            }
        }
    }

    expected = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15010520200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -42.6153,
                        -0.285467
                        ],
                        [
                        -42.6546,
                        -8.42863
                        ],
                        [
                        -33.1365,
                        -8.40183
                        ],
                        [
                        -33.1992,
                        -0.284565
                        ],
                        [
                        -42.6153,
                        -0.285467
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -42.6546,
                    -8.42863,
                    -33.1365,
                    -0.284565
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    "path": "150",
                    "row": "105",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND13.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND14.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND15.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105_L4_BAND16.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_105_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_105.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15010520200120",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            },
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011720200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -45.0915,
                        -10.9737
                        ],
                        [
                        -45.3265,
                        -19.062
                        ],
                        [
                        -35.3839,
                        -19.1354
                        ],
                        [
                        -35.519,
                        -11.0149
                        ],
                        [
                        -45.0915,
                        -10.9737
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -45.3265,
                    -19.1354,
                    -35.3839,
                    -10.9737
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    "path": "150",
                    "row": "117",
                    "satellite": "CBERS4",
                    "sensor": "AWFI",
                    "cloud_cover": 0,
                    "sync_loss": 0
                },
                "assets": {
                    "blue": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_117_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_117_L4_BAND13.tif"
                    },
                    "green": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_117_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_117_L4_BAND14.tif"
                    },
                    "red": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_117_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_117_L4_BAND15.tif"
                    },
                    "nir": {
                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_117_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_117_L4_BAND16.tif"
                    },
                    "thumbnail": {
                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_117_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_117.png"
                    }
                },
                "links": [
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011720200120",
                    "rel": "self"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                    "rel": "parent"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4_AWFI_L4_DN",
                    "rel": "collection"
                    },
                    {
                    "href": "http://localhost:8089/inpe-stac/stac",
                    "rel": "root"
                    }
                ]
            }
        ],
        "meta": {
            "page": 1,
            "limit": 2,
            "matched": 1932,
            "returned": 2
        }
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'gte': 50
            }
        }
    }

    expected = {
        "meta": {
            "page": 1,
            "limit": 2,
            'matched': 1,
            "returned": 1
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011120200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -43.8293,
                        -5.63972
                        ],
                        [
                        -43.9475,
                        -13.7608
                        ],
                        [
                        -34.2661,
                        -13.765
                        ],
                        [
                        -34.3792,
                        -5.64142
                        ],
                        [
                        -43.8293,
                        -5.63972
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -43.9475,
                    -13.765,
                    -34.2661,
                    -5.63972
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '111',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 50,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011120200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.search(params=params, method='POST')

    assert expected == result


def test_stac_search_post__with_query_parameter_lte_gte():
    """POST /stac/search"""

    service = STAC(url)

    params = {
        'bbox': [ -68.0273437, -25.0059726, -34.9365234, 0.3515602 ],
        'time': '2019-12-22T00:00:00/2020-01-22T23:59:00',
        'limit': 2,
        'query': {
            'cloud_cover': {
                'gte': 30,
                'lte': 60
            }
        }
    }

    expected = {
        "meta": {
            "page": 1,
            "limit": 2,
            'matched': 1,
            "returned": 1
        },
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "CBERS4_AWFI15011120200120",
                "collection": "CBERS4_AWFI_L4_DN",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                    [
                        [
                        -43.8293,
                        -5.63972
                        ],
                        [
                        -43.9475,
                        -13.7608
                        ],
                        [
                        -34.2661,
                        -13.765
                        ],
                        [
                        -34.3792,
                        -5.64142
                        ],
                        [
                        -43.8293,
                        -5.63972
                        ]
                    ]
                    ]
                },
                "bbox": [
                    -43.9475,
                    -13.765,
                    -34.2661,
                    -5.63972
                ],
                "properties": {
                    "datetime": "2020-01-21T12:16:23",
                    'path': '150',
                    'row': '111',
                    'satellite': 'CBERS4',
                    'sensor': 'AWFI',
                    'cloud_cover': 50,
                    'sync_loss': 0.0
                },
                "assets": {
                    "blue": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND13.tif".format(ASSETS_URL)
                    },
                    "green": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND14.tif".format(ASSETS_URL)
                    },
                    "nir": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND16.tif".format(ASSETS_URL)
                    },
                    "red": {
                        "href": "{}/api/download/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111_L4_BAND15.tif".format(ASSETS_URL)
                    },
                    "thumbnail": {
                        "href": "{}/datastore/TIFF/CBERS4/2020_01/CBERS_4_AWFI_DRD_2020_01_20.12_43_30_CB11/150_111_0/4_NN_UTM_WGS84/CBERS_4_AWFI_20200120_150_111.png".format(ASSETS_URL)
                    }
                },
                "links": [
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN/items/CBERS4_AWFI15011120200120".format(url),
                        "rel": "self"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "parent"
                    },
                    {
                        "href": "{}/collections/CBERS4_AWFI_L4_DN".format(url),
                        "rel": "collection"
                    },
                    {
                        "href": "{}/stac".format(url),
                        "rel": "root"
                    }
                ]
            }
        ]
    }

    result = service.search(params=params, method='POST')

    assert expected == result
