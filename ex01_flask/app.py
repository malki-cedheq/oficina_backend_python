# app.py
'''
API Mínima
Hello World
'''

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Hello,world!"}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
