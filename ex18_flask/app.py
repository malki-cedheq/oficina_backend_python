# app.py
'''
Flask-restx
'''
from flask import Flask

from resources import api

app = Flask(__name__)

app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post", "put", "delete"]

api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=8081)
