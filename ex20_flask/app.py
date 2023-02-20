'''
Arquivo: app.py
Descrição: API REST
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from flask import Flask
from variables import Variables
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from werkzeug.exceptions import InternalServerError, NotFound, MethodNotAllowed, BadRequest
from werkzeug.middleware.proxy_fix import ProxyFix
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
from db import initialize_db
from resources.usuario import user_bp as UsuarioResource
from services.usuario import Usuario as UsuarioService


# Configuração da aplicação
app = Flask(__name__)

app.config.from_object(Variables)

app.wsgi_app = ProxyFix(app.wsgi_app)

bootstrap = Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = app.config['APP_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# propaga erros de dependências para a aplicação
app.config['PROPAGATE_EXCEPTIONS'] = True
# desabilita auto ordenação das respostas JSON
app.config['JSON_SORT_KEYS'] = False
# habilita documentação
app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post", "put", "delete"]

# Inicialização do banco, esquemas, migração
initialize_db(app)

# Registro de rotas
app.register_blueprint(UsuarioResource)


# Gerenciamento de erros
@app.errorhandler(ValidationError)
def validation_error(err):
    return {"error": f"{err.messages}"}, 400


@app.errorhandler(BadRequest)
def bad_request_error(err):
    return {"error": f"{err}"}, 400


@app.errorhandler(NotFound)
def not_found_error(err):
    return {"error": f"{err}"}, 404


@app.errorhandler(MethodNotAllowed)
def method_not_allowed_error(err):
    return {"error": f"{err}"}, 405


@app.errorhandler(SQLAlchemyError)
def database_error(err):
    return {"error": f"{err}"}, 500


@app.errorhandler(InternalServerError)
def internal_server_error(err):
    return {"error": f"{err}"}, 500


# gerenciamento de login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id_usuario):
    return UsuarioService.find_by_id(id_usuario)


# Inicializa a aplicação
if __name__ == '__main__':
    app.run(host=app.config['APP_HOST'],
            port=app.config['APP_PORT'], debug=True)
