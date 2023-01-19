# main.py
'''
Injeção de dependências
'''
import uvicorn
from fastapi import Depends, FastAPI
import asyncio
from datetime import datetime


app = FastAPI()


async def some_async_task():
    await asyncio.sleep(1)
    now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return {"async message": now}


@app.get("/")
async def read(result: dict = Depends(some_async_task)):
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
