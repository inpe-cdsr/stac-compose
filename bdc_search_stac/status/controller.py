from bdc_search_stac.status import ns
from bdc_core.utils.flask import APIResource

api = ns

@api.route('/')
class StatusController(APIResource):
    """
    Full route: http://localhost:5000/stac-compose/status/
    """

    def get(self):
        """
        Returns application status
        """
        return {
            "status": "Running"
        }
