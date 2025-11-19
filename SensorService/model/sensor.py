from datetime import datetime
from typing import List

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.base import BaseModel


class SensorModel(BaseModel):
    __tablename__ = 'sensor'

    mac: Mapped[str] = mapped_column(String, primary_key=True)
    id_type: Mapped[int] = mapped_column(ForeignKey('type.id_type'))
    name: Mapped[str | None] = mapped_column(String)
    last_heartbeat: Mapped[datetime] = mapped_column(DateTime)

    type: Mapped['TypeModel'] = relationship(back_populates="sensors")
    datas: Mapped[List["DataModel"]] = relationship(back_populates="sensor")