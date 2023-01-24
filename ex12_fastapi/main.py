# main.py
'''
Middleware
usado para aplicar uma lógica a cada requisição antes de ser processada pelo View.
'''
import uvicorn
from fastapi import FastAPI, Request, status
import time

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    process_time = process_time*1000
    print(f"Requisição processada em {process_time} ms")
    return response


@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"message": "Hello Wordl"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
