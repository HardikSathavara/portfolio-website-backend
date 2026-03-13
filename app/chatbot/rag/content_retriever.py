from pathlib import Path


def load_content(file_path: str):

    path = Path(file_path)

    if not path.exists():
        return ""

    with open(path, "r", encoding="utf-8") as f:
        return f.read()