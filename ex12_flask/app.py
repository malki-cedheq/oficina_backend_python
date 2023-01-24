# app.py
'''
Middleware
usado para aplicar uma lógica a cada requisição antes de ser processada pelo View.
'''
from flask import Flask
import time


class middleware:
    def __init__(self, arg) -> None:
        self.app = arg

    def __call__(self, environ, start_response):
        start_time = time.time()
        response = self.app(environ, start_response)
        process_time = time.time() - start_time
        process_time = process_time*1000
        print(f"Requisição processada em {process_time} ms")
        return response


app = Flask(__name__)
app.wsgi_app = middleware(app.wsgi_app)


@app.route("/", methods=["GET"])
def home():
    return {"message": "Hello Wordl"}, 200


if __name__ == "__main__":
    app.run(debug=True, port=8081)
