from flask import Blueprint, g

from app.controllers.escalation_policies_controller import EscalationPoliciesController

escalation_policy_blueprint = Blueprint(
    "escalation_policy", __name__, url_prefix="/escalation_policies"
)


@escalation_policy_blueprint.route("/")
def list_escalation_policies():
    session = g.session
    escalation_policies_list = EscalationPoliciesController(
        session
    ).list_escalation_policies()

    return [
        escalation_policy.model_dump(mode="json")
        for escalation_policy in escalation_policies_list
    ]


@escalation_policy_blueprint.route("/create")
def store_escalation_policy():
    session = g.session
    escalation_policy = EscalationPoliciesController(session).store_escalation_policy(
        escalation_policy_data={"name": "prueba", "surname": "testtest"}
    )

    return escalation_policy.model_dump(mode="json")
