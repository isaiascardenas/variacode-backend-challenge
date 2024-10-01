from sqlalchemy.sql import text
from config.models import (
    Config,
)
from ..requests_client import RequestsClient
from database.session import create_session_maker
from app.models.user import User
from app.models.team import Team
from app.models.service import Service
from app.models.incident import Incident
from app.models.escalation_policy import EscalationPolicy


class PagerDutyService:
    client: RequestsClient
    base_url: str

    PAGE_SIZE = 10

    def setup(self, config: Config):
        self.base_url = config.pager_duty_config.api_endpoint
        self.client = RequestsClient(
            self.base_url, access_token=config.pager_duty_config.api_key
        )
        db_session = create_session_maker(config.db_config.full_url)

        self.seed_teams(db_session)
        self.seed_users(db_session)
        self.seed_escalation_policies(db_session)
        self.seed_services(db_session)
        self.seed_incidents(db_session)

    def fetch_teams(self, params):
        return self.client.get("/teams", query_params=params)

    def fetch_users(self, params):
        return self.client.get("/users", query_params=params)

    def fetch_services(self, params):
        return self.client.get("/services", query_params=params)

    def fetch_incidents(self, params):
        return self.client.get("/incidents", query_params=params)

    def fetch_escalation_policies(self, params):
        return self.client.get("/escalation_policies", query_params=params)

    def seed_teams(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = self.fetch_teams(query_params).json()
            total = response["total"]
            records = response["teams"]

            offset += len(records)

            for record in records:
                model = Team(
                    **{
                        "id": record["id"],
                        "name": record["name"],
                    }
                )
                db_session.add(model)

            db_session.commit()

    def seed_users(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = self.fetch_users(query_params).json()
            total = response["total"]
            records = response["users"]

            offset += len(records)

            for record in records:
                model = User(
                    **{
                        "id": record["id"],
                        "name": record["name"],
                        "email": record["email"],
                    }
                )
                db_session.add(model)
                db_session.commit()

                for team in record["teams"]:
                    db_session.execute(
                        text(
                            f"INSERT INTO team_user (team_id, user_id) VALUES ('{team['id']}', '{model.id}')"
                        )
                    )
                    db_session.commit()

    def seed_services(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = self.fetch_services(query_params).json()
            total = response["total"]
            records = response["services"]

            offset += len(records)

            for record in records:
                model = Service(
                    **{
                        "id": record["id"],
                        "name": record["name"],
                        "team_id": None
                        if not record["teams"]
                        else record["teams"][0]["id"],
                        "escalation_policy_id": None
                        if not record["escalation_policy"]
                        else record["escalation_policy"]["id"],
                    }
                )
                db_session.add(model)
                db_session.commit()

    def seed_incidents(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = self.fetch_incidents(query_params).json()
            total = response["total"]
            records = response["incidents"]

            offset += len(records)

            for record in records:
                model = Incident(
                    **{
                        "id": record["id"],
                        "title": record["title"],
                        "status": record["status"],
                        "service_id": record["service"]["id"],
                        "escalation_policy_id": record["escalation_policy"]["id"],
                    }
                )
                db_session.add(model)
                db_session.commit()

    def seed_escalation_policies(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = self.fetch_escalation_policies(query_params).json()
            total = response["total"]
            records = response["escalation_policies"]

            offset += len(records)

            for record in records:
                model = EscalationPolicy(
                    **{
                        "id": record["id"],
                        "name": record["name"],
                    }
                )
                db_session.add(model)
                db_session.commit()

                for team in record["teams"]:
                    db_session.execute(
                        text(
                            f"INSERT INTO escalation_policy_team (escalation_policy_id, team_id) VALUES ('{model.id}', '{team['id']}')"
                        )
                    )
                    db_session.commit()
