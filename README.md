# text-extraction

## Objetivo

Este projeto é um programa simples em Python que extrai texto de arquivos PDF usando a biblioteca PyPDF2 e imprime o texto no terminal.

## Instalação de Dependências

Instale as dependências usando pip:

```
pip install -r requirements.txt
```

## Como Executar

### Linha de comando (CLI)

A lógica de extração agora está organizada em `src/`. Use o script principal para extrair texto de um PDF:

```bash
py src/main.py caminho/para/arquivo.pdf
```

### Executar a API (Flask)

A API está no mesmo projeto e pode ser iniciada com a flag `--serve`:

```bash
py src/main.py --serve
```

A aplicação rodará em `http://localhost:5000`.

Envie um POST para `http://localhost:5000/extractions` com um campo de formulário chamado `file` contendo o PDF.

Exemplo de resposta JSON:

```json
{
  "message": "Texto extraído do PDF aqui..."
}
```

**Nota:** A API processa o arquivo em memória (sem salvar no disco).

## Testes

Crie um PDF de teste usando reportlab:

```bash
py -c "from reportlab.pdfgen import canvas; c = canvas.Canvas('teste.pdf'); c.drawString(100, 750, 'Este é um teste de extração de texto.'); c.save()"
```

Teste a CLI:

```bash
py src/main.py teste.pdf
```

Teste a API (com servidor rodando):

```bash
py -c "import requests; r=requests.post('http://127.0.0.1:5000/extractions', files={'file': open('teste.pdf','rb')}); print('Status:', r.status_code); print(r.text)"
```
