# resources/thing.py
from flask_restx import Namespace, Resource, reqparse

ns_thing = Namespace('things', description='Things operations')

parser_thing_register = reqparse.RequestParser()
parser_thing_register.add_argument(
    'nome', type=str, help='Deve informar o nome', required=True, location='json')


@ns_thing.route('/thing')
@ns_thing.doc('create', parser=parser_thing_register)
@ns_thing.response(201, 'Created')
class ItemRegisterResource(Resource):
    '''
        Recurso para a criação de novos registros
    '''

    def post(self):
        return {"method": "POST", "message": "Criado com sucesso!"}


@ns_thing.route('/things')
class ItemListResource(Resource):

    @ns_thing.doc('read all')
    def get(self):
        return {"method": "GET ALL", "message": {"itens": []}}


@ns_thing.route('/thing/<int:thing_id>')
@ns_thing.param('thing_id', 'Identificador do thing')
@ns_thing.expect('thing_id')
@ns_thing.doc(responses={
    200: 'Success',
    400: 'Validation Error',
    403: 'Not Authorized',
    404: 'Not Found',
    500: 'Internal Server Error'
})
class ItemResource(Resource):
    '''
    Recursos para recuperação, atualização e exclusão de registros a partir do id
    '''

    @ns_thing.doc('read por thing_id')
    def get(self, thing_id):
        if thing_id == 1:
            return {"method": "GET", "message": "{} encontrado!".format(thing_id)}
        ns_thing.abort(404, "{} não existe".format(thing_id))

    @ns_thing.doc('update por thing_id')
    def put(self, thing_id):
        if thing_id == 1:
            return {"method": "PUT", "message": f"{thing_id} atualizado com sucesso!"}
        ns_thing.abort(404, "{} não existe".format(thing_id))

    @ns_thing.doc('delete por thing_id')
    def delete(self, thing_id):
        if thing_id == 1:
            return {"method": "DELETE", "message": f"{thing_id} excluido com sucesso!"}
        ns_thing.abort(404, "{} não existe".format(thing_id))
