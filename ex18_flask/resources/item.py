# resources/item.py
from flask_restx import Namespace, Resource, reqparse

ns_item = Namespace('items', description='Items operations')

parser_item_register = reqparse.RequestParser()
parser_item_register.add_argument(
    'nome', type=str, help='Deve informar o nome', required=True, location='json')


@ns_item.route('/item')
@ns_item.doc('create', parser=parser_item_register)
@ns_item.response(201, 'Created')
class ItemRegisterResource(Resource):
    '''
        Recurso para a criação de novos registros
    '''

    def post(self):
        return {"method": "POST", "message": "Criado com sucesso!"}


@ns_item.route('/items')
class ItemListResource(Resource):

    @ns_item.doc('read all')
    def get(self):
        return {"method": "GET ALL", "message": {"itens": []}}


@ns_item.route('/item/<int:item_id>')
@ns_item.param('item_id', 'Identificador do item')
@ns_item.expect('item_id')
@ns_item.doc(responses={
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

    @ns_item.doc('read por item_id')
    def get(self, item_id):
        if item_id == 1:
            return {"method": "GET", "message": "{} encontrado!".format(item_id)}
        ns_item.abort(404, "{} não existe".format(item_id))

    @ns_item.doc('update por item_id')
    def put(self, item_id):
        if item_id == 1:
            return {"method": "PUT", "message": f"{item_id} atualizado com sucesso!"}
        ns_item.abort(404, "{} não existe".format(item_id))

    @ns_item.doc('delete por item_id')
    def delete(self, item_id):
        if item_id == 1:
            return {"method": "DELETE", "message": f"{item_id} excluido com sucesso!"}
        ns_item.abort(404, "{} não existe".format(item_id))
