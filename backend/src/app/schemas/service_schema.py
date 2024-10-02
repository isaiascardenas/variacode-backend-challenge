from pydantic import BaseModel, ConfigDict
from typing import Optional
from .incident_schema import Incident


class ServiceCreate(BaseModel):
    name: str
    team_id: Optional[str] = None
    escalation_policy_id: str
    incidents: Optional[list[Incident]] = []


class Service(ServiceCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class ServiceUpdate(ServiceCreate):
    pass
