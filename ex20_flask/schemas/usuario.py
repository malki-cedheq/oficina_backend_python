'''
Arquivo: schemas.usuario.py
Descrição:  schema para a entidade usuario na API REST
            schemas definem a estrutura dos dados e também a validação destes dados
Autores: Malki-çedheq Benjamim,
Criado em: 27/07/2022
Atualizado em: 19/02/2023
'''
from models.usuario import Usuario as UsuarioModel
from db import ma


class Usuario(ma.SQLAlchemyAutoSchema):  # Schema / SQLAlchemyAutoSchema
    class Meta:
        model = UsuarioModel
        load_instance = True
        include_fk = True

    # implementação de HATEOAS
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("bp.user_ops", id_usuario="<id_usuario>"),
            "collection": ma.URLFor("bp.user_list"),
        }
    )


usuario_schema = Usuario()
usuarios_schema = Usuario(many=True)
