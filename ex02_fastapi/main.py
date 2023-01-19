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


class Settings(BaseSettings):
    message: str

    class Config:
        env_file = "./ex02_fastapi/.env"


settings = Settings()

app = FastAPI()


@app.get("/settings")
def get_settings():
    return {"message": settings.message}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
