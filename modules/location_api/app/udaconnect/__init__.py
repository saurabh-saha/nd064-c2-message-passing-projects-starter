from app.udaconnect.models import Location  # noqa
from app.udaconnect.schemas import LocationSchema  # noqa


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_location_api

    api.add_namespace(udaconnect_location_api, path=f"/{root}")
