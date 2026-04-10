# text-extraction-api

## Objetivo

API REST em Python que extrai texto de arquivos PDF. Implementada com arquitetura em camadas (routes → controllers → services → models), seguindo boas práticas de desenvolvimento.

## Instalação de Dependências

Instale as dependências usando pip:

```
pip install -r requirements.txt
```

## Como Executar

**Iniciar a API Flask:**

```bash
py src/main.py
```

A API estará disponível em `http://localhost:5000`.

Envie um POST para `http://localhost:5000/extractions` com um campo de formulário chamado `file` contendo o PDF.

### Exemplo de requisição (cURL):

```bash
curl -F "file=@seu_arquivo.pdf" http://localhost:5000/extractions
```

### Exemplo de resposta JSON:

```json
{
  "data": {
    "name": "seu_arquivo.pdf",
    "content": "Texto extraído do PDF aqui..."
  }
}
```

Se houver erro, a resposta será:

```json
{
  "message": "Descrição do erro"
}
```


## Arquitetura do Projeto

O projeto segue uma arquitetura em camadas (MVC-like) com separação clara de responsabilidades:

```
src/
├── main.py                           # Entrypoint da aplicação
└── app/
    ├── models/
    │   └── Document.py               # Modelo de dados (PdfDocument)
    ├── services/
    │   └── ExtractionService.py      # Lógica de negócio (extração de texto)
    ├── controllers/
    │   └── ExtractionController.py   # Orquestrador de requisições
    ├── routes/
    │   └── ExtractionRoutes.py       # Definição de endpoints (rotas)
    └── main.py                        # Factory do app Flask
```

### Fluxo de uma requisição:

```
1. Cliente faz POST /extractions com PDF
   ↓
2. ExtractionRoutes intercepta e chama ExtractionController.extract_pdf()
   ↓
3. ExtractionController valida o arquivo e chama ExtractionService.extract_pdf()
   ↓
4. ExtractionService lê o PDF e retorna instância de Document
   ↓
5. ExtractionController transforma em JSON com jsonify()
   ↓
6. Resposta é enviada ao cliente
```

### Padrões utilizados:

- **Factory Pattern:** `create_app()` em `app/main.py` para criar a aplicação Flask
- **Blueprints:** Organização de rotas com `Flask.Blueprint`
- **Exceptions:** Uso de `raise` para tratamento de erros (sem `sys.exit()` ou `print()`)
- **Tipos:** Type hints em métodos para melhor documentação e IDE support
- **Validações:** Centralizadas no controlador antes de chamar a service


## Testes

Para testar a funcionalidade, primeiro crie um PDF de teste:

```bash
py -c "from reportlab.pdfgen import canvas; c = canvas.Canvas('teste.pdf'); c.drawString(100, 750, 'Este é um teste de extração de texto.'); c.save()"
```

Depois teste a API com cURL:

```bash
curl -F "file=@teste.pdf" http://localhost:5000/extractions
```

Ou com Python:

```python
import requests

with open('teste.pdf', 'rb') as f:
    r = requests.post('http://localhost:5000/extractions', files={'file': f})
    print(r.status_code)
    print(r.json())
```

## Dependências

- **Flask:** Framework web
- **PyPDF2:** Leitura e extração de PDFs
- **Werkzeug:** Manipulação de uploads de arquivos
- **reportlab:** Geração de PDFs (para testes)
