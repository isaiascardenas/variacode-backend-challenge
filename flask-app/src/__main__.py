from flask import Flask

from app import middlewares, routes
from config import load_config
from database.session import create_session_maker


def main() -> Flask:
    config = load_config()
    session_maker = create_session_maker(config.db_config.full_url)

    app = Flask(__name__)

    middlewares.register(app, session_maker)
    routes.register(app)

    print("!!!")
    print(config.app_config.app_port)
    print("!!!")

    return app


def run():
    app = main()
    app.run(host="0.0.0.0", port=3000, debug=True)


if __name__ == "__main__":
    run()
