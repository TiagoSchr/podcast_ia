from pathlib import Path

import pdfplumber
import docx


def read_document(path: str) -> str:
    """Lê PDF, DOCX ou TXT e retorna o texto completo."""
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        with pdfplumber.open(path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    if ext in {".docx", ".doc"}:
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    if ext == ".txt":
        return Path(path).read_text(encoding="utf-8")
    raise ValueError("Formato de arquivo não suportado")
