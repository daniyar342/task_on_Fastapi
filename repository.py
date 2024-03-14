from schemas import Task
from database import new_session,TaskOrm
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls,data:Task):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id
        
    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            queryset = await session.execute(query)
            return queryset.scalars().all()