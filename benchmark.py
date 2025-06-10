"""Benchmark simples para medir tempo e memória da criação do podcast."""

import time
import tracemalloc
from pathlib import Path

from pipeline.workflow import create_podcast
from pipeline.tts_simple import SimpleTTS


class DummyLLM:
    def generate(self, prompt: str) -> str:
        return f"roteiro:{prompt}"


def run(prompt: str = "teste"):
    tracemalloc.start()
    start = time.perf_counter()
    out = create_podcast(prompt, "benchmark.wav", llm_cls=DummyLLM, tts_cls=SimpleTTS)
    elapsed = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    report = f"tempo={elapsed:.2f}s atual={current/1024:.1f}KiB pico={peak/1024:.1f}KiB"
    Path("benchmark").mkdir(exist_ok=True)
    Path("benchmark/report.txt").write_text(report, encoding="utf-8")
    print(report)
    return out


if __name__ == "__main__":
    run()

