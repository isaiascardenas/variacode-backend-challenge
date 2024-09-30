from dotenv import load_dotenv
import os

from .models import (
    AppConfig,
    Config,
    DatabaseConfig,
    PagerDutyConfig,
)


DEFAULT_CONFIG_PATH: str = "./../../.env"


def load_config(path: str | None = None) -> Config:
    basedir = os.path.abspath(os.path.dirname(__file__))

    if path is None:
        load_dotenv(os.path.join(basedir, DEFAULT_CONFIG_PATH))
    else:
        load_dotenv(path)

    application_config = AppConfig(
        debug=os.environ.get("FLASK_ENV", "") == "development",
        app_name=os.environ.get("FLASK_APP", ""),
        app_port=int(os.environ.get("FLASK_RUN_PORT", "3000")),
        app_host=os.environ.get("FLASK_RUN_HOST", "0.0.0.0"),
    )

    database_config = DatabaseConfig(
        host=os.environ.get("DATABASE_HOST", ""),
        port=int(os.environ.get("DATABASE_PORT", "0")),
        database=os.environ.get("DATABASE_NAME", ""),
        user=os.environ.get("DATABASE_USER", ""),
        password=os.environ.get("DATABASE_PASSWORD", ""),
        echo=bool(os.environ.get("DATABASE_ECHO")),
    )

    pager_duty_config = PagerDutyConfig(
        api_key=os.environ.get("PAGER_DUTY_API_KEY", ""),
        api_endpoint=os.environ.get("PAGER_DUTY_API_ENDPOINT", ""),
    )

    return Config(application_config, database_config, pager_duty_config)
