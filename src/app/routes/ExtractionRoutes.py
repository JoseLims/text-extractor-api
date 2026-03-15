from flask import Blueprint, request, jsonify

from app.controllers.ExtractionController import extract_pdf

bp = Blueprint("extractions", __name__)


@bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de Extração de Texto de PDFs",
        "usage": "Envie um POST para /extractions com um arquivo PDF",
        "example": "curl -F 'file=@seu_arquivo.pdf' http://localhost:5000/extractions",
    })


@bp.route("/extractions", methods=["POST"])
def extractions():
    file = request.files.get("file")
    text, error = extract_pdf(file)
    if error:
        message, status = error
        return jsonify({"message": message}), status

    return jsonify({"message": text})
