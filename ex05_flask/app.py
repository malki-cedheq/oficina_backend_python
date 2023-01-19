# app.py
'''
Parâmetros Query
'''

from flask import Flask, request

app = Flask(__name__)


@app.route("/item/", methods=["GET"])  # /item?item_name=abajur
def read():
    item_name = request.args.get("item_name")
    return {"item_name": item_name}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
