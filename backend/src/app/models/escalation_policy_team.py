from sqlalchemy import Column, ForeignKey, String

from .base import BaseModel


class EscalationPolicyTeam(BaseModel):
    __tablename__ = "escalation_policy_team"

    escalation_policy_id = Column(
        "escalation_policy_id",
        String,
        ForeignKey("escalation_policies.id"),
        primary_key=True,
    )
    team_id = Column("team_id", String, ForeignKey("teams.id"), primary_key=True)
