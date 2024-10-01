import asyncio
from sqlalchemy.sql import text
from config.models import (
    Config,
)
from .requests_client import RequestsClient
from database.session import create_session_maker
from app.models.user import User
from app.models.team import Team
from app.models.service import Service
from app.models.incident import Incident
from app.models.escalation_policy import EscalationPolicy


class PagerDutyService:
    base_url: str
    api_key: str

    PAGE_SIZE = 10

    async def setup(self, config: Config):
        self.base_url = config.pager_duty_config.api_endpoint
        self.api_key = config.pager_duty_config.api_key

        db_session = create_session_maker(config.db_config.full_url)

        await self.seed_teams(db_session)
        await self.seed_users(db_session)
        await self.seed_escalation_policies(db_session)
        await self.seed_services(db_session)
        await self.seed_incidents(db_session)

    def fetch_teams(self, params):
        return RequestsClient(self.base_url, access_token=self.api_key).get(
            "/teams",
            query_params=params,
        )

    def fetch_users(self, params):
        return RequestsClient(self.base_url, access_token=self.api_key).get(
            "/users",
            query_params=params,
        )

    def fetch_services(self, params):
        return RequestsClient(self.base_url, access_token=self.api_key).get(
            "/services",
            query_params=params,
        )

    def fetch_incidents(self, params):
        return RequestsClient(self.base_url, access_token=self.api_key).get(
            "/incidents",
            query_params=params,
        )

    def fetch_escalation_policies(self, params):
        return RequestsClient(self.base_url, access_token=self.api_key).get(
            "/escalation_policies",
            query_params=params,
        )

    async def seed_teams(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = await asyncio.gather(self.fetch_teams(query_params))
            data = await response[0].json()

            total = data["total"]
            records = data["teams"]

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

    async def seed_users(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = await asyncio.gather(self.fetch_users(query_params))
            data = await response[0].json()

            total = data["total"]
            records = data["users"]

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

    async def seed_services(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = await asyncio.gather(self.fetch_services(query_params))
            data = await response[0].json()

            total = data["total"]
            records = data["services"]

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

    async def seed_incidents(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = await asyncio.gather(self.fetch_incidents(query_params))
            data = await response[0].json()

            total = data["total"]
            records = data["incidents"]

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

    async def seed_escalation_policies(self, db_session):
        offset = 0
        total = 1  # set total = 1 to force firt iteration

        while offset < total:
            query_params = {
                "total": "true",
                "limit": self.PAGE_SIZE,
                "offset": offset,
            }

            response = await asyncio.gather(
                self.fetch_escalation_policies(query_params)
            )
            data = await response[0].json()

            total = data["total"]
            records = data["escalation_policies"]

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
