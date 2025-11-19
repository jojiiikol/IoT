from pydantic import BaseModel


class BaseRepository():
    async def get(self):
        pass

    async def get_by_id(self, id: int):
        pass

    async def create(self, data: BaseModel):
        pass

