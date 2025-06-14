import argparse
import os

from pipeline.workflow import create_podcast
from pipeline.google_tts import GoogleTTS
from pipeline.tts_simple import SimpleTTS


def parse_args():
    parser = argparse.ArgumentParser(description="Transforma documentos em podcast")
    parser.add_argument("file", help="Arquivo PDF, DOCX ou TXT")
    parser.add_argument(
        "--output", default="resumo_podcast.mp3", help="Arquivo de saída do áudio"
    )
    parser.add_argument(
        "--tts",
        choices=["google", "simple"],
        default="google",
        help="Engine de síntese de voz",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    tts_cls = GoogleTTS if args.tts == "google" else SimpleTTS
    audio = create_podcast(args.file, args.output, tts_cls=tts_cls)
    print(f"Áudio gerado em: {audio}")


if __name__ == "__main__":
    main()
