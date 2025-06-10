import unittest
from unittest import mock
from pathlib import Path

from pipeline.workflow import create_podcast


class DummyLLM:
    def generate(self, prompt: str) -> str:
        return f"roteiro:{prompt}"


class DummyTTS:
    def __init__(self):
        self.called = False

    def synthesize(self, text_file: str, output_audio: str) -> str:
        self.called = True
        Path(output_audio).write_text("audio")
        return output_audio


class TestWorkflow(unittest.TestCase):
    def test_create_podcast(self):
        out = create_podcast("tema", "out.wav", llm_cls=DummyLLM, tts_cls=DummyTTS)
        self.assertTrue(Path(out).exists())
        Path(out).unlink()


if __name__ == "__main__":
    unittest.main()
