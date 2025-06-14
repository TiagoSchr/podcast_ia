from pathlib import Path

from .document import read_document
from .gemini import Gemini
from .google_tts import GoogleTTS
from .tts_simple import SimpleTTS


def create_podcast(
    file_path: str,
    output_audio: str = "resumo_podcast.mp3",
    summarizer_cls: type[Gemini] = Gemini,
    tts_cls: type[GoogleTTS] = GoogleTTS,
) -> str:
    """Gera um podcast a partir de um documento."""

    text = read_document(file_path)
    summarizer = summarizer_cls()
    summary = summarizer.summarize(text)

    tts = tts_cls()
    tts.synthesize(summary, output_audio)
    return output_audio
