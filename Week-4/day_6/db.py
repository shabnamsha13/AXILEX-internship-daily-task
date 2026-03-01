import sqlite3
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
               ("admin", "1234"))

# create table for CRUD
cursor.execute("""
CREATE TABLE IF NOT EXISTS records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")
conn.commit()
conn.close()
print("Database created successfully")