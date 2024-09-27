from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    surname: str | None


class User(UserCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserCreate):
    pass
