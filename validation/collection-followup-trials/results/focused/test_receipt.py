import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from receipt import write_receipt


class ReceiptTests(unittest.TestCase):
    def test_norwegian_label_is_utf8_under_ascii_locale(self) -> None:
        script = r'''
import codecs
import locale
from pathlib import Path
import sys
from receipt import write_receipt

assert codecs.lookup(locale.getpreferredencoding(False)).name == "ascii"
write_receipt(Path(sys.argv[1]), "\u00c6\u00d8\u00c5\u00e6\u00f8\u00e5")
'''
        environment = os.environ.copy()
        environment.update(
            LC_ALL="C",
            PYTHONUTF8="0",
            PYTHONCOERCECLOCALE="0",
            PYTHONDONTWRITEBYTECODE="1",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            subprocess.run(
                [sys.executable, "-c", script, str(path)],
                cwd=Path(__file__).resolve().parent,
                env=environment,
                stdin=subprocess.DEVNULL,
                check=True,
                timeout=10,
            )
            content = path.read_bytes()
            self.assertEqual(json.loads(content.decode("utf-8")), {"label": "ÆØÅæøå"})
            self.assertEqual(content, '{"label": "ÆØÅæøå"}'.encode("utf-8"))

    def test_ascii_label_keeps_existing_json_format(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            write_receipt(path, 'Example "label"')
            self.assertEqual(path.read_bytes(), b'{"label": "Example \\"label\\""}')

    def test_empty_label_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "receipt.json"
            write_receipt(path, "")
            self.assertEqual(path.read_bytes(), b'{"label": ""}')


if __name__ == "__main__":
    unittest.main()
