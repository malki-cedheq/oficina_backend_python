# main.py
'''
Parâmetros URL
'''
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{item_id}")
def read(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
