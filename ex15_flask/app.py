# app.py
'''
CORS
O middleware CORS (Cross-Origin Resource Sharing) verifica se as solicitações vêm ou não de origens permitidas
'''
from flask import Flask
from flask_cors import CORS
from routers.index_router import index_router

app = Flask(__name__)
CORS(app, origins=['*'])
app.register_blueprint(index_router)

if __name__ == "__main__":
    app.run(debug=True, port=8081)
