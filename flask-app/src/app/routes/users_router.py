from flask import Blueprint, g

from app.controllers.users_controller import UsersController

user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/")
def list_users():
    session = g.session
    users_list = UsersController(session).list_users()
    return [user.model_dump(mode="json") for user in users_list]
