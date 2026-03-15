from typing import Optional, Tuple

from app.services.ExtractionService import extract


def validate_file(file) -> Tuple[bool, Optional[Tuple[str, int]]]:
    if file is None:
        return False, ("Nenhum arquivo enviado.", 400)

    if file.filename == "":
        return False, ("Arquivo inválido.", 400)

    if not file.filename.lower().endswith(".pdf"):
        return False, ("O arquivo precisa ser um PDF.", 400)

    return True, None


def extract_pdf(file) -> Tuple[Optional[str], Optional[Tuple[str, int]]]:
    is_valid, error = validate_file(file)
    if not is_valid:
        return None, error

    try:
        text = extract(file)
        if not text:
            return None, ("O PDF não contém texto extraível.", 400)

        return text, None

    except Exception as e:
        return None, (str(e), 500)
