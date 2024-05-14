from sqlalchemy import select

from app.db.database import new_session
from app.models.task_table import TaskTable
from app.schemas.task_shemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas

    @classmethod
    async def find_one(cls, task_id: int) -> STask:
        async with new_session() as session:
            query = select(TaskTable).where(TaskTable.id == task_id)
            result = await session.execute(query)
            task_models = result.scalars().first()
            return task_models
