# app.py
'''
Configurações

    Environment Variables
    Config File
    Instance Folder
    Classes and inheritance

'''

import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()  # 1º carrega .env do diretório local


class Config(object):
    # uso de variável ambiente
    MESSAGE = os.environ.get("MESSAGE")


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/settings")
def get_settings():
    return {"message": app.config["MESSAGE"]}


if __name__ == "__main__":
    app.run(debug=True, port=8081)
