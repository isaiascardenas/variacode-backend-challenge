from flask import Blueprint, g

from app.controllers.users_controller import UsersController
from app.services.pager_duty.pager_duty_service import PagerDutyService

user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/")
def list_users():
    session = g.session
    users_list = UsersController(session).list_users()

    return [user.model_dump(mode="json") for user in users_list]


@user_blueprint.route("/create")
def store_user():
    session = g.session
    user = UsersController(session).store_user(
        user_data={"name": "prueba", "surname": "testtest"}
    )

    return user.model_dump(mode="json")


@user_blueprint.route("/test")
def test_endpoint():
    # pager_duty_client = PagerDutyService(access_token="u+b4CCjDZsXfuxx-w_fw")

    # response = pager_duty_client.fetch_users()
    # response = pager_duty_client.fetch_services()
    # response = pager_duty_client.fetch_incidents()
    # response = pager_duty_client.seed_users()

    return "<h1>Done!</h1>"
