"""Módulos para criação de podcasts a partir de documentos."""

from .config import GEMINI_API_KEY
from .document import read_document
from .gemini import Gemini
from .google_tts import GoogleTTS
from .tts_simple import SimpleTTS
from .workflow import create_podcast

__all__ = [
    "GEMINI_API_KEY",
    "read_document",
    "Gemini",
    "GoogleTTS",
    "SimpleTTS",
    "create_podcast",
]
