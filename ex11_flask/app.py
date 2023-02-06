# app.py
'''
Serialização e Desserialização
--Sugerido Flask-Marshmallow
'''

from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)


usuarios = [
    {"user_id": 1, "username": "jose",
        "email": "jose@email.com", "password": "1f2f3f"},
    {"user_id": 2, "username": "pedro",
        "email": "pedro@email.com", "password": "1e2e3e"},
    {"user_id": 3, "username": "marcos",
        "email": "marcos@email.com", "password": "1d2d3d"}
]


class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "email")  # campos expostos


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/usuarios", methods=["GET"])
def users() -> list:
    ''' Retorna lista com todos os usuários'''
    all_users = usuarios
    return users_schema.dump(all_users)


@app.route("/usuarios/<int:user_id>", methods=["GET"])
def user_detail(user_id: int) -> dict:
    ''' Retorna apenas o usuário a qual pertence o identificador'''

    # utilizando list comprehension, retorna dict
    user = list(users for users in usuarios if users['user_id'] == user_id)[0]

    # utilizando filter, retorna dict
    #user = list(filter(lambda usuarios: usuarios['user_id'] == user_id, usuarios))[0]

    # utilizando next, retorna dict
    #user = next((users for users in usuarios if users['user_id'] == user_id), {})

    print(user)
    return user_schema.dump(user)


if __name__ == "__main__":
    app.run(debug=True, port=8081)
