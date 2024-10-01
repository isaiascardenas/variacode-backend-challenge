from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: str | None


class User(UserCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserCreate):
    pass
