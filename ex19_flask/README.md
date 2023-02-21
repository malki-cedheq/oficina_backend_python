# README.md

## Requisitos

python +3.10
poetry

## Instalação de dependências

> pip install poetry
> poetry install

## Inicializar servidor sem WSGI

> poetry run python app.py

## Inicializar servidor WSGI (apenas unix)

cli: gunicorn --workers=4 --bind=0.0.0.0:8081 'app:app'

cada worker é executado em um processo individual
cada bind indica o endereço de exposição do serviço

> poetry run gunicorn -w 4 -b 0.0.0.0:8081 'app:app'

## Dockerização

### construindo a imagem docker

```
docker build --tag ex18_flask-docker .
```

### criando e executando o container

```
docker create --name ex18_flask-container -p 8081:8081 ex18_flask-docker
docker start -i ex18_flask-container
```
