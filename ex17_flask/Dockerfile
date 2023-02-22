FROM python:3.10-slim-buster
WORKDIR /ex17_flask-docker

EXPOSE 8081

RUN pip3 install --upgrade pip
RUN pip3 install poetry

COPY pyproject.toml pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .  

#CMD [ "poetry", "run" , "python3", "app.py"]
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8081", "app:app"]
