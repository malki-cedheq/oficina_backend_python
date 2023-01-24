# main.py
'''
Métodos HTTP
'''
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def create():
    return {"method": "POST"}


@app.get("/")
def read():
    return {"method": "GET"}


@app.put("/")
def update():
    return {"method": "PUT"}


@app.delete("/")
def delete():
    return {"method": "DELETE"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
