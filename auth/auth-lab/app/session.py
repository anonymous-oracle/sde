from __future__ import annotations
from datetime import datetime
from typing import Optional, Dict
from http import cookies
from crypto import rand_token
from timeutils import now_utc, expires_in, is_expired
from config import SESSION_TTL_SECONDS

class Session:
    """Represents a single authenticated session."""
    def __init__(self, user_id: str, expires_at: datetime):
        self.user_id = user_id
        self.created_at = now_utc()
        self.expires_at = expires_at
        self.last_seen = now_utc()

    def touch(self):
        """Renew idle timeout."""
        self.last_seen = now_utc()
        self.expires_at = expires_in(SESSION_TTL_SECONDS)

    @property
    def expired(self) -> bool:
        return is_expired(self.expires_at)
    

class SessionStore:
    """Naive in-memory session store."""
    def __init__(self):
        self._sessions: Dict[str, Session] = {}
    
    def create(self, user_id: str) -> str:
        sid = rand_token(24)
        session = Session(user_id=user_id, expires_at=expires_in(SESSION_TTL_SECONDS))
        self._sessions[sid] = session
        return sid
    
    def delete_session(self, sid: str) -> Optional[str]:
        return self._sessions.pop(sid, None)
    
    def get(self, sid: str) -> Optional[Session]:
        s = self._sessions.get(sid)
        if not s:
            return None
        if s.expired:
            self.delete_session(sid)
            return None
        s.touch()
        return s
    

