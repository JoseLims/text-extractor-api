from flask import Blueprint
from app.controllers.ClientController import ClientController

client_bp = Blueprint("clients", __name__)


@client_bp.route("/clients", methods=["POST"])
def store_client():
    return ClientController.store()