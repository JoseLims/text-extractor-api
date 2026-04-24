from flask import request, jsonify

from app.services.ExtractionService import ExtractionService


class ExtractionController:
    @staticmethod
    def store():
        try:
            file = request.files.get("file")
            client_id = request.form.get("client_id", type=int)

            document = ExtractionService.execute(file, client_id)

            response = jsonify({
                "data": {
                    "id": document.id,
                    "name": document.name,
                    "content": document.content,
                    "client": {
                        "id": document.client.id,
                        "name": document.client.name,
                        "email": document.client.email
                    }
                }
            })
            status_code = 201

        except ValueError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 400

        except LookupError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 404

        except Exception:
            response = jsonify({
                "message": "Erro interno do servidor."
            })
            status_code = 500

        return response, status_code

    @staticmethod
    def show(document_id):
        try:
            document = ExtractionService.find_by_id(document_id)

            response = jsonify({
                "data": {
                    "id": document.id,
                    "name": document.name,
                    "content": document.content,
                    "client": {
                        "id": document.client.id,
                        "name": document.client.name,
                        "email": document.client.email
                    }
                }
            })
            status_code = 200

        except LookupError as error:
            response = jsonify({
                "message": str(error)
            })
            status_code = 404

        except Exception:
            response = jsonify({
                "message": "Erro interno do servidor."
            })
            status_code = 500

        return response, status_code

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

            response = jsonify({
                "data": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "content": item.content,
                        "client": {
                            "id": item.client.id,
                            "name": item.client.name,
                            "email": item.client.email
                        }
                    }
                    for item in result["items"]
                ],
                "meta": {
                    "page": result["page"],
                    "limit": result["limit"],
                    "total": result["total"],
                    "pages": result["pages"]
                }
            })
            status_code = 200

        except Exception:
            response = jsonify({
                "message": "Erro interno do servidor."
            })
            status_code = 500

        return response, status_code

    @staticmethod
    def update(client_id, document_id):
        try:
            data = request.get_json()

            if not data:
                raise ValueError("Os dados da extração não foram enviados.")

            name = data.get("name")
            content = data.get("content")

            document = ExtractionService.update(
                client_id=client_id,
                document_id=document_id,
                name=name,
                content=content
            )

            response = jsonify({
                "data": {
                    "id": document.id,
                    "name": document.name,
                    "content": document.content,
                    "client": {
                        "id": document.client.id,
                        "name": document.client.name,
                        "email": document.client.email
                    }
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