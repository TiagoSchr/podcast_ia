"""Integração com o modelo F5-TTS."""

import sys
from pathlib import Path

from .config import F5_MODEL_PATH, REF_AUDIO

# Adiciona o caminho do módulo local F5-TTS-pt-br se existir
sys.path.append(str(Path(__file__).resolve().parents[1] / "F5-TTS-pt-br"))
try:
    from AgentF5TTSChunk import AgentF5TTS
except ModuleNotFoundError:  # pragma: no cover - dependência opcional
    AgentF5TTS = None


class F5TTS:
    """Síntese de voz utilizando o modelo F5-TTS."""

    def __init__(self, model_path: str | None = None, ref_audio: str | None = None):
        if AgentF5TTS is None:
            raise ImportError(
                "Dependência f5_tts ausente. Instale-a ou utilize SimpleTTS."
            )
        self.model_path = model_path or F5_MODEL_PATH
        self.ref_audio = ref_audio or REF_AUDIO
        self.agent = AgentF5TTS(ckpt_file=self.model_path, vocoder_name="vocos")

    def synthesize(self, text_file: str, output_audio: str, convert_to_mp3: bool = True) -> str:
        """Gera o áudio a partir do texto informado."""
        Path(output_audio).parent.mkdir(parents=True, exist_ok=True)
        self.agent.generate_speech(
            text_file=text_file,
            output_audio_file=output_audio,
            ref_audio=self.ref_audio,
            convert_to_mp3=convert_to_mp3,
        )
        return output_audio
