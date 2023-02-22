# resources/__init__.py

from flask import Blueprint
from flask_restx import Api, apidoc

from .usuario import ns_auth, ns_user

user_bp = Blueprint('user_bp', __name__, url_prefix='/api')
api = Api(user_bp, title='API Restful', version='1.0',
          description='API Restful com flask-restx', doc='/doc')


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


api.add_namespace(ns_auth, path='/auth')
api.add_namespace(ns_user, path='/op')
