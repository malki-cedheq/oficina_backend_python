'''
Arquivo: variables.py
Descrição: carrega as variáveis ambientes para API
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''

import os
from dotenv import load_dotenv

# Constantes de ambiente
load_dotenv()  # 1º carrega .env do diretório local


class Variables(object):
    # uso de variável ambiente
    APP_MODE = os.environ.get('APP_MODE')
    DB_OWNER = os.environ.get('DB_OWNER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_DATABASE = os.environ.get('DB_DATABASE')
    APP_HOST = os.environ.get('APP_HOST')
    APP_PORT = os.environ.get('APP_PORT')
    APP_URI = f'postgresql+psycopg2://{DB_OWNER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    MGDB_DATABASE = os.environ.get('MONGO_DATABASE')
    MGDB_OWNER = os.environ.get('MONGO_OWNER')
    MGDB_PASS = os.environ.get('MONGO_PASS')
    MGDB_HOST = os.environ.get('MONGO_HOST')
    MGDB_PORT = os.environ.get('MONGO_PORT')
    MGDB_URI = f'mongodb://{MGDB_OWNER}:{MGDB_PASS}@{MGDB_HOST}:{MGDB_HOST}/{MGDB_DATABASE}'
