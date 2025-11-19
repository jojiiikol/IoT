from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model.data import DataModel
from schema.data import CreateDataSchema


class DataRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.model = DataModel


    async def get(self):
        query = select(DataModel)
        result = await self.session.scalars(query)
        return result

    async def create(self, data: CreateDataSchema):
        data_model = DataModel(**data.model_dump())
        self.session.add(data_model)
        await self.session.commit()
