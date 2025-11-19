from fastapi import APIRouter
from fastapi.params import Depends

from schema.data import CreateDataSchema
from service.data import get_data_service

router = APIRouter(
    prefix="/data",
    tags=["data"]
)

@router.get("/")
async def get_data(service = Depends(get_data_service)):
    result = await service.get()
    return result

@router.post("/")
async def create_data(data: CreateDataSchema, service = Depends(get_data_service)):
    result = await service.create(data)
    return result