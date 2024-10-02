from pydantic import BaseModel, ConfigDict
from typing import Optional
from .service_schema import Service


class TeamCreate(BaseModel):
    name: str
    services: Optional[list[Service]] = []


class Team(TeamCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class TeamUpdate(TeamCreate):
    pass
