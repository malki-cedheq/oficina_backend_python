# main.py
'''
Configurações

    Environment Variables
    Config File
    Instance Folder
    Classes and inheritance

'''
import uvicorn
from fastapi import FastAPI
from pydantic import BaseSettings


class PedrinhoPai(BaseSettings):
    message: str
    nome: str

    class Config:
        env_file = "./ex02_fastapi/.env"


pedrinhoFilho = PedrinhoPai()

app = FastAPI()


@app.get("/settings")
def get_settings():
    return {
        "message": pedrinhoFilho.message,
        "nome": pedrinhoFilho.nome
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
