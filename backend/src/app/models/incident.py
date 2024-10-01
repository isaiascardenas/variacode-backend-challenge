from sqlalchemy.orm import Mapped, mapped_column

from .base import CreatedUpdatedAtMixin


class Incident(CreatedUpdatedAtMixin):
    __tablename__ = "incidents"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    status: Mapped[str]
    service_id: Mapped[str]
    escalation_policy_id: Mapped[str]
