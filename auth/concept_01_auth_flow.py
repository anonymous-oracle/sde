import secrets
from dataclasses import dataclass, field
from typing import Dict, Optional

# ---------------------------------------------------------
# 1. DATA MODELS (First Principles)
# ---------------------------------------------------------
@dataclass
class User:
    id: str
    username: str
    # In reality, we NEVER store plain passwords. 
    # This is for flow demonstration only.
    password_hash_simulation: str 

@dataclass
class Session:
    user_id: str
    ip_address: str
    is_active: bool = True

# ---------------------------------------------------------
# 2. MOCK DATABASE & SESSION STORE
# ---------------------------------------------------------
class System:
    def __init__(self):
        self.users: Dict[str, User] = {}
        # The "Stateful" part. Server memory holds active sessions.
        self.sessions: Dict[str, Session] = {} 

    def register(self, username, password):
        # ID generation using secure randomness
        user_id = secrets.token_hex(8)
        self.users[username] = User(user_id, username, password)
        return user_id

    def login(self, username, password, ip_address) -> Optional[str]:
        """
        Returns session_id if successful, None otherwise.
        """
        user = self.users.get(username)
        
        # AuthN Check
        if not user:
            return None
        
        # In real code: verify_hash(password, user.password_hash)
        if user.password_hash_simulation != password: 
            return None
            
        # Create Session (Stateful)
        # We issue a random reference ID, not the user ID directly.
        session_id = secrets.token_urlsafe(32)
        self.sessions[session_id] = Session(user.id, ip_address)
        
        return session_id

    def authenticate_request(self, session_id) -> Optional[User]:
        """
        Resolves a session ID back to a user.
        """
        if session_id not in self.sessions:
            return None
            
        session = self.sessions[session_id]
        
        if not session.is_active:
            return None
            
        # Find the user object from the session reference
        # In a DB, this would be: SELECT * FROM users WHERE id = session.user_id
        for user in self.users.values():
            if user.id == session.user_id:
                return user
        return None

# ---------------------------------------------------------
# 3. EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    app = System()
    
    # 1. Register
    app.register("alice", "secret123")
    
    # 2. Login (AuthN)
    # Alice exchanges credentials for a Session ID (Ticket)
    token = app.login("alice", "secret123", "192.168.1.5")
    print(f"Session Token: {token}")
    
    # 3. Subsequent Request (Identification via Token)
    # Alice sends ONLY the token. Server looks up State.
    current_user = app.authenticate_request(token)
    
    if current_user:
        print(f"Authorized access for: {current_user.username}")
    else:
        print("401 Unauthorized")