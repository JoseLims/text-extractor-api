from flask import request, jsonify

from app.services.AuthService import AuthService


class AuthController:
    @staticmethod
    def login():
        try:
            data = request.get_json()

            email = data.get("email")
            password = data.get("senha")

            session = AuthService.login(email, password)

            return jsonify({
                "token": session.token,
                "expires_at": session.expires_at.isoformat()
            }), 200

        except LookupError as e:
            return jsonify({"message": str(e)}), 401

        except ValueError as e:
            return jsonify({"message": str(e)}), 400

        except Exception:
            return jsonify({"message": "Erro interno"}), 500