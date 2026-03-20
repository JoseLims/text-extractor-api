from flask import request, jsonify
from app.services.ExtractionService import ExtractionService


class ExtractionController:
    """Controlador responsável por gerenciar requisições de extração de PDFs."""
    
    def __init__(self):
        self.extraction_service = ExtractionService
    
    def extract_pdf(self):
        """Método controlador para extrair texto de um PDF enviado.
        
        Valida o arquivo, chama o serviço de extração e retorna resposta JSON.
        """
        # Validar arquivo
        is_valid, error_response = self._validate_file()
        if not is_valid:
            return error_response
        
        # Extrair texto via service
        try:
            file = request.files['file']
            document = self.extraction_service.extract_pdf(file=file)
            
            return jsonify({
                "data": {
                    "name": document.name,
                    "content": document.content
                }
            }), 200
            
        except ValueError as e:
            return jsonify({"message": str(e)}), 400
        except Exception as e:
            return jsonify({"message": f"Erro interno: {str(e)}"}), 500
    
    def _validate_file(self):
        """Valida se o arquivo foi enviado e se é um PDF válido.
        
        Returns:
            Tuple[bool, dict]: (é válido?, resposta_json)
        """
        is_valid = True
        error_response = None
        
        if 'file' not in request.files:
            is_valid = False
            error_response = (jsonify({"message": "Nenhum arquivo enviado."}), 400)
        elif request.files['file'].filename == "":
            is_valid = False
            error_response = (jsonify({"message": "Arquivo inválido."}), 400)
        elif not request.files['file'].filename.lower().endswith(".pdf"):
            is_valid = False
            error_response = (jsonify({"message": "O arquivo precisa ser um PDF."}), 400)
        
        return is_valid, error_response

