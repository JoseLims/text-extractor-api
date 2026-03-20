from flask import Flask
from app.routes.ExtractionRoutes import extraction_routes


def create_app() -> Flask:
    """Factory para criar e configurar a aplicação Flask.
    
    Returns:
        Flask: Instância configurada da aplicação.
    """
    app = Flask(__name__)
    
    # Registrar blueprints
    app.register_blueprint(extraction_routes)
    
    return app
