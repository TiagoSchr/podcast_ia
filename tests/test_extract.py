import unittest
from pathlib import Path

from pipeline.extract import extract_text


class TestExtract(unittest.TestCase):
    def test_extract_text(self):
        text_file = Path("test.txt")
        text_file.write_text("olá mundo", encoding="utf-8")
        try:
            self.assertEqual(extract_text(str(text_file)), "olá mundo")
        finally:
            text_file.unlink()


if __name__ == "__main__":
    unittest.main()
