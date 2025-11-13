from datetime import datetime

from fastapi import APIRouter

from schema.sensor import SensorSchema

router = APIRouter(prefix="/sensor", tags=["sensor"])

@router.get("/")
async def get_sensors():
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
    sensor_schema = [SensorSchema.model_validate(sensor, from_attributes=True) for sensor in mock_data]
    return sensor_schema

