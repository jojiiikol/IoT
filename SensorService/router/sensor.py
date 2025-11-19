from datetime import datetime

from asyncpg import UniqueViolationError
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy import select, literal
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db import db
from schema.sensor import SensorSchema, RegistrationSchema, UpdateSensorSchema
from service.sensor import get_sensor_service

router = APIRouter(prefix="/sensor", tags=["sensor"])

mock_data = [
        {
            "mac": "A1:6B:8E:4C:5A:8E",
            "type": 1,
            "name": "Sensor 1",
            "last_heartbeat": datetime.now(),
        },
        {
            "mac": "A1:6F:8E:4C:5A:FE",
            "type": 3,
            "name": "Sensor 2",
            "last_heartbeat": datetime.now(),
        }
    ]

@router.post("/heartbeat/{mac}")
async def heartbeat(mac: str, service = Depends(get_sensor_service)):
    data = await service.heartbeat(mac)
    return data

@router.get("/{mac}")
async def get_by_mac(mac: str, service = Depends(get_sensor_service)):
    data = await service.get_by_mac(mac)
    return data

@router.get("/")
async def get_sensors(service = Depends(get_sensor_service)):
    data = await service.get()
    return data

@router.post("/")
async def registration_sensor(sensor: RegistrationSchema, service = Depends(get_sensor_service)):
    data = await service.create(sensor)
    return data

@router.put("/{mac}")
async def update_sensor(mac: str, sensor: UpdateSensorSchema, service = Depends(get_sensor_service)):
    data = await service.update(mac, sensor)
    return data



