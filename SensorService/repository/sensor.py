from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from model import SensorModel
from schema.sensor import RegistrationSchema, UpdateSensorSchema


class SensorRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = SensorModel

    async def get(self):
        query = select(SensorModel)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_mac(self, mac: str):
        query = select(SensorModel).where(SensorModel.mac == mac).options(joinedload(SensorModel.datas)).options(joinedload(SensorModel.type))
        result = await self.session.execute(query)
        return result.unique().scalar_one_or_none()

    async def create(self, data: RegistrationSchema):
        data = SensorModel(**data.model_dump())
        self.session.add(data)
        await self.session.commit()

    async def update(self, mac: str, data: UpdateSensorSchema):
        query = update(SensorModel).where(SensorModel.mac == mac).values(**data.model_dump(exclude_none=True))
        await self.session.execute(query)
        await self.session.commit()

