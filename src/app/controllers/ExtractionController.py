from flask import request, jsonify

from app.services.ExtractionService import ExtractionService


class ExtractionController:
    @staticmethod
    def store():
        try:
            file = request.files.get("file")
            document = ExtractionService.execute(file)

            return jsonify({
                "data": {
                    "id": document.id,
                    "name": document.name,
                    "content": document.content
                }
            }), 201

        except ValueError as error:
            return jsonify({
                "message": str(error)
            }), 400

        except Exception:
            return jsonify({
                "message": "Erro interno do servidor."
            }), 500

    @staticmethod
    def show(document_id):
        try:
            document = ExtractionService.find_by_id(document_id)

            if not document:
                return jsonify({
                    "message": "Documento não encontrado."
                }), 404

            return jsonify({
                "data": {
                    "id": document.id,
                    "name": document.name,
                    "content": document.content
                }
            }), 200

        except Exception:
            return jsonify({
                "message": "Erro interno do servidor."
            }), 500

    @staticmethod
    def index():
        try:
            page = request.args.get("page", default=1, type=int)
            limit = request.args.get("limit", default=10, type=int)
            name = request.args.get("name", default=None, type=str)

            result = ExtractionService.list_all(
                page=page,
                limit=limit,
                name=name
            )

            return jsonify({
                "data": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "content": item.content
                    }
                    for item in result["items"]
                ],
                "meta": {
                    "page": result["page"],
                    "limit": result["limit"],
                    "total": result["total"],
                    "pages": result["pages"]
                }
            }), 200

        except Exception:
            return jsonify({
                "message": "Erro interno do servidor."
            }), 500