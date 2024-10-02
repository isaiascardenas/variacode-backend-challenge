from sqlalchemy.sql import text
import pandas as pd

from app.models.base import BaseModel
from .base import Controller


class ReportsController(Controller[BaseModel]):
    def list_services(self) -> list[dict]:
        stmt = text("""
            SELECT
                services.id AS service_id,
                services.name AS service,
                COUNT(incidents.id) AS incidents_count
            FROM incidents
                JOIN services ON incidents.service_id = services.id
            GROUP BY services.id
            """)

        df = pd.read_sql(stmt, self.session.bind)
        df["incidents_count"] = df["incidents_count"].astype(str)

        return df.to_dict("records")

    def get_services_with_incidents(self) -> list[dict]:
        stmt = text("""
            SELECT
                services.id AS service_id,
                services.name AS service,
                incidents.id AS incident_id,
                incidents.title AS incident,
                incidents.status AS status
            FROM incidents
                JOIN services ON incidents.service_id = services.id
            """)

        df = pd.read_sql(stmt, self.session.bind)

        return df.to_dict("records")

    def get_incidents_by_service_id(self, service_id: str = "") -> list[dict]:
        if not service_id:
            stmt = text("""
                SELECT
                    incidents.id,
                    incidents.title,
                    incidents.status,
                    incidents.service_id
                FROM incidents
                """)
        else:
            stmt = text(
                """
                SELECT
                    incidents.id,
                    incidents.title,
                    incidents.status,
                    incidents.service_id
                FROM incidents
                WHERE
                    incidents.service_id = '{}'
                """.format(service_id)
            )

        df = pd.read_sql(stmt, self.session.bind)

        return df.to_dict("records")

    def get_incidents_by_status(self, status: str = "") -> list[dict]:
        if not status:
            stmt = text("""
                SELECT
                    incidents.id,
                    incidents.title,
                    incidents.status,
                    incidents.service_id
                FROM incidents
                """)
        else:
            stmt = text(
                """
                SELECT
                    incidents.id,
                    incidents.title,
                    incidents.status,
                    incidents.service_id
                FROM incidents
                WHERE
                    incidents.status = '{}'
                """.format(status)
            )

        df = pd.read_sql(stmt, self.session.bind)

        return df.to_dict("records")

    def get_teams_with_services(self) -> list[dict]:
        stmt = text("""
            SELECT
                teams.id AS team_id,
                teams.name AS team,
                services.id AS service_id,
                services.name AS service
            FROM teams
                JOIN services ON teams.id = services.team_id
            """)

        df = pd.read_sql(stmt, self.session.bind)

        return df.to_dict("records")

    def get_escalation_policies(self) -> list[dict]:
        stmt = text("""
            SELECT
                escalation_policies.id AS escalation_policy_id,
                escalation_policies.name AS team,
                services.id AS service_id,
                services.name AS service,
                teams.id AS team_id,
                teams.name AS team
            FROM
                escalation_policy_team
                RIGHT JOIN escalation_policies ON escalation_policy_team.escalation_policy_id = escalation_policies.id
                LEFT JOIN services ON services.escalation_policy_id = escalation_policies.id
                LEFT JOIN teams ON teams.id = escalation_policy_team.team_id
            """)

        df = pd.read_sql(stmt, self.session.bind)

        return df.to_dict("records")
