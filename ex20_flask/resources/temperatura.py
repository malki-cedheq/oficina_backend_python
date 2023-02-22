'''
Arquivo: resouces.temperatura.py
Descrição: Definição dos endpoints para o recurso temperatura
Autores: Malki-çedheq Benjamim,
Criado em: 25/08/2022
Atualizado em: 21/02/2022
'''
from flask import request
from flask_restx import Resource, reqparse, Namespace
from werkzeug.exceptions import InternalServerError
from marshmallow import ValidationError
from constants import NOT_FOUND_ERROR, INTERNAL_SERVER_ERROR, UNAUTHORIZED
from schemas.temperatura import temperatura_schema, temperaturas_schema
from services.temperatura import Temperatura as TemperaturaService

ns_temp = Namespace(
    'Temperatura NS', description='Operações com recurso temperatura')


@ns_temp.doc(responses={
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    204: 'No Content',
    304: 'Not Modified',
    400: 'Validation Error',
    401: 'Unauthorized ',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
})
@ns_temp.route('/readall', endpoint='temp_list')
class TempList(Resource):

    @ns_temp.doc('Recupera todos os temperaturas cadastrados')
    def get(self):
        '''
        requisição get
        retorna os registros de todos os usuarios cadastrados
        '''
        try:
            dados = TemperaturaService.find_all()

            if dados:
                return {"usuarios": temperaturas_schema.dump(dados, many=True)}, 200

            if not dados:
                return {"message": "Nenhum resultado encontrado."}, 200

            return NOT_FOUND_ERROR
        except InternalServerError:
            return INTERNAL_SERVER_ERROR


@ns_temp.route('/save', endpoint='temp_create')
@ns_temp.doc(responses={
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    204: 'No Content',
    304: 'Not Modified',
    400: 'Validation Error',
    401: 'Unauthorized ',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
})
class TempCreate(Resource):
    # coleta os dados da requisição
    parser = reqparse.RequestParser()  # usando flask-restx

    parser.add_argument('id_paciente', type=str, required=True,
                        help='Deve informar o nome', location='json')
    parser.add_argument('id_sessao', type=str, required=True,
                        help='Deve informar o email', location='json')
    parser.add_argument('id_exercicio', type=str, required=True,
                        help='Deve informar o senha', location='json')
    parser.add_argument('timestamp', type=str, required=True,
                        help='Deve informar o nivel_acesso', location='json')
    parser.add_argument('n_pacote', type=int, required=True,
                        help='Deve informar o email', location='json')
    parser.add_argument('temperatura', type=int, required=True,
                        help='Deve informar o email', location='json')

    @ns_temp.doc('Cadastra um nova temperatura', parser=parser)
    @ns_temp.expect(parser)
    def post(self):
        '''
        requisição post
        solicita cadastro de temperatura
        a requisição deve incluir os dados do temperatura em formato json
        retorna os dados cadastrados, em caso de sucesso
        retorna json com messagem, em caso de falha
        '''
        request_data = request.json

        # Valida e desserializa o request_data
        try:
            dados_validos = temperatura_schema.load(request_data)
        except ValidationError as error:
            return {"error": f"{error.messages}"}, 422

        # Grava o registro no db
        try:
            if TemperaturaService.save_to_db(dados_validos):
                return temperatura_schema.dump(dados_validos), 201
            return {"message": 'erro 1'}

        except InternalServerError:
            return INTERNAL_SERVER_ERROR


@ns_temp.route('/read', endpoint='temp_read')
@ns_temp.param('id_paciente', 'Identificador id_paciente')
@ns_temp.param('id_sessao', 'Identificador id_sessao')
@ns_temp.param('id_exercicio', 'Identificador id_exercicio')
@ns_temp.doc(responses={
    200: 'OK',
    201: 'Created',
    202: 'Accepted',
    204: 'No Content',
    304: 'Not Modified',
    400: 'Validation Error',
    401: 'Unauthorized ',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
})
class TempRead(Resource):
    @ ns_temp.doc('Recupera temperatura através do id_paciente&id_sessao&id_exercicio')
    @ ns_temp.expect('id_paciente')
    @ ns_temp.expect('id_sessao')
    @ ns_temp.expect('id_exercicio')
    def get(self):
        '''
        requisição get
        retorna o registro de temperatura espeficidado pelo id_sessao
        '''
        id_paciente = request.args.get("id_paciente")
        id_sessao = request.args.get("id_sessao")
        id_exercicio = request.args.get("id_exercicio")

        try:
            dados = TemperaturaService.find_by_query(
                id_paciente, id_sessao, id_exercicio)
            if dados:
                return {"temperaturas": temperaturas_schema.dump(dados, many=True)}, 200

            if not dados:
                return {"message": "Nenhum resultado encontrado."}, 200

            return NOT_FOUND_ERROR
        except InternalServerError:
            return INTERNAL_SERVER_ERROR
