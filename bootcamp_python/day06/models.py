# -------------------------------------------------------
# models.py
# Dataclass-based Task with type hints and a few helpers.
# -------------------------------------------------------
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
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
        return self.due_utc is not None and datetime.now(timezone.utc) > self.due_utc and not self.is_done

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        # Simple parse; real code would parse ISO strings to datetime
        return cls(
            title=data["title"],
            description=data.get("description"),
            is_done=bool(data.get("is_done", False)),
            due_utc=data.get("due_utc"),  # keep None/simple for now
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
            "created_utc": self.created_utc.isoformat(),
            "due_utc": self.due_utc.isoformat() if self.due_utc else None,
        }
