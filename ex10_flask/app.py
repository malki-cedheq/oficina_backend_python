# app.py
'''
Validação
'''

from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate


app = Flask(__name__)


class QueryModel(BaseModel):
    ''' Schema para validação do corpo das requisições http'''
    username: str
    password: str


@app.route("/login", methods=["GET"])  # /login?username=usuario&password=senha
@validate()
def get(query: QueryModel):
    return query


# request body {"username": "usuario","password": "senha"}
@app.route("/login", methods=["POST"])
@validate()
def post(body: QueryModel):
    if body.username == "usuario" and body.password == "senha":
        return {"message": "success"}
    return {"message": "Authentication Failed"}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
