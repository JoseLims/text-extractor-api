from flask import request, jsonify

from app.services.ClientService import ClientService


class ClientController:
    @staticmethod
    def store():
        try:
            data = request.get_json()

            if not data:
                raise ValueError("Os dados do cliente não foram enviados.")

            name = data.get("name")
            email = data.get("email")

            client = ClientService.create(name, email)

            response = jsonify({
                "data": {
                    "id": client.id,
                    "name": client.name,
                    "email": client.email
                }
            })
            status_code = 201

        except ValueError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 400

        except Exception:
            response = jsonify({
                "message": "Erro interno do servidor."
            })
            status_code = 500

        return response, status_code

    @staticmethod
    def update(client_id):
        try:
            data = request.get_json()

            if not data:
                raise ValueError("Os dados do cliente não foram enviados.")

            name = data.get("name")
            email = data.get("email")

            client = ClientService.update(client_id, name, email)

            response = jsonify({
                "data": {
                    "id": client.id,
                    "name": client.name,
                    "email": client.email
                }
            })
            status_code = 200

        except LookupError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 404

        except ValueError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 400

        except Exception:
            response = jsonify({
                "message": "Erro interno do servidor."
            })
            status_code = 500

        return response, status_code