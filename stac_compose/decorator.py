#!/usr/bin/env python3

from functools import wraps
from traceback import format_exc, print_stack
from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError

from flask_api import status

from stac_compose.log import logging


def catch_generic_exceptions(function):

    def log_error_message(error_message):
        print_traceback = '{0}\n{1}'.format(error_message, format_exc())

        logging.critical('{0}() - {1}'.format(
            function.__name__,
            print_traceback
        ))

    @wraps(function)
    def wrapper(*args, **kwargs):
        error_message = 'catch_generic_exceptions() - An unexpected error ocurred. Please, contact the administrator.'

        try:
            # try to execute the function
            return function(*args, **kwargs)

        except HTTPException as error:
            error_dict = {
                'code': error.code,
                'description': error.description,
                'name': error.name
            }

            error_message += '\nHTTPException: {}'.format(error_dict)

            log_error_message(error_message)

            return error_dict, error_dict['code']

        except Exception as error:
            error_dict = {
                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'description': 'Unexpected exception ocurred',
                'name': 'Exception'
            }

            error_message += '\nException: {}'.format(error_dict)

            log_error_message(error_message)

            return error_dict, status.HTTP_500_INTERNAL_SERVER_ERROR

    return wrapper
