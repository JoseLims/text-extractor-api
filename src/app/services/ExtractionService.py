from werkzeug.datastructures import FileStorage
from app.models.Document import Document
import PyPDF2


class ExtractionService:
    """Serviço responsável pela extração de texto de PDFs."""
    
    @staticmethod
    def extract_pdf(file: FileStorage) -> Document:
        """Extrai texto de um arquivo PDF.
        
        Args:
            file: Arquivo enviado via upload (FileStorage).
            
        Returns:
            Document: Instância contendo nome e conteúdo extraído.
            
        Raises:
            ValueError: Se houver erro na leitura ou validação.
        """
        try:
            reader = PyPDF2.PdfReader(file.stream)
            
            text_parts = []
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text_parts.append(page_text)
            
            extracted_text = "\n".join(text_parts).strip()
            
            if not extracted_text:
                raise ValueError("O PDF não contém texto extraível.")
            
            document = Document(
                name=file.filename,
                content=extracted_text
            )
            
            return document
            
        except Exception as e:
            raise ValueError(f"Erro ao ler o PDF: {str(e)}")
