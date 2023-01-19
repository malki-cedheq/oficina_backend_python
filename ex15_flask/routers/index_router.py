# routers/index_router.py
from flask import Blueprint

index_router = Blueprint("index_router", __name__)


@index_router.route("/", methods=["GET"])
def home():
    return {"message": "Hello Wordl"}, 200
