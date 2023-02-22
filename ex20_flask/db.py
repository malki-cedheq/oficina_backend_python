'''
Arquivo: db.py
Descrição: Integração com o banco de dados
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from flask_sqlalchemy import SQLAlchemy  # https://flask-sqlalchemy.palletsprojects.com
# https://flask-marshmallow.readthedocs.io
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate  # https://flask-migrate.readthedocs.io/
from sqlalchemy import text  # https://www.sqlalchemy.org/
from flask_pymongo import PyMongo  # https://pymongo.readthedocs.io

db = SQLAlchemy()
ma = Marshmallow()
mi = Migrate()
mo = PyMongo()  # instância do PyMongo


def initialize_db(app):
    db.app = app
    mo.app = app
    db.init_app(app)
    ma.init_app(app)
    mi.init_app(app, db)
    mo.init_app(app)

    with app.app_context():
        if app.config['APP_MODE'] == 'dev':
            db.drop_all()  # desabilitar quando Produção

        db.create_all()

        if app.config['APP_MODE'] == 'dev':
            preload_data()  # desabilitar quando Produção

# popula o db a partir de queries em arquivos sql


def preload_data():
    populate_usuarios()


def populate_usuarios():
    file = open('./ex19_flask/sql/QUERY_usuarios_insert.sql', encoding="utf-8")
    query = text(file.read())
    db.session.execute(query)
