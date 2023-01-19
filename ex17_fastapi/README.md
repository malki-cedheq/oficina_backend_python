# READMME.md

## Requisitos

python +3.10
poetry

## Instalação de dependências

> pip install poetry
> poetry install

## Inicializar servidor uvicorn

> poetry run uvicorn main:app --host 0.0.0.0 --port 8080 --reload

## Inicializar servidor WSGI (apenas unix)

cli: gunicorn --workers=4 --bind=0.0.0.0:8080 --worker-class=uvicorn.workers.UvicornWorker main:app

cada worker é executado em um processo individual
cada bind indica o endereço de exposição do serviço

> gunicorn -w 4 -b 0.0.0.0:8080 -k uvicorn.workers.UvicornWorker main:app

## Dockerização

### construindo a imagem docker

```
docker build --tag ex17_fastapi-docker .
```

### criando e executando o container

```
docker create --name ex17_fastapi-container -p 8081:8081 ex17_fastapi-docker
docker start -i ex17_fastapi-container
```
