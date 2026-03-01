from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
def connect_db():
    return sqlite3.connect("users.db")

# login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                       (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect("/dashboard")
        else:
            return "Login Failed!!"
    return render_template("login.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO records (name, email) VALUES (?, ?)", (name, email))
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
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/view")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        cursor.execute("UPDATE records SET name=?, email=? WHERE id=?", (name, email, id))
        conn.commit()
        conn.close()
        return redirect("/view")
    cursor.execute("SELECT * FROM records WHERE id=?", (id,))
    record = cursor.fetchone()
    conn.close()
    return render_template("edit.html", record=record)

@app.route("/dashboard")
def dashboard():
    return """
    <h2>Login Successful!!</h2>
    <a href='/add'>Add Record</a><br>
    <a href='/view'>View Records</a>
    """

if __name__ == "__main__":
    app.run(debug=True)