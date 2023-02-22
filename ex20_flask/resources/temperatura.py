'''
Arquivo: resouces.temperatura.py
Descrição: Definição dos endpoints para o recurso temperatura
Autores: Malki-çedheq Benjamim,
Criado em: 25/08/2022
Atualizado em: 21/02/2022
'''
from flask import request
from flask_restx import Resource, reqparse, Namespace
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from hmac import compare_digest
from werkzeug.exceptions import InternalServerError
from marshmallow import ValidationError
from constants import NOT_FOUND_ERROR, INTERNAL_SERVER_ERROR, UNAUTHORIZED
from schemas.temperatura import temperatura_schema, temperaturas_schema
from services.temperatura import Temperatura as TemperaturaService
from security import privilege_required

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
@ns_temp.route('/temperaturas', endpoint='temp_list')
class TempList(Resource):

    @ns_temp.doc('Recupera todos os temperaturas cadastrados')
    @login_required
    def get(self):
        '''
        requisição get
        retorna os registros de todos os usuarios cadastrados
        '''
        usuarios = TemperaturaService.find_all()

        if usuarios:
            return {"usuarios": temperaturas_schema.dump(usuarios, many=True)}, 200

        if not usuarios:
            return {"message": "Nenhum resultado encontrado."}, 200

        return NOT_FOUND_ERROR


@ns_temp.route('/usuario', endpoint='user_register')
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
    parser.add_argument('nome', type=str, required=True,
                        help='Deve informar o nome', location='json')
    parser.add_argument('email', type=str, required=True,
                        help='Deve informar o email', location='json')
    parser.add_argument('senha', type=str, required=True,
                        help='Deve informar o senha', location='json')
    parser.add_argument('nivel_acesso', type=int, required=True,
                        help='Deve informar o nivel_acesso', location='json')
    parser.add_argument('ativo', type=bool, required=True,
                        help='Deve informar o email', location='json')

    @ns_temp.doc('Cadastra um novo temperatura', parser=parser)
    @ns_temp.expect(parser)
    # @login_required
    # @privilege_required(acess_level=0)
    def post(self):
        '''
        requisição post
        solicita cadastro de temperatura
        a requisição deve incluir os dados do temperatura em formato json
        retorna os dados cadastrados, em caso de sucesso
        retorna json com messagem, em caso de falha
        '''
        request_data = request.get_json()  # usando flask
        usuario_nome = request_data["nome"]
        usuario_email = request_data["email"]

        usuario = TemperaturaService.find_by_nome(usuario_nome)

        if usuario:
            return {"message": f"Usuario {usuario_nome} já cadastrado."}, 400

        usuario = TemperaturaService.find_by_email(usuario_email)

        if usuario:
            return {"message": f"E-mail {usuario_email} já cadastrado."}, 400

        # Valida e desserializa o request_data
        try:
            usuario_valido = temperatura_schema.load(request_data)
        except ValidationError as error:
            return {"error": f"{error.messages}"}, 422

        # Grava o registro no db
        try:
            # Criptografa a senha antes de salvar o registro
            usuario_valido.senha = generate_password_hash(
                usuario_valido.senha, method='sha256')
            # Por padrão os temperaturas tem acesso bloqueado
            usuario_valido.ativo = bool(False)
            TemperaturaService.save_to_db(usuario_valido)

            link = "https://www.google.com.br"  # aqui deve constar o link da plataforma
            conteudo = f'<h2>Você foi registrado no sistema.</h2><p>Acesse <a href="{link}">este link</a> para ser redirecionado.</p>'
            TemperaturaService.send_email(usuario_valido, contents=conteudo)
            return temperatura_schema.dump(usuario_valido), 201
        except InternalServerError:
            return INTERNAL_SERVER_ERROR


@ns_temp.route('/usuario/<int:id_temperatura>', endpoint='temp_read')
@ns_temp.param('id_temperatura', 'Identificador do temperatura')
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
    parser_id = reqparse.RequestParser()
    parser_id.add_argument('id_temperatura', type=int, required=True,
                           help='Deve informar o id_temperatura')

    @ ns_temp.doc('Recupera temperatura através do id_temperatura', parser=parser_id)
    @ ns_temp.expect(parser_id)
    @ login_required
    def get(self, id_temperatura: int):
        '''
        requisição get
        retorna o registro de um usuario espeficidado pelo id_temperatura
        '''
        if (current_user.id_temperatura == id_temperatura or current_user.nivel_acesso == '0'):
            usuario = TemperaturaService.find_by_id(id_temperatura)
            if usuario:
                return temperatura_schema.dump(usuario), 200

            return NOT_FOUND_ERROR
        return UNAUTHORIZED


@ns_temp.route('/usuario/<int:id_temperatura>', endpoint='temp_update')
@ns_temp.param('id_temperatura', 'Identificador do temperatura')
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
class TempUpdate(Resource):
    # coleta os dados da requisição
    parser_put = reqparse.RequestParser()  # usando flask-restx
    parser_put.add_argument('id_temperatura', type=str, required=True,
                            help='Deve informar o id_temperatura', location='query')
    parser_put.add_argument('nome', type=str, required=False,
                            help='Deve informar o nome', location='json')
    parser_put.add_argument('email', type=str, required=False,
                            help='Deve informar o email', location='json')
    parser_put.add_argument('senha', type=str, required=False,
                            help='Deve informar o senha', location='json')
    parser_put.add_argument('nivel_acesso', type=int, required=False,
                            help='Deve informar o nivel_acesso', location='json')
    parser_put.add_argument('ativo', type=bool, required=False,
                            help='Deve informar o email', location='json')

    @ ns_temp.doc('Modifica um temperatura através do id_temperatura', parser=parser_put)
    @ ns_temp.expect(parser_put)
    @ ns_temp.response(201, 'Created')
    @ login_required
    @ privilege_required(acess_level=0)
    def put(self, id_temperatura: int):
        '''
        requisição put
        solicita atualização de temperatura específicado pelo id_temperatura
        a requisição deve incluir os dados do temperatura em formato json
        retorna os dados cadastrados, em caso de sucesso
        retorna json com messagem, em caso de falha
        '''
        usuario = TemperaturaService.find_by_id(id_temperatura)

        if usuario:  # se o temperatura exitir atualiza os dados

            # coleta os dados da requisição
            request_data = request.get_json()  # usando flask
            print(request_data)

            # Valida e desserializa o request_data
            try:
                usuario_valido = temperatura_schema.load(
                    request_data, instance=usuario, partial=True
                )
            except ValidationError as error:
                return {"error": f"{error.messages}"}, 422

            # Atualiza o registro no db
            try:
                TemperaturaService.save_to_db(usuario_valido)
                return temperatura_schema.dump(usuario_valido), 200
            except InternalServerError:
                return INTERNAL_SERVER_ERROR

        return NOT_FOUND_ERROR


@ns_temp.route('/usuario/<int:id_temperatura>', endpoint='temp_delete')
@ns_temp.param('id_temperatura', 'Identificador do temperatura')
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
class TempDelete(Resource):
    parser_id = reqparse.RequestParser()
    parser_id.add_argument('id_temperatura', type=int, required=True,
                           help='Deve informar o id_temperatura')

    @ ns_temp.doc('Remove um temperatura através do id_temperatura', parser=parser_id)
    @ ns_temp.expect(parser_id)
    @ login_required
    @ privilege_required(acess_level=0)
    def delete(self, id_temperatura: int):
        '''
        requisição delete
        solicita exclusão de temperatura específicado pelo id_temperatura
        retorna json com messagem de sucesso ou falha
        '''
        usuario = TemperaturaService.find_by_id(id_temperatura)

        if usuario:  # se temperatura existir
            # Apaga o registro no db
            try:
                usuario.delete_from_db()
                return {"message": f"Usuario {usuario.id_temperatura} excluido com sucesso."}, 200
            except InternalServerError:
                return INTERNAL_SERVER_ERROR

        return NOT_FOUND_ERROR
