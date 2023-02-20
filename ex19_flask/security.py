'''
Arquivo: security.py
Descrição: Funções auxiliares de segurança
Autores: Malki-çedheq Benjamim,
Criado em: 25/08/2022
Atualizado em: 25/08/2022
'''
from functools import wraps  # necessário para decorador personalizado
from flask_login import current_user

# Decodifica o nível de acesso numérico para rótulo (label)


def find_privilege(acess_level: int):
    privilege = ""
    match acess_level:
        case 0: privilege = "admin"
        case 1: privilege = "manager"
        case 2: privilege = "user"
        case _:
            privilege = ""
    return privilege

# Decorador personalizado que verifica o nivel de acesso do usuario LOGADO


def privilege_required(acess_level: int):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            privilege = find_privilege(acess_level=current_user.nivel_acesso)
            match acess_level:
                case 0:
                    if privilege == "admin":
                        return fn(*args, **kwargs)
                    else:
                        return {"message": "Acesso restrito! Necessário privilégio de administrador."}, 403
                case 1:
                    if privilege == "admin" or privilege == "manager":
                        return fn(*args, **kwargs)
                    else:
                        return {"message": "Acesso restrito! Necessário privilégio de administrador ou manager."}, 403
                case 2:
                    if privilege == "admin" or privilege == "manager" or privilege == "user":
                        return fn(*args, **kwargs)
                    else:
                        return {"message": "Acesso restrito! Necessário privilégio de administrador, manager ou user."}, 403
                case _:
                    return {"message": "Acesso restrito! Você não possui privilégio suficiente."}, 403
        return decorator
    return wrapper
