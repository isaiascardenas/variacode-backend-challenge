from pydantic import BaseModel, ConfigDict


class TeamCreate(BaseModel):
    name: str


class Team(TeamCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class TeamUpdate(TeamCreate):
    pass
