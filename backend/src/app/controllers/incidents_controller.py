from pydantic import TypeAdapter
from sqlalchemy import select
from sqlalchemy.sql import text
from sqlalchemy.orm import joinedload
import pandas as pd

from app.models.incident import Incident as IncidentModel
from app.models.service import Service as ServiceModel
from app.schemas.incident_schema import Incident as IncidentSchema

from .base import Controller


class IncidentsController(Controller[IncidentModel]):
    def list_incidents(self, group_by: str = "") -> list[IncidentSchema]:
        stmt = text("""
            SELECT
                services.id AS service_id,
                services.name AS service,
                COUNT(incidents.id) AS incidents_count
            FROM incidents
                JOIN services ON incidents.service_id = services.id
            GROUP BY services.id
            """)
        # result = self.session.execute(stmt)

        df = pd.read_sql(stmt, self.session.bind)
        # print(df.values.tolist())

        # return df.values.tolist()

        return [
            dict(zip(("service_id", "service", "incidents_count"), row))
            for row in df.values.tolist()
        ]

        stmt = (
            select(IncidentModel, ServiceModel)
            .options(joinedload(IncidentModel.service))
            .join(IncidentModel.service)
            .where(IncidentModel.status == "resolved")
        )
        result = self.session.scalars(stmt.order_by(IncidentModel.id)).fetchall()

        return TypeAdapter(list[IncidentSchema]).validate_python(result)

    def get_grouped_incidents(self, group_by: str = "") -> list[IncidentSchema]:
        stmt = text("""
            SELECT
                services.id AS service_id,
                services.name AS service,
                COUNT(incidents.id) AS incidents_count
            FROM incidents
                JOIN services ON incidents.service_id = services.id
            GROUP BY services.id
            """)
        # result = self.session.execute(stmt)

        df = pd.read_sql(stmt, self.session.bind)
        # print(df.values.tolist())

        # return df.values.tolist()

        return [
            dict(zip(("service_id", "service", "incidents_count"), row))
            for row in df.values.tolist()
        ]

    def store_incident(self, incident_data: dict) -> IncidentSchema:
        incident = IncidentModel(**incident_data)
        self.session.add(incident)
        self.session.commit()

        return TypeAdapter(IncidentSchema).validate_python(incident)
