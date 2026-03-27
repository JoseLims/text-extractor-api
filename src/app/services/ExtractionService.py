from pypdf import PdfReader

from app.extensions import db
from app.models.Document import Document


class ExtractionService:
    @staticmethod
    def execute(file):
        if file is None:
            raise ValueError("Nenhum arquivo enviado.")

        if file.filename == "":
            raise ValueError("Arquivo inválido.")

        if not file.filename.lower().endswith(".pdf"):
            raise ValueError("O arquivo precisa ser um PDF.")

        try:
            reader = PdfReader(file.stream)
            pages_text = []

            for page in reader.pages:
                page_text = page.extract_text() or ""
                if page_text.strip():
                    pages_text.append(page_text)

            content = "\n".join(pages_text).strip()

            if not content:
                raise ValueError("O PDF não contém texto extraível.")

            document = Document(
                name=file.filename,
                content=content
            )

            db.session.add(document)
            db.session.commit()

            return document

        except ValueError:
            raise
        except Exception as error:
            raise ValueError(f"Erro ao processar o PDF: {error}")