# resources/__init__.py
from flask import Blueprint
from flask_restx import Api, apidoc

from .item import ns_item
from .thing import ns_thing

api = Api(title='API Restful', version='1.0',
          description='API Restful com flask-restx', doc='/api/doc/')


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


api.add_namespace(ns_item, path='/api')
api.add_namespace(ns_thing, path='/api')
