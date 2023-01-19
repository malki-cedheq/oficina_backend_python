# main.py
'''
Templates e Statics
'''
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="./ex07_fastapi/templates")

app.mount("/static", StaticFiles(directory="./ex07_fastapi/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page_title": "FASTAPI"})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080)
