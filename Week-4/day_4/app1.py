from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="internship"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sql = "INSERT INTO contacts (name,email,message) VALUES (%s,%s,%s)"
    val = (name, email, message)

    cursor.execute(sql, val)
    db.commit()

    return redirect('/view')

@app.route('/view')
def view():
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    return render_template('view.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)