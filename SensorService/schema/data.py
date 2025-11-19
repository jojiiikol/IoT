from datetime import datetime
from typing import List

from pydantic import BaseModel

from schema.sensor import SensorSchema
from schema.type import TypeSchema


class DataSchema(BaseModel):
    mac: str
    data: str
    date_time: datetime

class CreateDataSchema(BaseModel):
    mac: str
    data: str
    date_time: datetime

class AdditionalSensorSchema(BaseModel):
    mac: str
    id_type: int
    name: str | None = None
    last_heartbeat: datetime
    datas: List[DataSchema]
    type: TypeSchema