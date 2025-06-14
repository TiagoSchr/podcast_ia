import os
import unittest

import eleven_tts


class TestElevenTTS(unittest.TestCase):
    def test_missing_api_key(self):
        os.environ.pop("ELEVEN_API_KEY", None)
        with self.assertRaises(SystemExit):
            eleven_tts.main()


if __name__ == "__main__":
    unittest.main()
