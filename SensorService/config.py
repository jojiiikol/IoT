from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()
class DatabaseConfig(BaseModel):
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    username: str = os.getenv("DB_USERNAME")
    password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")
    db_url: str = f"postgresql+asyncpg://{username}:{password}@{host}:{port}/{db_name}"


class MqttConfig(BaseModel):
    host: str = os.getenv("MQTT_HOST")
    port: int = int(os.getenv("MQTT_PORT"))