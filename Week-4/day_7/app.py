from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)

def connect_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT
    )
    """)
    conn.commit() 
    return conn

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = connect_db()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("register.html")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect("/dashboard")
        else:
            return "Invalid Login!!"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        conn = connect_db()
        conn.execute("INSERT INTO records (name, course) VALUES (?, ?)", (name, course))
        conn.commit()
        conn.close()

        return redirect("/view")
    return render_template("add.html")

@app.route("/view")
def view():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    data = cursor.fetchall()
    conn.close()
    return render_template("view.html", records=data)

@app.route("/delete/<int:id>")
def delete(id):
    conn = connect_db()
    conn.execute("DELETE FROM records WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/view")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["course"]
        cursor.execute("UPDATE records SET name=?, course=? WHERE id=?", (name, course, id))
        conn.commit()
        conn.close()
        return redirect("/view")

    cursor.execute("SELECT * FROM records WHERE id=?", (id,))
    record = cursor.fetchone()
    conn.close()
    return render_template("edit.html", record=record)

if __name__ == "__main__":
    connect_db().close()

    app.run(debug=True)
