'''
Arquivo: resouces.usuario.py
Descrição: Definição dos endpoints para o recurso usuário
Autores: Malki-çedheq Benjamim,
Criado em: 25/08/2022
Atualizado em: 19/02/2022
'''
from flask import Blueprint, flash, request
from flask_restx import Api, Resource, reqparse
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from hmac import compare_digest
from werkzeug.exceptions import InternalServerError
from marshmallow import ValidationError
from constants import NOT_FOUND_ERROR, INTERNAL_SERVER_ERROR, UNAUTHORIZED
from schemas.usuario import usuario_schema, usuarios_schema
from services.usuario import Usuario as UsuarioService
from security import privilege_required

user_bp = Blueprint('user_bp', __name__, url_prefix='/api')
user_api = Api(user_bp,  doc='/doc', version='1.0',
               title='Usuários API', description='Gerenciamento de Usuários')
user_ns = user_api.namespace(
    'User NS', path='/op', description='Operações com recurso usuario')

auth_ns = user_api.namespace(
    'Auth NS', path='/ctrl', description='Operações com recurso auth')


@user_ns.route('/usuarios', endpoint='user_list')
class UserList(Resource):

    @user_ns.doc('Recupera todos os usuários cadastrados')
    @login_required
    def get(self):
        '''
        requisição get
        retorna os registros de todos os usuarios cadastrados
        '''
        usuarios = UsuarioService.find_all()

        if usuarios:
            return {"usuarios": usuarios_schema.dump(usuarios, many=True)}, 200

        if not usuarios:
            return {"message": "Nenhum resultado encontrado."}, 200

        return NOT_FOUND_ERROR


@user_ns.route('/usuario', endpoint='user_register')
@user_ns.doc(responses={
    201: 'Created',
    400: 'Validation Error',
    403: 'Not Authorized',
    404: 'Not Found',
    500: 'Internal Server Error'
})
class UserRegister(Resource):
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

    @user_ns.doc('Cadastra um novo usuário', parser=parser)
    @user_ns.expect(parser)
    # @login_required
    # @privilege_required(acess_level=0)
    def post(self):
        '''
        requisição post
        solicita cadastro de usuário
        a requisição deve incluir os dados do usuário em formato json
        retorna os dados cadastrados, em caso de sucesso
        retorna json com messagem, em caso de falha
        '''
        request_data = request.get_json()  # usando flask
        usuario_nome = request_data["nome"]
        usuario_email = request_data["email"]

        usuario = UsuarioService.find_by_nome(usuario_nome)

        if usuario:
            return {"message": f"Usuario {usuario_nome} já cadastrado."}, 400

        usuario = UsuarioService.find_by_email(usuario_email)

        if usuario:
            return {"message": f"E-mail {usuario_email} já cadastrado."}, 400

        # Valida e desserializa o request_data
        try:
            usuario_valido = usuario_schema.load(request_data)
        except ValidationError as error:
            return {"error": f"{error.messages}"}, 422

        # Grava o registro no db
        try:
            # Criptografa a senha antes de salvar o registro
            usuario_valido.senha = generate_password_hash(
                usuario_valido.senha, method='sha256')
            # Por padrão os usuários tem acesso bloqueado
            usuario_valido.ativo = bool(False)
            UsuarioService.save_to_db(usuario_valido)

            link = "https://www.google.com.br"  # aqui deve constar o link da plataforma
            conteudo = f'<h2>Você foi registrado no sistema.</h2><p>Acesse <a href="{link}">este link</a> para ser redirecionado.</p>'
            UsuarioService.send_email(usuario_valido, contents=conteudo)
            return usuario_schema.dump(usuario_valido), 201
        except InternalServerError:
            return INTERNAL_SERVER_ERROR


@user_ns.route('/usuario/<int:id_usuario>', endpoint='user_ops')
@user_ns.param('id_usuario', 'Identificador do usuário')
@user_ns.doc(responses={
    200: 'Success',
    400: 'Validation Error',
    403: 'Not Authorized',
    404: 'Not Found',
    500: 'Internal Server Error'
})
class User(Resource):
    parser_id = reqparse.RequestParser()
    parser_id.add_argument('id_usuario', type=int, required=True,
                           help='Deve informar o id_usuario')

    @user_ns.doc('Recupera usuário através do id_usuario', parser=parser_id)
    @user_ns.expect(parser_id)
    @login_required
    def get(self, id_usuario: int):
        '''
        requisição get
        retorna o registro de um usuario espeficidado pelo id_usuario
        '''
        if (current_user.id_usuario == id_usuario or current_user.nivel_acesso == '0'):
            usuario = UsuarioService.find_by_id(id_usuario)
            if usuario:
                return usuario_schema.dump(usuario), 200

            return NOT_FOUND_ERROR
        return UNAUTHORIZED

    # coleta os dados da requisição
    parser_put = reqparse.RequestParser()  # usando flask-restx
    parser_put.add_argument('id_usuario', type=str, required=True,
                            help='Deve informar o id_usuario', location='query')
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

    @user_ns.doc('Modifica um usuário através do id_usuario', parser=parser_put)
    @user_ns.expect(parser_put)
    @login_required
    @privilege_required(acess_level=0)
    def put(self, id_usuario: int):
        '''
        requisição put
        solicita atualização de usuário específicado pelo id_usuario
        a requisição deve incluir os dados do usuário em formato json
        retorna os dados cadastrados, em caso de sucesso
        retorna json com messagem, em caso de falha
        '''
        usuario = UsuarioService.find_by_id(id_usuario)

        if usuario:  # se o usuário exitir atualiza os dados

            # coleta os dados da requisição
            request_data = request.get_json()  # usando flask
            print(request_data)

            # Valida e desserializa o request_data
            try:
                usuario_valido = usuario_schema.load(
                    request_data, instance=usuario, partial=True
                )
            except ValidationError as error:
                return {"error": f"{error.messages}"}, 422

            # Atualiza o registro no db
            try:
                UsuarioService.save_to_db(usuario_valido)
                return usuario_schema.dump(usuario_valido), 200
            except InternalServerError:
                return INTERNAL_SERVER_ERROR

        return NOT_FOUND_ERROR

    @user_ns.doc('Remove um usuário através do id_usuario', parser=parser_id)
    @user_ns.expect(parser_id)
    @login_required
    @privilege_required(acess_level=0)
    def delete(self, id_usuario: int):
        '''
        requisição delete
        solicita exclusão de usuário específicado pelo id_usuario
        retorna json com messagem de sucesso ou falha
        '''
        usuario = UsuarioService.find_by_id(id_usuario)

        if usuario:  # se usuário existir
            # Apaga o registro no db
            try:
                usuario.delete_from_db()
                return {"message": f"Usuario {usuario.id_usuario} excluido com sucesso."}, 200
            except InternalServerError:
                return INTERNAL_SERVER_ERROR

        return NOT_FOUND_ERROR

# Recurso para login do usuário


parser_login = reqparse.RequestParser()  # usando flask-restx
parser_login.add_argument('email', type=str, required=True,
                          help='Deve informar o email', location='json')
parser_login.add_argument('senha', type=str, required=True,
                          help='Deve informar o senha', location='json')


@user_ns.doc('Login do usuário a partir do e-mail e senha', parser=parser_login)
@user_ns.expect(parser_login)
@auth_ns.route('/login', endpoint='login')
class Login(Resource):

    @auth_ns.doc('Recurso para login do usuário')
    def post(self):
        '''
        requisição post
        solicita o login de um usuário
        a requisição deve incluir os dados de login do usuário em formato "FORM SUBMIT"
        em caso de sucesso ocorre redirecionamento para página profile
        em caso de falha retorna mensagem de erro e redireciona para página de login
        '''
        # coleta os dados da requisição
        args = parser_login.parse_args()
        usuario_password = args["senha"]
        usuario_email = args["email"]

        #print(f'Senha informada: {usuario_password} \nSenha hash: {generate_password_hash(usuario_password, method="sha256")}')
        usuario = UsuarioService.find_by_email(usuario_email)
        if usuario is None:
            return {"message": f"Usuário de e-mail {usuario_email} não encontrado."}, 404

        # verifica se o usuário existe e a senha corresponde e se está ativo
        if usuario and check_password_hash(usuario.senha, usuario_password) and compare_digest(usuario_email, usuario.email) and usuario.ativo:
            if login_user(usuario):
                return {"isLogged": "true"}, 200

        flash('Credenciais inválidas.')
        return {"isLogged": "false"}, 200

# Recurso de logout do usuário


@auth_ns.route('/logout', endpoint='logout')
class Logout(Resource):

    @auth_ns.doc('Recurso de logout do usuário')
    @login_required
    def get(self):
        '''
        requisição get
        desloga o usuário corrente
        limpa o current_user do Flask-Login
        e redireciona para página index
        '''
        if logout_user():
            return {"isLogged": "false"}, 200
        return {"isLogged": "false"}, 200
