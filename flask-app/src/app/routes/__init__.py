from flask import Flask

from .users_router import user_blueprint
from .teams_router import team_blueprint


def register(app: Flask) -> None:
    app.register_blueprint(user_blueprint)
    app.register_blueprint(team_blueprint)
