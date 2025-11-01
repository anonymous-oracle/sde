class AuthError(Exception):
    """Base class for auth-related errors."""

class InvalidCredentials(AuthError):
    pass

class TokenExpired(AuthError):
    pass

class SecurityViolation(AuthError):
    pass