# -------------------------------------------------------
# test_cli_imports.py
# PURPOSE: Verify the CLI entrypoint imports cleanly.
# -------------------------------------------------------
import importlib

def test_cli_imports():
    module = importlib.import_module("bootcamp_python.cli.tasks_cli")
    assert hasattr(module, "build_parser")

