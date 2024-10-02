from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .team import Team
from .escalation_policy_team import EscalationPolicyTeam
from .base import CreatedUpdatedAtMixin


class EscalationPolicy(CreatedUpdatedAtMixin):
    __tablename__ = "escalation_policies"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(unique=True)

    teams: Mapped[List[Team]] = relationship("Team", secondary="escalation_policy_team")
