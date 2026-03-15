from flask import Flask, request, jsonify
from pdf_extractor import extract

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API de Extração de Texto de PDFs",
        "usage": "Envie um POST para /extractions com um arquivo PDF",
        "example": "curl -F 'file=@seu_arquivo.pdf' http://localhost:5000/extractions"
    })

@app.route("/extractions", methods=["POST"])

def extract_pdf():
    if "file" not in request.files:
        return jsonify({"message": "Nenhum arquivo enviado."}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"message": "Arquivo inválido."}), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"message": "O arquivo precisa ser um PDF."}), 400

    try:
        text = extract(file)  # Passa objeto file diretamente

        if not text:
            return jsonify({"message": "O PDF não contém texto extraível."}), 400

        return jsonify({"message": text})

    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)