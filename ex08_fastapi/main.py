# main.py
'''
Tarefas Assíncronas
--Sugerido uso de Celery--
'''
import uvicorn
from fastapi import FastAPI, BackgroundTasks
import asyncio
from datetime import datetime

app = FastAPI()


async def some_async_task():
    await asyncio.sleep(1)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return {"async message": now}


@app.get("/")  # recurso assincrono
async def home():
    result = await some_async_task()
    return result


@app.get("/read/{filename}")  # background tasks
async def read(filename: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(some_async_task, filename)
    return {"message": "processing..."}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
