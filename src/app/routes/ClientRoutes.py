from flask import Blueprint
from app.controllers.ClientController import ClientController

client_bp = Blueprint("clients", __name__)


@client_bp.route("/clients", methods=["POST"])
def store_client():
    return ClientController.store()


@client_bp.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    return ClientController.update(client_id)