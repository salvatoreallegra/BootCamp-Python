# -------------------------------------------------------
# storage.py
# JSON-backed storage with safe load/save and exceptions.
# -------------------------------------------------------
from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any

class StorageError(Exception):
    """Raised for storage-related errors (IO/JSON/etc.)."""

def load_tasks(path: Path) -> list[dict]:
    try:
        if not path.exists():
            return []
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        raise StorageError(f"Failed to load tasks from {path}") from exc

def save_tasks(path: Path, tasks: list[dict]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except Exception as exc:
        raise StorageError(f"Failed to save tasks to {path}") from exc