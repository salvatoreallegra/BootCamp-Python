# -------------------------------------------------------
# test_storage.py
# Tests for load/save with temporary paths.
# -------------------------------------------------------
from pathlib import Path
import json
import pytest
from bootcamp_python.day05.storage import load_tasks, save_tasks, StorageError

def test_load_returns_empty_if_missing(tmp_path: Path):
    path = tmp_path / "tasks.json"
    assert load_tasks(path) == []

def test_save_and_load_roundtrip(tmp_path: Path):
    path = tmp_path / "tasks.json"
    data = [{"title": "A", "done": False}]
    save_tasks(path, data)
    assert load_tasks(path) == data

def test_load_raises_storage_error_when_invalid_json(tmp_path: Path):
    path = tmp_path / "tasks.json"
    path.write_text("{ invalid json ]")
    with pytest.raises(StorageError):
        load_tasks(path)
