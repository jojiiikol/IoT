from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from model import TypeModel


class TypeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self):
        query = select(TypeModel)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int):
        query = select(TypeModel).where(TypeModel.id_type == id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()