from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.incident import Incident as IncidentModel
from app.models.service import Service as ServiceModel
from app.models.team import Team as TeamModel
from app.models.escalation_policy import EscalationPolicy as EscalationPolicyModel
from app.schemas.service_schema import Service as ServiceSchema
from app.schemas.incident_schema import Incident as IncidentSchema
from app.schemas.team_schema import Team as TeamSchema
from app.schemas.escalation_policy_schema import (
    EscalationPolicy as EscalationPolicySchema,
)

from .base import Controller


class DashboardController(Controller[ServiceModel]):
    def get_services(self) -> list[ServiceSchema]:
        stmt = select(ServiceModel)
        result = self.session.scalars(stmt.order_by(ServiceModel.id)).fetchall()

        return TypeAdapter(list[ServiceSchema]).validate_python(result)

    def get_services_with_incidents(self) -> list[ServiceSchema]:
        stmt = select(ServiceModel)
        result = self.session.scalars(stmt.order_by(ServiceModel.id)).fetchall()

        return TypeAdapter(list[ServiceSchema]).validate_python(result)

    def get_incidents_by_service_id(self, service_id: str = "") -> list[IncidentSchema]:
        if not service_id:
            stmt = select(IncidentModel)
        else:
            stmt = select(IncidentModel).where(IncidentModel.service_id == service_id)

        result = self.session.scalars(stmt.order_by(IncidentModel.id)).fetchall()

        return TypeAdapter(list[IncidentSchema]).validate_python(result)

    def get_incidents_by_status(self, status: str = "") -> list[IncidentSchema]:
        if not status:
            stmt = select(IncidentModel)
        else:
            stmt = select(IncidentModel).where(IncidentModel.status == status)

        result = self.session.scalars(stmt.order_by(IncidentModel.id)).fetchall()

        return TypeAdapter(list[IncidentSchema]).validate_python(result)

    def get_teams_with_services(self) -> list[TeamSchema]:
        stmt = select(TeamModel)
        result = self.session.scalars(stmt.order_by(TeamModel.id)).fetchall()

        return TypeAdapter(list[TeamSchema]).validate_python(result)

    def get_escalation_policies(self) -> list[EscalationPolicySchema]:
        stmt = select(EscalationPolicyModel)
        result = self.session.scalars(
            stmt.order_by(EscalationPolicyModel.id)
        ).fetchall()

        return TypeAdapter(list[EscalationPolicySchema]).validate_python(result)
