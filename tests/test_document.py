import unittest
from pathlib import Path

from pipeline.document import read_document


class TestDocument(unittest.TestCase):
    def test_read_text(self):
        text_file = Path("test.txt")
        text_file.write_text("ola", encoding="utf-8")
        try:
            self.assertEqual(read_document(str(text_file)), "ola")
        finally:
            text_file.unlink()


if __name__ == "__main__":
    unittest.main()
