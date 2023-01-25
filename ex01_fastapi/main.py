# main.py
'''
API Mínima
Hello World
'''

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
