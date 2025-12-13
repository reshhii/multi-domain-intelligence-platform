from security import hash_password, verify_password

password = "MySecurePassword123"

hashed = hash_password(password)
print("Hashed password:", hashed)

print("Correct password:", verify_password("MySecurePassword123", hashed))
print("Wrong password:", verify_password("wrongpassword", hashed))
