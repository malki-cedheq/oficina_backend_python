# resources/__init__.py

from flask_restx import Api, apidoc

from .item import api as ns1

api = Api(title='API Restful', version='1.0',
          description='API Restful com flask-restx',)


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


api.add_namespace(ns1, path='/api')
