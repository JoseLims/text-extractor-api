from flask import jsonify, request

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