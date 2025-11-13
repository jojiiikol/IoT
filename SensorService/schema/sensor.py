from datetime import datetime

from pydantic import BaseModel


class SensorSchema(BaseModel):
    mac: str
    type: int
    name: str | None
    last_heartbeat: datetime

