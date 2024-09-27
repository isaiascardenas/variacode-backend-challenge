from flask import Flask

from .users_router import user_blueprint


def register(app: Flask) -> None:
    app.register_blueprint(user_blueprint)
