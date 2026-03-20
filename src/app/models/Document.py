class Document:
    """Modelo que representa um documento PDF extraído."""
    
    def __init__(self, name: str, content: str):
        self.name = name          # Nome do arquivo
        self.content = content    # Conteúdo extraído
