from pydantic import BaseModel, ConfigDict
from typing import Optional
from .team_schema import Team


class EscalationPolicyCreate(BaseModel):
    name: str
    teams: Optional[list[Team]] = []


class EscalationPolicy(EscalationPolicyCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class EscalationPolicyUpdate(EscalationPolicyCreate):
    pass
