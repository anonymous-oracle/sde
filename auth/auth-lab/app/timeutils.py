from __future__ import annotations
from datetime import datetime, timezone, timedelta

def now_utc() -> datetime:
    return datetime.now(tz=timezone.utc)

def expires_in(seconds: int) -> datetime:
    return now_utc() + timedelta(seconds=seconds)

def is_expired(when: datetime) -> bool:
    return now_utc() >= when

