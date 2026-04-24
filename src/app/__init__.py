from flask import Flask, jsonify

from app.config import Config
from app.extensions import db, migrate
from app.models import Client, Document
from app.routes.ExtractionRoutes import extraction_bp
from app.routes.ClientRoutes import client_bp
from app.routes.AuthRoutes import auth_bp 


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
    app.register_blueprint(client_bp)
    app.register_blueprint(auth_bp)  
    return app