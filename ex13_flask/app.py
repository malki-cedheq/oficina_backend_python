# app.py
'''
Modularização
Decomposição da aplicação em models, schemas, routers, services, views, templates, etc
'''
from flask import Flask
from routers.index_router import index_router

app = Flask(__name__)

app.register_blueprint(index_router)

if __name__ == "__main__":
    app.run(debug=True, port=8081)
