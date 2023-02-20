'''
Arquivo: constants.py
Descrição: coletânea de constantes personalizadas utilizadas na aplicação
Autores: Malki-çedheq Benjamim,
Criado em: 31/07/2022
Atualizado em: 19/02/2023
'''

INTERNAL_SERVER_ERROR = (
    {"message": "Ocorreu um erro interno no servidor."}, 500)
NOT_FOUND_ERROR = ({"message": "O recurso não foi encontrado."}, 404)
METHOD_NOT_ALLOWED_ERROR = (
    {"message": "O método não é permitido nesta API."}, 405)
UNAUTHORIZED = ({"message": "Acesso não autorizado."}, 401)
