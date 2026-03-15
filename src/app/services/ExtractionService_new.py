import PyPDF2


def extract(source):
    """Extrai texto de um PDF.

    Args:
        source: caminho para arquivo PDF (str) ou um file-like object.

    Returns:
        Texto extraído como string.

    Raises:
        ValueError: se ocorrer qualquer erro ao ler o PDF.
    """

    try:
        if isinstance(source, str):
            file_obj = open(source, "rb")
            close_after = True
        else:
            file_obj = source
            close_after = False

        reader = PyPDF2.PdfReader(file_obj)
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text_parts.append(page_text)

        result = "\n".join(text_parts).strip()

        if close_after:
            file_obj.close()

        return result

    except Exception as e:
        raise ValueError(f"Erro ao ler o PDF: {str(e)}")
