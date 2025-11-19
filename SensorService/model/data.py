from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, relationship

from model.base import BaseModel


class DataModel(BaseModel):
    __tablename__ = 'data'

    id: Mapped["int"] = Column(Integer, primary_key=True, autoincrement=True)
    mac: Mapped["str"] = Column(ForeignKey('sensor.mac'), nullable=False)
    data: Mapped["str"] = Column(String)
    date_time: Mapped[datetime] = Column(DateTime)

    sensor: Mapped["SensorModel"] = relationship("SensorModel", back_populates="datas")
