from flask import Flask, jsonify

from app.config import Config
from app.extensions import db, migrate

# importar models para o Flask-Migrate reconhecer
from app.models import Document

# importar blueprint
from app.routes.ExtractionRoutes import extraction_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "API de Extração de Texto de PDFs",
            "usage": "Envie um POST para /extractions com um arquivo PDF"
        })

    app.register_blueprint(extraction_bp)

    return app