# -------------------------------------------------------
# tasks_cli.py
# A tiny CLI to add/list/complete tasks with logging & errors.
# Run: python tasks_cli.py add --title "Learn Day 5"
# -------------------------------------------------------
from __future__ import annotations
import argparse
import logging
from pathlib import Path
from typing import Dict, Any, List
from bootcamp_python.day05.storage import load_tasks, save_tasks, StorageError

# Configure logging once, with level INFO
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO
)
log = logging.getLogger("tasks_cli")

DATA_PATH = Path("data/tasks.json")

def cmd_add(args: argparse.Namespace) -> int:
    """Add a new task."""
    try:
        tasks = load_tasks(DATA_PATH)
        tasks.append({"title": args.title, "done": False})
        save_tasks(DATA_PATH, tasks)
        log.info("Added task: %s", args.title)
        return 0
    except StorageError as e:
        log.error("Storage error: %s", e)
        return 1

def cmd_list(args: argparse.Namespace) -> int:
    """List tasks."""
    try:
        tasks = load_tasks(DATA_PATH)
        for idx, t in enumerate(tasks, start=1):
            status = "✔" if t.get("done") else " "
            print(f"{idx}. [{status}] {t.get('title')}")
        log.info("Listed %d tasks", len(tasks))
        return 0
    except StorageError as e:
        log.error("Storage error: %s", e)
        return 1

def cmd_done(args: argparse.Namespace) -> int:
    """Mark a task as done by 1-based index."""
    try:
        tasks = load_tasks(DATA_PATH)
        idx = args.index - 1
        if idx < 0 or idx >= len(tasks):
            log.error("Invalid index: %s", args.index)
            return 2
        tasks[idx]["done"] = True
        save_tasks(DATA_PATH, tasks)
        log.info("Completed task #%d: %s", args.index, tasks[idx].get("title"))
        return 0
    except StorageError as e:
        log.error("Storage error: %s", e)
        return 1

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tasks")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("--title", required=True, help="Task title")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="List tasks")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="Mark a task as done by index")
    p_done.add_argument("--index", type=int, required=True)
    p_done.set_defaults(func=cmd_done)

    return p

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)

if __name__ == "__main__":
    raise SystemExit(main())
