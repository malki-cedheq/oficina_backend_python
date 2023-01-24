# app.py
'''
Parâmetros URL
'''

from flask import Flask

app = Flask(__name__)


@app.route("/item/<int:item_id>", methods=["GET"])
def read(item_id: int):
    return {"item_id": item_id}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
