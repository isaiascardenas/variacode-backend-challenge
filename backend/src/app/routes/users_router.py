from flask import Blueprint, Response, g

from app.controllers.users_controller import UsersController

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


@user_blueprint.route("/show")
def show():
    return """
        <html><body>
        Users report. <a href="/users/report">download</a>
        </body></html>
        """


@user_blueprint.route("/report")
def download():
    csv = "1,2,3\n4,5,6\n"

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=myplot.csv"},
    )
