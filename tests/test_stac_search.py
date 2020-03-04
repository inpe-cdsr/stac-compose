#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/stac/search/ endpoint."""

from json import load

from tests.utils import StacComposeTester


URN = '/stac-compose/stac/search/'


class TestStacComposeStacSearch(StacComposeTester):

    def setUp(self):
        self.set_urn(URN)

    # Provider: INPE-CDSR

    def test__post__stac_compose_stac_search__inpe_cdsr_cbers4_awfi_l4_dn_and_cbers4a_wfi_l4_dn_and_cbers4a_wpm_l2_dn__limit_1_and_query(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

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
                        "matched": 369,
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
            "providers": [
                {
                    "name": "INPE-CDSR",
                    "method": "POST",
                    "collections": [
                        {"name": "CBERS4_AWFI_L4_DN"},
                        {"name": "CBERS4A_WFI_L4_DN"},
                        {"name": "CBERS4A_WPM_L2_DN"}
                    ],
                    "query": {
                        "cloud_cover": {
                            "gte": 0,
                            "lte": 10
                        }
                    }
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)

    def test__post__stac_compose_stac_search__inpe_cdsr_cbers_awfi_l4_sr__collection_does_not_have_items(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        expected = {
            "INPE-CDSR": {
                "CBERS4_AWFI_L4_SR": {
                    "type": "FeatureCollection",
                    "features": [],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 0,
                        "returned": 0
                    }
                }
            }
        }

        body = {
            "providers": [
                {
                    "name": "INPE-CDSR",
                    "method": "POST",
                    "collections": [
                        {"name": "CBERS4_AWFI_L4_SR"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)

    def test__post__stac_compose_stac_search__inpe_cdsr_cbers_xyz_l4_sr__collection_does_not_exist(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        expected = {
            "INPE-CDSR": {
                "CBERS4_XYZ_L4_SR": {
                    "type": "FeatureCollection",
                    "features": [],
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "matched": 0,
                        "returned": 0
                    }
                }
            }
        }

        body = {
            "providers": [
                {
                    "name": "INPE-CDSR",
                    "method": "POST",
                    "collections": [
                        {"name": "CBERS4_XYZ_L4_SR"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)

    # Provider: LANDSAT8-SENTINEL2-AWS

    def test__post__stac_compose_stac_search__landsat8_sentinel2_aws_landsat_8_l1_and_sentinel_2_l1c__limit_1_and_query(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        expected = {
            "LANDSAT8-SENTINEL2-AWS": {
                "landsat-8-l1": {
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "returned": 1,
                        "matched": 182
                    },
                    "type": "FeatureCollection",
                    "features": [
                        {
                        "type": "Feature",
                        "id": "LC82310752020044",
                        "bbox": [
                            -65.80241,
                            -22.72686,
                            -63.57209,
                            -20.61604
                        ],
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                    -65.40865393847542,
                                    -20.61689411370787
                                    ],
                                    [
                                    -63.57377080824341,
                                    -20.975459850589534
                                    ],
                                    [
                                    -63.96353615798685,
                                    -22.724812021720155
                                    ],
                                    [
                                    -65.80029281035198,
                                    -22.36713054158154
                                    ],
                                    [
                                    -65.40865393847542,
                                    -20.61689411370787
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
                                    "full_width_half_max": 0.02,
                                    "center_wavelength": 0.44,
                                    "name": "B1",
                                    "gsd": 30,
                                    "common_name": "coastal"
                                },
                                {
                                    "full_width_half_max": 0.06,
                                    "center_wavelength": 0.48,
                                    "name": "B2",
                                    "gsd": 30,
                                    "common_name": "blue"
                                },
                                {
                                    "full_width_half_max": 0.06,
                                    "center_wavelength": 0.56,
                                    "name": "B3",
                                    "gsd": 30,
                                    "common_name": "green"
                                },
                                {
                                    "full_width_half_max": 0.04,
                                    "center_wavelength": 0.65,
                                    "name": "B4",
                                    "gsd": 30,
                                    "common_name": "red"
                                },
                                {
                                    "full_width_half_max": 0.03,
                                    "center_wavelength": 0.86,
                                    "name": "B5",
                                    "gsd": 30,
                                    "common_name": "nir"
                                },
                                {
                                    "full_width_half_max": 0.08,
                                    "center_wavelength": 1.6,
                                    "name": "B6",
                                    "gsd": 30,
                                    "common_name": "swir16"
                                },
                                {
                                    "full_width_half_max": 0.2,
                                    "center_wavelength": 2.2,
                                    "name": "B7",
                                    "gsd": 30,
                                    "common_name": "swir22"
                                },
                                {
                                    "full_width_half_max": 0.18,
                                    "center_wavelength": 0.59,
                                    "name": "B8",
                                    "gsd": 15,
                                    "common_name": "pan"
                                },
                                {
                                    "full_width_half_max": 0.02,
                                    "center_wavelength": 1.37,
                                    "name": "B9",
                                    "gsd": 30,
                                    "common_name": "cirrus"
                                },
                                {
                                    "full_width_half_max": 0.8,
                                    "center_wavelength": 10.9,
                                    "name": "B10",
                                    "gsd": 100,
                                    "common_name": "lwir11"
                                },
                                {
                                    "full_width_half_max": 1,
                                    "center_wavelength": 12,
                                    "name": "B11",
                                    "gsd": 100,
                                    "common_name": "lwir12"
                                }
                            ],
                            "datetime": "2020-02-13T14:18:09.661889+00:00",
                            "eo:sun_azimuth": 81.21412609,
                            "eo:sun_elevation": 56.91053723,
                            "eo:cloud_cover": 7,
                            "eo:row": "075",
                            "eo:column": "231",
                            "landsat:product_id": "LC08_L1TP_231075_20200213_20200225_01_T1",
                            "landsat:scene_id": "LC82310752020044LGN00",
                            "landsat:processing_level": "L1TP",
                            "landsat:tier": "T1",
                            "landsat:revision": "00",
                            "eo:epsg": 32720
                        },
                        "assets": {
                            "index": {
                                "type": "text/html",
                                "title": "HTML index page",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_MTL.txt"
                            },
                            "thumbnail": {
                                "title": "Thumbnail image",
                                "type": "image/jpeg",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_thumb_large.jpg"
                            },
                            "B1": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    0
                                ],
                                "title": "Band 1 (coastal)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B1.TIF"
                            },
                            "B2": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    1
                                ],
                                "title": "Band 2 (blue)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B2.TIF"
                            },
                            "B3": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    2
                                ],
                                "title": "Band 3 (green)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B3.TIF"
                            },
                            "B4": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    3
                                ],
                                "title": "Band 4 (red)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B4.TIF"
                            },
                            "B5": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    4
                                ],
                                "title": "Band 5 (nir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B5.TIF"
                            },
                            "B6": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    5
                                ],
                                "title": "Band 6 (swir16)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B6.TIF"
                            },
                            "B7": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    6
                                ],
                                "title": "Band 7 (swir22)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B7.TIF"
                            },
                            "B8": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    7
                                ],
                                "title": "Band 8 (pan)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B8.TIF"
                            },
                            "B9": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    8
                                ],
                                "title": "Band 9 (cirrus)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B9.TIF"
                            },
                            "B10": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    9
                                ],
                                "title": "Band 10 (lwir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B10.TIF"
                            },
                            "B11": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    10
                                ],
                                "title": "Band 11 (lwir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B11.TIF"
                            },
                            "ANG": {
                                "title": "Angle coefficients file",
                                "type": "text/plain",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_ANG.txt"
                            },
                            "MTL": {
                                "title": "original metadata file",
                                "type": "text/plain",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_MTL.txt"
                            },
                            "BQA": {
                                "title": "Band quality data",
                                "type": "image/x.geotiff",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_BQA.TIF"
                            }
                        },
                        "links": [
                            {
                                "rel": "self",
                                "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1/items/LC82310752020044"
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
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2019-12-01T00%3A00%3A00%2F2020-02-13T23%3A59%3A59&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                },
                "sentinel-2-l1c": {
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "returned": 1,
                        "matched": 3724
                    },
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "S2A_19KEQ_20200213_0",
                            "bbox": [
                                -69.00018623022196,
                                -23.598345902589184,
                                -67.92406485876405,
                                -22.602951501396298
                            ],
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                        -69.00018623022196,
                                        -23.598345902589184
                                        ],
                                        [
                                        -69.0001848677525,
                                        -22.606504481568752
                                        ],
                                        [
                                        -67.93193462295525,
                                        -22.602951501396298
                                        ],
                                        [
                                        -67.92406485876405,
                                        -23.59461895528854
                                        ],
                                        [
                                        -69.00018623022196,
                                        -23.598345902589184
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
                                "datetime": "2020-02-13T14:49:11.042000+00:00",
                                "eo:platform": "sentinel-2a",
                                "eo:cloud_cover": 1.6,
                                "sentinel:utm_zone": 19,
                                "sentinel:latitude_band": "K",
                                "sentinel:grid_square": "EQ",
                                "sentinel:sequence": "0",
                                "sentinel:product_id": "S2A_MSIL1C_20200213T143721_N0209_R096_T19KEQ_20200213T180805"
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/preview.jpg"
                                },
                                "info": {
                                    "title": "Basic JSON metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/tileInfo.json"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/metadata.xml"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/TKI.jp2"
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B01.jp2"
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B02.jp2"
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B03.jp2"
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B04.jp2"
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B05.jp2"
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B06.jp2"
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B07.jp2"
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B08.jp2"
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B08.jp2"
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B09.jp2"
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B10.jp2"
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B11.jp2"
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B11.jp2"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items/S2A_19KEQ_20200213_0"
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
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2019-12-01T00%3A00%3A00%2F2020-02-13T23%3A59%3A59&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                }
            }
        }

        body = {
            "providers": [
                {
                    "name": "LANDSAT8-SENTINEL2-AWS",
                    "method": "POST",
                    "collections": [
                        {"name": "landsat-8-l1"},
                        {"name": "sentinel-2-l1c"}
                    ],
                    "query": {
                        "eo:cloud_cover": {
                            "gte": 0,
                            "lte": 10
                        }
                    }
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)

    # Provider: CBERS4-AWS

    def test__post__stac_compose_stac_search__cbers4_aws_cbers4mux_cbers4awfi__limit_1_and_query(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        expected = {
            "CBERS4-AWS": {
                "CBERS4MUX": {
                    'context': {
                        'limit': 1,
                        'matched': 1,
                        'page': 1,
                        'returned': 1
                    },
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
                    'context': {
                        'limit': 1,
                        'matched': 1,
                        'page': 1,
                        'returned': 1
                    },
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

        body = {
            "providers": [
                {
                    "name": "CBERS4-AWS",
                    "method": "GET",
                    "collections": [
                        {"name": "CBERS4MUX"},
                        {"name": "CBERS4AWFI"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)

    # Providers: INPE-CDSR, LANDSAT8-SENTINEL2-AWS and CBERS4-AWS

    def test__post__stac_compose_stac_search__inpe_cdsr_landsat8_sentinel2_aws_cbers4_aws__limit_1_and_query(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

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
                        "matched": 369,
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
            },
            "LANDSAT8-SENTINEL2-AWS": {
                "landsat-8-l1": {
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "returned": 1,
                        "matched": 182
                    },
                    "type": "FeatureCollection",
                    "features": [
                        {
                        "type": "Feature",
                        "id": "LC82310752020044",
                        "bbox": [
                            -65.80241,
                            -22.72686,
                            -63.57209,
                            -20.61604
                        ],
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                    -65.40865393847542,
                                    -20.61689411370787
                                    ],
                                    [
                                    -63.57377080824341,
                                    -20.975459850589534
                                    ],
                                    [
                                    -63.96353615798685,
                                    -22.724812021720155
                                    ],
                                    [
                                    -65.80029281035198,
                                    -22.36713054158154
                                    ],
                                    [
                                    -65.40865393847542,
                                    -20.61689411370787
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
                                    "full_width_half_max": 0.02,
                                    "center_wavelength": 0.44,
                                    "name": "B1",
                                    "gsd": 30,
                                    "common_name": "coastal"
                                },
                                {
                                    "full_width_half_max": 0.06,
                                    "center_wavelength": 0.48,
                                    "name": "B2",
                                    "gsd": 30,
                                    "common_name": "blue"
                                },
                                {
                                    "full_width_half_max": 0.06,
                                    "center_wavelength": 0.56,
                                    "name": "B3",
                                    "gsd": 30,
                                    "common_name": "green"
                                },
                                {
                                    "full_width_half_max": 0.04,
                                    "center_wavelength": 0.65,
                                    "name": "B4",
                                    "gsd": 30,
                                    "common_name": "red"
                                },
                                {
                                    "full_width_half_max": 0.03,
                                    "center_wavelength": 0.86,
                                    "name": "B5",
                                    "gsd": 30,
                                    "common_name": "nir"
                                },
                                {
                                    "full_width_half_max": 0.08,
                                    "center_wavelength": 1.6,
                                    "name": "B6",
                                    "gsd": 30,
                                    "common_name": "swir16"
                                },
                                {
                                    "full_width_half_max": 0.2,
                                    "center_wavelength": 2.2,
                                    "name": "B7",
                                    "gsd": 30,
                                    "common_name": "swir22"
                                },
                                {
                                    "full_width_half_max": 0.18,
                                    "center_wavelength": 0.59,
                                    "name": "B8",
                                    "gsd": 15,
                                    "common_name": "pan"
                                },
                                {
                                    "full_width_half_max": 0.02,
                                    "center_wavelength": 1.37,
                                    "name": "B9",
                                    "gsd": 30,
                                    "common_name": "cirrus"
                                },
                                {
                                    "full_width_half_max": 0.8,
                                    "center_wavelength": 10.9,
                                    "name": "B10",
                                    "gsd": 100,
                                    "common_name": "lwir11"
                                },
                                {
                                    "full_width_half_max": 1,
                                    "center_wavelength": 12,
                                    "name": "B11",
                                    "gsd": 100,
                                    "common_name": "lwir12"
                                }
                            ],
                            "datetime": "2020-02-13T14:18:09.661889+00:00",
                            "eo:sun_azimuth": 81.21412609,
                            "eo:sun_elevation": 56.91053723,
                            "eo:cloud_cover": 7,
                            "eo:row": "075",
                            "eo:column": "231",
                            "landsat:product_id": "LC08_L1TP_231075_20200213_20200225_01_T1",
                            "landsat:scene_id": "LC82310752020044LGN00",
                            "landsat:processing_level": "L1TP",
                            "landsat:tier": "T1",
                            "landsat:revision": "00",
                            "eo:epsg": 32720
                        },
                        "assets": {
                            "index": {
                                "type": "text/html",
                                "title": "HTML index page",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_MTL.txt"
                            },
                            "thumbnail": {
                                "title": "Thumbnail image",
                                "type": "image/jpeg",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_thumb_large.jpg"
                            },
                            "B1": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    0
                                ],
                                "title": "Band 1 (coastal)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B1.TIF"
                            },
                            "B2": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    1
                                ],
                                "title": "Band 2 (blue)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B2.TIF"
                            },
                            "B3": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    2
                                ],
                                "title": "Band 3 (green)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B3.TIF"
                            },
                            "B4": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    3
                                ],
                                "title": "Band 4 (red)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B4.TIF"
                            },
                            "B5": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    4
                                ],
                                "title": "Band 5 (nir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B5.TIF"
                            },
                            "B6": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    5
                                ],
                                "title": "Band 6 (swir16)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B6.TIF"
                            },
                            "B7": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    6
                                ],
                                "title": "Band 7 (swir22)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B7.TIF"
                            },
                            "B8": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    7
                                ],
                                "title": "Band 8 (pan)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B8.TIF"
                            },
                            "B9": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    8
                                ],
                                "title": "Band 9 (cirrus)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B9.TIF"
                            },
                            "B10": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    9
                                ],
                                "title": "Band 10 (lwir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B10.TIF"
                            },
                            "B11": {
                                "type": "image/x.geotiff",
                                "eo:bands": [
                                    10
                                ],
                                "title": "Band 11 (lwir)",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_B11.TIF"
                            },
                            "ANG": {
                                "title": "Angle coefficients file",
                                "type": "text/plain",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_ANG.txt"
                            },
                            "MTL": {
                                "title": "original metadata file",
                                "type": "text/plain",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_MTL.txt"
                            },
                            "BQA": {
                                "title": "Band quality data",
                                "type": "image/x.geotiff",
                                "href": "https://landsat-pds.s3.amazonaws.com/c1/L8/231/075/LC08_L1TP_231075_20200213_20200225_01_T1/LC08_L1TP_231075_20200213_20200225_01_T1_BQA.TIF"
                            }
                        },
                        "links": [
                            {
                                "rel": "self",
                                "href": "https://sat-api.developmentseed.org/collections/landsat-8-l1/items/LC82310752020044"
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
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2019-12-01T00%3A00%3A00%2F2020-02-13T23%3A59%3A59&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                },
                "sentinel-2-l1c": {
                    "context": {
                        "page": 1,
                        "limit": 1,
                        "returned": 1,
                        "matched": 3724
                    },
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": "S2A_19KEQ_20200213_0",
                            "bbox": [
                                -69.00018623022196,
                                -23.598345902589184,
                                -67.92406485876405,
                                -22.602951501396298
                            ],
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                        -69.00018623022196,
                                        -23.598345902589184
                                        ],
                                        [
                                        -69.0001848677525,
                                        -22.606504481568752
                                        ],
                                        [
                                        -67.93193462295525,
                                        -22.602951501396298
                                        ],
                                        [
                                        -67.92406485876405,
                                        -23.59461895528854
                                        ],
                                        [
                                        -69.00018623022196,
                                        -23.598345902589184
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
                                "datetime": "2020-02-13T14:49:11.042000+00:00",
                                "eo:platform": "sentinel-2a",
                                "eo:cloud_cover": 1.6,
                                "sentinel:utm_zone": 19,
                                "sentinel:latitude_band": "K",
                                "sentinel:grid_square": "EQ",
                                "sentinel:sequence": "0",
                                "sentinel:product_id": "S2A_MSIL1C_20200213T143721_N0209_R096_T19KEQ_20200213T180805"
                            },
                            "assets": {
                                "thumbnail": {
                                    "title": "Thumbnail",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/preview.jpg"
                                },
                                "info": {
                                    "title": "Basic JSON metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/tileInfo.json"
                                },
                                "metadata": {
                                    "title": "Complete XML metadata",
                                    "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/19/K/EQ/2020/2/13/0/metadata.xml"
                                },
                                "tki": {
                                    "title": "True color image",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3,
                                        2,
                                        1
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/TKI.jp2"
                                },
                                "B01": {
                                    "title": "Band 1 (coastal)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        0
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B01.jp2"
                                },
                                "B02": {
                                    "title": "Band 2 (blue)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B02.jp2"
                                },
                                "B03": {
                                    "title": "Band 3 (green)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        2
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B03.jp2"
                                },
                                "B04": {
                                    "title": "Band 4 (red)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        3
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B04.jp2"
                                },
                                "B05": {
                                    "title": "Band 5",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        4
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B05.jp2"
                                },
                                "B06": {
                                    "title": "Band 6",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        5
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B06.jp2"
                                },
                                "B07": {
                                    "title": "Band 7",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        6
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B07.jp2"
                                },
                                "B08": {
                                    "title": "Band 8 (nir)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        7
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B08.jp2"
                                },
                                "B8A": {
                                    "title": "Band 8A",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        8
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B08.jp2"
                                },
                                "B09": {
                                    "title": "Band 9",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        9
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B09.jp2"
                                },
                                "B10": {
                                    "title": "Band 10 (cirrus)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        10
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B10.jp2"
                                },
                                "B11": {
                                    "title": "Band 11 (swir16)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        11
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B11.jp2"
                                },
                                "B12": {
                                    "title": "Band 12 (swir22)",
                                    "type": "image/jp2",
                                    "eo:bands": [
                                        12
                                    ],
                                    "href": "https://sentinel-s2-l1c.s3.amazonaws.com/tiles/19/K/EQ/2020/2/13/0/B11.jp2"
                                }
                            },
                            "links": [
                                {
                                    "rel": "self",
                                    "href": "https://sat-api.developmentseed.org/collections/sentinel-2-l1c/items/S2A_19KEQ_20200213_0"
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
                            "href": "https://sat-api.developmentseed.org/stac/search?datetime=2019-12-01T00%3A00%3A00%2F2020-02-13T23%3A59%3A59&intersects=%5Bobject%20Object%5D&query=%5Bobject%20Object%5D&page=2&limit=1"
                        }
                    ]
                }
            },
            "CBERS4-AWS": {
                "CBERS4MUX": {
                    'context': {
                        'limit': 1,
                        'matched': 1,
                        'page': 1,
                        'returned': 1
                    },
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
                    'context': {
                        'limit': 1,
                        'matched': 1,
                        'page': 1,
                        'returned': 1
                    },
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

        body = {
            "providers": [
                {
                    "name": "INPE-CDSR",
                    "method": "POST",
                    "collections": [
                        {"name": "CBERS4_AWFI_L4_DN"},
                        {"name": "CBERS4A_WFI_L4_DN"},
                        {"name": "CBERS4A_WPM_L2_DN"}
                    ],
                    "query": {
                        "cloud_cover": {
                            "gte": 0,
                            "lte": 10
                        }
                    }
                },
                {
                    "name": "LANDSAT8-SENTINEL2-AWS",
                    "method": "POST",
                    "collections": [
                        {"name": "landsat-8-l1"},
                        {"name": "sentinel-2-l1c"}
                    ],
                    "query": {
                        "eo:cloud_cover": {
                            "gte": 0,
                            "lte": 10
                        }
                    }
                },
                {
                    "name": "CBERS4-AWS",
                    "method": "GET",
                    "collections": [
                        {"name": "CBERS4MUX"},
                        {"name": "CBERS4AWFI"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body)


class TestStacComposeStacSearchError(StacComposeTester):

    def setUp(self):
        self.set_urn(URN)

    # Provider: CBERS4-AWS

    def test__post__stac_compose_stac_search__cbers4_aws_cbers4mux__limit_1000__timeout(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        limit = 1000

        expected = {
            "CBERS4-AWS": {
                "CBERS4MUX": {
                    'context': {
                        'limit': limit,
                        'matched': 0,
                        'page': 1,
                        'returned': 0,
                        'meta': {
                            'error': '504 Gateway Timeout: {\'message\': \'Endpoint request timed out\'}'
                        }
                    },
                    "type": "FeatureCollection",
                    "features": []
                },
                "CBERS4AWFI": {
                    'context': {
                        'limit': limit,
                        'matched': 0,
                        'page': 1,
                        'returned': 0,
                        'meta': {
                            'error': '504 Gateway Timeout: {\'message\': \'Endpoint request timed out\'}'
                        }
                    },
                    "type": "FeatureCollection",
                    "features": []
                }
            }
        }

        body = {
            "providers": [
                {
                    "name": "CBERS4-AWS",
                    "method": "GET",
                    "collections": [
                        {"name": "CBERS4MUX"},
                        {"name": "CBERS4AWFI"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": limit
        }

        self.post(expected, body=body)

    # Other

    def test__post__stac_compose_stac_search__abc_cdsr__400_bad_request__provider_does_not_exist(self):
        """POST http://localhost:8089/stac-compose/stac/search/"""

        expected = {
            'code': 400,
            'description': 'Provider `ABC-CDSR` does not exist.',
            'name': 'Bad Request'
        }

        body = {
            "providers": [
                {
                    "name": "ABC-CDSR",
                    "method": "POST",
                    "collections": [
                        {"name": "CBERS4_XYZ_L4_SR"}
                    ]
                }
            ],
            "bbox": [-68.0273437, -25.0059726, -34.9365234, 0.3515602],
            "time": "2019-12-01T00:00:00/2020-02-13T23:59:59",
            "limit": 1
        }

        self.post(expected, body=body, expected_status_code=400)
