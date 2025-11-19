from fastapi import APIRouter, Depends

from schema.type import TypeSchema
from service.type import get_type_service

router = APIRouter(
    prefix="/type",
    tags=["type"]
)

@router.get("/")
async def get(service = Depends(get_type_service)):
    data = await service.get()
    return data
