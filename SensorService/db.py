from sqlalchemy import literal, select
import asyncio
from config import DatabaseConfig
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class DBConnection:
    def __init__(self, db_config: DatabaseConfig = DatabaseConfig()):
        self.url = db_config.db_url
        self.engine = create_async_engine(self.url)
        self.session_factory = async_sessionmaker(bind=self.engine, expire_on_commit=False)

    async def get_async_session(self):
        async with self.session_factory() as session:
            yield session

db = DBConnection()

