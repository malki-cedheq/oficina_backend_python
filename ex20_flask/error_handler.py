'''
Arquivo: error_handler.py
Descrição: Trata os erros
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from werkzeug.exceptions import InternalServerError, NotFound, MethodNotAllowed, BadRequest
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError


def initialize_error_handler(app):
    ''' Gerenciamento de erros '''

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
