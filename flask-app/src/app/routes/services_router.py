from flask import Blueprint, g

from app.controllers.services_controller import ServicesController

service_blueprint = Blueprint("service", __name__, url_prefix="/services")


@service_blueprint.route("/")
def list_services():
    session = g.session
    services_list = ServicesController(session).list_services()

    return [service.model_dump(mode="json") for service in services_list]


@service_blueprint.route("/create")
def store_service():
    session = g.session
    service = ServicesController(session).store_service(
        service_data={"name": "prueba", "surname": "testtest"}
    )

    return service.model_dump(mode="json")
