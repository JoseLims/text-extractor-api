import argparse
import os

from app.main import create_app
from app.services.ExtractionService import extract


def run_cli(pdf_path: str) -> None:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {pdf_path}")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("O arquivo precisa ser um PDF.")

    text = extract(pdf_path)
    if not text:
        print("O PDF não contém texto extraível.")
        return

    print(text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrai texto de PDFs (CLI e API)")
    parser.add_argument("--serve", action="store_true", help="Inicia a API Flask")
    parser.add_argument("pdf", nargs="?", help="Caminho para o PDF a ser extraído")
    args = parser.parse_args()

    if args.serve:
        create_app().run(debug=True)
    elif args.pdf:
        run_cli(args.pdf)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
