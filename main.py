from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Optional,Annotated
from database import *
from contextlib import contextmanager

from router import router as task_router

app = FastAPI()
app.include_router(task_router)


@app.on_event("startup")
async def startup_event():
    await delete_tables()
    await create_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
