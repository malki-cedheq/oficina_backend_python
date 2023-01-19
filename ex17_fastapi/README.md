# READMME.md

## Requisitos

python +3.10
poetry

## Instalação de dependências

> pip install poetry
> poetry install

## Inicializar servidor uvicorn

> poetry run uvicorn app:app --reload

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
