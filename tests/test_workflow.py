import unittest
from pathlib import Path

from pipeline.workflow import create_podcast


class DummySummarizer:
    def summarize(self, text: str) -> str:
        return "resumo:" + text


class DummyTTS:
    def synthesize(self, text: str, output: str) -> str:
        Path(output).write_text("audio")
        return output


class TestWorkflow(unittest.TestCase):
    def test_create_podcast(self):
        doc = Path("doc.txt")
        doc.write_text("conteudo", encoding="utf-8")
        try:
            out = create_podcast(
                str(doc),
                "out.mp3",
                summarizer_cls=DummySummarizer,
                tts_cls=DummyTTS,
            )
            self.assertTrue(Path(out).exists())
        finally:
            doc.unlink()
            Path(out).unlink()


if __name__ == "__main__":
    unittest.main()
