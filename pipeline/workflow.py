from pathlib import Path
from .llm import LLM
from .tts import TTS


def create_podcast(prompt: str, output_audio: str) -> str:
    llm = LLM()
    script = llm.generate(prompt)
    text_path = Path("script.txt")
    text_path.write_text(script, encoding="utf-8")

    tts = TTS()
    return tts.synthesize(str(text_path), output_audio)
