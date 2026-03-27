from flask import Blueprint

from app.controllers.ExtractionController import ExtractionController

extraction_bp = Blueprint("extractions", __name__)


@extraction_bp.route("/extractions", methods=["POST"])
def store_extraction():
    return ExtractionController.store()