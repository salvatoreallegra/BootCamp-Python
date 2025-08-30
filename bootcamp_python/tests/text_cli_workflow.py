# -------------------------------------------------------
# test_cli_workflow.py
# PURPOSE: End-to-end workflow: add -> list -> done.
# -------------------------------------------------------
import tasks_cli
from bootcamp_python.storage.json_storage import load_tasks

def run_cli(args):
    parser = tasks_cli.build_parser()
    parsed = parser.parse_args(args)
    return parsed.func(parsed)

def test_full_workflow(tmp_path):
    # Override data path to use tmp_path
    tasks_cli.DATA_PATH = tmp_path / "tasks.json"

    # Step 1: Add two tasks
    rc1 = run_cli(["add", "--title", "Task A"])
    rc2 = run_cli(["add", "--title", "Task B"])
    assert rc1 == rc2 == 0

    # Step 2: List tasks
    rc3 = run_cli(["list"])
    assert rc3 == 0

    tasks = load_tasks(tasks_cli.DATA_PATH)
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task A"

    # Step 3: Mark first as done
    rc4 = run_cli(["done", "--index", "1"])
    assert rc4 == 0

    tasks = load_tasks(tasks_cli.DATA_PATH)
    assert tasks[0]["is_done"] is True
