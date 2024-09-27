from sqlalchemy.orm import Mapped, mapped_column

from .base import CreatedUpdatedAtMixin


class User(CreatedUpdatedAtMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str | None] = mapped_column(unique=True)
    surname: Mapped[str]
