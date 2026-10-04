import json
from pathlib import Path


def write_receipt(path: Path, label: str) -> None:
    path.write_text(json.dumps({"label": label}, ensure_ascii=False))
