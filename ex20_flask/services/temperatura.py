'''
Arquivo: services.temperatura.py
Descrição: Interface entre os documento e db via PyMongo
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from db import mo
from typing import List
from models.temperatura import Temperatura as TemperaturaModel


class Temperatura(TemperaturaModel):
    @classmethod
    def find_all(cls) -> List["TemperaturaModel"]:
        return mo.db.temperatura.find()

    @classmethod
    def find_by_sessao(cls, id_sessao: str) -> List["TemperaturaModel"]:
        return mo.db.temperatura.find({"id_sessao": id_sessao})

    @classmethod
    def find_by_query(cls, id_paciente: str, id_sessao: str, id_exercicio: str) -> List["TemperaturaModel"]:
        return mo.db.temperatura.find({"id_paciente": id_paciente, "id_sessao": id_sessao, "id_exercicio": id_exercicio})

    def save_to_db(self) -> bool:
        try:
            mo.db.temperatura.insert_one(self)
            return True
        except:
            return False
