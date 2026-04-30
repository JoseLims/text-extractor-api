from flask import request, jsonify
from app.services.ClientService import ClientService


class ClientController:

    @staticmethod
    def create():
        try:
            data = request.get_json()
            client = ClientService.create(data)

            return jsonify({
                "id": client.id,
                "name": client.name,
                "email": client.email
            }), 201

        except ValueError as e:
            return jsonify({"message": str(e)}), 400

        except Exception:
            return jsonify({"message": "Erro interno"}), 500

    @staticmethod
    def find_by_id(client_id):
        try:
            client = ClientService.find_by_id(client_id)

            return jsonify({
                "id": client.id,
                "name": client.name,
                "email": client.email
            }), 200

        except LookupError as e:
            return jsonify({"message": str(e)}), 404

        except Exception:
            return jsonify({"message": "Erro interno"}), 500

    @staticmethod
    def list():
        try:
            page = int(request.args.get("page", 1))
            limit = int(request.args.get("limit", 10))
            name = request.args.get("name")

            pagination = ClientService.list(page, limit, name)

            return jsonify({
                "data": [
                    {
                        "id": c.id,
                        "name": c.name,
                        "email": c.email
                    } for c in pagination.items
                ],
                "page": pagination.page,
                "total": pagination.total
            }), 200

        except Exception:
            return jsonify({"message": "Erro interno"}), 500

    @staticmethod
    def update(client_id):
        try:
            data = request.get_json()
            client = ClientService.update(client_id, data)

            return jsonify({
                "id": client.id,
                "name": client.name,
                "email": client.email
            }), 200

        except LookupError as e:
            return jsonify({"message": str(e)}), 404

        except Exception:
            return jsonify({"message": "Erro interno"}), 500

    @staticmethod
    def delete(client_id):
        try:
            ClientService.delete(client_id)

            return jsonify({
                "message": "Cliente removido com sucesso"
            }), 200

        except LookupError as e:
            return jsonify({"message": str(e)}), 404

        except Exception:
            return jsonify({"message": "Erro interno"}), 500