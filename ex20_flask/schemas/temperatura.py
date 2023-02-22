'''
Arquivo: schemas.temperatura.py
Descrição:  schema para a entidade temperatura na API REST
            schemas definem a estrutura dos dados e também a validação destes dados
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from models.temperatura import Temperatura as TemperaturaModel
from db import ma


class Temperatura(ma.Schema):  # Schema
    class Meta:
        model = TemperaturaModel
        load_instance = True
        fields = ("id_paciente", "id_sessao", "id_exercicio",
                  "timestamp", "n_pacote", "temperatura")

    # implementação de HATEOAS
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("bp.temp_read", id_temperatura="<id_temperatura>"),
            "collection": ma.URLFor("bp.temp_list"),
        }
    )


temperatura_schema = Temperatura()
temperaturas_schema = Temperatura(many=True)
