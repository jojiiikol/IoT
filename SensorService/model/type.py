from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from model.base import BaseModel


class TypeModel(BaseModel):
    __tablename__ = 'type'

    id_type: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    sensors: Mapped["SensorModel"] = relationship(back_populates="type")