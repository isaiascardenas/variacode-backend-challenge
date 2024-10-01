from pydantic import BaseModel, ConfigDict


class ServiceCreate(BaseModel):
    name: str
    team_id: str
    escalation_policy_id: str


class Service(ServiceCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class ServiceUpdate(ServiceCreate):
    pass
