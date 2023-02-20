'''
Arquivo: models.usuario.py
Descrição: Mapeamento Objeto Relacional (ORM) da entidade usuario
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from flask_login import UserMixin
from db import db
from models.autodate import AutoDate


class Usuario(UserMixin, AutoDate, db.Model):
    __tablename__ = 'usuarios'  # relaciona a tabela usuarios
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False, unique=True)
    nivel_acesso = db.Column(db.SmallInteger, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    def get_id(self):
        return (self.id_usuario)

    def __repr__(self):
        return f"<Usuario {self.id_usuario}>"
