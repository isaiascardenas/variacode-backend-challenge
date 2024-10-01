from flask import Blueprint, g

from app.controllers.incidents_controller import IncidentsController

incident_blueprint = Blueprint("incident", __name__, url_prefix="/incidents")


@incident_blueprint.route("/")
def list_incidents():
    session = g.session
    incidents_list = IncidentsController(session).list_incidents()

    return [incident.model_dump(mode="json") for incident in incidents_list]


@incident_blueprint.route("/create")
def store_incident():
    session = g.session
    incident = IncidentsController(session).store_incident(
        incident_data={"name": "prueba", "surname": "testtest"}
    )

    return incident.model_dump(mode="json")
