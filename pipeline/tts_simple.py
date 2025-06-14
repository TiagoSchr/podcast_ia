"""TTS simples usando gTTS."""

from pathlib import Path
from gtts import gTTS


class SimpleTTS:
    def __init__(self, lang: str = "pt"):
        self.lang = lang

    def synthesize(self, text: str, output_audio: str) -> str:
        """Converte o texto em áudio MP3."""
        if Path(text).exists():
            text = Path(text).read_text(encoding="utf-8")
        Path(output_audio).parent.mkdir(parents=True, exist_ok=True)
        tts = gTTS(text, lang=self.lang)
        tts.save(output_audio)
        return output_audio
