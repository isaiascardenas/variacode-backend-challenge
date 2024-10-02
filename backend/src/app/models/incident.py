from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

# from .service import Service
from .base import CreatedUpdatedAtMixin


class Incident(CreatedUpdatedAtMixin):
    __tablename__ = "incidents"

    id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    status: Mapped[str]
    service_id: Mapped[str] = mapped_column(ForeignKey("services.id"))
    escalation_policy_id: Mapped[str]

    # service: Mapped["Service"] = relationship(back_populates="incidents")
