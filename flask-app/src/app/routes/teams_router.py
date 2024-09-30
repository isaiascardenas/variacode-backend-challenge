from flask import Blueprint, g

from app.controllers.teams_controller import TeamsController

team_blueprint = Blueprint("team", __name__, url_prefix="/teams")


@team_blueprint.route("/")
def list_teams():
    session = g.session
    teams_list = TeamsController(session).list_teams()

    return [team.model_dump(mode="json") for team in teams_list]


@team_blueprint.route("/create")
def store_team():
    session = g.session
    team = TeamsController(session).store_team(
        team_data={"name": "prueba", "surname": "testtest"}
    )

    return team.model_dump(mode="json")
