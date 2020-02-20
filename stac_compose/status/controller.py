
#!/usr/bin/env python3

from bdc_core.utils.flask import APIResource

from stac_compose.status import ns


api = ns


@api.route('/')
class StatusController(APIResource):
    """
    Full route: http://localhost:8089/stac-compose/status/
    """

    def get(self):
        """
        Returns application status
        """
        return {
            "status": "Running"
        }
