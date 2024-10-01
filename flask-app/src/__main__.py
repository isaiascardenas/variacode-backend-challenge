from flask import Flask

from app import middlewares, routes
from config import load_config
from database.session import create_session_maker
from app.services.pager_duty.pager_duty_service import PagerDutyService


def main() -> Flask:
    config = load_config()
    session_maker = create_session_maker(config.db_config.full_url)

    app = Flask(__name__)

    middlewares.register(app, session_maker)
    routes.register(app)

    with app.app_context():
        pager_duty_client = PagerDutyService()
        pager_duty_client.setup(config)

    return (app, config)


def run():
    app, config = main()
    app.run(
        host=config.app_config.app_host,
        port=config.app_config.app_port,
        # debug=config.app_config.debug,
        debug=False,
    )


if __name__ == "__main__":
    run()
