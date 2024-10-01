from pydantic import BaseModel, ConfigDict


class IncidentCreate(BaseModel):
    title: str
    status: str
    service_id: str
    escalation_policy_id: str


class Incident(IncidentCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class IncidentUpdate(IncidentCreate):
    pass
