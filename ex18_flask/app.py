# app.py
'''
Restful
'''
from flask import Flask, url_for

from resources import api

app = Flask(__name__)

app.config.SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post", "put", "delete"]

api.init_app(app)


#assert url_for('api.doc') == '/api/doc/'

if __name__ == "__main__":
    app.run(debug=True, port=8081)
