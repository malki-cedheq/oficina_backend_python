# main.py
'''
CORS
O middleware CORS (Cross-Origin Resource Sharing) verifica se as solicitações vêm ou não de origens permitidas
'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.index_router import index_router

app = FastAPI()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins)
app.include_router(index_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
