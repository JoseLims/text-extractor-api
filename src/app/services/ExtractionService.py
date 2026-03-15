import PyPDF2

def extract(source):
    try:
        # Se for string (caminho), abre arquivo
        if isinstance(source, str):
            file_obj = open(source, 'rb')
        else:
            # Se for objeto file-like (como de Flask), usa diretamente
            file_obj = source

        reader = PyPDF2.PdfReader(file_obj)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        result = text.strip()

        # Fecha arquivo apenas se abrimos nós mesmos
        if isinstance(source, str):
            file_obj.close()

        return result
    except Exception as e:
        raise ValueError(f"Erro ao ler o PDF: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erro: informe um arquivo PDF.")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("Erro: arquivo não encontrado.")
        sys.exit(1)

    if not file_path.lower().endswith('.pdf'):
        print("Erro: o arquivo precisa ser um PDF.")
        sys.exit(1)

    try:
        text = extract(file_path)
        if not text:
            print("Erro: o PDF não contém texto extraível.")
            sys.exit(1)
        print(text)
    except ValueError as e:
        print(e)
        sys.exit(1)