import os
from pathlib import Path
from elevenlabs import save
from elevenlabs.client import ElevenLabs


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.mp3"


def main() -> None:
    api_key = os.getenv("ELEVEN_API_KEY")
    voice_id = os.getenv("ELEVEN_VOICE_ID", "EXAVITQu4vr4xnSDxMaL")
    if not api_key:
        raise SystemExit("Defina a variável ELEVEN_API_KEY")

    try:
        text = Path(INPUT_FILE).read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Arquivo {INPUT_FILE} não encontrado")

    client = ElevenLabs(api_key=api_key)
    try:
        client.voices.get(voice_id=voice_id)
    except Exception as exc:
        raise SystemExit(f"Voz não encontrada: {exc}")

    try:
        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id="eleven_flash_v2_5",
            output_format="mp3_44100_128",
        )
        save(audio, OUTPUT_FILE)
    except Exception as exc:
        raise SystemExit(f"Erro ao gerar áudio: {exc}")

    print(f"Áudio salvo em {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
