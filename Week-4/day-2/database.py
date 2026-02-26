import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

cursor.execute("DROP TABLE IF EXISTS Students")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("DROP TABLE IF EXISTS Tasks")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    status TEXT
)
""")

cursor.execute("INSERT INTO Users(name,email) VALUES('shabnam','shab@gmail.com')")
cursor.execute("INSERT INTO Users(name,email) VALUES('sam','sam@gmail.com')")
cursor.execute("INSERT INTO Students(name,age) VALUES('shabnam',21)")
cursor.execute("INSERT INTO Students(name,age) VALUES('sam',22)")
cursor.execute("INSERT INTO Tasks(task_name,status) VALUES('complete db task','pending')")
cursor.execute("INSERT INTO Tasks(task_name,status) VALUES('complete db task','completed')")

conn.commit()

print("Users Table:")
for row in cursor.execute("SELECT * FROM Users"):
    print(row)

print("\nStudents Table:")
for row in cursor.execute("SELECT * FROM Students"):
    print(row)

print("\nTasks Table:")
for row in cursor.execute("SELECT * FROM Tasks"):
    print(row)

conn.close()