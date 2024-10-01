from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.incident import Incident as IncidentModel
from app.schemas.incident_schema import Incident as IncidentSchema

from .base import Controller


class IncidentsController(Controller[IncidentModel]):
    def list_incidents(self) -> list[IncidentSchema]:
        stmt = select(IncidentModel)
        result = self.session.scalars(stmt.order_by(IncidentModel.id)).fetchall()

        return TypeAdapter(list[IncidentSchema]).validate_python(result)

    def store_incident(self, incident_data: dict) -> IncidentSchema:
        incident = IncidentModel(**incident_data)
        self.session.add(incident)
        self.session.commit()

        return TypeAdapter(IncidentSchema).validate_python(incident)
