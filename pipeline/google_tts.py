"""Wrapper para síntese usando Google Cloud Text-to-Speech."""

from pathlib import Path
from google.cloud import texttospeech


class GoogleTTS:
    def __init__(self, voice: str = "pt-BR-Neural2-A"):
        self.client = texttospeech.TextToSpeechClient()
        self.voice = voice

    def synthesize(self, text: str, output: str) -> str:
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice_params = texttospeech.VoiceSelectionParams(
            language_code="pt-BR",
            name=self.voice,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice_params, audio_config=audio_config
        )
        Path(output).write_bytes(response.audio_content)
        return output
