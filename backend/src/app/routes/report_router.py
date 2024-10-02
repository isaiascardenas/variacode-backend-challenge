from flask import Blueprint, Response, g, request

from app.controllers.reports_controller import ReportsController
from app.services.report_service.report_service import get_csv_string

report_blueprint = Blueprint("report", __name__, url_prefix="/reports")


@report_blueprint.route("/services")
def list_services():
    session = g.session
    data = ReportsController(session).list_services()

    if not data:
        return show_empty_report()

    return Response(
        get_csv_string(
            data=data,
            headers=list(data[0].keys()),
        ),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=services_report.csv"},
    )


@report_blueprint.route("/services/incidents")
def get_services_with_incidents():
    session = g.session
    data = ReportsController(session).get_services_with_incidents()

    if not data:
        return show_empty_report()

    return Response(
        get_csv_string(
            data=data,
            headers=list(data[0].keys()),
        ),
        mimetype="text/csv",
        headers={
            "Content-disposition": "attachment; filename=services_with_incidents_report.csv"
        },
    )


@report_blueprint.route("/incidents")
def get_incidents_by():
    session = g.session
    search_by = request.args.get("search_by", None)
    search_value = request.args.get("search_value", None)
    data = []
    report_name = "incidents_report.csv"

    if search_by == "service_id":
        report_name = "incidents_by_service_id_report.csv"
        data = ReportsController(session).get_incidents_by_service_id(search_value)
    elif search_by == "status":
        report_name = "incidents_by_status_report.csv"
        data = ReportsController(session).get_incidents_by_status(search_value)
    else:
        data = ReportsController(session).get_incidents_by_service_id()

    if not data:
        return show_empty_report()

    return Response(
        get_csv_string(
            data=data,
            headers=list(data[0].keys()),
        ),
        mimetype="text/csv",
        headers={"Content-disposition": f"attachment; filename={report_name}"},
    )


@report_blueprint.route("/teams/services")
def get_teams_with_services():
    session = g.session
    data = ReportsController(session).get_teams_with_services()

    if not data:
        return show_empty_report()

    return Response(
        get_csv_string(
            data=data,
            headers=list(data[0].keys()),
        ),
        mimetype="text/csv",
        headers={
            "Content-disposition": "attachment; filename=teams_with_services_report.csv"
        },
    )


@report_blueprint.route("/escalation_policies")
def get_escalation_policies():
    session = g.session
    data = ReportsController(session).get_escalation_policies()

    if not data:
        return show_empty_report()

    return Response(
        get_csv_string(
            data=data,
            headers=list(data[0].keys()),
        ),
        mimetype="text/csv",
        headers={
            "Content-disposition": "attachment; filename=escalation_policies_report.csv"
        },
    )


def show_empty_report():
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
