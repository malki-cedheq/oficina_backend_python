# main.py
'''
TDD
Test Driven Development
***EM CONSTRUÇÃO***
'''
import uvicorn
from fastapi import FastAPI
from .routers.index_router import index_router

app = FastAPI()

app.include_router(index_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
