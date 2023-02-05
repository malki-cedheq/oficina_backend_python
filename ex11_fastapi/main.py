# main.py
'''
Serialização e Desserialização
'''
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Response(BaseModel):
    ''' handles object serialization '''
    username: str
    email: str


class Request(Response):
    ''' handles deserialization '''
    password: str


@app.post("/login", response_model=Response)
async def login(req: Request):
    '''
    body request deve conter username, password e email
    '''
    if req.username == "usuario" and req.password == "senha":
        return req
    return {"message": "Authentication Failed"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
