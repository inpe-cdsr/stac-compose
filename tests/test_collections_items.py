#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/collections/items/ endpoint."""

from json import load

from tests.utils import StacComposeTester


URN_collections_items = '/stac-compose/collections/items/'


class TestStacComposeCollectionsItems(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections_items)

    # Provider: INPE-CDSR

    def test__get__stac_compose_collections_items__inpe_cdsr_cbers4_awfi_l4_dn_and_cbers4a_wfi_l4_dn_and_cbers4a_wpm_l2_dn_limit_1(self):
        """
        http://localhost:8089/stac-compose/collections/items/?collections=INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2019-12-01T00:00:00/2020-02-13T23:59:00&limit=1
        """

        expected = {
            "INPE-CDSR": {
                "CBERS4_AWFI_L4_DN": {
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
                                "sync_loss": 0.0
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
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 391,
                        "returned": 1
                    }
                },
                "CBERS4A_WFI_L4_DN": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "CBERS4A_WFI15911720200110",
                            "collection": "CBERS4A_WFI_L4_DN",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -48.864,
                                            0.75986
                                        ],
                                        [
                                            -48.8923,
                                            -6.97426
                                        ],
                                        [
                                            -41.1819,
                                            -6.97487
                                        ],
                                        [
                                            -41.2097,
                                            0.759925
                                        ],
                                        [
                                            -48.864,
                                            0.75986
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -48.8923,
                                -6.97487,
                                -41.1819,
                                0.759925
                            ],
                            "properties": {
                                "datetime": "2020-01-21T12:16:23",
                                "path": "159",
                                "row": "117",
                                "satellite": "CBERS4A",
                                "sensor": "WFI",
                                "cloud_cover": 0,
                                "sync_loss": 0.0
                            },
                            "assets": {
                                "red": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND15.tif"
                                },
                                "blue": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND13.tif"
                                },
                                "green": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND14.tif"
                                },
                                "nir": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND16.tif"
                                },
                                "thumbnail": {
                                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117.png"
                                }
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI15911720200110",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "collection"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 9,
                        "returned": 1
                    }
                },
                "CBERS4A_WPM_L2_DN": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "CBERS4A_WPM15911220200110",
                            "collection": "CBERS4A_WPM_L2_DN",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -44.7212,
                                            1.29834
                                        ],
                                        [
                                            -44.7212,
                                            0.256597
                                        ],
                                        [
                                            -43.7049,
                                            0.256534
                                        ],
                                        [
                                            -43.7045,
                                            1.29803
                                        ],
                                        [
                                            -44.7212,
                                            1.29834
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -44.7212,
                                0.256534,
                                -43.7045,
                                1.29834
                            ],
                            "properties": {
                                "datetime": "2020-01-21T12:16:23",
                                "path": "159",
                                "row": "112",
                                "satellite": "CBERS4A",
                                "sensor": "WPM",
                                "cloud_cover": 0,
                                "sync_loss": 0.0
                            },
                            "assets": {
                                "green": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND2.tif"
                                },
                                "pan": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND0.tif"
                                },
                                "nir": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND4.tif"
                                },
                                "red": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND3.tif"
                                },
                                "blue": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND1.tif"
                                },
                                "thumbnail": {
                                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112.png"
                                }
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items/CBERS4A_WPM15911220200110",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "collection"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 176,
                        "returned": 1
                    }
                }
            }
        }

        query_string = {
            'collections': 'INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN',
            'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
            'time': '2019-12-01T00:00:00/2020-02-13T23:59:00',
            'limit': 1
        }

        self.get(expected, query_string=query_string)

    '''
    def test__post__stac_compose_collections_items__inpe_cdsr_cbers4_awfi_l4_dn_and_cbers4a_wfi_l4_dn_and_cbers4a_wpm_l2_dn_limit_1_query(self):
        """
        http://localhost:8089/stac-compose/collections/items/?collections=INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2019-12-01T00:00:00/2020-02-13T23:59:00&limit=1
        """

        expected = {
            "INPE-CDSR": {
                "CBERS4_AWFI_L4_DN": {
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
                                "sync_loss": 0.0
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
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 391,
                        "returned": 1
                    }
                },
                "CBERS4A_WFI_L4_DN": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "CBERS4A_WFI15911720200110",
                            "collection": "CBERS4A_WFI_L4_DN",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -48.864,
                                            0.75986
                                        ],
                                        [
                                            -48.8923,
                                            -6.97426
                                        ],
                                        [
                                            -41.1819,
                                            -6.97487
                                        ],
                                        [
                                            -41.2097,
                                            0.759925
                                        ],
                                        [
                                            -48.864,
                                            0.75986
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -48.8923,
                                -6.97487,
                                -41.1819,
                                0.759925
                            ],
                            "properties": {
                                "datetime": "2020-01-21T12:16:23",
                                "path": "159",
                                "row": "117",
                                "satellite": "CBERS4A",
                                "sensor": "WFI",
                                "cloud_cover": 0,
                                "sync_loss": 0.0
                            },
                            "assets": {
                                "red": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND15.tif"
                                },
                                "blue": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND13.tif"
                                },
                                "green": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND14.tif"
                                },
                                "nir": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117_L4_BAND16.tif"
                                },
                                "thumbnail": {
                                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WFI_RAW_2020_01_10.13_29_00_ETC2/159_117_0/4_NN_LCC_WGS84/CBERS_4A_WFI_20200110_159_117.png"
                                }
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN/items/CBERS4A_WFI15911720200110",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WFI_L4_DN",
                                    "rel": "collection"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 9,
                        "returned": 1
                    }
                },
                "CBERS4A_WPM_L2_DN": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "CBERS4A_WPM15911220200110",
                            "collection": "CBERS4A_WPM_L2_DN",
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -44.7212,
                                            1.29834
                                        ],
                                        [
                                            -44.7212,
                                            0.256597
                                        ],
                                        [
                                            -43.7049,
                                            0.256534
                                        ],
                                        [
                                            -43.7045,
                                            1.29803
                                        ],
                                        [
                                            -44.7212,
                                            1.29834
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -44.7212,
                                0.256534,
                                -43.7045,
                                1.29834
                            ],
                            "properties": {
                                "datetime": "2020-01-21T12:16:23",
                                "path": "159",
                                "row": "112",
                                "satellite": "CBERS4A",
                                "sensor": "WPM",
                                "cloud_cover": 0,
                                "sync_loss": 0.0
                            },
                            "assets": {
                                "green": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND2.tif"
                                },
                                "pan": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND0.tif"
                                },
                                "nir": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND4.tif"
                                },
                                "red": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND3.tif"
                                },
                                "blue": {
                                    "href": "http://cdsr.dpi.inpe.br/api/download/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112_L2_BAND1.tif"
                                },
                                "thumbnail": {
                                    "href": "http://cdsr.dpi.inpe.br/datastore/TIFF/CBERS4A/2020_01/CBERS_4A_WPM_RAW_2020_01_10.13_29_00_ETC2/159_112_0/2_NN_UTM_WGS84/CBERS_4A_WPM_20200110_159_112.png"
                                }
                            },
                            "links": [
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN/items/CBERS4A_WPM15911220200110",
                                    "rel": "self"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "parent"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/collections/CBERS4A_WPM_L2_DN",
                                    "rel": "collection"
                                },
                                {
                                    "href": "http://localhost:8089/inpe-stac/stac",
                                    "rel": "root"
                                }
                            ]
                        }
                    ],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 176,
                        "returned": 1
                    }
                }
            }
        }

        body = {
            'providers': [
                {
                    'name': 'INPE-CDSR',
                    'collections': [
                        {'name': 'CBERS4_AWFI_L4_DN'},
                        {'name': 'CBERS4A_WFI_L4_DN'},
                        {'name': 'CBERS4A_WPM_L2_DN'}
                    ],
                    'query': {
                        'cloud_cover': {
                            "gte": 0,
                            "lte": 10
                        },
                    }
                }
            ],
            'bbox': [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            'time': ['2019-12-01T00:00:00', '2020-02-13T23:59:00'],
            'limit': 1
        }

        self.post(expected, body=body)
    '''
    # Provider: LANDAST8-SENTINEL2-AWS

    def test__get__stac_compose_collections_items__landsat8_sentinel2_aws_landsat_8_l1_and_sentinel_2_l1c_limit_1(self):
        """
        http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=1
        """

        self.maxDiff = None

        expected = {
            "LANDAST8-SENTINEL2-AWS": {
                "landsat-8-l1": {
                    "type": "FeatureCollection",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 748,
                        "returned": 1
                    },
                    "features": [
                        {
                            "type": "Feature",
                            "id": "LC82310782020044",
                            "bbox": [
                                -66.88899,
                                -27.05112,
                                -64.56824,
                                -24.93065
                            ],
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -66.49304305702688,
                                            -24.932756418193854
                                        ],
                                        [
                                            -64.57098632376038,
                                            -25.28391152003526
                                        ],
                                        [
                                            -64.96363270562209,
                                            -27.049545312089084
                                        ],
                                        [
                                            -66.88818548270888,
                                            -26.700636378760883
                                        ],
                                        [
                                            -66.49304305702688,
                                            -24.932756418193854
                                        ]
                                    ]
                                ]
                            },
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
                                ],
                                "datetime": "2020-02-13T14:19:21.483266+00:00",
                                "eo:sun_azimuth": 75.40561993,
                                "eo:sun_elevation": 55.36817654,
                                "eo:cloud_cover": 26,
                                "eo:row": "078",
                                "eo:column": "231",
                                "landsat:product_id": "LC08_L1TP_231078_20200213_20200213_01_RT",
                                "landsat:scene_id": "LC82310782020044LGN00",
                                "landsat:processing_level": "L1TP",
                                "landsat:tier": "RT",
                                "landsat:revision": "00",
                                "eo:epsg": 32720
                            },
                            "assets": {
                                "index": {
                                    "type": "text/html",
                                    "title": "HTML index page",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_MTL.txt"
                                },
                                "thumbnail": {
                                    "title": "Thumbnail image",
                                    "type": "image/jpeg",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_thumb_large.jpg"
                                },
                                "B1": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        0
                                    ],
                                    "title": "Band 1 (coastal)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B1.TIF"
                                },
                                "B2": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        1
                                    ],
                                    "title": "Band 2 (blue)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B2.TIF"
                                },
                                "B3": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        2
                                    ],
                                    "title": "Band 3 (green)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B3.TIF"
                                },
                                "B4": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        3
                                    ],
                                    "title": "Band 4 (red)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B4.TIF"
                                },
                                "B5": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        4
                                    ],
                                    "title": "Band 5 (nir)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B5.TIF"
                                },
                                "B6": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        5
                                    ],
                                    "title": "Band 6 (swir16)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B6.TIF"
                                },
                                "B7": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        6
                                    ],
                                    "title": "Band 7 (swir22)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B7.TIF"
                                },
                                "B8": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        7
                                    ],
                                    "title": "Band 8 (pan)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B8.TIF"
                                },
                                "B9": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        8
                                    ],
                                    "title": "Band 9 (cirrus)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B9.TIF"
                                },
                                "B10": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        9
                                    ],
                                    "title": "Band 10 (lwir)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B10.TIF"
                                },
                                "B11": {
                                    "type": "image/x.geotiff",
                                    "eo:bands": [
                                        10
                                    ],
                                    "title": "Band 11 (lwir)",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_B11.TIF"
                                },
                                "ANG": {
                                    "title": "Angle coefficients file",
                                    "type": "text/plain",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_ANG.txt"
                                },
                                "MTL": {
                                    "title": "original metadata file",
                                    "type": "text/plain",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_MTL.txt"
                                },
                                "BQA": {
                                    "title": "Band quality data",
                                    "type": "image/x.geotiff",
                                    "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/078/LC08_L1TP_231078_20200213_20200213_01_RT/LC08_L1TP_231078_20200213_20200213_01_RT_BQA.TIF"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1/items/LC82310782020044"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1"
                                },
                                {
                                    "rel": "collection",
                                    "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1"
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
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2020-01-13T00%3A00%3A00%2F2020-02-13T23%3A59%3A00&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                },
                "sentinel-2-l1c": {
                    "type": "FeatureCollection",
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 10675,
                        "returned": 1
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
                        }
                    ],
                    "links": [
                        {
                            "rel": "next",
                            "title": "Next page of results",
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2020-01-13T00%3A00%3A00%2F2020-02-13T23%3A59%3A00&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                }
            }
        }

        query_string = {
            'collections': 'LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c',
            'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
            'time': '2020-01-13T00:00:00/2020-02-13T23:59:00',
            'limit': 1
        }

        self.get(expected, query_string=query_string)

    '''
    # this test is commented, because it is slow
    def test__get__stac_compose_collections_items__landsat8_sentinel2_aws_sentinel_2_l1c_limit_2000(self):
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
    # Provider: CBERS4-AWS

    def test__get__stac_compose_collections_items__cbers4_aws_cbers4mux_cbers4awfi_limit_1(self):
        """
        http://localhost:8089/stac-compose/collections/items?collections=LANDAST8-SENTINEL2-AWS:landsat-8-l1,LANDAST8-SENTINEL2-AWS:sentinel-2-l1c&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2020-01-13T00:00:00/2020-02-13T23:59:00&limit=1
        """

        expected = {
            "CBERS4-AWS": {
                "CBERS4MUX": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "id": "CBERS_4_MUX_20191201_158_099_L2",
                            "type": "Feature",
                            "geometry": {
                                "type": "MultiPolygon",
                                "coordinates": [
                                    [
                                        [
                                            [
                                                -45.103133,
                                                0.457109
                                            ],
                                            [
                                                -44.029154,
                                                0.290961
                                            ],
                                            [
                                                -43.794924,
                                                1.354751
                                            ],
                                            [
                                                -44.869022,
                                                1.520895
                                            ],
                                            [
                                                -45.103133,
                                                0.457109
                                            ]
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -45.104787,
                                0.281009,
                                -43.791657,
                                1.54059
                            ],
                            "collection": "CBERS4MUX",
                            "properties": {
                                "datetime": "2019-12-01T13:11:37Z",
                                "eo:sun_azimuth": 136.589,
                                "eo:sun_elevation": 58.0225,
                                "eo:off_nadir": -0.0104568,
                                "eo:epsg": 32745,
                                "eo:instrument": "MUX",
                                "cbers:data_type": "L2",
                                "cbers:path": 158,
                                "cbers:row": 99
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2.json"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/MUX/158/099/catalog.json"
                                },
                                {
                                    "rel": "collection",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/MUX/collection.json"
                                }
                            ],
                            "assets": {
                                "thumbnail": {
                                    "href": "https://s3.amazonaws.com/cbers-meta-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099.jpg",
                                    "type": "image/jpeg"
                                },
                                "metadata": {
                                    "href": "s3://cbers-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099_L2_BAND6.xml",
                                    "title": "INPE original metadata",
                                    "type": "text/xml"
                                },
                                "B5": {
                                    "href": "s3://cbers-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099_L2_BAND5.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        0
                                    ]
                                },
                                "B6": {
                                    "href": "s3://cbers-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099_L2_BAND6.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        1
                                    ]
                                },
                                "B7": {
                                    "href": "s3://cbers-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099_L2_BAND7.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B8": {
                                    "href": "s3://cbers-pds/CBERS4/MUX/158/099/CBERS_4_MUX_20191201_158_099_L2/CBERS_4_MUX_20191201_158_099_L2_BAND8.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        3
                                    ]
                                }
                            }
                        }
                    ]
                },
                "CBERS4AWFI": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "id": "CBERS_4_AWFI_20191201_158_099_L2",
                            "type": "Feature",
                            "geometry": {
                                "type": "MultiPolygon",
                                "coordinates": [
                                    [
                                        [
                                            [
                                                -49.121426,
                                                -1.787801
                                            ],
                                            [
                                                -41.230899,
                                                -3.014614
                                            ],
                                            [
                                                -39.73469,
                                                3.768995
                                            ],
                                            [
                                                -47.632002,
                                                4.995838
                                            ],
                                            [
                                                -49.121426,
                                                -1.787801
                                            ]
                                        ]
                                    ]
                                ]
                            },
                            "bbox": [
                                -49.131277,
                                -3.052144,
                                -39.713359,
                                5.057464
                            ],
                            "collection": "CBERS4AWFI",
                            "properties": {
                                "datetime": "2019-12-01T13:11:36Z",
                                "eo:sun_azimuth": 138.03,
                                "eo:sun_elevation": 58.0073,
                                "eo:off_nadir": -0.0104568,
                                "eo:epsg": 32745,
                                "eo:instrument": "AWFI",
                                "cbers:data_type": "L2",
                                "cbers:path": 158,
                                "cbers:row": 99
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2.json"
                                },
                                {
                                    "rel": "parent",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/AWFI/158/099/catalog.json"
                                },
                                {
                                    "rel": "collection",
                                    "href": "https://cbers-stac-0-7.s3.amazonaws.com/CBERS4/AWFI/collection.json"
                                }
                            ],
                            "assets": {
                                "thumbnail": {
                                    "href": "https://s3.amazonaws.com/cbers-meta-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099.jpg",
                                    "type": "image/jpeg"
                                },
                                "metadata": {
                                    "href": "s3://cbers-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099_L2_BAND14.xml",
                                    "title": "INPE original metadata",
                                    "type": "text/xml"
                                },
                                "B13": {
                                    "href": "s3://cbers-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099_L2_BAND13.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        0
                                    ]
                                },
                                "B14": {
                                    "href": "s3://cbers-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099_L2_BAND14.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        1
                                    ]
                                },
                                "B15": {
                                    "href": "s3://cbers-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099_L2_BAND15.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        2
                                    ]
                                },
                                "B16": {
                                    "href": "s3://cbers-pds/CBERS4/AWFI/158/099/CBERS_4_AWFI_20191201_158_099_L2/CBERS_4_AWFI_20191201_158_099_L2_BAND16.tif",
                                    "type": "image/vnd.stac.geotiff; cloud-optimized=true",
                                    "eo:bands": [
                                        3
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        }

        query_string = {
            'collections': 'CBERS4-AWS:CBERS4MUX,CBERS4-AWS:CBERS4AWFI',
            'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
            'time': '2019-12-01T00:00:00/2020-02-13T23:59:00',
            'limit': 1
        }

        self.get(expected, query_string=query_string)



class TestStacComposeCollectionsItemsError(StacComposeTester):

    def setUp(self):
        self.set_urn(URN_collections_items)

    def test__get__stac_compose_collections_items__400_bad_request__required_fields(self):
        test_cases = [
            {
                'url': 'http://localhost:8089/stac-compose/collections/items/?bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2019-12-01T00:00:00/2020-02-13T23:59:00&limit=1',
                'expected': {
                    'code': 400,
                    'message': '{"collections": ["required field"]}'
                },
                'query_string': {
                    'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
                    'time': '2019-12-01T00:00:00/2020-02-13T23:59:00',
                    'limit': 1
                }
            },
            {
                'url': 'http://localhost:8089/stac-compose/collections/items/?collections=INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN&time=2019-12-01T00:00:00/2020-02-13T23:59:00&limit=1',
                'expected': {
                    'code': 400,
                    'message': '{"bbox": ["required field"]}'
                },
                'query_string': {
                    'collections': 'INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN',
                    'time': '2019-12-01T00:00:00/2020-02-13T23:59:00',
                    'limit': 1
                }
            },
            {
                'url': 'http://localhost:8089/stac-compose/collections/items/?collections=INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&limit=1',
                'expected': {
                    'code': 400,
                    'message': '{"time": ["required field"]}'
                },
                'query_string': {
                    'collections': 'INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN',
                    'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
                    'limit': 1
                }
            },
            {
                'url': 'http://localhost:8089/stac-compose/collections/items/?collections=INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN&bbox=-68.0273437,-25.0059726,-34.9365234,0.3515602&time=2019-12-01T00:00:00/2020-02-13T23:59:00',
                'expected': {
                    'code': 400,
                    'message': '{"limit": ["required field"]}'
                },
                'query_string': {
                    'collections': 'INPE-CDSR:CBERS4_AWFI_L4_DN,INPE-CDSR:CBERS4A_WFI_L4_DN,INPE-CDSR:CBERS4A_WPM_L2_DN',
                    'bbox': '-68.0273437,-25.0059726,-34.9365234,0.3515602',
                    'time': '2019-12-01T00:00:00/2020-02-13T23:59:00'
                }
            }
        ]

        for test_case in test_cases:
            self.get(test_case['expected'], query_string=test_case['query_string'], expected_status_code=400)
