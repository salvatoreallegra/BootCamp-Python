# bootcamp_python/day06/models.py
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import Optional

@dataclass
class Task:
    title: str
    description: Optional[str] = None
    is_done: bool = False
    created_utc: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    due_utc: Optional[datetime] = None

    @property
    def is_overdue(self) -> bool:
        """
        True only if there's a due date, the task is not done, and the due time
        is in the past (with a tiny grace so 'due now' isn't flagged).
        """
        if self.due_utc is None or self.is_done:
            return False
        now = datetime.now(timezone.utc)
        return (now - self.due_utc) > timedelta(seconds=1)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        # Minimal parse; if you store ISO strings for datetimes, parse them here.
        return cls(
            title=data["title"],
            description=data.get("description"),
            is_done=bool(data.get("is_done", False)),
            due_utc=data.get("due_utc"),  # parse if needed
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
            "created_utc": self.created_utc.isoformat(),
            "due_utc": self.due_utc.isoformat() if self.due_utc else None,
        }
