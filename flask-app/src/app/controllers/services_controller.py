from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.service import Service as ServiceModel
from app.schemas.service_schema import Service as ServiceSchema

from .base import Controller


class ServicesController(Controller[ServiceModel]):
    def list_services(self) -> list[ServiceSchema]:
        stmt = select(ServiceModel)
        result = self.session.scalars(stmt.order_by(ServiceModel.id)).fetchall()

        return TypeAdapter(list[ServiceSchema]).validate_python(result)

    def store_service(self, service_data: dict) -> ServiceSchema:
        service = ServiceModel(**service_data)
        self.session.add(service)
        self.session.commit()

        return TypeAdapter(ServiceSchema).validate_python(service)
