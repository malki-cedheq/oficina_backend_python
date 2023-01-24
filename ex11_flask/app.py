# app.py
'''
Serialização e Desserialização
--Sugerido Flask-Marshmallow
'''

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    dicionario = {"message": "Hello Word", "valor": 100, "boolean": True}
    return jsonify(dicionario)  # serialização


if __name__ == "__main__":
    app.run(debug=True, port=8081)
