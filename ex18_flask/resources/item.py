# resources/item.py
from flask_restx import Namespace, Resource, reqparse

api = Namespace('items', description='Items operations')


@api.route('/item/<int:item_id>')
@api.param('item_id', 'Identificador do item')
@api.doc(responses={
    200: 'Success',
    400: 'Validation Error',
    403: 'Not Authorized',
    404: 'Not Found',
    500: 'Internal Server Error'
})
class ItemResource(Resource):
    parser = reqparse.RequestParser()
    '''parser.add_argument('item_id', type=int, required=True,
                        help='Deve informar o item_id')'''

    @api.doc('read por item_id', parser=parser)
    def get(self, item_id):
        if item_id == 1:
            return {"method": "GET", "message": "{} encontrado!".format(item_id)}
        api.abort(404, "{} não existe".format(item_id))

    @api.doc('create')
    @api.response(201, 'Created')
    def post(self):
        return {"method": "POST", "message": "Criado com sucesso!"}

    @api.doc('update por item_id', parser=parser)
    def put(self, item_id):
        if item_id == 1:
            return {"method": "PUT", "message": f"{item_id} atualizado com sucesso!"}
        api.abort(404, "{} não existe".format(item_id))

    @api.doc('delete por item_id', parser=parser)
    def delete(self, item_id):
        if item_id == 1:
            return {"method": "DELETE", "message": f"{item_id} excluido com sucesso!"}
        api.abort(404, "{} não existe".format(item_id))


@api.route('/items')
class ItemListResource(Resource):

    @api.doc('read all')
    def get(self):
        return {"method": "GET ALL", "message": {"itens": []}}
