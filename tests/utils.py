#!/usr/bin/env python3

"""Unit-test for STAC Compose operations related to /stac-compose/providers/ endpoint."""

from unittest import TestCase
from json import loads

from stac_compose import app as stac_compose_app


class StacComposeTesterException(Exception):
    def __init__(self, message):
        super().__init__(message)


class StacComposeTester(TestCase):

    def __init__(self, *args, **kwargs):
        # it is necessary to extend from TestCase and override __init__ correctly
        TestCase.__init__(self, *args, **kwargs)

        self.app = stac_compose_app.test_client()
        self.__urn__ = None
        self.__headers__ = {}

    ######################################################################
    # GETTERS
    ######################################################################

    def get_urn(self):
        if self.__urn__ is None:
            raise StacComposeTesterException('There is not an available URN. You must set one by using StacComposeTester.set_urn() method.')

        return self.__urn__

    def set_urn(self, urn):
        self.__urn__ = urn

    def get_headers(self):
        return self.__headers__

    def set_headers(self, headers):
        self.__headers__ = headers

    ######################################################################
    # UTILS
    ######################################################################

    # def get_headers(self, headers=None):
    #     # if 'headers' is empty, then add the cached 'self.__headers__'
    #     if headers is None:
	#         headers = self.__headers__
    #     # else it returns the passed 'headers'
    #     return headers

    # def error_asserts(self, response, status_code, error_message):
    #     # method to encapsulate the error asserts

    #     self.assertEqual(response.status_code, status_code)
    #     self.assertEqual(response.data, error_message)

    ######################################################################
    # GET, POST, DELETE METHODS
    ######################################################################

    def __get(self, query_string=''):
        return self.app.get(self.get_urn(), query_string=query_string, headers=self.__headers__)

    def get(self, expected_data={}, query_string={}, expected_status_code=200, expected_content_type='application/json'):
        result = self.__get(query_string)

        # print('\nStacComposeTester.get() - self.get_urn(): ', self.get_urn())
        # print('\nStacComposeTester.get() - query_string: ', query_string)

        self.assertEqual(expected_status_code, result.status_code)
        self.assertIn(expected_content_type, result.content_type)

        # get the JSON in dict form
        data = loads(result.data)

        # print('\nStacComposeTester.get() - data: ', data)

        self.assertEqual(expected_data, data)

        return data

    def post(self, body):
        response = self.app.post(self.get_urn(), data=dumps(body), headers=self.__headers__)

        id = int(response.data.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(id, b"")

        return id

    def put(self, body):
        response = self.app.put(self.get_urn(), data=dumps(body), headers=self.__headers__)

        self.assertEqual(response.status_code, 200)

    def delete(self, query_string={}):
        response = self.app.delete(self.get_urn(), query_string=query_string, headers=self.__headers__)

        self.assertEqual(response.status_code, 200)

    ######################################################################
    # GET, POST, DELETE ERROR METHODS
    ######################################################################

    # def get_error(self, query_string="", status_code=500, error_message="", headers=None):
    #     headers = self.get_headers(headers=headers)

    #     response = self.app.get(self.get_urn(), query_string=query_string, headers=headers)

    #     self.error_asserts(response, status_code, error_message)

    # def post_error(self, body, status_code=500, error_message="", headers=None):
    #     headers = self.get_headers(headers=headers)

    #     response = self.app.post(self.get_urn(), data=dumps(body), headers=headers)

    #     self.error_asserts(response, status_code, error_message)

    # def put_error(self, body, status_code=500, error_message="", headers=None):
    #     headers = self.get_headers(headers=headers)

    #     response = self.app.put(self.get_urn(), data=dumps(body), headers=headers)

    #     self.error_asserts(response, status_code, error_message)

    # def delete_error(self, query_string="", status_code=500, error_message="", headers=None):
    #     headers = self.get_headers(headers=headers)

    #     response = self.app.delete(self.get_urn(), query_string=query_string, headers=headers)

    #     self.error_asserts(response, status_code, error_message)

