from sqlalchemy.orm import Mapped, mapped_column

from .base import CreatedUpdatedAtMixin


class Service(CreatedUpdatedAtMixin):
    __tablename__ = "services"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(unique=True)
    team_id: Mapped[str | None] = mapped_column(nullable=True)
    escalation_policy_id: Mapped[str | None] = mapped_column(nullable=True)
