# app.py
'''
Arquivo: app.py
Descrição: API REST  com Flask-restx
            registrando API com api.init_app
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from flask import Flask

from resources import api

app = Flask(__name__)

app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post", "put", "delete"]

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081)
