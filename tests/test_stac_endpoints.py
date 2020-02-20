#!/usr/bin/env python3

"""Unit-test for STAC-COMPOSE operations."""



# ASSETS_URL = 'http://localhost:8089'
# ASSETS_URL = 'http://cdsr.dpi.inpe.br'


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
