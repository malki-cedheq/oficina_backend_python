# main.py
'''
Modularização
Decomposição da aplicação em models, schemas, routers, services, views, templates, etc
'''
import uvicorn
from fastapi import FastAPI
from routers.index_router import index_router

app = FastAPI()

app.include_router(index_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
