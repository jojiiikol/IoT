from fastapi import Depends

from depends import get_type_repository
from repository.type import TypeRepository
from schema.type import TypeSchema


def get_type_service(repository = Depends(get_type_repository)):
    return TypeService(repository)


class TypeService:
    def __init__(self, repository):
        self.repository = repository

    async def get(self):
        data = await self.repository.get()
        data = [TypeSchema.model_validate(typ, from_attributes=True) for typ in data]
        return data