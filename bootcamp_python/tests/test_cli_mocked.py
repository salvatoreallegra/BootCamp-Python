import types
import builtins
from pathlib import Path
import pytest

# Import the CLI module after patching path constant if needed
import bootcamp_python.cli.tasks_cli as tasks_cli

class FakeStore:
    def __init__(self):
        self.data = []

    def load(self, path):
        return list(self.data)

    def save(self, path, tasks):
        self.data = list(tasks)

@pytest.fixture
def fstore():
    return FakeStore()

@pytest.fixture(autouse=True)
def patch_storage(monkeypatch, fstore):
    # Patch storage functions the CLI imports
    from bootcamp_python.storage import json_storage

    monkeypatch.setattr(json_storage, "load_tasks", lambda p: fstore.load(p))
    monkeypatch.setattr(json_storage, "save_tasks", lambda p, t: fstore.save(p, t))

def test_cli_add(monkeypatch, capsys):
    # Simulate: tasks_cli.py add --title "X"
    parser = tasks_cli.build_parser()
    args = parser.parse_args(["add", "--title", "X"])

    rc = args.func(args)
    assert rc == 0

def test_cli_list(monkeypatch, capsys, fstore):
    # pre-populate fake store
    fstore.data = [{"title": "A", "done": False}, {"title": "B", "done": True}]

    parser = tasks_cli.build_parser()
    args = parser.parse_args(["list"])
    rc = args.func(args)
    assert rc == 0

    out = capsys.readouterr().out
    assert "1. [ ] A" in out
    assert "2. [✔] B" in out

def test_cli_done(monkeypatch, fstore):
    fstore.data = [{"title": "A", "done": False}]
    parser = tasks_cli.build_parser()
    args = parser.parse_args(["done", "--index", "1"])
    rc = args.func(args)
    assert rc == 0
    assert fstore.data[0]["done"] is True

    
