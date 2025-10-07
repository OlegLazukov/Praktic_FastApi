from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    ...

class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)
        print("Таблицы успешно созданы")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")


async def delete_tables():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Model.metadata.drop_all)
        print("Таблицы успешно удалены")
    except Exception as e:
        print(f"Ошибка при удалении таблиц: {e}")