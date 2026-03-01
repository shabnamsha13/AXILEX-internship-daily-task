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

# dashboard page
@app.route("/dashboard")
def dashboard():
    return "<h2>Login Successful.. Welcome!</h2>"


if __name__ == "__main__":
    app.run(debug=True)