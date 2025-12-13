import bcrypt


def hash_password(password: str) -> bytes:
    """
    Takes a plain-text password and returns a hashed version using bcrypt.
    """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed


def verify_password(password: str, hashed_password: bytes) -> bool:
    """
    Verifies a plain-text password against a stored bcrypt hash.
    """
    password_bytes = password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_password)
