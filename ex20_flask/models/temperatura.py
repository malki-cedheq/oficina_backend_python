'''
Arquivo: models.temperatura.py
Descrição: Object Document Mapping (ODM) da entidade temperatura (mongodb)
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''


class Temperatura():
    def __init__(self, id_paciente, id_sessao, id_exercicio, timestamp, n_pacote, temperatura):
        self.id_paciente = id_paciente
        self.id_sessao = id_sessao
        self.id_exercicio = id_exercicio
        self.timestamp = timestamp
        self.n_pacote = n_pacote
        self.temperatura = temperatura

    def to_json(self):  # converte o documento em JSON
        return {
            "id_paciente":  self.id_paciente,
            "id_sessao":    self.id_sessao,
            "id_exercicio": self.id_exercicio,
            "timestamp":    self.timestamp,
            "n_pacote":     self.n_pacote,
            "temperatura":  self.temperatura
        }
