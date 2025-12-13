from auth.auth import login_user

print(login_user("reshika", "SecurePass123"))  # True
print(login_user("reshika", "WrongPass"))       # False
