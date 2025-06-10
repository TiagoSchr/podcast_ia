from pathlib import Path


def extract_text(path: str) -> str:
    """Lê o conteúdo de um arquivo de texto."""
    return Path(path).read_text(encoding="utf-8")
