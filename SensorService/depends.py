from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import db
from model import SensorModel
from repository.data import DataRepository
from repository.sensor import SensorRepository
from repository.type import TypeRepository


def get_data_repository(session: AsyncSession = Depends(db.get_async_session)) -> DataRepository:
    return DataRepository(session)

def get_sensor_repository(session: AsyncSession = Depends(db.get_async_session)) -> SensorRepository:
    return SensorRepository(session)

def get_type_repository(session: AsyncSession = Depends(db.get_async_session)) -> TypeRepository:
    return TypeRepository(session)