from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from mqtt.client import MqttClient
from router.sensor import router as sensor_router
from router.data import router as data_router
from router.type import router as type_router


mqtt_client = MqttClient()
@asynccontextmanager
async def lifespan(app: FastAPI):
    mqtt_client.connect()
    mqtt_client.subscribe("test")
    mqtt_client.start()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(sensor_router)
app.include_router(data_router)
app.include_router(type_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


