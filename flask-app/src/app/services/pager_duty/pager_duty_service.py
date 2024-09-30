from config.models import (
    Config,
)
from database.session import create_session_maker
from app.models.user import User as UserModel
from app.models.team import Team as TeamModel
from ..requests_client import RequestsClient


class PagerDutyService:
    client: RequestsClient
    base_url: str

    def setup(self, config: Config):
        self.base_url = config.pager_duty_config.api_endpoint
        self.client = RequestsClient(
            self.base_url, access_token=config.pager_duty_config.api_key
        )
        db_session = create_session_maker(config.db_config.full_url)

        self.seed_teams(db_session)
        self.seed_users(db_session)

    def fetch_users(self):
        return self.client.get("/users", query_params={"total": "true"})

    def fetch_teams(self):
        return self.client.get("/teams", query_params={"total": "true"})

    def fetch_services(self):
        return self.client.get("/services", query_params={"total": "true"})

    def fetch_incidents(self):
        return self.client.get("/incidents", query_params={"total": "true"})

    def fetch_escalation_policies(self):
        return self.client.get("/escalation_policies", query_params={"total": "true"})

    def seed_teams(self, db_session):
        records = self.fetch_teams()

        for record in records.json()["teams"]:
            model = TeamModel(
                **{
                    "id": record["id"],
                    "name": record["name"],
                }
            )
            db_session.add(model)
            db_session.commit()

    def seed_users(self, db_session):
        records = self.fetch_users()

        for record in records.json()["users"]:
            model = UserModel(
                **{
                    "id": record["id"],
                    "name": record["name"],
                    "email": record["email"],
                }
            )
            db_session.add(model)
            db_session.commit()
