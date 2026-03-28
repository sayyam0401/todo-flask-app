from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def home():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    db.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    db = get_db()
    db.execute("INSERT INTO tasks (name) VALUES (?)", (task,))
    db.commit()
    db.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run()
