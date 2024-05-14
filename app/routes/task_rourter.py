from typing import Annotated

from fastapi import APIRouter, Depends

from app.repositories.task_repository import TaskRepository
from app.schemas.task_shemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("/task_add")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("/all_tasks")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


@router.get("/task/{task_id}", response_model=STask)
async def get_task(task_id: int) -> STask:
    print(task_id)
    task = await TaskRepository.find_one(task_id)
    return task
