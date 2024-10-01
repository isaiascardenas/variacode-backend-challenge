from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.user import User as UserModel
from app.schemas.user_schema import User as UserSchema

from .base import Controller


class UsersController(Controller[UserModel]):
    def list_users(self) -> list[UserSchema]:
        stmt = select(UserModel)
        result = self.session.scalars(stmt.order_by(UserModel.id)).fetchall()

        return TypeAdapter(list[UserSchema]).validate_python(result)

    def store_user(self, user_data: dict) -> UserSchema:
        user = UserModel(**user_data)
        self.session.add(user)
        self.session.commit()

        return TypeAdapter(UserSchema).validate_python(user)
