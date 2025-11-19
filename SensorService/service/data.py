from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from depends import get_data_repository, get_sensor_repository
from repository.base import BaseRepository
from schema.data import DataSchema, CreateDataSchema
from schema.sensor import UpdateSensorSchema


def get_data_service(repository = Depends(get_data_repository),
                     sensor_repository = Depends(get_sensor_repository)):
    return DataService(repository, sensor_repository)

class DataService:
    def __init__(self, repository: BaseRepository, sensor_repository: BaseRepository):
        self.repository = repository
        self.sensor_repository = sensor_repository


    async def get(self):
        result = await self.repository.get()
        result = [DataSchema.model_validate(data, from_attributes=True) for data in result]
        return result

    async def create(self, data: CreateDataSchema):
        update_sensor_data = UpdateSensorSchema(last_heartbeat=datetime.now())
        await self.sensor_repository.update(mac=data.mac, data=update_sensor_data)

        data.date_time = datetime.now()
        await self.repository.create(data)
        return data