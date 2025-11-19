from datetime import datetime
from typing import List

from pydantic import BaseModel, Field



class SensorSchema(BaseModel):
    mac: str
    id_type: int
    name: str | None = None
    last_heartbeat: datetime


class RegistrationSchema(BaseModel):
    mac: str = Field(max_length=17)
    id_type: int

class UpdateSensorSchema(BaseModel):
    id_type: int | None = None
    name: str | None = None
    last_heartbeat: datetime | None = None