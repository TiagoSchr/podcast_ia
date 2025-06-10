import argparse
import os
from pipeline.workflow import create_podcast
from pipeline.tts import F5TTS
from pipeline.tts_simple import SimpleTTS


def parse_args():
    parser = argparse.ArgumentParser(description="Gera um podcast em áudio a partir de um prompt")
    parser.add_argument("prompt", help="Texto ou tema para gerar o roteiro")
    parser.add_argument("--output", default="output/podcast.mp3", help="Arquivo de saída do áudio")
    parser.add_argument("--tts", choices=["f5", "simple"], default="simple", help="Engine de síntese de voz")
    return parser.parse_args()


def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    tts_cls = F5TTS if args.tts == "f5" else SimpleTTS
    audio = create_podcast(args.prompt, args.output, tts_cls=tts_cls)
    print(f"Áudio gerado em: {audio}")


if __name__ == "__main__":
    main()
