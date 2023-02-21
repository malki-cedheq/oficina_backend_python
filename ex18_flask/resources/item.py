# resources/item.py
from flask_restx import Namespace, Resource, reqparse

api = Namespace('items', description='Items operations')

parser_item_register = reqparse.RequestParser()
parser_item_register.add_argument(
    'nome', type=str, help='Deve informar o nome', required=True, location='json')


@api.route('/item')
@api.doc('create', parser=parser_item_register)
@api.response(201, 'Created')
class ItemRegisterResource(Resource):
    '''
        Recurso para a criação de novos registros
    '''

    def post(self):
        return {"method": "POST", "message": "Criado com sucesso!"}


@api.route('/items')
class ItemListResource(Resource):

    @api.doc('read all')
    def get(self):
        return {"method": "GET ALL", "message": {"itens": []}}


@api.route('/item/<int:item_id>')
@api.param('item_id', 'Identificador do item')
@api.expect('item_id')
@api.doc(responses={
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

    @api.doc('read por item_id')
    def get(self, item_id):
        if item_id == 1:
            return {"method": "GET", "message": "{} encontrado!".format(item_id)}
        api.abort(404, "{} não existe".format(item_id))

    @api.doc('update por item_id')
    def put(self, item_id):
        if item_id == 1:
            return {"method": "PUT", "message": f"{item_id} atualizado com sucesso!"}
        api.abort(404, "{} não existe".format(item_id))

    @api.doc('delete por item_id')
    def delete(self, item_id):
        if item_id == 1:
            return {"method": "DELETE", "message": f"{item_id} excluido com sucesso!"}
        api.abort(404, "{} não existe".format(item_id))
