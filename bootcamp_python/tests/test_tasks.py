# -------------------------------------------------------
# test_task.py
# Unit tests for Task class behavior.
# -------------------------------------------------------
from bootcamp_python.day03.day03_oop import Task

def test_task_constructs_with_defaults():
    t = Task("Do the thing")
    assert t.title == "Do the thing"
    assert t.description == ""
    assert t.is_done is False

def test_mark_done_sets_flag_true():
    t = Task("Finish Day 4")
    t.mark_done()
    assert t.is_done is True

def test_str_representation_contains_title_and_state():
    t = Task("X")
    s = str(t)
    assert "Task(title='X'" in s
    assert "done=False" in s
