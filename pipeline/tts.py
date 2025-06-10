import sys
from pathlib import Path
from .config import F5_MODEL_PATH, REF_AUDIO

# Adiciona o caminho do módulo local F5-TTS-pt-br
sys.path.append(str(Path(__file__).resolve().parents[1] / "F5-TTS-pt-br"))
from AgentF5TTSChunk import AgentF5TTS


class TTS:
    def __init__(self, model_path: str | None = None, ref_audio: str | None = None):
        self.model_path = model_path or F5_MODEL_PATH
        self.ref_audio = ref_audio or REF_AUDIO
        self.agent = AgentF5TTS(ckpt_file=self.model_path, vocoder_name="vocos")

    def synthesize(self, text_file: str, output_audio: str, convert_to_mp3: bool = True) -> str:
        Path(output_audio).parent.mkdir(parents=True, exist_ok=True)
        self.agent.generate_speech(
            text_file=text_file,
            output_audio_file=output_audio,
            ref_audio=self.ref_audio,
            convert_to_mp3=convert_to_mp3,
        )
        return output_audio
