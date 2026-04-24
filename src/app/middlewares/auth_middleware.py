from flask import request, jsonify

from app.services.AuthService import AuthService


def require_auth():
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token não informado"}), 401

    try:
        session = AuthService.validate_session(token)
        request.client = session.client
    except Exception as e:
        return jsonify({"message": str(e)}), 401