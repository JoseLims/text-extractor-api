from flask import Blueprint
from app.controllers.AuthController import AuthController

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth", methods=["POST"])
def login():
    return AuthController.login()