from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .service import Service
from .base import CreatedUpdatedAtMixin


class Team(CreatedUpdatedAtMixin):
    __tablename__ = "teams"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(unique=True)

    services: Mapped[List["Service"]] = relationship(
        "Service", backref="team", lazy="select"
    )
