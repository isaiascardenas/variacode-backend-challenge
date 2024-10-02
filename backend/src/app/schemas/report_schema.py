from pydantic import BaseModel


class ExistingServices(BaseModel):
    service_id: str
    service_name: str
    incidents_count: int


class IncidentsPerService(BaseModel):
    service_id: str
    service_name: str
    incidents_count: int


class IncidentsByServiceAndStatus(BaseModel):
    service_id: str
    service_name: str
    incident_status: str
    incidents_count: int


class TeamsWithServices(BaseModel):
    team_id: str
    team_name: str
    service_id: str
    service_name: int


class EscalationPoliciesWithServices(BaseModel):
    escalation_policy_id: str
    escalation_policy_name: str
    service_id: str
    service_name: int


class EscalationPoliciesWithTeams(BaseModel):
    escalation_policy_id: str
    escalation_policy_name: str
    team_id: str
    team_name: int
