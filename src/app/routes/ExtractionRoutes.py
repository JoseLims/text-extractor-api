from flask import Blueprint
from app.controllers.ExtractionController import ExtractionController

extraction_bp = Blueprint("extractions", __name__)


@extraction_bp.route("/extractions", methods=["POST"])
def store_extraction():
    return ExtractionController.store()


@extraction_bp.route("/extractions", methods=["GET"])
def list_extractions():
    return ExtractionController.index()


@extraction_bp.route("/extractions/<int:document_id>", methods=["GET"])
def show_extraction(document_id):
    return ExtractionController.show(document_id)


@extraction_bp.route("/clients/<int:client_id>/extractions/<int:document_id>", methods=["PUT"])
def update_extraction(client_id, document_id):
    return ExtractionController.update(client_id, document_id)