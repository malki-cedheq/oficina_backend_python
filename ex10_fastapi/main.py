# main.py
'''
Validação
'''
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Request(BaseModel):
    ''' Schema para validação do corpo das requisições http'''
    username: str
    password: str


@app.get("/login")  # /login?username=usuario&password=senha
async def read(username: str, password: str):
    return {"username": username, "password": password}


@app.post("/login")  # request body {"username": "usuario","password": "senha"}
async def login(req: Request):
    if req.username == "usuario" and req.password == "senha":
        return {"message": "success"}
    return {"message": "Authentication Failed"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
