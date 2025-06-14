"""Benchmark simples da criação de podcasts."""

import time
import tracemalloc
from pathlib import Path

from pipeline.workflow import create_podcast
from pipeline.tts_simple import SimpleTTS


class DummySummarizer:
    def summarize(self, text: str) -> str:
        return text


def run(file_path: str = "bench.txt"):
    Path(file_path).write_text("conteudo", encoding="utf-8")
    tracemalloc.start()
    start = time.perf_counter()
    out = create_podcast(
        file_path,
        "benchmark.mp3",
        summarizer_cls=DummySummarizer,
        tts_cls=SimpleTTS,
    )
    elapsed = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    report = f"tempo={elapsed:.2f}s atual={current/1024:.1f}KiB pico={peak/1024:.1f}KiB"
    Path("benchmark").mkdir(exist_ok=True)
    Path("benchmark/report.txt").write_text(report, encoding="utf-8")
    print(report)
    Path(file_path).unlink()
    return out


if __name__ == "__main__":
    run()
