from flask import Flask

from .users_router import user_blueprint
from .teams_router import team_blueprint
from .services_router import service_blueprint
from .incidents_router import incident_blueprint
from .escalation_policies_router import escalation_policy_blueprint


def register(app: Flask) -> None:
    app.register_blueprint(user_blueprint)
    app.register_blueprint(team_blueprint)
    app.register_blueprint(service_blueprint)
    app.register_blueprint(incident_blueprint)
    app.register_blueprint(escalation_policy_blueprint)
