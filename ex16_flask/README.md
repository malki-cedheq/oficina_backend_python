# READMME.md

## Requisitos

python +3.10
poetry

## Instalação de dependências

> pip install poetry
> poetry install

## Inicializar servidor

> poetry run python app.py

## Inicializar servidor WSGI (unix)

> gunicorn -w 4 'app:app'
