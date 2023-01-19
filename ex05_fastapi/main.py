# main.py
'''
Parâmetros Query
'''
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/item")  # /item?item_name=abajur
def read(item_name: str):
    return {"item_name": item_name}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
