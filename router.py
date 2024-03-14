from fastapi import APIRouter,Depends
from schemas import *
from repository import *
from typing import Annotated

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.post('/post')
async def add_taks(
    task : Annotated[Task,Depends()]
):
    id_task = await TaskRepository.add_one(task)
    return {'data':id_task}


@router.get('/get')
async def find_all():
    result = await TaskRepository.find_all()
    return {"data":result}