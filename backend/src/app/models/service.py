from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

from .incident import Incident
from .base import CreatedUpdatedAtMixin


class Service(CreatedUpdatedAtMixin):
    __tablename__ = "services"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(unique=True)
    team_id: Mapped[str] = mapped_column(ForeignKey("teams.id"), nullable=True)
    escalation_policy_id: Mapped[str | None] = mapped_column(nullable=True)

    incidents: Mapped[List["Incident"]] = relationship(
        "Incident", backref="service", lazy="select"
    )
