from pydantic import TypeAdapter
from sqlalchemy import select
from sqlalchemy.sql import text
import pandas as pd

from app.models.service import Service as ServiceModel
from app.schemas.service_schema import Service as ServiceSchema

from .base import Controller


class ServicesController(Controller[ServiceModel]):
    def list_services(self) -> list[ServiceSchema]:
        stmt = select(ServiceModel)
        result = self.session.scalars(stmt.order_by(ServiceModel.id)).fetchall()

        return TypeAdapter(list[ServiceSchema]).validate_python(result)

    def get_grouped_incidents(self) -> list[ServiceSchema]:
        stmt = text("""
            SELECT
                services.id AS service_id,
                services.name AS service,
                COUNT(incidents.id) AS incidents_count
            FROM incidents
                JOIN services ON incidents.service_id = services.id
            GROUP BY services.id
            """)
        # result = self.session.execute(stmt)

        df = pd.read_sql(stmt, self.session.bind)
        # print(df.values.tolist())

        # return df.values.tolist()

        return [
            dict(zip(("service_id", "service", "incidents_count"), row))
            for row in df.values.tolist()
        ]

    def store_service(self, service_data: dict) -> ServiceSchema:
        service = ServiceModel(**service_data)
        self.session.add(service)
        self.session.commit()

        return TypeAdapter(ServiceSchema).validate_python(service)
