# -------------------------------------------------------
# task.py
# PURPOSE: Dataclass-based Task entity with helpers.
# Now part of the "models" package.
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
        return (
            self.due_utc is not None and
            datetime.now(timezone.utc) > self.due_utc and
            not self.is_done
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "is_done": self.is_done,
            "created_utc": self.created_utc.isoformat(),
            "due_utc": self.due_utc.isoformat() if self.due_utc else None,
        }
