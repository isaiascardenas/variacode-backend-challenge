from flask import Blueprint, Response, g

from app.controllers.services_controller import ServicesController
from app.services.report_service.report_service import get_csv_string

service_blueprint = Blueprint("service", __name__, url_prefix="/services")


@service_blueprint.route("/")
def list_services():
    session = g.session
    services_list = ServicesController(session).list_services()

    return {
        "total": len(services_list),
        "services": [service.model_dump(mode="json") for service in services_list],
    }


@service_blueprint.route("/incidents")
def get_incidents():
    session = g.session
    services_list = ServicesController(session).get_grouped_incidents()

    return services_list

    # return {
    #     "total": len(services_list),
    #     "services": [service.model_dump(mode="json") for service in services_list],
    # }


@service_blueprint.route("/create")
def store_service():
    session = g.session
    service = ServicesController(session).store_service(
        service_data={"name": "prueba", "surname": "testtest"}
    )

    return service.model_dump(mode="json")


@service_blueprint.route("/show")
def show():
    return """
        <html><body>
        Services report. <a href="/services/report">download</a>
        </body></html>
        """


@service_blueprint.route("/report")
def download():
    session = g.session
    services_list = ServicesController(session).list_services()

    if not services_list:
        return """
            <html><body>
            <script>
            function showAlert() {
            alert("The report its empty, no data found");
            }
            showAlert();
            </script>
            </body></html>
            """

    csv = get_csv_string(
        data=[service.model_dump(mode="json") for service in services_list],
        headers=list(services_list[0].model_dump(mode="json").keys()),
    )

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=services_report.csv"},
    )
