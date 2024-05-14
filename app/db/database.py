from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config.db_config import DB_URL

# "sqlite+aiosqlite:///tasks.db"

async_engine = create_async_engine(DB_URL)

new_session = async_sessionmaker(async_engine, expire_on_commit=False)
