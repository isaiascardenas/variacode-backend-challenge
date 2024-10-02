from flask import Blueprint, g, request

from app.controllers.dashboard_controller import DashboardController

dashboard_blueprint = Blueprint("dashbaord", __name__, url_prefix="/dashboard")


@dashboard_blueprint.route("/services")
def list_services():
    session = g.session
    services_list = DashboardController(session).get_services()
    serialized_services = [service.model_dump(mode="json") for service in services_list]

    return {
        "total": len(services_list),
        "services": [
            dict({k: v for k, v in service.items() if k not in {"incidents"}})
            for service in serialized_services
        ],
    }


@dashboard_blueprint.route("/services/incidents")
def get_services_with_incidents():
    session = g.session
    services_list = DashboardController(session).get_services_with_incidents()
    serialized_services = [service.model_dump(mode="json") for service in services_list]

    return {
        "total": len(serialized_services),
        "services": [
            dict(service, incidents_count=len(service["incidents"]))
            for service in serialized_services
        ],
    }


@dashboard_blueprint.route("/incidents")
def get_incidents_by():
    session = g.session
    search_by = request.args.get("search_by", None)
    search_value = request.args.get("search_value", None)
    incidents_list = []

    if search_by == "service_id":
        incidents_list = DashboardController(session).get_incidents_by_service_id(
            search_value
        )
    elif search_by == "status":
        incidents_list = DashboardController(session).get_incidents_by_status(
            search_value
        )
    else:
        incidents_list = DashboardController(session).get_incidents_by_service_id()

    return {
        "total": len(incidents_list),
        "incidents": [incident.model_dump(mode="json") for incident in incidents_list],
    }


@dashboard_blueprint.route("/teams/services")
def get_teams_with_services():
    session = g.session
    team_list = DashboardController(session).get_teams_with_services()
    serialized_teams = [team.model_dump(mode="json") for team in team_list]

    return {
        "total": len(serialized_teams),
        "teams": [
            dict(team, services_count=len(team["services"]))
            for team in serialized_teams
        ],
    }


@dashboard_blueprint.route("/escalation_policies")
def get_escalation_policies():
    session = g.session
    ep_list = DashboardController(session).get_escalation_policies()
    serialized_ep = [ep.model_dump(mode="json") for ep in ep_list]

    return {
        "total": len(serialized_ep),
        "escalation_policies": serialized_ep,
    }
