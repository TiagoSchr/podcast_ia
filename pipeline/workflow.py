from pathlib import Path
from .llm import LLM
from .tts import F5TTS


def create_podcast(
    prompt: str,
    output_audio: str,
    llm_cls: type[LLM] = LLM,
    tts_cls: type[F5TTS] = F5TTS,
) -> str:
    """Gera um podcast a partir de um prompt."""

    llm = llm_cls()
    script = llm.generate(prompt)
    text_path = Path("script.txt")
    text_path.write_text(script, encoding="utf-8")

    tts = tts_cls()
    return tts.synthesize(str(text_path), output_audio)
