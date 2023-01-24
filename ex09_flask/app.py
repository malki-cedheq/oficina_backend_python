# app.py
'''
Injeção de Dependências
a injeção de dependências é uma técnica 
onde um objeto (ou método estático) 
fornece as dependências de outro objeto. 
Uma dependência é um objeto que pode ser usado, ou seja, um serviço.
'''

from flask import Flask
from flask_injector import FlaskInjector
from injector import Module, Injector


def configure_views(arg):
    @arg.route("/", methods=["GET"])
    def home():
        return {"message": "Done"}


class AppModule(Module):
    def __init__(self, arg):
        self.app = arg


app = Flask(__name__)

injector = Injector([AppModule(app)])
configure_views(arg=app)
FlaskInjector(app=app, injector=injector)


if __name__ == "__main__":
    app.run(debug=True, port=8081)
