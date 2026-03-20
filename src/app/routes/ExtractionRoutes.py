from flask import Blueprint, jsonify
from app.controllers.ExtractionController import ExtractionController

# Instanciar o controlador
extraction_controller = ExtractionController()

# Criar blueprint para as rotas de extracton
extraction_routes = Blueprint("extractions", __name__)


@extraction_routes.route("/", methods=["GET"])
def home():
    """Endpoint de status da API."""
    return jsonify({
        "message": "API de Extração de Texto de PDFs",
        "usage": "Envie um POST para /extractions com um arquivo PDF",
        "example": "curl -F 'file=@seu_arquivo.pdf' http://localhost:5000/extractions"
    })


@extraction_routes.route("/extractions", methods=["POST"])
def extractions():
    """Endpoint para extrair texto de um PDF via upload."""
    return extraction_controller.extract_pdf()
