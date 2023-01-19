# app.py
'''
Métodos HTTP
'''

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def create():
    return {"method": "POST"}


@app.route("/", methods=["GET"])
def read():
    return {"method": "GET"}


@app.route("/", methods=["PUT"])
def update():
    return {"method": "PUT"}


@app.route("/", methods=["DELETE"])
def delete():
    return {"method": "DELETE"}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
