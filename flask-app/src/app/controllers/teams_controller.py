from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.team import Team as TeamModel
from app.schemas.team_schema import Team as TeamSchema

from .base import Controller


class TeamsController(Controller[TeamModel]):
    def list_teams(self) -> list[TeamSchema]:
        stmt = select(TeamModel)
        result = self.session.scalars(stmt.order_by(TeamModel.id)).fetchall()

        return TypeAdapter(list[TeamSchema]).validate_python(result)

    def store_team(self, team_data: dict) -> TeamSchema:
        team = TeamModel(**team_data)
        self.session.add(team)
        self.session.commit()

        return TypeAdapter(TeamSchema).validate_python(team)
