'''
Arquivo: services.usuario.py
Descrição: Interface entre os objetos e db via SQLAlchemy
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from typing import List
from sqlalchemy.exc import SQLAlchemyError
from db import db
from libs.yagmail_sender import envia_email
from models.usuario import Usuario as UsuarioModel


class Usuario(UsuarioModel):

    @classmethod
    def find_by_email(cls, email: str) -> "UsuarioModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_nome(cls, nome: str) -> "UsuarioModel":
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id_usuario: int) -> "UsuarioModel":
        return cls.query.filter_by(id_usuario=id_usuario).first()

    @classmethod
    def find_all(cls) -> List["UsuarioModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def update_db(self) -> None:
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def delete_from_db(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def send_email(self, contents):
        try:
            subject = "Oficina Backend"
            envia_email(to=self.email, subject=subject, contents=contents)
            return {'message': 'sucesso'}
        except:
            return {'message': 'erro'}
