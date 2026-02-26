import sqlite3

db = sqlite3.connect("internship.db")
data = db.cursor()

name_input = "sara"
age_input = 20

data.execute("INSERT INTO Students(name,age) VALUES(?,?)", (name_input, age_input))
db.commit()

print("Record added\n")

print("Current Records:")
records = data.execute("SELECT * FROM Students")
for r in records:
    print(r)

data.execute("UPDATE Students SET age=? WHERE name=?", (20, name_input))
db.commit()

print("\nRecord updated\n")

print("After Update:")
records = data.execute("SELECT * FROM Students")
for r in records:
    print(r)

data.execute("DELETE FROM Students WHERE name=?", (name_input,))
db.commit()

print("\nRecord deleted\n")

print("Final Records:")
records = data.execute("SELECT * FROM Students")
for r in records:
    print(r)

db.close()