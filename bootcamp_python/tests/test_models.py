# -------------------------------------------------------
# test_models.py
# Parametrized tests for Task dataclass behavior.
# -------------------------------------------------------
from datetime import datetime, timedelta, timezone
import pytest
from bootcamp_python.day06.models import Task

def test_defaults_and_repr():
    t = Task("X")
    assert t.title == "X"
    assert t.description is None
    assert t.is_done is False
    assert t.created_utc.tzinfo is not None  # timezone-aware
    assert "Task(" in repr(t)

@pytest.mark.parametrize("done,offset_hours,expected", [
    (False, -1, True),   # due 1 hour ago, not done -> overdue
    (True, -1, False),   # due past but done -> not overdue
    (False,  1, False),  # due in future -> not overdue
    (False,  0, False),  # due now -> treat as not overdue for simplicity
])
def test_is_overdue(done, offset_hours, expected):
    due = datetime.now(timezone.utc) + timedelta(hours=offset_hours)
    t = Task("X", is_done=done, due_utc=due)
    assert t.is_overdue == expected

def test_from_to_dict_roundtrip():
    data = {"title": "A", "description": "B", "is_done": True}
    t = Task.from_dict(data)
    d2 = t.to_dict()
    assert d2["title"] == "A"
    assert d2["description"] == "B"
    assert d2["is_done"] is True
