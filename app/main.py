from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes.task_rourter import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start, please wait")
    yield


title = "My base project FastAPI"
app = FastAPI(lifespan=lifespan, title=title, docs_url="/")
app.include_router(tasks_router)
