'''
Arquivo: app.py
Descrição: API REST  com Flask-restx
            registrando API com Blueprints
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
import uuid

from flask import Flask
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

from variables import Variables
from db import initialize_db
from error_handler import initialize_error_handler
from resources import bp as blueprint
from services.usuario import Usuario as UsuarioService

# Instância da aplicação
app = Flask(__name__)

# Configuração da aplicação
app.config.from_object(Variables)
# O URI do banco de dados que deve ser usado para a conexão
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['APP_URI']
app.config['SECRET_KEY'] = str(uuid.uuid4())  # gera um uuuid aleatório
# propaga erros de dependências para a aplicação
app.config['PROPAGATE_EXCEPTIONS'] = True
# desabilita auto ordenação das respostas JSON
app.config['JSON_SORT_KEYS'] = False
app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = [
    "get", "post", "put", "delete"]  # habilita documentação

app.wsgi_app = ProxyFix(app.wsgi_app)

# Inicialização do banco, esquemas, migração
initialize_db(app)

# Registro de rotas
app.register_blueprint(blueprint)

# Gerenciamento de erros
initialize_error_handler(app)

# Gerenciamento de login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id_usuario):
    return UsuarioService.find_by_id(id_usuario)


# Inicializa a aplicação
if __name__ == '__main__':
    app.run(host=app.config['APP_HOST'],
            port=app.config['APP_PORT'], debug=True)
