# README.md

## Requisitos

python +3.10
poetry

### Configuração de Variáveis Ambiente

Criar arquivo .env:

```
DB_OWNER = 'usuario' # postgresql
DB_PASS = 'senha'
DB_HOST = '0.0.0.0'
DB_PORT = '5432'
DB_DATABASE = 'oficina_backend'

MONGO_OWNER = 'usuario' # mongodb
MONGO_PASS = 'senha'
MONGO_HOST = '0.0.0.0'
MONGO_PORT = '27017'
MONGO_DATABASE = 'oficina_backend'

APP_HOST = '0.0.0.0'
APP_PORT = '8081'
APP_MODE = 'dev' #dev (desenvolvimento)/ #prod (producao)
```

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
docker create --name ex19_flask-container -p 8081:8081 ex19_flask-docker
docker start -i ex19_flask-container
```
