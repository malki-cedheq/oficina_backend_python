'''
Arquivo: models.autodate.py
Descrição: Mapeamento Objeto Relacional (ORM) para campos criado_em e modificado_em
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from datetime import datetime
from db import db

class AutoDate(object):
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modificado_em = db.Column(db.DateTime, onupdate=datetime.utcnow)
    