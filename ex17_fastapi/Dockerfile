FROM python:3.10-slim-buster
WORKDIR /ex17_fastapi-docker

EXPOSE 8080

RUN pip3 install --upgrade pip
RUN pip3 install poetry

COPY pyproject.toml pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .  

#CMD [ "poetry", "run" , "python3", "main.py"]
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8080", "--worker-class=uvicorn.workers.UvicornWorker", "main:app"]
