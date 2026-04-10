from pypdf import PdfReader
from werkzeug.datastructures import FileStorage

from app.extensions import db
from app.models.Document import Document


class ExtractionService:
    @staticmethod
    def execute(file: FileStorage) -> Document:
        if file is None:
            raise ValueError("Nenhum arquivo enviado.")

        if file.filename == "":
            raise ValueError("Arquivo inválido.")

        if not file.filename.lower().endswith(".pdf"):
            raise ValueError("O arquivo precisa ser um PDF.")

        try:
            reader = PdfReader(file.stream)
            extracted_pages = []

            for page in reader.pages:
                page_text = page.extract_text() or ""
                if page_text.strip():
                    extracted_pages.append(page_text)

            extracted_text = "\n".join(extracted_pages).strip()

            if not extracted_text:
                raise ValueError("O PDF não contém texto extraível.")

            document = Document(
                name=file.filename,
                content=extracted_text
            )

            db.session.add(document)
            db.session.commit()

            return document

        except ValueError:
            raise

        except Exception as error:
            db.session.rollback()
            raise ValueError(f"Erro ao processar o PDF: {error}")

    @staticmethod
    def find_by_id(document_id: int) -> Document:
        document = Document.query.get(document_id)

        if not document:
            raise LookupError("Documento não encontrado.")

        return document

    @staticmethod
    def list_all(page=1, limit=10, name=None):
        query = Document.query

        if name:
            query = query.filter(Document.name.ilike(f"%{name}%"))

        pagination = query.order_by(Document.id.asc()).paginate(
            page=page,
            per_page=limit,
            error_out=False
        )

        return {
            "items": pagination.items,
            "page": pagination.page,
            "limit": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages
        }