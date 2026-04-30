from flask import Blueprint
from app.controllers.ClientController import ClientController

client_bp = Blueprint("clients", __name__)

@client_bp.route("/clients", methods=["POST"])
def create():
    return ClientController.create()

@client_bp.route("/clients", methods=["GET"])
def list_clients():
    return ClientController.list()

@client_bp.route("/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
    return ClientController.find_by_id(client_id)

@client_bp.route("/clients/<int:client_id>", methods=["PUT"])
def update_client(client_id):
    return ClientController.update(client_id)

@client_bp.route("/clients/<int:client_id>", methods=["DELETE"])
def delete_client(client_id):
    return ClientController.delete(client_id)