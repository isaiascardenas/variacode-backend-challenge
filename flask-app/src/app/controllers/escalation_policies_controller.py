from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.escalation_policy import EscalationPolicy as EscalationPolicyModel
from app.schemas.escalation_policy_schema import (
    EscalationPolicy as EscalationPolicySchema,
)

from .base import Controller


class EscalationPoliciesController(Controller[EscalationPolicyModel]):
    def list_escalation_policies(self) -> list[EscalationPolicySchema]:
        stmt = select(EscalationPolicyModel)
        result = self.session.scalars(
            stmt.order_by(EscalationPolicyModel.id)
        ).fetchall()

        return TypeAdapter(list[EscalationPolicySchema]).validate_python(result)

    def store_escalation_policy(
        self, escalation_policy_data: dict
    ) -> EscalationPolicySchema:
        escalation_policy = EscalationPolicyModel(**escalation_policy_data)
        self.session.add(escalation_policy)
        self.session.commit()

        return TypeAdapter(EscalationPolicySchema).validate_python(escalation_policy)
