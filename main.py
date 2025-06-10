import argparse
import os
from pipeline.workflow import create_podcast


def parse_args():
    parser = argparse.ArgumentParser(description="Gera um podcast em áudio a partir de um prompt")
    parser.add_argument("prompt", help="Texto ou tema para gerar o roteiro")
    parser.add_argument("--output", default="output/podcast.mp3", help="Arquivo de saída do áudio")
    return parser.parse_args()


def main():
    args = parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    audio = create_podcast(args.prompt, args.output)
    print(f"Áudio gerado em: {audio}")


if __name__ == "__main__":
    main()
