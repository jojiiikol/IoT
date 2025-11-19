from datetime import datetime

from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError

from depends import get_sensor_repository, get_type_repository
from model import SensorModel
from repository.base import BaseRepository
from schema.data import AdditionalSensorSchema
from schema.sensor import SensorSchema, RegistrationSchema, UpdateSensorSchema


def get_sensor_service(repository = Depends(get_sensor_repository), type_repository = Depends(get_type_repository)):
    return SensorService(repository, type_repository)

class SensorService:
    def __init__(self, repository: BaseRepository, type_repository: BaseRepository):
        self.repository = repository
        self.type_repository = type_repository

    async def get(self):
        sensors = await self.repository.get()
        sensors = [SensorSchema.model_validate(sensor, from_attributes=True) for sensor in sensors]
        return sensors

    async def get_by_mac(self, mac: str):
        sensor = await self.repository.get_by_mac(mac)
        sensor = AdditionalSensorSchema.model_validate(sensor, from_attributes=True)
        return sensor

    async def create(self, data: RegistrationSchema):
        try:
            data = SensorSchema(**data.model_dump(), last_heartbeat=datetime.now())
            await self.repository.create(data)
            return data
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def update(self, mac: str, sensor: UpdateSensorSchema):
        await self.repository.update(mac, sensor)
        return sensor

    async def heartbeat(self, mac: str):
        data = UpdateSensorSchema(last_heartbeat=datetime.now())
        await self.repository.update(mac=mac, data=data)
        return data