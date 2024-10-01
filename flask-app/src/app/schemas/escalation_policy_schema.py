from pydantic import BaseModel, ConfigDict


class EscalationPolicyCreate(BaseModel):
    name: str


class EscalationPolicy(EscalationPolicyCreate):
    id: str

    model_config = ConfigDict(from_attributes=True)


class EscalationPolicyUpdate(EscalationPolicyCreate):
    pass
