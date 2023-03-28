import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

conn = sqlite3.connect("users.db")

c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS users (
        user_name text PRIMARY KEY,
        email text,
        user_password text
        )"""
)

admin_password_complete = generate_password_hash("admin", method="sha256")

c.execute(
    "INSERT INTO users VALUES (:user, :email, :user_password)",
    {
        "user": "admin",
        "email": None,
        "user_password": str(admin_password_complete),
    },
)

conn.commit()

conn.close()