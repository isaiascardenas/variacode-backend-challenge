from dataclasses import dataclass


@dataclass
class AppConfig:
    debug: bool
    app_name: str
    app_port: int
    app_host: str


@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    echo: bool

    # default values
    rdbms: str = "mysql"
    connector: str = "pymysql"

    @property
    def full_url(self) -> str:
        return "{}+{}://{}:{}@{}:{}/{}".format(
            self.rdbms,
            self.connector,
            self.user,
            self.password,
            self.host,
            self.port,
            self.database,
        )


@dataclass
class PagerDutyConfig:
    api_key: str
    api_endpoint: str


@dataclass
class Config:
    app_config: AppConfig
    db_config: DatabaseConfig
    pager_duty_config: PagerDutyConfig
