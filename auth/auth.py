import os
from security import hash_password, verify_password

USER_FILE = os.path.join("data", "users.txt")


def user_exists(username: str) -> bool:
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line or ":" not in line:
                continue  # skip bad lines safely

            stored_username, _ = line.split(":", 1)
            if stored_username == username:
                return True

    return False



def register_user(username: str, password: str) -> bool:
    if user_exists(username):
        return False

    os.makedirs("data", exist_ok=True)

    hashed_password = hash_password(password).decode("utf-8")

    with open(USER_FILE, "a") as file:
        file.write(f"{username}:{hashed_password}\n")

    return True


def authenticate_user(username: str, password: str) -> bool:
    if not os.path.exists(USER_FILE):
        return False
    
    with open(USER_FILE, "r") as file:
        for line in file:
            stored_username, stored_hash = line.strip().split(":", 1)
            if stored_username == username:
                return verify_password(password, stored_hash.encode("utf-8"))
    return False



def login_user(username: str, password: str) -> bool:
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line or ":" not in line:
                continue

            stored_username, stored_hash = line.split(":", 1)

            if stored_username == username:
                return verify_password(password, stored_hash.encode("utf-8"))

    return False

    