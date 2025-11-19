from pydantic import BaseModel


class TypeSchema(BaseModel):
    id_type: int
    name: str
